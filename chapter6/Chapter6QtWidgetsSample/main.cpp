#include "mainwindow.h"
#include <QApplication>
#include <QTranslator>
#include <QLocale>
#include <QDir>

/******************************************************************************/
/*!
 * \brief main main関数
 * \param[in] argc コマンドラインオプションの数
 * \param[in] argv コマンドラインプションそれぞれの文字列へのポインタ
 * \return
 */
int main(int argc, char *argv[])
{
  QApplication app(argc, argv);
  MainWindow w;
  w.show();

  return app.exec();  ///< event loop
}
