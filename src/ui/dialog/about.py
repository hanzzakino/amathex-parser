from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class AboutDialog(object):
    def __init__(self, global_style):
        self.style = global_style

    def setupUi(self, dialog):
        if not dialog.objectName():
            dialog.setObjectName(u'dialog')
        dialog.resize(280, 140)
        dialog.setFixedSize(280, 140)
        self.btn_aboutOK = QPushButton(dialog)
        self.btn_aboutOK.setObjectName(u'btn_aboutOK')
        self.btn_aboutOK.setGeometry(QRect(110, 90, 75, 31))
        self.label = QLabel(dialog)
        self.label.setObjectName(u'label')
        self.label.setGeometry(QRect(10, 10, 260, 81))
        self.label.setFont(self.style.fnt_roboto(12))
        self.label.setLayoutDirection(Qt.LeftToRight)
        self.label.setFrameShape(QFrame.NoFrame)
        self.label.setFrameShadow(QFrame.Plain)
        self.label.setTextFormat(Qt.MarkdownText)
        self.label.setScaledContents(False)
        self.label.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
        self.label.setWordWrap(False)

        self.retranslateUi(dialog)
        self.btn_aboutOK.clicked.connect(dialog.close)

        QMetaObject.connectSlotsByName(dialog)
    # setupUi

    # Set text values here
    def retranslateUi(self, dialog):
        dialog.setWindowTitle(
            QCoreApplication.translate('dialog', u'About', None))
        self.btn_aboutOK.setText(QCoreApplication.translate(
            'dialog', u'OK', None))
        self.label.setText(QCoreApplication.translate('dialog', u'## MathEx\n'
                                                      '#### Math Expression Parser\n'
                                                      '##### By: Hanz Aquino', None))
    # retranslateUi
