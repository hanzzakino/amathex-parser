'''
@author: Hanz Aquino


A UI for my Math expression solver algorithm called MathExParser

'''
__author__ = 'Hanz Aquino'
__version__ = '$Revision: 1.0 $'
__datecreated__ = '$Date: 2022-02-17 $'

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from MathExParser import MathParser
import sys

colr_bg = "#212121"
colr_bg2 = "#303030"
colr_txtDim = "rgb(160,160,160)"
colr_accent = "#77bdfb"
colr_txtfield = "rgb(230,230,230)"


class Ui_dialog_AboutMathex(object):
    def setupUi(self, dialog_AboutMathex):
        if not dialog_AboutMathex.objectName():
            dialog_AboutMathex.setObjectName(u"dialog_AboutMathex")
        dialog_AboutMathex.resize(280, 140)
        dialog_AboutMathex.setFixedSize(280, 140)
        self.btn_aboutOK = QPushButton(dialog_AboutMathex)
        self.btn_aboutOK.setObjectName(u"btn_aboutOK")
        self.btn_aboutOK.setGeometry(QRect(110, 90, 75, 31))
        self.label = QLabel(dialog_AboutMathex)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 260, 81))
        font = QFont()
        font.setFamily(u"Roboto")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setLayoutDirection(Qt.LeftToRight)
        self.label.setFrameShape(QFrame.NoFrame)
        self.label.setFrameShadow(QFrame.Plain)
        self.label.setTextFormat(Qt.MarkdownText)
        self.label.setScaledContents(False)
        self.label.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.label.setWordWrap(False)

        self.retranslateUi(dialog_AboutMathex)
        self.btn_aboutOK.clicked.connect(dialog_AboutMathex.close)

        QMetaObject.connectSlotsByName(dialog_AboutMathex)
    # setupUi

    def retranslateUi(self, dialog_AboutMathex):
        dialog_AboutMathex.setWindowTitle(QCoreApplication.translate("dialog_AboutMathex", u"About", None))
        self.btn_aboutOK.setText(QCoreApplication.translate("dialog_AboutMathex", u"OK", None))
        self.label.setText(QCoreApplication.translate("dialog_AboutMathex", u"## MathEx\n"
"#### Math Expression Parser\n"
"##### By: Hanz Aquino", None))
    # retranslateUi



