#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>

/// uiファイルで生成されるMainWindows画面クラス
namespace Ui {
class MainWindow;
}

class Translation;
class QGraphicsScene;

/*!
 * \brief The MainWindow class フルーツクイズ画面制御クラス
 */
class MainWindow : public QMainWindow
{
 Q_OBJECT

 public:
  explicit MainWindow(QWidget *parent = Q_NULLPTR);
  ~MainWindow();

 protected:
  void changeEvent(QEvent *event);

 private:
  /// MainWindows画面クラス オブジェクト
  Ui::MainWindow *ui;
  /// 言語翻訳クラス オブジェクト
  Translation *translation;
  /// リンゴ画像表示用 QGraphicsSceneオブジェクト
  QGraphicsScene *graphics_scene_apple;
  /// 正解判定 ○Ｘ画像表示用 QGraphicsSceneオブジェクト
  QGraphicsScene *graphics_scene_judge;
  /// クイズ判定フラグ
  bool is_judge;

  void UiInit();
  void setUiJudge(bool isRight);

 private Q_SLOTS:
  void on_action_Quit_triggered();  ///< メニューバー(File - Exit)のアクション slot

  void on_pushButtonMelon_clicked();      ///< Melonボタン クリック slot
  void on_pushButtonApple_clicked();      ///< Appleボタン クリック slot
  void on_pushButtonStrawbery_clicked();  ///< Strawberyボタン クリック slot

  /// 言語切り替えCombBox (slot)
  void on_comboBoxLanguage_currentIndexChanged(int index);
};

#endif // MAINWINDOW_H
