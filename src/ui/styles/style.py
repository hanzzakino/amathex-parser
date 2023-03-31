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
            colr_fg = 'rgb(235,235,235)'
            colr_txtDim = 'rgb(160,160,160)'
            colr_accent = '#2678db'
            colr_txtfield = '#303030'
        else:
            colr_bg = '#ffffff'
            colr_fg = 'black'
            colr_txtDim = 'rgb(50,50,50)'
            colr_accent = '#2678db'
            colr_txtfield = 'rgb(235,235,235)'

        return (
            f'''
            QWindow#Amthex {{ 
            }}
            QWidget {{ 
                background-color: {colr_bg};
            }}
            QPushButton {{
                outline: none;
                border-radius: 4px;
                background-color: {colr_accent};
                color: white;
            }}
            QLineEdit {{
                border-style: none;
                padding: 0px 10px 0px 10px;
                background-color: {colr_txtfield};
                color: {colr_fg};
                border-radius: 4px;
                letter-spacing: 0.5px;
            }}
            QLabel {{ 
                color: {colr_txtDim};
                letter-spacing: 1px;
            }}
            QLabel#lbl_maintitle {{ 
                color: {colr_accent};
            }}

            QMenuBar::item {{
                background-color: {colr_bg};
                color: {colr_txtDim};
            }}

            QMenuBar::item:selected {{
                background-color: {colr_accent};
                color: #FFFFFF;
            }}

            QMenuBar::item:pressed {{
                background-color: {colr_accent};
                color: #FFFFFF;
            }}

            QMenuBar::item:hover {{
                background-color: {colr_accent};
            }}

            QMenu {{
                background-color: {colr_bg};
            }}

            QMenu::item {{
                background-color: {colr_bg};
                color: {colr_txtDim};
            }}

            QMenu::item:selected {{
                background-color: {colr_accent};
                color: #FFFFFF;
            }}

            QMenu::item:pressed {{
                background-color: {colr_accent};
                color: #FFFFFF;
            }}

            QMenu::item:hover {{
                background-color: {colr_accent};
            }}


            ''')
