#-------------------------------------------------------------------------------
# はじめてのQt 簡単！多言語対応のアプリをつくろう
# Chapter6 - Qt Widgets Sample
#
# \note
#   プロジェクトで使用している変数については、以下を参照。
#   qmake Manual - Variables
#     https://doc.qt.io/qt-5/qmake-variable-reference.html
#   qmake Manual - Replace Functions
#     https://doc.qt.io/qt-5/qmake-function-reference.html
#   qmake Manual - Test Functions
#     https://doc.qt.io/qt-5/qmake-test-function-reference.html
#   qmake Manual - Advanced Usage
#     https://doc.qt.io/Qt-5/qmake-advanced-usage.html
#-------------------------------------------------------------------------------

# プロジェクトで使用するQtモジュールを指定
#   core - Qt Core
#   gui  - Qt GUI
QT += core gui

# QT_MAJOR_VERSION(Qtのメジャーバージョン)が4より大きいかをテスト
#   Qt4までは、Qt Widgetsを使用する場合には、Qt GUIのモジュール指定だけ
#   でよかったが、Qt5からは
#   widgets - Qt Widgets
#   をモジュール指定する必要があるため。
greaterThan(QT_MAJOR_VERSION, 4): QT += widgets

# プロジェクトのターゲット名の指定
TARGET    = Chapter6QtWidgetsSample

# プロジェクトを生成するときに使用するテンプレートの指定
#   app - アプリケーションを構築するためのMakefileを作成
TEMPLATE  = app

# プロジェクト構成とコンパイラオプションの指定
#   c++11 - C++11のサポートを有効にします
#           ( このオプションは、コンパイラがC++11をサポートしていない場合、
#             またはC++標準を選択できない場合には効果なし )
CONFIG   += c++11

# Default rules for deployment
qnx:                   target.path = /tmp/$${TARGET}/bin
else: unix:!android:   target.path = /opt/$${TARGET}/bin
!isEmpty(target.path): INSTALLS += target

# build時に生成される、objectファイル等の出力先ディレクトリ名を
#  Qt Projectと同じ仕様に合わせる
load(qt_build_config)
################################################################################
# コンパイル時の検索 #includeディレクトリ指定
INCLUDEPATH += \
    $$PWD/src/

# プロジェクトで使用するソースファイル指定
SOURCES += \
    $$PWD/main.cpp \
    $$PWD/src/mainwindow.cpp \
    $$PWD/src/translation.cpp

# プロジェクトで使用するヘッダファイル指定
HEADERS += \
    $$PWD/src/mainwindow.h \
    $$PWD/src/translation.h

# プロジェクトで使用するuiファイル指定
FORMS += \
    $$PWD/ui/mainwindow.ui

# プロジェクトで使用するリソースファイル指定
RESOURCES += \
    image.qrc \
    i18n.qrc

# プロジェクトで使用する翻訳ファイル指定
# [参考情報]
#   "TRANSLATIONS"ではなく、"EXTRA_TRANSLATIONS"で指定された場合には、
#   lreleaseを使用してQt翻訳バイナリファイル( .qm )のみ
#   実行できるようになります。
#   ただしこの場合は、
#     CONFIG += lrelease
#     CONFIG += lrelease lrelease embed_translations
#   を設定した時に有効となり、Qt Creatorの「ツール(T)」経由での
#   lrelease実行では、認識されません
#   詳細は、"第7章 翻訳ファイルの自動生成と翻訳対象文字の自動保管"を参照してください。
#CONFIG += lrelease
#LRELEASE_DIR = $$PWD/i18n
TRANSLATIONS += \
    i18n/$${TARGET}_en.ts \
    i18n/$${TARGET}_de.ts \
    i18n/$${TARGET}_zh.ts \
    i18n/$${TARGET}_ja.ts
