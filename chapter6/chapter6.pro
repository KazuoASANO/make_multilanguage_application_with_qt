# Qt for Pythonのプロジェクトは翻訳専用なので
# サブプロジェクトに含めない（C++のビルドエラーになる為）
TEMPLATE = subdirs

SUBDIRS += \
    $$PWD/Chapter6QtWidgetsSample \
    $$PWD/Chapter6QtQuickSample
