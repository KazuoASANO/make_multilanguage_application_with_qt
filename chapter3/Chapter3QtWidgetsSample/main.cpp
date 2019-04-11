#include "mainwindow.h"
#include <QApplication>
#include <QTranslator>  ///< 翻訳ファイルの設定で使用
#include <QLocale>      ///< ロケールの呼び出しで使用
#include <QDir>         ///< リソースファイルからのファイルサーチで使用

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
  QTranslator translator;

  /*!
   * Systemロケールの文字を取得（例：ja,zh）
   *
   * \note
   *  良く使用される国名コードの標準ISO3166(日本なら "jp")ではなく、
   *  BCP47 のうちSimple language subtag(言語コードの2文字。日本語なら"ja")
   *  を取得します。
   */
  QString locale = QLocale::system().bcp47Name();

  /*!
   * リソースファイルの :/i18nディレクトリから
   * 登録しているリソースファイルを抽出
   * （:/i18n/Section33Sample_*.qm にマッチするファイルを抽出）
   */
  QDir qm_dir(":/i18n");
  QString serch_name = app.applicationName() + "_*.qm";
  QStringList list_qm_files = qm_dir.entryList(QStringList(serch_name));
  foreach(const QString &qm_file, list_qm_files) {
    /// Systemロケールと一致するQt翻訳バイナリファイル名との一致確認
    if (qm_file.lastIndexOf(locale + ".qm") != -1) {
      QString load_file = qm_dir.absolutePath() + QDir::separator() + qm_file;
      /// QTranslatorクラスにQt翻訳バイナリファイルをセット
      if (translator.load(load_file)) {
        /// 翻訳バイナリファイルをアプリケーションに適用
        app.installTranslator(&translator);
      }
      break;
    }
  }

  /*!
   * \attention : MainWindowクラスより前に翻訳バイナリファイルを
   *              アプリケーションに適用しないと翻訳化されません。
   */
  MainWindow w;
  w.show();

  return app.exec();  ///< event loop
}
