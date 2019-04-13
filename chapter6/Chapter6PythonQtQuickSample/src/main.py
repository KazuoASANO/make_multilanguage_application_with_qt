import os
import sys
import qml_rc
import image_rc
import i18n_rc
from PySide2.QtWidgets import QApplication
from PySide2.QtQml import QQmlApplicationEngine
from PySide2.QtCore import QLocale, QDir, QTranslator, QUrl
from Translation import Translation


def main():
    """ 環境変数に Qt Quick Controls 2 のコンフィグファイル設定 を追加する
      環境変数 QT_QUICK_CONTROLS_CONF に対して、本 Code と同じ
      ディレクトリにある qtquickcontrols2.conf
      ( Qt Quick Controls 2 の Configuration File ファイル)
      を設定
    """
    os.environ['QT_QUICK_CONTROLS_CONF'] = '../qtquickcontrols2.conf'

    app = QApplication(sys.argv)
    app.setApplicationName('Chapter6PythonQtQuickSample')

    """ Systemロケールの文字を取得（例：ja, zh）
        \note
        良く使用される国名コードの標準ISO3166(日本なら"jp")ではなく、
        BCP47のうちSimple language subtag(言語コードの2文字。日本語なら "ja")
        を取得します。
    """
    locale = QLocale.system().bcp47Name()

    """
    リソースファイルの :/i18nディレクトリから
    登録しているリソースファイルを抽出
    （:/i18n/Chapter3QtQuickSample_*.qm にマッチするファイルを抽出）
    """
    qm_dir = QDir(':/i18n')
    search_name = app.applicationName() + '_' + locale + '.qm'
    list_search = [search_name]
    list_qm_files = qm_dir.entryList(list_search)
    for qm_file in list_qm_files:
        load_file = qm_dir.absolutePath() + QDir.separator() + qm_file
        # QTranslatorクラスにQt翻訳バイナリファイルをセット
        translator = QTranslator()
        if translator.load(load_file):
            # 翻訳バイナリファイルをアプリケーションに適用
          app.installTranslator(translator)
        break

    engine = QQmlApplicationEngine()

    # QML経由でアクセスするtranslationクラスのインスタンスを生成する
    translation = Translation(engine)
    # Translation クラスを QML の countDown としてバインディングする
    engine.rootContext().setContextProperty("Translation", translation)

    url = QUrl('qrc:/ui/main.qml')
    # QML ファイルのロード
    engine.load(url)
    # ルートオブジェクトのリストが見つからない場合は
    # 起動できないため、終了する
    if not engine.rootObjects():
        sys.exit(-1)

    ret = app.exec_()
    sys.exit(ret)


if __name__ == '__main__':
    main()
