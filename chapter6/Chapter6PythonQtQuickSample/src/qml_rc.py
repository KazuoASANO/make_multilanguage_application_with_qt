# -*- coding: utf-8 -*-

# Resource object code
#
# Created: 日 4月 14 08:24:21 2019
#      by: The Resource Compiler for PySide2 (Qt v5.12.2)
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore

qt_resource_data = b"\
\x00\x00\x02\xc3\
\xef\
\xbb\xbf;;;;;;;;;;;;;;\
;;;;;;;;;;;;;;;;\
;;;;;;;;;;;;;;;;\
;;;;;;;;;;;;;;;;\
;;;;;;;;;;;;;;;;\
;;\x0a; Qt\xe3\x82\xaf\xe3\x82\xa4\xe3\x83\x83\
\xe3\x82\xaf\xe3\x82\xb3\xe3\x83\xb3\xe3\x83\x88\xe3\x83\xad\xe3\
\x83\xbc\xe3\x83\xab\xe8\xa8\xad\xe5\xae\x9a\xe3\x83\x95\xe3\x82\
\xa1\xe3\x82\xa4\xe3\x83\xab\x0a;   (Qt \
Quick Controls C\
onfiguration Fil\
e)\x0a;\x0a; Qt Quick \
Controls2\xe3\x81\xa7\xe4\xbd\xbf\xe7\
\x94\xa8\xe3\x81\x99\xe3\x82\x8b\xe3\x82\xb9\xe3\x82\xbf\xe3\x82\
\xa4\xe3\x83\xab\xe6\xa7\x8b\xe6\x88\x90\xe3\x83\x95\xe3\x82\xa1\
\xe3\x82\xa4\xe3\x83\xab\x0a; \xe3\x82\xb9\xe3\x82\xbf\xe3\
\x82\xa4\xe3\x83\xab\xe3\x81\xa8\xe7\x89\xb9\xe5\xae\x9a\xe3\x82\
\xb9\xe3\x82\xbf\xe3\x82\xa4\xe3\x83\xab\xe5\x9b\xba\xe6\x9c\x89\
\xe3\x81\xae\xe5\xb1\x9e\xe6\x80\xa7\xe3\x82\x92\xe6\x8c\x87\xe5\
\xae\x9a\xe3\x81\x99\xe3\x82\x8b\xe3\x80\x82\x0a;\x0a; \
\x5cnote\x0a;   \xe8\xa9\xb3\xe7\xb4\xb0\
\xe3\x81\xab\xe3\x81\xa4\xe3\x81\x84\xe3\x81\xa6\xe3\x81\xaf\xe3\
\x80\x81\xe4\xbb\xa5\xe4\xb8\x8b\xe3\x82\x92\xe5\x8f\x82\xe7\x85\
\xa7\xe3\x80\x82\x0a;   https:/\
/doc.qt.io/qt-5/\
qtquickcontrols2\
-configuration.h\
tml\x0a;;;;;;;;;;;;\
;;;;;;;;;;;;;;;;\
;;;;;;;;;;;;;;;;\
;;;;;;;;;;;;;;;;\
;;;;;;;;;;;;;;;;\
;;;;\x0a\x0a[Controls]\
\x0a;Style=Default\x0a\
;Style=Fusion\x0a;S\
tyle=Universal\x0aS\
tyle=Material\x0a;S\
tyle=Imagine\x0a\x0a[M\
aterial]\x0a;Theme=\
Light\x0a;Theme=Dar\
k\x0aTheme=System\x0a\x0a\
[Universal]\x0a;The\
me=Light\x0a;Theme=\
Dark\x0aTheme=Syste\
m\x0a\
\x00\x00\x0d\x04\
\xef\
\xbb\xbfimport QtQuick\
 2.12\x0aimport QtQ\
uick.Controls 2.\
12\x0aimport QtQuic\
k.Layouts 1.0\x0a\x0aP\
age {\x0a    id: _p\
age\x0a    width: 4\
00\x0a    height: 3\
00\x0a    property \
alias _combbox_l\
anguage: _combbo\
x_language\x0a    p\
roperty alias _b\
utton_strawberry\
: _button_strawb\
erry\x0a    propert\
y alias _button_\
apple: _button_a\
pple\x0a    propert\
y alias _button_\
melon: _button_m\
elon\x0a    propert\
y alias _frame_j\
udge: _frame_jud\
ge\x0a    property \
alias _image_jud\
ge: _image_judge\
\x0a    property al\
ias _label_judge\
: _label_judge\x0a\x0a\
    ColumnLayout\
 {\x0a        x: 0\x0a\
        y: 0\x0a   \
     width: pare\
nt.width\x0a       \
 height: parent.\
height\x0a        a\
nchors.horizonta\
lCenter: parent.\
horizontalCenter\
\x0a\x0a        ComboB\
ox {\x0a           \
 id: _combbox_la\
nguage\x0a         \
   x: 262\x0a      \
      y: 0\x0a     \
       Layout.al\
ignment: Qt.Alig\
nRight | Qt.Alig\
nVCenter\x0a       \
     focusPolicy\
: Qt.NoFocus\x0a   \
         current\
Index: 2\x0a       \
     model: List\
Model {\x0a        \
        id: _lis\
tmode_language\x0a \
               L\
istElement {\x0a   \
                \
 text: qsTr(\x22Eng\
lish\x22)\x0a         \
       }\x0a       \
         ListEle\
ment {\x0a         \
           text:\
 qsTr(\x22German\x22)\x0a\
                \
}\x0a              \
  ListElement {\x0a\
                \
    text: qsTr(\x22\
Japanese\x22)\x0a     \
           }\x0a   \
             Lis\
tElement {\x0a     \
               t\
ext: qsTr(\x22Chine\
se\x22)\x0a           \
     }\x0a         \
   }\x0a        }\x0a \
       Image {\x0a \
           id: _\
image_apple\x0a    \
        width: 3\
80\x0a            h\
eight: 190\x0a     \
       Layout.al\
ignment: Qt.Alig\
nHCenter | Qt.Al\
ignVCenter\x0a     \
       fillMode:\
 Image.PreserveA\
spectFit\x0a       \
     source: \x22qr\
c:/apple.png\x22\x0a  \
      }\x0a\x0a       \
 Label {\x0a       \
     id: _label_\
question\x0a       \
     text: qsTr(\
\x22What's is this?\
\x22)\x0a            v\
erticalAlignment\
: Text.AlignVCen\
ter\x0a            \
font.pointSize: \
16\x0a            h\
orizontalAlignme\
nt: Text.AlignHC\
enter\x0a          \
  Layout.alignme\
nt: Qt.AlignHCen\
ter | Qt.AlignVC\
enter\x0a        }\x0a\
\x0a        RowLayo\
ut {\x0a           \
 Layout.alignmen\
t: Qt.AlignHCent\
er | Qt.AlignVCe\
nter\x0a\x0a          \
  Button {\x0a     \
           id: _\
button_melon\x0a   \
             tex\
t: qsTr(\x22Melon\x22)\
\x0a               \
 display: Abstra\
ctButton.TextOnl\
y\x0a              \
  font.pointSize\
: 15\x0a           \
     Layout.pref\
erredWidth: 130\x0a\
            }\x0a\x0a \
           Butto\
n {\x0a            \
    id: _button_\
apple\x0a          \
      text: qsTr\
(\x22Apple\x22)\x0a      \
          font.p\
ointSize: 15\x0a   \
             Lay\
out.preferredWid\
th: 130\x0a        \
    }\x0a          \
  Button {\x0a     \
           id: _\
button_strawberr\
y\x0a              \
  text: qsTr(\x22St\
rawberry\x22)\x0a     \
           font.\
pointSize: 15\x0a  \
              La\
yout.preferredWi\
dth: 130\x0a       \
     }\x0a        }\
\x0a    }\x0a\x0a    Fram\
e {\x0a        id: \
_frame_judge\x0a   \
     visible: fa\
lse\x0a        x: 0\
\x0a        width: \
parent.width\x0a   \
     height: 225\
\x0a        anchors\
.top: parent.top\
\x0a        anchors\
.topMargin: 33\x0a \
       anchors.h\
orizontalCenter:\
 parent.horizont\
alCenter\x0a\x0a      \
  Image {\x0a      \
      id: _image\
_judge\x0a         \
   anchors.fill:\
 parent\x0a        \
    fillMode: Im\
age.PreserveAspe\
ctFit\x0a\x0a         \
   Label {\x0a     \
           id: _\
label_judge\x0a    \
            anch\
ors.horizontalCe\
nter: parent.hor\
izontalCenter\x0a  \
              an\
chors.verticalCe\
nter: parent.ver\
ticalCenter\x0a    \
            anch\
ors.top: parent.\
top\x0a            \
    font.pointSi\
ze: 20\x0a         \
       verticalA\
lignment: Text.A\
lignVCenter\x0a    \
            hori\
zontalAlignment:\
 Text.AlignHCent\
er\x0a            }\
\x0a        }\x0a    }\
\x0a}\x0a\
\x00\x00\x04\xd2\
\xef\
\xbb\xbfimport QtQuick\
 2.12\x0aimport QtQ\
uick.Controls 2.\
12\x0a\x0a/*!\x0a * \x5cbrea\
f \xe3\x82\xa2\xe3\x83\x97\xe3\x83\xaa\xe3\x83\x9b\xe3\x83\
\xbc\xe3\x83\xa0 QML\xe3\x82\xaa\xe3\x83\x96\xe3\x82\
\xb8\xe3\x82\xa7\xe3\x82\xaf\xe3\x83\x88\x0a */\x0aH\
omeForm {\x0a  // \xe6\
\xad\xa3\xe8\xa7\xa3\xe3\x83\xbb\xe4\xb8\x8d\xe6\xad\xa3\xe8\xa7\
\xa3\xe7\x94\xa8\xe3\x81\xae\xe5\x88\xa4\xe5\xae\x9aboo\
lean\xe3\x83\x97\xe3\x83\xad\xe3\x83\x91\xe3\x83\x86\
\xe3\x82\xa3\x0a  property b\
ool isJudge: fal\
se\x0a\x0a  /*!\x0a  * \x5cb\
rief \xe6\xad\xa3\xe8\xaa\xa4\xe5\x88\xa4\xe5\xae\
\x9a\xe6\x8f\x8f\xe7\x94\xbb\xe8\xbf\xbd\xe5\x8a\xa0\xe3\x81\xa8\
\xe8\xa1\xa8\xe7\xa4\xba\x0a  * \x5cpara\
m[in] isRight tr\
ue:\xe6\xad\xa3\xe8\xa7\xa3 / fals\
e:\xe4\xb8\x8d\xe6\xad\xa3\xe8\xa7\xa3\x0a  */\
\x0a  function setU\
iJudge(isRight) \
{\x0a    // HomeFor\
m.ui _frame_judg\
e QML\xe3\x82\xaa\xe3\x83\x96\xe3\x82\xb8\xe3\x82\
\xa7\xe3\x82\xaf\xe3\x83\x88\xe3\x81\xae\xe8\xa1\xa8\xe7\xa4\xba\
\xe3\x82\x92\xe6\x9c\x89\xe5\x8a\xb9\x0a    _f\
rame_judge.visib\
le = true;\x0a    i\
f (isRight) {\x0a  \
    _image_judge\
.source = \x22qrc:/\
right.png\x22  ///<\
 \xe3\x83\xaa\xe3\x82\xbd\xe3\x83\xbc\xe3\x82\xb9\xe3\x83\x95\
\xe3\x82\xa1\xe3\x82\xa4\xe3\x83\xab\xe3\x81\xae\xe2\x97\x8b\xe7\
\x94\xbb\xe5\x83\x8f\xe3\x82\x92set\x0a    \
  _label_judge.t\
ext = qsTr(\x22Righ\
t\x22);      ///< \x22\
\xe6\xad\xa3\xe8\xa7\xa3\x22\xe6\x96\x87\xe5\xad\x97\xe5\x88\x97\
(\x22Right\x22)\xe3\x82\x92set\x0a\
    } else {\x0a   \
   _image_judge.\
source = \x22qrc:/w\
rong.png\x22  ///< \
\xe3\x83\xaa\xe3\x82\xbd\xe3\x83\xbc\xe3\x82\xb9\xe3\x83\x95\xe3\
\x82\xa1\xe3\x82\xa4\xe3\x83\xab\xe3\x81\xae\xef\xbc\xb8\xe7\x94\
\xbb\xe5\x83\x8f\xe3\x82\x92set\x0a     \
 _label_judge.te\
xt = qsTr(\x22Wrong\
\x22);      ///< \x22\xe4\
\xb8\x8d\xe6\xad\xa3\xe8\xa7\xa3\x22\xe6\x96\x87\xe5\xad\x97\xe5\
\x88\x97(\x22Wrong\x22)\xe3\x82\x92se\
t\x0a    }\x0a    // \xe6\
\xad\xa3\xe8\xa7\xa3\xe3\x83\xbb\xe4\xb8\x8d\xe6\xad\xa3\xe8\xa7\
\xa3\xe7\x94\xa8\xe3\x81\xae\xe5\x88\xa4\xe5\xae\x9a\xe3\x83\x97\
\xe3\x83\xad\xe3\x83\x91\xe3\x83\x86\xe3\x82\xa3\xe3\x81\xab\xe6\
\xad\xa3\xe8\xaa\xa4\xe5\x88\xa4\xe5\xae\x9a\xe3\x82\x92\xe3\x82\
\xbb\xe3\x83\x83\xe3\x83\x88\x0a    isJu\
dge = isRight;\x0a \
 }\x0a\x0a  /* HomeFor\
m.ui\xe3\x81\xa7\xe3\x81\xae\xe3\x83\x9c\xe3\x82\xbf\
\xe3\x83\xb3\xe3\x82\xaf\xe3\x83\xaa\xe3\x83\x83\xe3\x82\xafs\
lot\xe5\x87\xa6\xe7\x90\x86 */\x0a  _\
button_strawberr\
y.onClicked: set\
UiJudge(false); \
 // \xe4\xb8\x8d\xe6\xad\xa3\xe8\xa7\xa3\xe8\xa1\xa8\
\xe7\xa4\xba\x0a  _button_ap\
ple.onClicked:  \
    setUiJudge(t\
rue);   // \xe6\xad\xa3\xe8\xa7\
\xa3\xe8\xa1\xa8\xe7\xa4\xba\x0a  _butto\
n_melon.onClicke\
d:      setUiJud\
ge(false);  // \xe4\
\xb8\x8d\xe6\xad\xa3\xe8\xa7\xa3\xe8\xa1\xa8\xe7\xa4\xba\x0a}\
\x0a\
\x00\x00\x04\xc7\
\xef\
\xbb\xbfimport QtQuick\
 2.12\x0aimport QtQ\
uick.Controls 2.\
12\x0a\x0a/*!\x0a * \x5cbrea\
f Top-Lv \xe3\x82\xa2\xe3\x83\x97\xe3\
\x83\xaa\xe3\x82\xb1\xe3\x83\xbc\xe3\x82\xb7\xe3\x83\xa7\xe3\x83\
\xb3 \xe3\x82\xa6\xe3\x82\xa3\xe3\x83\xb3\xe3\x83\x89\xe3\x82\
\xa6 QML\xe3\x82\xaa\xe3\x83\x96\xe3\x82\xb8\xe3\x82\
\xa7\xe3\x82\xaf\xe3\x83\x88\x0a */\x0aAppl\
icationWindow {\x0a\
  id: _window\x0a\x0a \
 visible: true\x0a \
 width: 400\x0a  he\
ight: 350\x0a\x0a  // \
\xe6\x9c\x80\xe5\xb0\x8f\xe3\x83\xbb\xe6\x9c\x80\xe5\xa4\xa7\xe3\
\x82\xb5\xe3\x82\xa4\xe3\x82\xba\xe3\x82\x92\xe3\x80\x81Ap\
plicationWindow\xe3\
\x81\xae \xe5\xb9\x85/\xe9\xab\x98\xe3\x81\x95 \xe3\x81\
\xab\xe5\x90\x88\xe3\x82\x8f\xe3\x81\x9b\xe3\x82\x8b\x0a  \
minimumWidth: wi\
dth\x0a  minimumHei\
ght: height\x0a  ma\
ximumWidth: widt\
h\x0a  maximumHeigh\
t: height\x0a\x0a  // \
\xe3\x82\xa2\xe3\x83\x97\xe3\x83\xaa\xe3\x82\xb1\xe3\x83\xbc\xe3\
\x82\xb7\xe3\x83\xa7\xe3\x83\xb3\xe3\x82\xbf\xe3\x82\xa4\xe3\x83\
\x88\xe3\x83\xab\x0a  title: qs\
Tr(\x22Fruits Quiz\x22\
)\x0a\x0a  // \xe3\x82\xa2\xe3\x83\x97\xe3\x83\
\xaa\xe3\x82\xb1\xe3\x83\xbc\xe3\x82\xb7\xe3\x83\xa7\xe3\x83\xb3\
\xe3\x83\xa1\xe3\x83\x8b\xe3\x83\xa5\xe3\x83\xbc\xe3\x83\x90\xe3\
\x83\xbc\xe8\xa8\xad\xe5\xae\x9a\x0a  menuB\
ar: MenuBar {\x0a  \
  Menu {\x0a      t\
itle: qsTr(\x22&Fil\
e\x22)\x0a      MenuIt\
em {\x0a        tex\
t: qsTr(\x22E&xit\x22)\
\x0a        // Exit\
\xe3\x81\x8c\xe6\x8a\xbc\xe3\x81\x95\xe3\x82\x8c\xe3\x81\x9f\xe3\
\x82\x89\xe3\x80\x81\xe3\x82\xa2\xe3\x83\x97\xe3\x83\xaa\xe3\x82\
\x92\xe9\x96\x89\xe3\x81\x98\xe3\x82\x8b\x0a     \
   onTriggered: \
Qt.quit()\x0a      \
}\x0a    }\x0a  }\x0a\x0a  /\
/ \xe3\x82\xa2\xe3\x83\x97\xe3\x83\xaa\xe3\x83\x9b\xe3\x83\
\xbc\xe3\x83\xa0\xe7\x94\xbb\xe9\x9d\xa2\xe3\x82\x92\xe8\xa8\xad\
\xe5\xae\x9a\x0a  Home {\x0a   \
 /* HomeForm.ui\xe3\
\x81\xa7\xe3\x81\xae\xe3\x82\xb3\xe3\x83\xb3\xe3\x83\x9c\xe3\x83\
\x9c\xe3\x83\x83\xe3\x82\xaf\xe3\x82\xb9 index\
\xe5\xa4\x89\xe6\x9b\xb4 slot\xe5\x87\xa6\xe7\x90\
\x86 */\x0a    _combbo\
x_language.onCur\
rentIndexChanged\
: {\x0a      // C++\
\xe3\x81\xae\xe3\x83\x97\xe3\x83\xad\xe3\x83\x91\xe3\x83\x86\xe3\
\x82\xa3\xe5\x8c\x96\xe3\x81\x97\xe3\x81\x9fTrans\
lation\xe3\x82\xaf\xe3\x83\xa9\xe3\x82\xb9\xe3\
\x81\xa7\xe3\x81\xae\xe7\xbf\xbb\xe8\xa8\xb3\xe3\x83\x95\xe3\x82\
\xa1\xe3\x82\xa4\xe3\x83\xab\xe3\x82\x92\xe3\x82\xa4\xe3\x83\xb3\
\xe3\x82\xb9\xe3\x83\x88\xe3\x83\xbc\xe3\x83\xab\xe5\x87\xa6\xe7\
\x90\x86\x0a      Transla\
tion.language = \
_combbox_languag\
e.currentIndex;\x0a\
      if (_frame\
_judge.visible =\
== true) {\x0a     \
   // \xe3\x82\xaf\xe3\x82\xa4\xe3\x82\xba \
\xe6\xad\xa3\xe8\xa7\xa3/\xe4\xb8\x8d\xe6\xad\xa3\xe8\xa7\xa3\
 \xe8\xa1\xa8\xe7\xa4\xba\xe3\x81\xae\xe5\x86\x8d\xe6\x8f\x8f\
\xe7\x94\xbb\x0a        setU\
iJudge(isJudge);\
\x0a      }\x0a    }\x0a \
 }\x0a\x0a}\x0a\
"

