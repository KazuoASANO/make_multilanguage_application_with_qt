from PySide2.QtCore import QObject, QTranslator, QLocale, QDir, Signal, Property
from PySide2.QtWidgets import QApplication
from PySide2.QtQml import QQmlApplicationEngine


class Translation(QObject):
    # 値が設定された時の状態をQML側に伝えるシグナルインスタンス
    languageChanged = Signal(int)

    # \brief ロケール言語文字列(QMLのCombBoxの並びと同一) * /
    #                   英語  ドイツ語 日本語 中国語
    language_strings = ["en", "de", "ja", "zh"]

    def __init__(self, engine, parent=None):
        super(Translation, self).__init__(parent)

        """ Systemロケールの文字を取得（例：ja, zh）
            \note
            良く使用される国名コードの標準ISO3166(日本なら"jp")ではなく、
            BCP47のうちSimple language subtag(言語コードの2文字。日本語なら "ja")
            を取得します。
        """
        self.locale = QLocale.system().bcp47Name()

        # Qt国際化対応クラス オブジェクト
        self.translator = QTranslator(self)

        self.qml_engine = engine

        # # 現在のロケールのindex値取得
        # self.lang = self.language()
        # # 翻訳ファイルのセット
        # self.set_language(self.lang)

    """ 
    \brief Translation::language 現在のロケールの言語のindex取得
    \return int型の Translation::Language値
    """
    # @Property(int, notify=languageChanged)
    def language(self):
        # 現在のロケールから、設定できるロケール言語文字列の配列番号取得
        max_language_num = len(self.language_strings)
        for language_num in range(max_language_num):
            if self.locale == self.language_strings[language_num]:
                break

        # ロケール文字がすべて一致しない場合は、英語にする
        if max_language_num == language_num:
            language_num = self.language_strings.index('en')
            self.locale = self.language_strings[language_num]

        return language_num

    """
    \brief Translation::set_language 指定された言語の翻訳ファイルをインストールする
    \param[in] value : インストールする言語index(Widget / QML側から通知)
    """
    # @language.setter
    def set_language(self, value):
        self.locale = self.language_strings[value]

        """
        リソースファイルの :/i18nディレクトリから
        登録しているリソースファイルを抽出
        （:/i18n/$${TARGET}_*.qm にマッチするファイルを抽出）
        """
        qm_dir = QDir(':/i18n')
        app = QApplication.instance()
        search_name = app.applicationName() + '_' + self.locale + '.qm'
        list_search = [search_name]
        list_qm_files = qm_dir.entryList(list_search)
        for qm_file in list_qm_files:
            # 以前の翻訳ファイルをremove
            app.removeTranslator(self.translator)

            load_file = qm_dir.absolutePath() + QDir.separator() + qm_file
            # QTranslatorクラスにQt翻訳バイナリファイルをセット
            if self.translator.load(load_file):
                # 翻訳バイナリファイルをアプリケーションに適用
                app.installTranslator(self.translator)
                # QML側のui関連を再描画
                self.qml_engine.retranslate()
                break

        self.languageChanged.emit(value)

    # QMLへのプロパティ公開
    language = Property(int, language, set_language, languageChanged)
