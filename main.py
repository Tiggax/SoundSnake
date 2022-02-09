# This Python file uses the following encoding: utf-8
from gui.uis.windows.main_window.functions_main_window import *
import sys
import os
from qt_core import *
from gui.core.json_settings import Settings

from gui.uis.windows.main_window import *
from gui.widgets import *

os.environ["QT_FONT_DPI"] = "96"


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Load widgets from "gui\uis\main_window\ui_main.py"
        self.ui = UI_MainWindow()
        self.ui.setup_ui(self)

        # LOAD SETTINGS
        settings = Settings()
        self.settings = settings.items

        # SETUP MAIN WINDOW
        self.hide_grips = True # Show/Hide resize grips
        SetupMainWindow.setup_gui(self)

        # SHOW MAIN WINDOW
        self.show()

    # LEFT MENU BTN IS CLICKED
    # Run function when btn is clicked
    # Check funtion by object name / btn_id
    # ///////////////////////////////////////////////////////////////
    def btn_clicked(self):
        # GET BT CLICKED
        btn = SetupMainWindow.setup_btns(self)

        # click events

        #HOME
        if btn.objectName() == "btn_home":
            self.ui.left_menu.select_only_one(btn.objectName())

            MainFunctions.set_page(self, self.ui.load_pages.page_1)
        #Search
        if btn.objectName() == "btn_search":
            self.ui.left_menu.select_only_one(btn.objectName())

            MainFunctions.set_page(self, self.ui.load_pages.page_2)
        #Settings
        if btn.objectName() == "btn_settings":
            self.ui.left_menu.select_only_one(btn.objectName())

            MainFunctions.set_page(self, self.ui.load_pages.page_3)
        

        # TITLE BAR MENU
        # ///////////////////////////////////////////////////////////////
        
        # SETTINGS TITLE BAR
        

    # LEFT MENU BTN IS RELEASED
    # Run function when btn is released
    # Check funtion by object name / btn_id
    # ///////////////////////////////////////////////////////////////
    def btn_released(self):
        # GET BT CLICKED
        btn = SetupMainWindow.setup_btns(self)

        # DEBUG
        print(f"Button {btn.objectName()}, released!")

    # RESIZE EVENT
    # ///////////////////////////////////////////////////////////////
    def resizeEvent(self, event):
        SetupMainWindow.resize_grips(self)

    # MOUSE CLICK EVENTS
    # ///////////////////////////////////////////////////////////////
    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        self.dragPos = event.globalPos()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("icon.ico"))
    window = MainWindow()

    sys.exit(app.exec())