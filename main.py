import os
import sys
from PySide2 import QtCore
from src.ui_interface import *
from Custom_Widgets import *
from Custom_Widgets.QAppSettings import QAppSettings


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.menu_bar.customizeQCustomSlideMenu(
            defaultWidth=150,
            defaultHeight="auto",
            # CHANGE THE WIDGET SIZE WHEN CALLAPSED/MINIMIZED
            collapsedWidth=0,
            collapsedHeight=0,
            # CHANGE THE WIDGET SIZE WHEN EXPANDED/MAXIMIZED
            expandedWidth=150,
            expandedHeight="parent",

            collapsingAnimationDuration=100,
            collapsingAnimationEasingCurve=QtCore.QEasingCurve.OutQuad,
            # CHANGE ANIMATION DURATION AND EASING CURVE WHEN THE WIDGET IS EXPANDING
            expandingAnimationDuration=200,
            expandingAnimationEasingCurve=QtCore.QEasingCurve.InBack,
        )
        self.ui.pushButton_6.clicked.connect(lambda: self.ui.menu_bar.slideMenu())

        # # COLLAPSE THE WIDGET IF IT IS CURRENTLY EXPANDED
        #self.ui.menu_bar.slideMenu()

        # # COLLAPSE WIDGET SIZE
        #self.ui.menu_bar.collapseMenu()

        # # EXPAND WIDGET SIZE
        # # self.ui.menu_bar.expandMenu()

        self.ui.percentage_bar_btn.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.percentage_bar_charts))
        self.ui.temperature_bar_btn.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.temperature_bar_charts))
        self.ui.line_chart_btn.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.line_charts))
        self.ui.nested_donut_btn.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.nested_donuts))
        self.ui.bar_chart_btn.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.bar_charts))

        loadJsonStyle(self, self.ui, jsonFiles={
            "json-styles/style.json"
            })

        self.show() 

        QAppSettings.updateAppSettings(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
