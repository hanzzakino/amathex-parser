from PyQt5.QtGui import *


class Style():
    def __init__(self, theme):
        self.theme = theme

    def fnt_roboto(self, size):
        font = QFont()
        font.setFamily(u'Roboto')
        font.setPointSize(size)
        return font

    def fnt_roboto_bold(self, size):
        font = QFont()
        font.setFamily(u'Roboto')
        font.setPointSize(size)
        font.setBold(True)
        font.setWeight(75)
        return font

    def current_theme(self):
        if self.theme == 'dark':
            colr_bg = '#212121'
            colr_bg2 = '#303030'
            colr_txtDim = 'rgb(160,160,160)'
            colr_accent = '#77bdfb'
            colr_txtfield = 'rgb(230,230,230)'
            return (
                f'''

                QWindow#Mathex {{   }}
                QWidget#widget_main {{ background-color: {colr_bg}; }}
                QLineEdit#txt_input {{ border-style: none; padding: 0px 10px 0px 10px; background-color: {colr_txtfield}; }}
                QLabel#lbl_input {{ color: {colr_txtDim}; }}
                QLineEdit#txt_output {{ border-style: none; padding: 0px 10px 0px 10px; background-color: {colr_txtfield}; }}
                QLabel#lbl_output {{ color: {colr_txtDim}; }}
                QLabel#lbl_maintitle {{ color: {colr_accent}; }}
                QMenuBar#menuBar {{ color: {colr_txtDim}; background-color: {colr_bg2}; }}
                QMenu#menu_help {{ color: {colr_txtDim}; background-color: {colr_bg2}; }}
                
                ''')
        else:
            colr_bg = '#ffffff'
            colr_bg2 = '#ffffff'
            colr_txtDim = 'rgb(50,50,50)'
            colr_accent = '#77bdfb'
            colr_txtfield = 'rgb(235,235,235)'
            return (
                f'''

                QWindow#Mathex {{   }}
                QWidget#widget_main {{ background-color: {colr_bg}; }}
                QLineEdit#txt_input {{ border-style: none; padding: 0px 10px 0px 10px; background-color: {colr_txtfield}; }}
                QLabel#lbl_input {{ color: {colr_txtDim}; }}
                QLineEdit#txt_output {{ border-style: none; padding: 0px 10px 0px 10px; background-color: {colr_txtfield}; }}
                QLabel#lbl_output {{ color: {colr_txtDim}; }}
                QLabel#lbl_maintitle {{ color: {colr_accent}; }}
                QMenuBar#menuBar {{ color: {colr_txtDim}; background-color: {colr_bg2}; }}
                QMenu#menu_help {{ color: {colr_txtDim}; background-color: {colr_bg2}; }}
                
                ''')
