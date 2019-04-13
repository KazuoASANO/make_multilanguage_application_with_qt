import sys
import image_rc
import i18n_rc
from PySide2.QtWidgets import QApplication, QGraphicsScene, QMainWindow
from PySide2.QtCore import QEvent
from PySide2.QtGui import QPixmap
from Translation import Translation
from MainWindow import Ui_MainWindow


class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        # 言語翻訳クラス オブジェクト
        self.translation = Translation(self)

        # file = QFile(ui_file)
        # file.open(QFile.ReadOnly)
        #
        # # 指定されたuiファイルを QUiLoader 経由で読み出す
        # loader = QUiLoader()
        # self.ui = loader.load(file)
        #
        # 動的翻訳の場合は、QUiLoader()系でのuiファイル直接loadではなく
        # uicを使用して、uiファイルをPythonファイルに変換してから使用する。
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # リンゴ画像表示用 QGraphicsSceneオブジェクト生成
        self.graphics_scene_apple = QGraphicsScene(self)
        # 正解判定 ○Ｘ画像表示用 QGraphicsSceneオブジェクト生成
        self.graphics_scene_judge = QGraphicsScene(self)
        # クイズ判定フラグ
        self.is_judge = False
        self.ui_init()

        # uiとのsignal / slot接続
        self.ui.action_Quit.triggered.connect(sys.exit)
        self.ui.pushButtonMelon.clicked.connect(self.push_button_melon_clicked)
        self.ui.pushButtonApple.clicked.connect(self.push_button_apple_clicked)
        self.ui.pushButtonStrawbery.clicked.connect(
            self.push_button_strawberry_clicked)
        self.ui.comboBoxLanguage.currentIndexChanged.connect(
            self.combobox_language_currentindex_changed)

    # \brief MainWindow::changeEvent Widgetイベントの取得
    # \param[in] event : QEventイベントタイプ
    def changeEvent(self, event):
        # 翻訳バイナリファイルがインストールされた時に発生するイベント
        if event.type() == QEvent.LanguageChange:
            # GUIパーツ再描画
            self.ui.retranslateUi(self)
            if self.ui.widgetJudge.isVisible():
                # クイズ 正解/不正解 表示の再翻訳
                self.setUiJudge(self.is_judge)

        super(MainWindow, self).changeEvent(event)

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

        # 現在の取得している言語を取得
        lang_num = self.translation.language()
        # 言語切り替えCombBoxの値に反映
        self.ui.comboBoxLanguage.setCurrentIndex(lang_num)

    # \brief 正解判定Widgetへの正誤判定描画追加と表示
    # \param[in] is_right True: 正解 / False:不正解
    def setUiJudge(self, is_right):
        # クラスメンバー(is_judge)に判定booleanをセット
        self.is_judge = is_right
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

        # 現在の取得している言語を取得
        lang_index = self.translation.language()
        # 言語切り替えCombBoxの値に反映
        self.ui.comboBoxLanguage.setCurrentIndex(lang_index)

    # \brief Melonボタン クリック処理 (slot)
    def push_button_melon_clicked(self):
        self.setUiJudge(False)

    # \brief Appleボタン クリック処理 (slot)
    def push_button_apple_clicked(self):
        self.setUiJudge(True)

    # \brief Strawberryボタン クリック処理 (slot)
    def push_button_strawberry_clicked(self):
        self.setUiJudge(False)

    # \brief 言語切り替えCombBox処理 (slot)
    # \param[in] index : コンボボックスindex値
    def combobox_language_currentindex_changed(self, index):
        # CombBoxのインデックスに基づいて翻訳ファイルをインストール
        self.translation.set_language(index)


def main():
    app = QApplication(sys.argv)
    app.setApplicationName('Chapter6PythonQtWidgetsSample')

    w = MainWindow()
    w.show()

    ret = app.exec_()
    sys.exit(ret)


if __name__ == '__main__':
    main()
