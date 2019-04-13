import QtQuick 2.12
import QtQuick.Controls 2.12
import QtQuick.Layouts 1.0

Page {
    id: _page
    width: 400
    height: 300
    property alias _combbox_language: _combbox_language
    property alias _button_strawberry: _button_strawberry
    property alias _button_apple: _button_apple
    property alias _button_melon: _button_melon
    property alias _frame_judge: _frame_judge
    property alias _image_judge: _image_judge
    property alias _label_judge: _label_judge

    ColumnLayout {
        x: 0
        y: 0
        width: parent.width
        height: parent.height
        anchors.horizontalCenter: parent.horizontalCenter

        ComboBox {
            id: _combbox_language
            x: 262
            y: 0
            Layout.alignment: Qt.AlignRight | Qt.AlignVCenter
            focusPolicy: Qt.NoFocus
            currentIndex: 2
            model: ListModel {
                id: _listmode_language
                ListElement {
                    text: qsTr("English")
                }
                ListElement {
                    text: qsTr("German")
                }
                ListElement {
                    text: qsTr("Japanese")
                }
                ListElement {
                    text: qsTr("Chinese")
                }
            }
        }
        Image {
            id: _image_apple
            width: 380
            height: 190
            Layout.alignment: Qt.AlignHCenter | Qt.AlignVCenter
            fillMode: Image.PreserveAspectFit
            source: "qrc:/apple.png"
        }

        Label {
            id: _label_question
            text: qsTr("What's is this?")
            verticalAlignment: Text.AlignVCenter
            font.pointSize: 16
            horizontalAlignment: Text.AlignHCenter
            Layout.alignment: Qt.AlignHCenter | Qt.AlignVCenter
        }

        RowLayout {
            Layout.alignment: Qt.AlignHCenter | Qt.AlignVCenter

            Button {
                id: _button_melon
                text: qsTr("Melon")
                display: AbstractButton.TextOnly
                font.pointSize: 15
                Layout.preferredWidth: 130
            }

            Button {
                id: _button_apple
                text: qsTr("Apple")
                font.pointSize: 15
                Layout.preferredWidth: 130
            }
            Button {
                id: _button_strawberry
                text: qsTr("Strawberry")
                font.pointSize: 15
                Layout.preferredWidth: 130
            }
        }
    }

    Frame {
        id: _frame_judge
        visible: false
        x: 0
        width: parent.width
        height: 225
        anchors.top: parent.top
        anchors.topMargin: 33
        anchors.horizontalCenter: parent.horizontalCenter

        Image {
            id: _image_judge
            anchors.fill: parent
            fillMode: Image.PreserveAspectFit

            Label {
                id: _label_judge
                anchors.horizontalCenter: parent.horizontalCenter
                anchors.verticalCenter: parent.verticalCenter
                anchors.top: parent.top
                font.pointSize: 20
                verticalAlignment: Text.AlignVCenter
                horizontalAlignment: Text.AlignHCenter
            }
        }
    }
}
