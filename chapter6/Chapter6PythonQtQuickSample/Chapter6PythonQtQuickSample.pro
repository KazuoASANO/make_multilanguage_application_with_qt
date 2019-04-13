#-------------------------------------------------------------------------------
# はじめてのQt 簡単！多言語対応のアプリをつくろう
# Chapter6 - Qt Quick Sample with Qt for Python
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
TARGET = Chapter6PythonQtQuickSample

################################################################################
# プロジェクトで使用するソースファイル指定
# \note
#  プロジェクトから追加した場合、Python Codeは、
#    DISTFILES
#  以下に配置されるが、-lupdateを有効
SOURCES += \
    $$PWD/src/main.py \
    $$PWD/src/Translation.py

# プロジェクトで使用する、雑ファイル指定
OTHER_FILES += \
    $$PWD/qtquickcontrols2.conf     # Qt Quick Controls Configuration File

# プロジェクトで使用するリソースファイル指定
RESOURCES += \
    $$PWD/qml.qrc \
    $$PWD/image.qrc \
    $$PWD/i18n.qrc

# プロジェクトで使用する翻訳ファイル指定
TRANSLATIONS += \
    i18n/$${TARGET}_en.ts \
    i18n/$${TARGET}_de.ts \
    i18n/$${TARGET}_zh.ts \
    i18n/$${TARGET}_ja.ts

# qmlファイルをlupdateで検出できるようにする設定
#
# lupdate_only {} で囲み、その中に SOURCES 変数にて
# QMLファイルを登録します。 lupdate_onlyの文字列は、Qtプロジェクト上で
# 定義していない為、真偽値が"偽"となりコンパイル時には使用されません。
#
# 次の例では、プロジェクトファイル内に、3つのQMLファイルを指定しています。
lupdate_only {
  SOURCES += \
    $$PWD/ui/Home.qml \
    $$PWD/ui/HomeForm.ui.qml \
    $$PWD/ui/main.qml
}
# <非推奨な書き方>
# lupdate にて、QMLファイルの特定ができず
# Qt Linguistの「ソーステキストビュー」にQMLコードが表示されません。
#lupdate_only {
# SOURCES += \
#   $$PWD/ui/*.qml
#}
