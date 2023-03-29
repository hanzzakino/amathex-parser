from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from lib.mathex import MathParser
from ui.dialog.about import AboutDialog


colr_bg = "#212121"
colr_bg2 = "#303030"
colr_txtDim = "rgb(160,160,160)"
colr_accent = "#77bdfb"
colr_txtfield = "rgb(230,230,230)"


class MainUI(object):
    def setupUi(self, Mathex):
        if not Mathex.objectName():
            Mathex.setObjectName(u"Mathex")

        Mathex.resize(640, 340)
        Mathex.setFixedSize(640, 340)
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
        self.widget_main.setStyleSheet(
            f"QWidget#widget_main {{ background-color: {colr_bg}; }}")

        self.txt_input = QLineEdit(self.widget_main)
        self.txt_input.setObjectName(u"txt_input")
        self.txt_input.setPlaceholderText("Math Expression")
        self.txt_input.setGeometry(QRect(20, 120, 600, 40))
        self.txt_input.setFont(fnt_roboto_12)
        self.txt_input.setStyleSheet(
            f"QLineEdit#txt_input {{ border-style: none; padding: 0px 10px 0px 10px; background-color: {colr_txtfield}; }}")

        self.lbl_input = QLabel(self.widget_main)
        self.lbl_input.setObjectName(u"lbl_input")
        self.lbl_input.setStyleSheet(
            f"QLabel#lbl_input {{ color: {colr_txtDim}; }}")
        self.lbl_input.setGeometry(QRect(20, 100, 47, 13))
        self.lbl_input.setFont(fnt_roboto_12)

        self.txt_output = QLineEdit(self.widget_main)
        self.txt_output.setObjectName(u"txt_output")
        self.txt_output.setPlaceholderText("Answer")
        self.txt_output.setGeometry(QRect(20, 230, 600, 40))
        self.txt_output.setReadOnly(True)
        self.txt_output.setFont(fnt_roboto_12)
        self.txt_output.setStyleSheet(
            f"QLineEdit#txt_output {{ border-style: none; padding: 0px 10px 0px 10px; background-color: {colr_txtfield}; }}")

        self.lbl_output = QLabel(self.widget_main)
        self.lbl_output.setObjectName(u"lbl_output")
        self.lbl_output.setStyleSheet(
            f"QLabel#lbl_output {{ color: {colr_txtDim}; }}")
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
                    self.txt_output.setText(
                        str(par.solveExpression(inputText)))
            except Exception as e:
                self.txt_output.setText("Error")

        self.txt_input.textChanged.connect(parseMath)

        self.lbl_maintitle = QLabel(self.widget_main)
        self.lbl_maintitle.setObjectName(u"lbl_maintitle")
        self.lbl_maintitle.setStyleSheet(
            f"QLabel#lbl_maintitle {{ color: {colr_accent}; }}")
        self.lbl_maintitle.setGeometry(QRect(20, 20, 191, 51))
        self.lbl_maintitle.setFont(fnt_robotobold)

        self.menuBar = QMenuBar(Mathex)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 640, 20))
        self.menuBar.setStyleSheet(
            f"QMenuBar#menuBar {{ color: {colr_txtDim}; background-color: {colr_bg2}; }}")

        self.menu_help = QMenu(self.menuBar)
        self.menu_help.setObjectName(u"menu_help")
        self.menu_help.setStyleSheet(
            f"QMenu#menu_help {{ color: {colr_txtDim}; background-color: {colr_bg2}; }}")
        self.menuBar.addAction(self.menu_help.menuAction())

        self.atn_about = QAction(Mathex)
        self.atn_about.setObjectName(u"atn_about")
        self.menu_help.addAction(self.atn_about)

        def launchAboutDialog():
            about_dialog = AboutDialog()
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
        # Mathex.setWindowTitle(
        #     QCoreApplication.translate("Mathex", u"Mathex", None))
        self.lbl_input.setText(
            QCoreApplication.translate("Mathex", u"Input:", None))
        self.lbl_output.setText(
            QCoreApplication.translate("Mathex", u"Output:", None))
        self.menu_help.setTitle(
            QCoreApplication.translate("Mathex", u"Help", None))
        self.atn_about.setText(
            QCoreApplication.translate("Mathex", u"About", None))
        self.lbl_maintitle.setText(
            QCoreApplication.translate("Mathex", u"MathEx", None))
