﻿import QtQuick 2.12
import QtQuick.Controls 2.12

/*!
 * \breaf Top-Lv アプリケーション ウィンドウ QMLオブジェクト
 */
ApplicationWindow {
  id: _window

  visible: true
  width: 400
  height: 350

  // 最小・最大サイズを、ApplicationWindowの 幅/高さ に合わせる
  minimumWidth: width
  minimumHeight: height
  maximumWidth: width
  maximumHeight: height

  // アプリケーションタイトル
  title: qsTr("Fruits Quiz")

  // アプリケーションメニューバー設定
  menuBar: MenuBar {
    Menu {
      title: qsTr("&File")
      MenuItem {
        text: qsTr("E&xit")
        // Exitが押されたら、アプリを閉じる
        onTriggered: Qt.quit()
      }
    }
  }

  // アプリホーム画面を設定
  Home {}
}
