#include "translation.h"

#include <QTranslator>
#include <QLocale>      ///< ロケールの呼び出しで使用
#include <QDir>         ///< リソースファイルからのファイルサーチで使用
#include <QApplication> ///< 翻訳ファイルのremove / installで使用

/******************************************************************************/

/*! \brief ロケール言語文字列 */
static const char *language_strings[] = {
  "en", ///< 英語
  "de", ///< ドイツ語
  "ja", ///< 日本語
  "zh"  ///< 中国語
};

/******************************************************************************/
/*!
 * \brief Translation::Translation コンストラクタ
 * \param[in] parent 親クラスのQObjectポインタ
 */
Translation::Translation(QObject *parent)
  : QObject(parent),
  translator(new QTranslator(parent))
{
  /*!
   * Systemロケールの文字を取得（例：ja,zh）
   *
   * \note
   *  良く使用される国名コードの標準ISO3166(日本なら "jp")ではなく、
   *  BCP47 のうちSimple language subtag(言語コードの2文字。日本語なら"ja")
   *  を取得します。
   */
  locale = QLocale::system().bcp47Name();
  /// 現在のロケールのenum値取得
  Language lang = getLanguage();
  /// 翻訳ファイルのセット
  setTranslation(lang);
}

/******************************************************************************/
/*!
 * \brief Translation::getLanguage 現在のロケールの言語を取得
 * \return Translation::Language値
 */
Translation::Language Translation::getLanguage()
{
  int language_num;

  /// 現在のロケールから、設定できるロケール言語文字列の配列番号取得
  int max_language_num = sizeof(language_strings) / sizeof (char*);
  for (language_num = 0; language_num < max_language_num; ++language_num) {
    if ( locale.compare(language_strings[language_num], Qt::CaseSensitive) == 0 ) {
      break;
    }
  }

  /// ロケール文字が一致しない場合は、英語にする
  if (max_language_num == language_num) {
    language_num = LanguageEnglish;
    locale = language_strings[language_num];
  }

  return static_cast<Language>(language_num);
}

/******************************************************************************/
/*!
 * \brief Translation::setTranslation 翻訳ファイルをインストールする
 * \param[in] language : インストールする言語
 */
void Translation::setTranslation(Translation::Language language)
{
  locale = language_strings[language];

  /*!
   * リソースファイルの :/i18nディレクトリから
   * 登録しているリソースファイルを抽出
   * （:/i18n/$${TARGET}_*.qm にマッチするファイルを抽出）
   */
  QDir qm_dir(":/i18n");
  QString serch_name = qApp->applicationName() + "_*.qm";
  QStringList list_qm_files = qm_dir.entryList(QStringList(serch_name));
  foreach(const QString &qm_file, list_qm_files) {
    /// Systemロケールと一致するQt翻訳バイナリファイル名との一致確認
    if (qm_file.lastIndexOf(locale + ".qm") != -1) {
      /// 以前の翻訳ファイルをremove
      qApp->removeTranslator(translator);

      QString load_file = qm_dir.absolutePath() + QDir::separator() + qm_file;
      /// QTranslatorクラスにQt翻訳バイナリファイルをセット
      if (translator->load(load_file)) {
        /// 翻訳バイナリファイルをアプリケーションに適用
        qApp->installTranslator(translator);
      }
      break;
    }
  }
}
