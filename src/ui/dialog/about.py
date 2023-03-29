from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class AboutDialog(object):
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
        self.label.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
        self.label.setWordWrap(False)

        self.retranslateUi(dialog_AboutMathex)
        self.btn_aboutOK.clicked.connect(dialog_AboutMathex.close)

        QMetaObject.connectSlotsByName(dialog_AboutMathex)
    # setupUi

    def retranslateUi(self, dialog_AboutMathex):
        dialog_AboutMathex.setWindowTitle(
            QCoreApplication.translate("dialog_AboutMathex", u"About", None))
        self.btn_aboutOK.setText(QCoreApplication.translate(
            "dialog_AboutMathex", u"OK", None))
        self.label.setText(QCoreApplication.translate("dialog_AboutMathex", u"## MathEx\n"
                                                      "#### Math Expression Parser\n"
                                                      "##### By: Hanz Aquino", None))
    # retranslateUi
