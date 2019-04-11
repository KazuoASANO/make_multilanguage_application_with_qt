import QtQuick 2.12
import QtQuick.Controls 2.12

/*!
 * \breaf アプリホーム QMLオブジェクト
 */
HomeForm {
  // 正解・不正解用の判定booleanプロパティ
  property bool isJudge: false

  /*!
  * \brief 正誤判定描画追加と表示
  * \param[in] isRight true:正解 / false:不正解
  */
  function setUiJudge(isRight) {
    // HomeForm.ui _frame_judge QMLオブジェクトの表示を有効
    _frame_judge.visible = true;
    if (isRight) {
      _image_judge.source = "qrc:/right.png"  ///< リソースファイルの○画像をset
      _label_judge.text = qsTr("Right");      ///< "正解"文字列("Right")をset
    } else {
      _image_judge.source = "qrc:/wrong.png"  ///< リソースファイルのＸ画像をset
      _label_judge.text = qsTr("Wrong");      ///< "不正解"文字列("Wrong")をset
    }
    // 正解・不正解用の判定プロパティに正誤判定をセット
    isJudge = isRight;
  }

  /* HomeForm.uiでのボタンクリックslot処理 */
  _button_strawberry.onClicked: setUiJudge(false);  // 不正解表示
  _button_apple.onClicked:      setUiJudge(true);   // 正解表示
  _button_melon.onClicked:      setUiJudge(false);  // 不正解表示
}
