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

        # Create charts
        ####################################################################################
        #  bar graph data + body
        country_dict = self._create_wealth_data()
        percentage_bar_ser = QtCharts.QPercentBarSeries()
        bar_series = QtCharts.QBarSeries()

        # Create data sets
        for x in country_dict:
            wealth_set = QtCharts.QBarSet(x)
            wealth_set.append([country_dict[x]['cumulative_wealth'], country_dict[x]['count']])
            bar_series.append(wealth_set)
            percentage_bar_ser.append(wealth_set)

        moisture_regulation_data = self._create_regulation_data()

        # BarChart
        ############################################
        chart = QtCharts.QChart()
        chart.addSeries(bar_series)
        chart.setTitle("Regionally sorted companies")

        categories = ["wealth", "count"]
        axis_x = QtCharts.QBarCategoryAxis()
        axis_x.append(categories)
        chart.setAxisX(axis_x, bar_series)

        axis_y = QtCharts.QValueAxis()
        axis_y.setRange(0, 40)
        chart.setAxisY(axis_y, bar_series)

        chart.legend().setAlignment(Qt.AlignRight)
        self.ui.chart_view = QtCharts.QChartView(chart)
        self.ui.chart_view.setRenderHint(QPainter.Antialiasing)
        self.ui.chart_view.chart().setTheme(QtCharts.QChart.ChartThemeDark)

        size_policy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        size_policy.setHeightForWidth(self.ui.chart_view.sizePolicy().hasHeightForWidth())
        self.ui.chart_view.setSizePolicy(size_policy)
        self.ui.chart_view.setMinimumSize(0, 300)

        self.ui.gridLayout_6.addWidget(self.ui.chart_view)
        self.ui.frame_28.setStyleSheet("background-color: transparent")

        # percentage bar
        ##################################################
        chart = QtCharts.QChart()
        chart.addSeries(percentage_bar_ser)
        chart.setTitle("Regionally sorted companies")

        axis_x = QtCharts.QBarCategoryAxis()
        axis_x.append(categories)
        chart.setAxisX(axis_x, percentage_bar_ser)

        axis_y = QtCharts.QValueAxis()
        axis_y.setRange(0, 100)
        chart.setAxisY(axis_y, percentage_bar_ser)

        chart.legend().setAlignment(Qt.AlignRight)
        self.ui.chart_view = QtCharts.QChartView(chart)
        self.ui.chart_view.setRenderHint(QPainter.Antialiasing)
        self.ui.chart_view.chart().setTheme(QtCharts.QChart.ChartThemeDark)

        size_policy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        size_policy.setHeightForWidth(self.ui.chart_view.sizePolicy().hasHeightForWidth())
        self.ui.chart_view.setSizePolicy(size_policy)
        self.ui.chart_view.setMinimumSize(0, 300)

        self.ui.gridLayout.addWidget(self.ui.chart_view)

        # Temperature chart graph
        ###################################################
        humidity = QtCharts.QBarSet("Vlhkost")
        temperature = QtCharts.QBarSet("Teplota")
        humidity.append(moisture_regulation_data[0])
        temperature.append(moisture_regulation_data[1])

        series = QtCharts.QStackedBarSeries()
        series.append(humidity)
        series.append(temperature)

        chart = QtCharts.QChart()
        chart.addSeries(series)
        chart.setTitle("Vlhkost a teplota v komoře za posledních 12 dní")
        chart.setAnimationOptions(QtCharts.QChart.SeriesAnimations)
        categories = ["den 1", "den 2", "den 3", "den 4", "den 5", "den 6", "den 7", "den 8", "den 9",
                      "den 10", "den 11", "den 12"]

        axis_x = QtCharts.QBarCategoryAxis()
        axis_x.append(categories)
        chart.addAxis(axis_x, Qt.AlignBottom)
        axis_y = QtCharts.QValueAxis()
        axis_y.setRange(0, 200)
        chart.addAxis(axis_y, Qt.AlignLeft)
        series.attachAxis(axis_x)
        series.attachAxis(axis_y)

        self.ui.chart_view = QtCharts.QChartView(chart)
        self.ui.chart_view.setRenderHint(QPainter.Antialiasing)
        self.ui.chart_view.chart().setTheme(QtCharts.QChart.
                                            ChartThemeDark)
        self.ui.chart_view.setSizePolicy(size_policy)
        self.ui.chart_view.setMinimumSize(0, 300)

        self.ui.gridLayout_3.addWidget(self.ui.chart_view)

        # Line graph
        ###################################################

        self.speed_data = QtCharts.QLineSeries()
        data = [0, 2, 5, 8, 15, 20, 26, 36, 40, 48, 55, 69, 85, 99]
        for row, speed in enumerate(data):
            self.speed_data.append(row, speed)
        self.chart = QtCharts.QChart()
        self.chart.legend().hide()
        self.chart.addSeries(self.speed_data)
        self.chart.createDefaultAxes()
        self.chart.setTitle("speed in m/s")

        self.chart_view = QtCharts.QChartView(chart=self.chart)
        self.chart_view.setRenderHint(QPainter.RenderHint.Antialiasing)
        self.chart.setAnimationOptions(QtCharts.QChart.AllAnimations)
        self.chart_view.chart().setTheme(QtCharts.QChart.
                                         ChartThemeDark)

        size_policy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        size_policy.setHeightForWidth(self.chart_view
                                      .sizePolicy().hasHeightForWidth())
        self.chart_view.setSizePolicy(size_policy)
        self.chart_view.setMinimumSize(0, 300)
        self.ui.gridLayout_5.addWidget(self.chart_view)

        # pie charts
        #####################################################

        self.chart_view = QtCharts.QChartView()
        self.chart_view.setRenderHint(QPainter.Antialiasing)
        self.chart = self.chart_view.chart()

        self.chart.legend().setVisible(False)
        self.chart.setTitle("speed")
        self.chart.setAnimationOptions(QtCharts.QChart.AllAnimations)
        self.chart_view.chart().setTheme(QtCharts.QChart.
                                         ChartThemeDark)

        self.chart_view.setSizePolicy(size_policy)
        self.chart_view.setMinimumSize(0, 300)

        self.ui.gridLayout_4.addWidget(self.chart_view)

        donut = []


        # # COLLAPSE THE WIDGET IF IT IS CURRENTLY EXPANDED
        #self.ui.menu_bar.slideMenu()

        # # COLLAPSE WIDGET SIZE
        #self.ui.menu_bar.collapseMenu()

        # # EXPAND WIDGET SIZE
        # # self.ui.menu_bar.expandMenu()

        # switching between slides
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
    def _create_wealth_data():
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

    def _create_regulation_data(self):
        temperature = []
        humidity = []
        row_count = 0
        with open("./data/mosture_regulation.csv") as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                humidity.append(float(row[0]))
                temperature.append(float(row[1]))
                if row_count > 11:
                    break
                row_count += 1
        return humidity, temperature



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
