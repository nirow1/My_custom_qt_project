# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interfacejPGJaL.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from Custom_Widgets.QCustomSlideMenu import QCustomSlideMenu


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1000, 650)
        MainWindow.setMinimumSize(QSize(1000, 650))
        MainWindow.setMaximumSize(QSize(2000, 1440))
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
                                         "font: 11pt \"Yu Gothic UI\";\n"
                                         "border-radius: 1px;\n"
                                         "")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.menu_bar = QCustomSlideMenu(self.centralwidget)
        self.menu_bar.setObjectName(u"menu_bar")
        self.menu_bar.setMinimumSize(QSize(150, 0))
        self.menu_bar.setMaximumSize(QSize(200, 16777215))
        self.menu_bar.setStyleSheet(u"background-color: rgb(204, 204, 204);")
        self.verticalLayout = QVBoxLayout(self.menu_bar)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(6, 6, 6, 6)
        self.frame_3 = QFrame(self.menu_bar)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMaximumSize(QSize(16777215, 60))
        self.frame_3.setStyleSheet(u"background-color: rgb(230, 230, 230);")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_12 = QLabel(self.frame_3)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMinimumSize(QSize(0, 40))
        self.label_12.setMaximumSize(QSize(40, 40))
        self.label_12.setPixmap(QPixmap(u":/feather/icons/feather/pie-chart.png"))
        self.label_12.setScaledContents(True)

        self.horizontalLayout_7.addWidget(self.label_12)

        self.label = QLabel(self.frame_3)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamily(u"Yu Gothic UI")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)

        self.horizontalLayout_7.addWidget(self.label)

        self.verticalLayout.addWidget(self.frame_3)

        self.frame_6 = QFrame(self.menu_bar)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setStyleSheet(u"QPushButton {\n"
                                   "border-radius: 8px;\n"
                                   "border: 1px solid #4CAF50;\n"
                                   "}\n"
                                   "QPushButton:hover {\n"
                                   "background-color: rgb(230, 230, 230);\n"
                                   "}\n"
                                   "QPushButton:pressed {\n"
                                   "        background-color: #729D1F; /* Even darker orange on click */\n"
                                   "    }")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_6)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.percentage_bar_btn = QPushButton(self.frame_6)
        self.percentage_bar_btn.setObjectName(u"percentage_bar_btn")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.percentage_bar_btn.sizePolicy().hasHeightForWidth())
        self.percentage_bar_btn.setSizePolicy(sizePolicy)
        self.percentage_bar_btn.setMinimumSize(QSize(0, 30))
        icon = QIcon()
        icon.addFile(u":/feather/icons/feather/bar-chart-2.png", QSize(), QIcon.Normal, QIcon.Off)
        self.percentage_bar_btn.setIcon(icon)
        self.percentage_bar_btn.setIconSize(QSize(20, 20))

        self.verticalLayout_3.addWidget(self.percentage_bar_btn)

        self.temperature_bar_btn = QPushButton(self.frame_6)
        self.temperature_bar_btn.setObjectName(u"temperature_bar_btn")
        sizePolicy.setHeightForWidth(self.temperature_bar_btn.sizePolicy().hasHeightForWidth())
        self.temperature_bar_btn.setSizePolicy(sizePolicy)
        self.temperature_bar_btn.setMinimumSize(QSize(0, 30))
        self.temperature_bar_btn.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u":/font_awesome_solid/icons/font_awesome/solid/temperature-empty.png", QSize(), QIcon.Normal,
                      QIcon.Off)
        self.temperature_bar_btn.setIcon(icon1)
        self.temperature_bar_btn.setIconSize(QSize(20, 20))

        self.verticalLayout_3.addWidget(self.temperature_bar_btn)

        self.nested_donut_btn = QPushButton(self.frame_6)
        self.nested_donut_btn.setObjectName(u"nested_donut_btn")
        self.nested_donut_btn.setMinimumSize(QSize(0, 30))
        icon2 = QIcon()
        icon2.addFile(u":/feather/icons/feather/target.png", QSize(), QIcon.Normal, QIcon.Off)
        self.nested_donut_btn.setIcon(icon2)
        self.nested_donut_btn.setIconSize(QSize(20, 20))

        self.verticalLayout_3.addWidget(self.nested_donut_btn)

        self.line_chart_btn = QPushButton(self.frame_6)
        self.line_chart_btn.setObjectName(u"line_chart_btn")
        self.line_chart_btn.setMinimumSize(QSize(0, 30))
        icon3 = QIcon()
        icon3.addFile(u":/feather/icons/feather/git-merge.png", QSize(), QIcon.Normal, QIcon.Off)
        self.line_chart_btn.setIcon(icon3)
        self.line_chart_btn.setIconSize(QSize(20, 20))

        self.verticalLayout_3.addWidget(self.line_chart_btn)

        self.bar_chart_btn = QPushButton(self.frame_6)
        self.bar_chart_btn.setObjectName(u"bar_chart_btn")
        self.bar_chart_btn.setMinimumSize(QSize(0, 30))
        icon4 = QIcon()
        icon4.addFile(u":/feather/icons/feather/bar-chart.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bar_chart_btn.setIcon(icon4)
        self.bar_chart_btn.setIconSize(QSize(20, 20))

        self.verticalLayout_3.addWidget(self.bar_chart_btn)

        self.verticalLayout.addWidget(self.frame_6)

        self.frame_5 = QFrame(self.menu_bar)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMaximumSize(QSize(16777215, 50))
        self.frame_5.setStyleSheet(u"background-color: rgb(230, 230, 230);")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_5)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_2 = QLabel(self.frame_5)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(16777215, 50))

        self.verticalLayout_4.addWidget(self.label_2)

        self.verticalLayout.addWidget(self.frame_5)

        self.frame_4 = QFrame(self.menu_bar)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_7 = QLabel(self.frame_4)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_9.addWidget(self.label_7)

        self.verticalLayout.addWidget(self.frame_4)

        self.horizontalLayout.addWidget(self.menu_bar)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(5, 0, 5, 0)
        self.header_frame = QFrame(self.frame_2)
        self.header_frame.setObjectName(u"header_frame")
        self.header_frame.setStyleSheet(u"background-color: rgb(204, 204, 204);")
        self.header_frame.setFrameShape(QFrame.StyledPanel)
        self.header_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.header_frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, -1, 0, -1)
        self.frame_10 = QFrame(self.header_frame)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMaximumSize(QSize(150, 16777215))
        self.frame_10.setStyleSheet(u"QPushButton {\n"
                                    "border-radius: 5px;\n"
                                    "}\n"
                                    "QPushButton:hover {\n"
                                    "background-color: rgb(230, 230, 230);\n"
                                    "}\n"
                                    "QPushButton:pressed {\n"
                                    "        background-color: #729D1F; /* Even darker orange on click */\n"
                                    "    }")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pushButton_6 = QPushButton(self.frame_10)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setMinimumSize(QSize(0, 30))
        self.pushButton_6.setMaximumSize(QSize(40, 16777215))
        icon5 = QIcon()
        icon5.addFile(u"./Qss/icons/Icons/feather/align-center.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_6.setIcon(icon5)
        self.pushButton_6.setIconSize(QSize(25, 25))

        self.horizontalLayout_3.addWidget(self.pushButton_6)

        self.label_3 = QLabel(self.frame_10)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.horizontalLayout_2.addWidget(self.frame_10)

        self.frame_12 = QFrame(self.header_frame)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_4 = QLabel(self.frame_12)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_4)

        self.horizontalLayout_2.addWidget(self.frame_12)

        self.frame_11 = QFrame(self.header_frame)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMaximumSize(QSize(150, 16777215))
        self.frame_11.setStyleSheet(u"QPushButton {\n"
                                    "border-radius: 4px;\n"
                                    "}\n"
                                    "QPushButton:hover {\n"
                                    "background-color: rgb(230, 230, 230);\n"
                                    "}")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.minimaze_window_button = QPushButton(self.frame_11)
        self.minimaze_window_button.setObjectName(u"minimaze_window_button")
        self.minimaze_window_button.setMaximumSize(QSize(30, 16777215))
        self.minimaze_window_button.setToolTipDuration(-1)
        icon6 = QIcon()
        icon6.addFile(u":/feather/icons/feather/checkbox_indeterminate.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimaze_window_button.setIcon(icon6)
        self.minimaze_window_button.setIconSize(QSize(20, 20))

        self.horizontalLayout_5.addWidget(self.minimaze_window_button)

        self.restore_window_button = QPushButton(self.frame_11)
        self.restore_window_button.setObjectName(u"restore_window_button")
        self.restore_window_button.setMaximumSize(QSize(30, 16777215))
        icon7 = QIcon()
        icon7.addFile(u":/feather/icons/feather/maximize-2.png", QSize(), QIcon.Normal, QIcon.Off)
        self.restore_window_button.setIcon(icon7)
        self.restore_window_button.setIconSize(QSize(20, 20))

        self.horizontalLayout_5.addWidget(self.restore_window_button)

        self.close_window_button = QPushButton(self.frame_11)
        self.close_window_button.setObjectName(u"close_window_button")
        self.close_window_button.setMaximumSize(QSize(30, 16777215))
        self.close_window_button.setAutoFillBackground(False)
        icon8 = QIcon()
        icon8.addFile(u":/feather/icons/feather/x.png", QSize(), QIcon.Normal, QIcon.Off)
        self.close_window_button.setIcon(icon8)
        self.close_window_button.setIconSize(QSize(20, 20))
        self.close_window_button.setCheckable(False)
        self.close_window_button.setAutoExclusive(False)
        self.close_window_button.setAutoDefault(False)

        self.horizontalLayout_5.addWidget(self.close_window_button)

        self.horizontalLayout_2.addWidget(self.frame_11)

        self.verticalLayout_5.addWidget(self.header_frame)

        self.frame_8 = QFrame(self.frame_2)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setStyleSheet(u"")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_8)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, -1, 0, -1)
        self.stackedWidget = QStackedWidget(self.frame_8)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.percentage_bar_charts = QWidget()
        self.percentage_bar_charts.setObjectName(u"percentage_bar_charts")
        self.verticalLayout_8 = QVBoxLayout(self.percentage_bar_charts)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.frame_15 = QFrame(self.percentage_bar_charts)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_15)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_6 = QLabel(self.frame_15)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_6, 0, Qt.AlignTop)

        self.verticalLayout_8.addWidget(self.frame_15, 0, Qt.AlignTop)

        self.frame_16 = QFrame(self.percentage_bar_charts)
        self.frame_16.setObjectName(u"frame_16")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_16.sizePolicy().hasHeightForWidth())
        self.frame_16.setSizePolicy(sizePolicy1)
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_16)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame_17 = QFrame(self.frame_16)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)

        self.gridLayout.addWidget(self.frame_17, 0, 0, 1, 1)

        self.verticalLayout_8.addWidget(self.frame_16)

        self.stackedWidget.addWidget(self.percentage_bar_charts)
        self.temperature_bar_charts = QWidget()
        self.temperature_bar_charts.setObjectName(u"temperature_bar_charts")
        self.verticalLayout_12 = QVBoxLayout(self.temperature_bar_charts)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.frame_21 = QFrame(self.temperature_bar_charts)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_21)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_8 = QLabel(self.frame_21)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.label_8, 0, Qt.AlignTop)

        self.verticalLayout_12.addWidget(self.frame_21)

        self.frame_18 = QFrame(self.temperature_bar_charts)
        self.frame_18.setObjectName(u"frame_18")
        sizePolicy1.setHeightForWidth(self.frame_18.sizePolicy().hasHeightForWidth())
        self.frame_18.setSizePolicy(sizePolicy1)
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_18)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.frame_20 = QFrame(self.frame_18)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)

        self.gridLayout_3.addWidget(self.frame_20, 0, 0, 1, 1)

        self.verticalLayout_12.addWidget(self.frame_18)

        self.stackedWidget.addWidget(self.temperature_bar_charts)
        self.nested_donuts = QWidget()
        self.nested_donuts.setObjectName(u"nested_donuts")
        self.verticalLayout_14 = QVBoxLayout(self.nested_donuts)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.frame_24 = QFrame(self.nested_donuts)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_24)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_9 = QLabel(self.frame_24)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setAlignment(Qt.AlignCenter)

        self.verticalLayout_13.addWidget(self.label_9, 0, Qt.AlignTop)

        self.verticalLayout_14.addWidget(self.frame_24)

        self.frame_22 = QFrame(self.nested_donuts)
        self.frame_22.setObjectName(u"frame_22")
        sizePolicy1.setHeightForWidth(self.frame_22.sizePolicy().hasHeightForWidth())
        self.frame_22.setSizePolicy(sizePolicy1)
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_22)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.frame_23 = QFrame(self.frame_22)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)

        self.gridLayout_4.addWidget(self.frame_23, 0, 0, 1, 1)

        self.verticalLayout_14.addWidget(self.frame_22)

        self.stackedWidget.addWidget(self.nested_donuts)
        self.line_charts = QWidget()
        self.line_charts.setObjectName(u"line_charts")
        self.verticalLayout_16 = QVBoxLayout(self.line_charts)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.frame_27 = QFrame(self.line_charts)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_27)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.label_10 = QLabel(self.frame_27)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setAlignment(Qt.AlignCenter)

        self.verticalLayout_15.addWidget(self.label_10, 0, Qt.AlignTop)

        self.verticalLayout_16.addWidget(self.frame_27)

        self.frame_25 = QFrame(self.line_charts)
        self.frame_25.setObjectName(u"frame_25")
        sizePolicy1.setHeightForWidth(self.frame_25.sizePolicy().hasHeightForWidth())
        self.frame_25.setSizePolicy(sizePolicy1)
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_25)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.frame_26 = QFrame(self.frame_25)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)

        self.gridLayout_5.addWidget(self.frame_26, 0, 0, 1, 1)

        self.verticalLayout_16.addWidget(self.frame_25)

        self.stackedWidget.addWidget(self.line_charts)
        self.bar_charts = QWidget()
        self.bar_charts.setObjectName(u"bar_charts")
        self.verticalLayout_18 = QVBoxLayout(self.bar_charts)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.frame_30 = QFrame(self.bar_charts)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setFrameShape(QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_30)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.label_11 = QLabel(self.frame_30)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setAlignment(Qt.AlignCenter)

        self.verticalLayout_17.addWidget(self.label_11, 0, Qt.AlignTop)

        self.verticalLayout_18.addWidget(self.frame_30)

        self.frame_28 = QFrame(self.bar_charts)
        self.frame_28.setObjectName(u"frame_28")
        sizePolicy1.setHeightForWidth(self.frame_28.sizePolicy().hasHeightForWidth())
        self.frame_28.setSizePolicy(sizePolicy1)
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.frame_28)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.frame_29 = QFrame(self.frame_28)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)

        self.gridLayout_6.addWidget(self.frame_29, 0, 0, 1, 1)

        self.verticalLayout_18.addWidget(self.frame_28)

        self.stackedWidget.addWidget(self.bar_charts)

        self.verticalLayout_7.addWidget(self.stackedWidget)

        self.verticalLayout_5.addWidget(self.frame_8)

        self.frame_9 = QFrame(self.frame_2)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setStyleSheet(u"background-color: rgb(204, 204, 204);")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(-1, -1, 9, -1)
        self.frame_13 = QFrame(self.frame_9)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_13)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.frame_13)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_6.addWidget(self.label_5)

        self.horizontalLayout_6.addWidget(self.frame_13)

        self.size_grip = QFrame(self.frame_9)
        self.size_grip.setObjectName(u"size_grip")
        self.size_grip.setMaximumSize(QSize(10, 10))
        self.size_grip.setStyleSheet(u"border-radius: 8px;\n"
                                     "border: 1px solid #4CAF50;")
        self.size_grip.setFrameShape(QFrame.StyledPanel)
        self.size_grip.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.size_grip)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_6.addWidget(self.size_grip)

        self.verticalLayout_5.addWidget(self.frame_9)

        self.horizontalLayout.addWidget(self.frame_2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.close_window_button.setDefault(False)
        self.stackedWidget.setCurrentIndex(4)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_12.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"QT CHARTS", None))
        self.percentage_bar_btn.setText(QCoreApplication.translate("MainWindow", u"Procentu\u00e1ln\u00ed", None))
        self.temperature_bar_btn.setText(QCoreApplication.translate("MainWindow", u"Teplotn\u00ed", None))
        self.nested_donut_btn.setText(QCoreApplication.translate("MainWindow", u"Zahnizd\u011bny", None))
        self.line_chart_btn.setText(QCoreApplication.translate("MainWindow", u"Linkov\u00fd", None))
        self.bar_chart_btn.setText(QCoreApplication.translate("MainWindow", u"Sloupcov\u00fd", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"SOMETHING", None))
        self.label_7.setText("")
        self.pushButton_6.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Menu", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"DASHBOARD", None))
        self.minimaze_window_button.setText("")
        self.restore_window_button.setText("")
        self.close_window_button.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Procentu\u00e1ln\u00ed Graf", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Teplotn\u00ed Graf", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Zahnizd\u011bn\u00fd Graf", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Linkov\u00fd Graf", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Sloupcov\u00fd diagram", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u00a9 Copy Right 4Jtech 2024", None))
    # retranslateUi
