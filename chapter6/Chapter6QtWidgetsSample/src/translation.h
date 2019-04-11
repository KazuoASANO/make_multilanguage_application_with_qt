#ifndef TRANSLATION_H
#define TRANSLATION_H

#include <QObject>

class QTranslator;

/*!
 * \brief The Translation class 言語翻訳制御クラス
 */
class Translation : public QObject
{
 Q_OBJECT
 public:
  /*!
   * \brief The Language enum 翻訳対応言語
   */
  enum Language {
    LanguageEnglish = 0,  ///< 英語
    LanguageGerman,       ///< ドイツ語
    LanguageJapanese,     ///< 日本語
    LanguageChinese       ///< 中国語
  };
  Q_ENUM(Language)

 public:
  explicit Translation(QObject *parent = Q_NULLPTR);
  Language getLanguage();
  void setTranslation(Language language);

 private:
  /// Qt国際化対応クラス オブジェクト
  QTranslator *translator;
  /// ロケール言語文字列(BCP47 のうちSimple language subtag(言語コードの2文字))
  QString locale;
};

#endif // TRANSLATION_H
