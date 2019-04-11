#include "mainwindow.h"
#include "ui_mainwindow.h"

#include <QGraphicsScene>

#include "translation.h"

/******************************************************************************/
/*!
 * \brief MainWindow::MainWindow コンストラクタ
 * \param[in] parent 親クラスQWidgetポインタ
 */
MainWindow::MainWindow(QWidget *parent)
  : QMainWindow(parent),
  ui(new Ui::MainWindow),
  translation(new Translation(parent)),
  graphics_scene_apple(new QGraphicsScene(parent)),
  graphics_scene_judge(new QGraphicsScene(parent)),
  is_judge(false)
{
  /// UI部分の初期表示
  UiInit();
}

/******************************************************************************/
/*!
 * \brief MainWindow::~MainWindow デストラクタ
 */
MainWindow::~MainWindow()
{
  delete ui;
}

/******************************************************************************/
/*!
 * \brief MainWindow::changeEvent Widgetイベントの取得
 * \param[in] event : QEventイベントタイプ
 */
void MainWindow::changeEvent(QEvent *event)
{
  /// 翻訳バイナリファイルがインストールされた時に発生するイベント
  if (event->type() == QEvent::LanguageChange) {
    /// uiファイルの再翻訳
    ui->retranslateUi(this);
    if (ui->widgetJudge->isVisible()) {
      /// クイズ 正解/不正解 表示の再翻訳
      setUiJudge(is_judge);
    }
  }
  QMainWindow::changeEvent(event);
}

/******************************************************************************/
/*!
 * \brief MainWindow::UiInit UI初期表示
 */
void MainWindow::UiInit()
{
  /// 親のMainWindow WidgetへUi::MainWindowのWidgetツリーの紐付け
  ui->setupUi(this);
  /// リンゴ画像表示用のQGraphicsViewクラスへ、リンゴ画像表示用 QGraphicsSceneをセット
  ui->graphicsView->setScene(graphics_scene_apple);
  /// リソースファイルのリンゴ画像をQPixmapにセット
  QPixmap pixmap(":/apple.png");
  /// リンゴ画像表示用 QGraphicsSceneに、リンゴ画像のQPixmapをセット
  graphics_scene_apple->addPixmap(pixmap);

  /*!
   * 正解判定 ○Ｘ画像表示用のQGraphicsViewクラスへ、
   * 正解判定 ○Ｘ画像表示用表示用 QGraphicsSceneをセット
   */
  ui->graphicsViewjudge->setScene(graphics_scene_judge);
  /// 正解判定Widgetを、親WidegtのTopへ上げる
  ui->widgetJudge->raise();
  /// 正解判定Widget非表示
  ui->widgetJudge->setVisible(false);

  /// 現在の取得している言語を取得
  Translation::Language lang = translation->getLanguage();
  /// 言語切り替えCombBoxの値に反映
  ui->comboBoxLanguage->setCurrentIndex(static_cast<int>(lang));
}

/******************************************************************************/
/*!
 * \brief MainWindow::setUiJudge 正解判定Widgetへの正誤判定描画追加と表示
 * \param[in] isRight true:正解 / false:不正解
 */
void MainWindow::setUiJudge(bool isRight)
{
  is_judge = isRight; ///< クラスメンバー(is_judge)に判定booleanをセット
  /// 正解判定 ○Ｘ画像表示用表示用 QGraphicsSceneのsceneデータを全てクリア
  graphics_scene_judge->clear();
  /// 正解判定文字列のクリア
  ui->labelJudge->clear();

  QPixmap pixmap;
  if (isRight) {
    /* 正解 */
    pixmap.load(":/right.png"); ///< リソースファイルの○画像をQPixmapにセット
    ui->labelJudge->setText(tr("Right")); ///< "正解"文字列("Right")をセット
  } else {
    /* 不正解 */
    pixmap.load(":/wrong.png"); ///< リソースファイルのＸ画像をQPixmapにセット
    ui->labelJudge->setText(tr("Wrong")); ///< "不正解"文字列("Wrong")をセット
  }
  /// リンゴ画像表示用 QGraphicsSceneに、正誤○Ｘ画像のQPixmapをセット
  graphics_scene_judge->addPixmap(pixmap);
  /// 正解判定Widget表示
  ui->widgetJudge->setVisible(true);
}

/******************************************************************************/
/*!
 * \brief MainWindow::on_action_Quit_triggered
 *          メニューバー(File - Exit)のアクション処理 (slot)
 */
void MainWindow::on_action_Quit_triggered()
{
  /// アプリケーションを閉じる
  qApp->quit();
}

/******************************************************************************/
/*!
 * \brief MainWindow::on_pushButtonMelon_clicked
 *          Melonボタン クリック処理 (slot)
 */
void MainWindow::on_pushButtonMelon_clicked()
{
  /// 不正解表示
  setUiJudge(false);
}

/******************************************************************************/
/*!
 * \brief MainWindow::on_pushButtonApple_clicked
 *          Appleボタン クリック処理 (slot)
 */
void MainWindow::on_pushButtonApple_clicked()
{
  /// 正解表示
  setUiJudge(true);
}

/******************************************************************************/
/*!
 * \brief MainWindow::on_pushButtonStrawbery_clicked
 *          Strawberyボタン クリック処理 (slot)
 */
void MainWindow::on_pushButtonStrawbery_clicked()
{
  /// 不正解表示
  setUiJudge(false);
}

/******************************************************************************/
/*!
 * \brief MainWindow::on_comboBoxLanguage_currentIndexChanged
 *          言語切り替えCombBox処理 (slot)
 * \param[in] index : コンボボックスindex値
 */
void MainWindow::on_comboBoxLanguage_currentIndexChanged(int index)
{
  /// CombBoxのインデックスに基づいて翻訳ファイルをインストール
  translation->setTranslation(static_cast<Translation::Language>(index));
}
