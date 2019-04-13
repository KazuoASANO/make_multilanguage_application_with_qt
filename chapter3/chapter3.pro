# Qt for Pythonのプロジェクトは翻訳専用なので
# サブプロジェクトに含めない（C++のビルドエラーになる為）
TEMPLATE = subdirs

SUBDIRS += \
    $$PWD/Chapter3QtWidgetsSample \
    $$PWD/Chapter3QtQuickSample