class Ui_Mathex(object):
    def setupUi(self, Mathex):
        if not Mathex.objectName():
            Mathex.setObjectName(u"Mathex")

        Mathex.resize(640, 340)
        Mathex.setFixedSize(640,340)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Mathex.sizePolicy().hasHeightForWidth())
        Mathex.setSizePolicy(sizePolicy)
        Mathex.setStyleSheet(f"QWindow#Mathex {{  }}")
        

        fnt_roboto_12 = QFont()
        fnt_roboto_12.setFamily(u"Roboto")
        fnt_roboto_12.setPointSize(12)

        fnt_roboto_10 = QFont()
        fnt_roboto_10.setFamily(u"Roboto")
        fnt_roboto_10.setPointSize(10)

        fnt_robotobold = QFont()
        fnt_robotobold.setFamily(u"Roboto")
        fnt_robotobold.setPointSize(28)
        fnt_robotobold.setBold(True)
        fnt_robotobold.setWeight(75)

        self.widget_main = QWidget(Mathex)
        self.widget_main.setObjectName(u"widget_main")
        self.widget_main.setStyleSheet(f"QWidget#widget_main {{ background-color: {colr_bg}; }}")

        self.txt_input = QLineEdit(self.widget_main)
        self.txt_input.setObjectName(u"txt_input")
        self.txt_input.setPlaceholderText("Math Expression")
        self.txt_input.setGeometry(QRect(20, 120, 600, 40))
        self.txt_input.setFont(fnt_roboto_12)
        self.txt_input.setStyleSheet(f"QLineEdit#txt_input {{ border-style: none; padding: 0px 10px 0px 10px; background-color: {colr_txtfield}; }}")
        
        self.lbl_input = QLabel(self.widget_main)
        self.lbl_input.setObjectName(u"lbl_input")
        self.lbl_input.setStyleSheet(f"QLabel#lbl_input {{ color: {colr_txtDim}; }}")
        self.lbl_input.setGeometry(QRect(20, 100, 47, 13))
        self.lbl_input.setFont(fnt_roboto_12)

        self.txt_output = QLineEdit(self.widget_main)
        self.txt_output.setObjectName(u"txt_output")
        self.txt_output.setPlaceholderText("Answer")
        self.txt_output.setGeometry(QRect(20, 230, 600, 40))
        self.txt_output.setReadOnly(True)
        self.txt_output.setFont(fnt_roboto_12)
        self.txt_output.setStyleSheet(f"QLineEdit#txt_output {{ border-style: none; padding: 0px 10px 0px 10px; background-color: {colr_txtfield}; }}")

        self.lbl_output = QLabel(self.widget_main)
        self.lbl_output.setObjectName(u"lbl_output")
        self.lbl_output.setStyleSheet(f"QLabel#lbl_output {{ color: {colr_txtDim}; }}")
        self.lbl_output.setGeometry(QRect(20, 210, 47, 13))
        self.lbl_output.setFont(fnt_roboto_12)

        par = MathParser()
        def parseMath():
            try:
                # ((5-(-3*4*5))/(67-9))^3 - 1.407524908770347 = 0
                inputText = self.txt_input.text()
                if inputText == "":
                    self.txt_output.setText("")
                else:
                    self.txt_output.setText(str(par.solveExpression(inputText)))
            except Exception as e:
                self.txt_output.setText("Error")
                
        self.txt_input.textChanged.connect(parseMath)

        self.lbl_maintitle = QLabel(self.widget_main)
        self.lbl_maintitle.setObjectName(u"lbl_maintitle")
        self.lbl_maintitle.setStyleSheet(f"QLabel#lbl_maintitle {{ color: {colr_accent}; }}")
        self.lbl_maintitle.setGeometry(QRect(20, 20, 191, 51))
        self.lbl_maintitle.setFont(fnt_robotobold)

        self.menuBar = QMenuBar(Mathex)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 640, 20))
        self.menuBar.setStyleSheet(f"QMenuBar#menuBar {{ color: {colr_txtDim}; background-color: {colr_bg2}; }}")
        
        self.menu_help = QMenu(self.menuBar)
        self.menu_help.setObjectName(u"menu_help")
        self.menu_help.setStyleSheet(f"QMenu#menu_help {{ color: {colr_txtDim}; background-color: {colr_bg2}; }}")
        self.menuBar.addAction(self.menu_help.menuAction())
        
        self.atn_about = QAction(Mathex)
        self.atn_about.setObjectName(u"atn_about")
        self.menu_help.addAction(self.atn_about)
        
        def launchAboutDialog():
            about_dialog  = Ui_dialog_AboutMathex()
            dlg = QDialog(Mathex)
            about_dialog.setupUi(dlg)
            dlg.exec()
        self.atn_about.triggered.connect(launchAboutDialog)
        
        
        Mathex.setMenuBar(self.menuBar)
        Mathex.setCentralWidget(self.widget_main)
        

        QWidget.setTabOrder(self.txt_input, self.txt_output)
        self.retranslateUi(Mathex)
        QMetaObject.connectSlotsByName(Mathex)
    
    
    def retranslateUi(self, Mathex):
        Mathex.setWindowTitle(QCoreApplication.translate("Mathex", u"Mathex", None))
        self.lbl_input.setText(QCoreApplication.translate("Mathex", u"Input:", None))
        self.lbl_output.setText(QCoreApplication.translate("Mathex", u"Output:", None))
        self.menu_help.setTitle(QCoreApplication.translate("Mathex", u"Help", None))
        self.atn_about.setText(QCoreApplication.translate("Mathex", u"About", None))
        self.lbl_maintitle.setText(QCoreApplication.translate("Mathex", u"MathEx", None))





if __name__ == "__main__":
        app = QApplication(sys.argv)
        window = QMainWindow()
        ui = Ui_Mathex()
        ui.setupUi(window)
        window.show()
        sys.exit(app.exec())

