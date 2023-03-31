from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from lib.mathex import MathParser
from ui.dialog.about import AboutDialog
from ui.styles.style import Style


class MainUI(object):
    def __init__(self, parentWindow):

        if not parentWindow.objectName():
            parentWindow.setObjectName(u'parentWindow')

        # UI Setup
        parentWindow.resize(640, 340)
        parentWindow.setFixedSize(640, 340)
        self.sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.sizePolicy.setHorizontalStretch(0)
        self.sizePolicy.setVerticalStretch(0)
        self.sizePolicy.setHeightForWidth(
            parentWindow.sizePolicy().hasHeightForWidth())
        parentWindow.setSizePolicy(self.sizePolicy)

        self.global_style = Style('light')
        parentWindow.setStyleSheet(self.global_style.current_theme())

        self.par = MathParser()

        # UI Elements
        self.widget_main = QWidget(parentWindow)
        self.widget_main.setObjectName(u'widget_main')

        # Title
        self.lbl_maintitle = QLabel(self.widget_main)
        self.lbl_maintitle.setObjectName(u'lbl_maintitle')
        self.lbl_maintitle.setGeometry(QRect(20, 20, 191, 51))
        self.lbl_maintitle.setFont(self.global_style.fnt_roboto_bold(28))

        # Input Field
        self.lbl_input = QLabel(self.widget_main)
        self.lbl_input.setObjectName(u'lbl_input')
        self.lbl_input.setGeometry(QRect(20, 100, 60, 16))
        self.lbl_input.setFont(self.global_style.fnt_roboto(12))

        self.txt_input = QLineEdit(self.widget_main)
        self.txt_input.setObjectName(u'txt_input')
        self.txt_input.setGeometry(QRect(20, 120, 600, 40))
        self.txt_input.setFont(self.global_style.fnt_roboto(12))

        def parseMath():
            # ((5-(-3*4*5))/(67-9))^3 - 1.407524908770347 = 0
            inputText = self.txt_input.text()
            if inputText == '':
                self.txt_output.setText('')
            else:
                self.txt_output.setText(
                    str(self.par.solveExpression(inputText)))
        self.txt_input.textChanged.connect(parseMath)

        # Output Field
        self.txt_output = QLineEdit(self.widget_main)
        self.txt_output.setObjectName(u'txt_output')
        self.txt_output.setGeometry(QRect(20, 230, 600, 40))
        self.txt_output.setReadOnly(True)
        self.txt_output.setFont(self.global_style.fnt_roboto(12))

        self.lbl_output = QLabel(self.widget_main)
        self.lbl_output.setObjectName(u'lbl_output')
        self.lbl_output.setGeometry(QRect(20, 210, 60, 16))
        self.lbl_output.setFont(self.global_style.fnt_roboto(12))

        # Menu Bar
        self.menu_bar = QMenuBar(parentWindow)
        self.menu_bar.setObjectName(u'menu_bar')
        self.menu_bar.setGeometry(QRect(0, 0, 640, 20))

        # Help menu
        self.menu_help = QMenu(self.menu_bar)
        self.menu_help.setObjectName(u'menu_help')
        self.menu_bar.addAction(self.menu_help.menuAction())

        self.atn_about = QAction(parentWindow)
        self.atn_about.setObjectName(u'atn_about')

        def launchAboutDialog():
            about_dialog = AboutDialog(self.global_style)
            child_dialog = QDialog(parentWindow)
            about_dialog.setupUi(child_dialog)
            child_dialog.exec()
        self.atn_about.triggered.connect(launchAboutDialog)
        self.menu_help.addAction(self.atn_about)

        # View menu
        self.menu_view = QMenu(self.menu_bar)
        self.menu_view.setObjectName(u'menu_view')
        self.menu_bar.addAction(self.menu_view.menuAction())

        self.submenu_theme = QMenu(parentWindow)
        self.submenu_theme.setObjectName(u'submenu_theme')
        self.menu_view.addMenu(self.submenu_theme)

        self.atn_theme_dark = QAction(parentWindow)
        self.atn_theme_dark.setObjectName(u'atn_theme_dark')

        def changeThemeToDark():
            self.global_style.theme = 'dark'
            parentWindow.setStyleSheet(self.global_style.current_theme())
            self.atn_theme_light.setChecked(False)
            self.atn_theme_dark.setChecked(True)
        self.atn_theme_dark.triggered.connect(changeThemeToDark)
        self.atn_theme_dark.setCheckable(True)
        self.submenu_theme.addAction(self.atn_theme_dark)

        self.atn_theme_light = QAction(parentWindow)
        self.atn_theme_light.setObjectName(u'atn_theme_light')

        def changeThemeToLight():
            self.global_style.theme = 'light'
            parentWindow.setStyleSheet(self.global_style.current_theme())
            self.atn_theme_light.setChecked(True)
            self.atn_theme_dark.setChecked(False)
        self.atn_theme_light.triggered.connect(changeThemeToLight)
        self.atn_theme_light.setCheckable(True)
        self.atn_theme_light.setChecked(True)
        self.submenu_theme.addAction(self.atn_theme_light)

        # Set Layout
        parentWindow.setMenuBar(self.menu_bar)
        parentWindow.setCentralWidget(self.widget_main)

        # Additional Options
        QWidget.setTabOrder(self.txt_input, self.txt_output)
        QMetaObject.connectSlotsByName(parentWindow)

        # Set UI texts
        self.retranslateUi(parentWindow)

    # Set text values here
    def retranslateUi(self, parentWindow):
        parentWindow.setWindowTitle(
            QCoreApplication.translate('parentWindow', u'Mathex v1.0', None))
        self.lbl_input.setText(
            QCoreApplication.translate('parentWindow', u'Input:', None))
        self.txt_output.setPlaceholderText(
            QCoreApplication.translate('parentWindow', u'Answer', None))
        self.txt_input.setPlaceholderText(
            QCoreApplication.translate('parentWindow', u'Math Expression', None))
        self.lbl_output.setText(
            QCoreApplication.translate('parentWindow', u'Output:', None))
        self.menu_help.setTitle(
            QCoreApplication.translate('parentWindow', u'Help', None))
        self.menu_view.setTitle(
            QCoreApplication.translate('parentWindow', u'View', None))
        self.atn_about.setText(
            QCoreApplication.translate('parentWindow', u'About', None))
        self.submenu_theme.setTitle(
            QCoreApplication.translate('parentWindow', u'Theme', None))
        self.atn_theme_dark.setText(
            QCoreApplication.translate('parentWindow', u'Dark', None))
        self.atn_theme_light.setText(
            QCoreApplication.translate('parentWindow', u'Light', None))
        self.lbl_maintitle.setText(
            QCoreApplication.translate('parentWindow', u'MathEx', None))