qt_resource_name = b"\
\x00\x15\
\x08\x1e\x16f\
\x00q\
\x00t\x00q\x00u\x00i\x00c\x00k\x00c\x00o\x00n\x00t\x00r\x00o\x00l\x00s\x002\x00.\
\x00c\x00o\x00n\x00f\
\x00\x02\
\x00\x00\x07\xb9\
\x00u\
\x00i\
\x00\x0f\
\x02\x83\xbc\xbc\
\x00H\
\x00o\x00m\x00e\x00F\x00o\x00r\x00m\x00.\x00u\x00i\x00.\x00q\x00m\x00l\
\x00\x08\
\x068a\xdc\
\x00H\
\x00o\x00m\x00e\x00.\x00q\x00m\x00l\
\x00\x08\
\x08\x01Z\x5c\
\x00m\
\x00a\x00i\x00n\x00.\x00q\x00m\x00l\
"

qt_resource_struct = b"\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x02\x00\x00\x00\x01\
\x00\x00\x000\x00\x02\x00\x00\x00\x03\x00\x00\x00\x03\
\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\
\x00\x00\x00:\x00\x00\x00\x00\x00\x01\x00\x00\x02\xc7\
\x00\x00\x00^\x00\x00\x00\x00\x00\x01\x00\x00\x0f\xcf\
\x00\x00\x00t\x00\x00\x00\x00\x00\x01\x00\x00\x14\xa5\
"

def qInitResources():
    QtCore.qRegisterResourceData(0x01, qt_resource_struct, qt_resource_name, qt_resource_data)

def qCleanupResources():
    QtCore.qUnregisterResourceData(0x01, qt_resource_struct, qt_resource_name, qt_resource_data)

qInitResources()
