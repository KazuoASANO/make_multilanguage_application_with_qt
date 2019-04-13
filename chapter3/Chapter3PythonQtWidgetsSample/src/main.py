import sys
import image_rc
import i18n_rc
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QMainWindow, QApplication, QGraphicsScene
from PySide2.QtCore import QFile, QLocale, QDir, QTranslator
from PySide2.QtGui import QPixmap


class MainWindow(QMainWindow):

    def __init__(self, ui_file, parent=None):
        super(MainWindow, self).__init__(parent)
        file = QFile(ui_file)
        file.open(QFile.ReadOnly)

        # 指定されたuiファイルを QUiLoader 経由で読み出す
        loader = QUiLoader()
        self.ui = loader.load(file)

        file.close()

        # リンゴ画像表示用 QGraphicsSceneオブジェクト生成
        self.graphics_scene_apple = QGraphicsScene(self)
        # 正解判定 ○Ｘ画像表示用 QGraphicsSceneオブジェクト生成
        self.graphics_scene_judge = QGraphicsScene(self)

        self.ui_init()

        # uiとのsignal / slot接続
        self.ui.action_Quit.triggered.connect(sys.exit)
        self.ui.pushButtonMelon.clicked.connect(self.push_button_melon_clicked)
        self.ui.pushButtonApple.clicked.connect(self.push_button_apple_clicked)
        self.ui.pushButtonStrawbery.clicked.connect(
            self.push_button_strawberry_clicked)

    # \brief UI初期表示
    def ui_init(self):
        # リンゴ画像表示用のQGraphicsViewクラスへ、リンゴ画像表示用
        #         QGraphicsSceneをセット
        self.ui.graphicsView.setScene(self.graphics_scene_apple)
        # リソースファイルのリンゴ画像をQPixmapにセット
        pix_map = QPixmap(':/apple.png')
        # リンゴ画像表示用 QGraphicsSceneに、リンゴ画像のQPixmapをセット
        self.graphics_scene_apple.addPixmap(pix_map)

        # 正解判定 ○Ｘ画像表示用のQGraphicsViewクラスへ、
        # 正解判定 ○Ｘ画像表示用表示用 QGraphicsSceneをセット
        self.ui.graphicsViewjudge.setScene(self.graphics_scene_judge)
        # 正解判定Widgetを、親WidegtのTopへ上げる
        self.ui.widgetJudge.raise_()
        # 正解判定Widget非表示
        self.ui.widgetJudge.setVisible(False)

    # \brief 正解判定Widgetへの正誤判定描画追加と表示
    # \param[in] is_right True: 正解 / False:不正解
    def setUiJudge(self, is_right):
        # 正解判定 ○Ｘ画像表示用表示用 QGraphicsSceneのsceneデータを全てクリア
        self.graphics_scene_judge.clear()
        # 正解判定文字列のクリア
        self.ui.labelJudge.clear()

        if is_right:
            # 正解 ####################################
            # リソースファイルの○画像をQPixmapにセット
            pix_map = QPixmap(':/right.png')
            # "正解" 文字列("Right") をセット
            self.ui.labelJudge.setText(self.tr('Right'))
        else:
            # 不正解 #################################
            # リソースファイルのＸ画像をQPixmapにセット
            pix_map = QPixmap(':/wrong.png')
            # "不正解" 文字列("Wrong") をセット
            self.ui.labelJudge.setText(self.tr('Wrong'))

        # リンゴ画像表示用 QGraphicsSceneに、正誤○Ｘ画像のQPixmapをセット
        self.graphics_scene_judge.addPixmap(pix_map)
        # 正解判定Widget表示
        self.ui.widgetJudge.setVisible(True)

    # \brief Melonボタン クリック処理 (slot)
    def push_button_melon_clicked(self):
        self.setUiJudge(False)

    # \brief Appleボタン クリック処理 (slot)
    def push_button_apple_clicked(self):
        self.setUiJudge(True)

    # \brief Strawberryボタン クリック処理 (slot)
    def push_button_strawberry_clicked(self):
        self.setUiJudge(False)


def main():
    app = QApplication(sys.argv)
    app.setApplicationName('Section33Sample')

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
    （:/i18n/Section33Sample_${ロケール}.qm に完全一致するファイルを抽出）
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

    w = MainWindow('../ui/mainwindow.ui')
    w.ui.show()

    ret = app.exec_()
    sys.exit(ret)


if __name__ == '__main__':
    main()
