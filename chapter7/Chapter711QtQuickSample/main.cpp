#include <QGuiApplication>
#include <QTranslator>
#include <QLocale>
#include <QDir>
#include <QQmlApplicationEngine>
#include <QQmlContext>

#include <translation.h>

/******************************************************************************/
/*!
 * \brief main main関数
 * \param[in] argc コマンドラインオプションの数
 * \param[in] argv コマンドラインプションそれぞれの文字列へのポインタ
 * \return
 */
int main(int argc, char *argv[])
{
  QCoreApplication::setAttribute(Qt::AA_EnableHighDpiScaling);

  QGuiApplication app(argc, argv);
  QQmlApplicationEngine engine;

  /// 動的翻訳処理クラスの生成
  Translation translation(&engine);
  /// translationクラス変数を、QMLへ"Translation"として公開する
  engine.rootContext()->setContextProperty("Translation", &translation);
  /// リソースファイルから、ui/main.qmlをアプリケーションのtop viewとしてロード
  engine.load(QUrl(QStringLiteral("qrc:/ui/main.qml")));
  if (engine.rootObjects().isEmpty())
    return -1;

  return app.exec();  ///< event loop
}
