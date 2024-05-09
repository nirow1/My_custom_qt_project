import csv
import os
import sys
from PySide2 import QtCore
from PySide2.QtCharts import QtCharts
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

        #  todo: make a 2 charts one with names and general wealth and the other with name and number of countries in it
        country_dict = self._create_percentage_bar_chart()
        print(country_dict)
        series = QtCharts.QBarSeries()


        bar_series = QtCharts.QBarSeries()
        # Create data sets
        for x in country_dict:
            wealth_set = QtCharts.QBarSet(x)
            wealth_set.append([country_dict[x]['cumulative_wealth'], country_dict[x]['count']])
            bar_series.append(wealth_set)

        # Create bar series

        # Create chart
        chart = QtCharts.QChart()
        chart.addSeries(bar_series)
        chart.setTitle("Regionally sorted companies")

        # Set X-axis (category axis)
        categories = ["wealth", "count"]
        axis_x = QtCharts.QBarCategoryAxis()
        axis_x.append(categories)
        chart.setAxisX(axis_x, bar_series)

        # Set Y-axis (value axis)
        axis_y = QtCharts.QValueAxis()
        axis_y.setRange(0, 40)
        chart.setAxisY(axis_y, bar_series)

        chart.legend().setAlignment(Qt.AlignRight)
        self.ui.chart_view = QtCharts.QChartView(chart)
        self.ui.chart_view.setRenderHint(QPainter.Antialiasing)
        self.ui.chart_view.chart().setTheme(QtCharts.QChart.ChartThemeDark)

        size_policy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.ui.chart_view.sizePolicy().hasHeightForWidth())
        self.ui.chart_view.setSizePolicy(size_policy)
        self.ui.chart_view.setMinimumSize(0, 300)

        self.ui.gridLayout_6.addWidget(self.ui.chart_view)
        self.ui.frame_28.setStyleSheet("background-color: transparent")


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

    @staticmethod
    def _create_percentage_bar_chart():
        country_list = {}
        row_count = 0

        with open("./data/companies.csv") as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                if row[5] not in country_list:
                    country_list[row[5]] = {"cumulative_wealth": float(row[3]), "count": 1}
                else:
                    country_list[row[5]]["count"] += 1
                    country_list[row[5]]["cumulative_wealth"] += float(row[3])
                row_count += 1
        return country_list


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
