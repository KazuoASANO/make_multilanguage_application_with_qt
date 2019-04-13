#-------------------------------------------------------------------------------
# はじめてのQt 簡単！多言語対応のアプリをつくろう
# Chapter3 - Qt Widgets Sample with Qt for Python
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

# プロジェクトのターゲット名の指定
TARGET    = Section33Sample

################################################################################
# プロジェクトで使用するソースファイル指定
# \note
#  プロジェクトから追加した場合、Python Codeは、
#    DISTFILES
#  以下に配置されるが、-lupdateを有効
SOURCES += \
    $$PWD/src/main.py

# プロジェクトで使用するuiファイル指定
FORMS += \
    $$PWD/ui/mainwindow.ui

# プロジェクトで使用するリソースファイル指定
RESOURCES += \
    image.qrc \
    i18n.qrc

# プロジェクトで使用する翻訳ファイル指定
TRANSLATIONS += \
    i18n/$${TARGET}_en.ts \
    i18n/$${TARGET}_de.ts \
    i18n/$${TARGET}_zh.ts \
    i18n/$${TARGET}_ja.ts
