# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Roverling218.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCharts import QChartView
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtMultimediaWidgets import QVideoWidget
from PySide6.QtWidgets import (QApplication, QCheckBox, QDoubleSpinBox, QFormLayout,
    QFrame, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QSlider, QSpacerItem, QSpinBox,
    QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1372, 1205)
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"Inter"])
        font.setPointSize(12)
        MainWindow.setFont(font)
        self.actionGPS_Map = QAction(MainWindow)
        self.actionGPS_Map.setObjectName(u"actionGPS_Map")
        self.actionGPS_Map.setMenuRole(QAction.NoRole)
        self.actionGPS_Clear = QAction(MainWindow)
        self.actionGPS_Clear.setObjectName(u"actionGPS_Clear")
        self.actionGPS_Clear.setMenuRole(QAction.NoRole)
        self.actionRecord = QAction(MainWindow)
        self.actionRecord.setObjectName(u"actionRecord")
        self.actionRecord.setMenuRole(QAction.NoRole)
        self.actionLoad = QAction(MainWindow)
        self.actionLoad.setObjectName(u"actionLoad")
        self.actionLoad.setMenuRole(QAction.NoRole)
        self.actionPlay = QAction(MainWindow)
        self.actionPlay.setObjectName(u"actionPlay")
        self.actionPlay.setMenuRole(QAction.NoRole)
        self.actionGPS_Reset = QAction(MainWindow)
        self.actionGPS_Reset.setObjectName(u"actionGPS_Reset")
        self.actionGPS_Reset.setMenuRole(QAction.NoRole)
        self.actionCommsStop = QAction(MainWindow)
        self.actionCommsStop.setObjectName(u"actionCommsStop")
        self.actionCommsStop.setMenuRole(QAction.NoRole)
        self.actionMagReset = QAction(MainWindow)
        self.actionMagReset.setObjectName(u"actionMagReset")
        self.actionMagReset.setMenuRole(QAction.NoRole)
        self.actionGPSVarReset = QAction(MainWindow)
        self.actionGPSVarReset.setObjectName(u"actionGPSVarReset")
        self.actionGPSVarReset.setMenuRole(QAction.NoRole)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_2 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.COL1 = QFrame(self.centralwidget)
        self.COL1.setObjectName(u"COL1")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.COL1.sizePolicy().hasHeightForWidth())
        self.COL1.setSizePolicy(sizePolicy1)
        self.COL1.setFrameShape(QFrame.NoFrame)
        self.COL1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.COL1)
        self.verticalLayout_17.setSpacing(2)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.COMMS = QFrame(self.COL1)
        self.COMMS.setObjectName(u"COMMS")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.COMMS.sizePolicy().hasHeightForWidth())
        self.COMMS.setSizePolicy(sizePolicy2)
        font1 = QFont()
        font1.setFamilies([u"Inter"])
        font1.setPointSize(9)
        self.COMMS.setFont(font1)
        self.COMMS.setFrameShape(QFrame.Box)
        self.COMMS.setFrameShadow(QFrame.Raised)
        self.COMMS.setLineWidth(2)
        self.verticalLayout_12 = QVBoxLayout(self.COMMS)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(3, 0, 3, 0)
        self.frame_18 = QFrame(self.COMMS)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.NoFrame)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_18)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.label_58 = QLabel(self.frame_18)
        self.label_58.setObjectName(u"label_58")
        font2 = QFont()
        font2.setFamilies([u"Inter"])
        font2.setPointSize(10)
        font2.setBold(True)
        self.label_58.setFont(font2)

        self.horizontalLayout_11.addWidget(self.label_58)

        self.frame_3 = QFrame(self.frame_18)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_3)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 3, 5, 0)
        self.PB_CommsStop = QPushButton(self.frame_3)
        self.PB_CommsStop.setObjectName(u"PB_CommsStop")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.PB_CommsStop.sizePolicy().hasHeightForWidth())
        self.PB_CommsStop.setSizePolicy(sizePolicy3)

        self.verticalLayout.addWidget(self.PB_CommsStop)


        self.horizontalLayout_11.addWidget(self.frame_3)


        self.verticalLayout_12.addWidget(self.frame_18)

        self.frame_22 = QFrame(self.COMMS)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setFrameShape(QFrame.NoFrame)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_22)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.Fcomms = QFrame(self.frame_22)
        self.Fcomms.setObjectName(u"Fcomms")
        self.Fcomms.setFrameShape(QFrame.NoFrame)
        self.Fcomms.setFrameShadow(QFrame.Raised)
        self.formLayout = QFormLayout(self.Fcomms)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setHorizontalSpacing(17)
        self.formLayout.setVerticalSpacing(3)
        self.formLayout.setContentsMargins(0, 2, 0, 5)
        self.label_59 = QLabel(self.Fcomms)
        self.label_59.setObjectName(u"label_59")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_59)

        self.Ppulse = QPushButton(self.Fcomms)
        self.Ppulse.setObjectName(u"Ppulse")
        sizePolicy4 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.Ppulse.sizePolicy().hasHeightForWidth())
        self.Ppulse.setSizePolicy(sizePolicy4)
        self.Ppulse.setMaximumSize(QSize(100, 22))
        font3 = QFont()
        font3.setFamilies([u"Inter"])
        font3.setPointSize(8)
        font3.setBold(False)
        self.Ppulse.setFont(font3)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.Ppulse)

        self.label_69 = QLabel(self.Fcomms)
        self.label_69.setObjectName(u"label_69")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_69)

        self.Gpulse = QPushButton(self.Fcomms)
        self.Gpulse.setObjectName(u"Gpulse")
        sizePolicy5 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.Gpulse.sizePolicy().hasHeightForWidth())
        self.Gpulse.setSizePolicy(sizePolicy5)
        self.Gpulse.setMaximumSize(QSize(100, 16777215))
        font4 = QFont()
        font4.setFamilies([u"Inter"])
        font4.setPointSize(8)
        self.Gpulse.setFont(font4)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.Gpulse)


        self.verticalLayout_14.addWidget(self.Fcomms)

        self.Fsignal = QWidget(self.frame_22)
        self.Fsignal.setObjectName(u"Fsignal")
        self.Fsignal.setFont(font1)
        self.gridLayout_8 = QGridLayout(self.Fsignal)
        self.gridLayout_8.setSpacing(0)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(4, 0, 0, 0)
        self.label_66 = QLabel(self.Fsignal)
        self.label_66.setObjectName(u"label_66")

        self.gridLayout_8.addWidget(self.label_66, 3, 0, 1, 1)

        self.label_70 = QLabel(self.Fsignal)
        self.label_70.setObjectName(u"label_70")

        self.gridLayout_8.addWidget(self.label_70, 2, 1, 1, 1)

        self.label_63 = QLabel(self.Fsignal)
        self.label_63.setObjectName(u"label_63")

        self.gridLayout_8.addWidget(self.label_63, 3, 1, 1, 1)

        self.label_67 = QLabel(self.Fsignal)
        self.label_67.setObjectName(u"label_67")
        font5 = QFont()
        font5.setFamilies([u"Inter"])
        font5.setPointSize(7)
        font5.setBold(True)
        self.label_67.setFont(font5)

        self.gridLayout_8.addWidget(self.label_67, 1, 2, 1, 1)

        self.label_65 = QLabel(self.Fsignal)
        self.label_65.setObjectName(u"label_65")

        self.gridLayout_8.addWidget(self.label_65, 2, 2, 1, 1)

        self.label_61 = QLabel(self.Fsignal)
        self.label_61.setObjectName(u"label_61")
        self.label_61.setFont(font5)

        self.gridLayout_8.addWidget(self.label_61, 1, 1, 1, 1)

        self.label_68 = QLabel(self.Fsignal)
        self.label_68.setObjectName(u"label_68")
        self.label_68.setFont(font5)

        self.gridLayout_8.addWidget(self.label_68, 1, 0, 1, 1)

        self.label_62 = QLabel(self.Fsignal)
        self.label_62.setObjectName(u"label_62")

        self.gridLayout_8.addWidget(self.label_62, 3, 2, 1, 1)

        self.label_60 = QLabel(self.Fsignal)
        self.label_60.setObjectName(u"label_60")

        self.gridLayout_8.addWidget(self.label_60, 2, 0, 1, 1)


        self.verticalLayout_14.addWidget(self.Fsignal)


        self.verticalLayout_12.addWidget(self.frame_22)


        self.verticalLayout_17.addWidget(self.COMMS)

        self.SYS = QFrame(self.COL1)
        self.SYS.setObjectName(u"SYS")
        sizePolicy2.setHeightForWidth(self.SYS.sizePolicy().hasHeightForWidth())
        self.SYS.setSizePolicy(sizePolicy2)
        self.SYS.setFont(font1)
        self.SYS.setFrameShape(QFrame.Box)
        self.SYS.setFrameShadow(QFrame.Raised)
        self.SYS.setLineWidth(2)
        self.verticalLayout_16 = QVBoxLayout(self.SYS)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(3, 0, 3, 0)
        self.Fbattery = QFrame(self.SYS)
        self.Fbattery.setObjectName(u"Fbattery")
        font6 = QFont()
        font6.setFamilies([u"Inter"])
        font6.setPointSize(2)
        self.Fbattery.setFont(font6)
        self.Fbattery.setFrameShape(QFrame.NoFrame)
        self.Fbattery.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.Fbattery)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 5, 0, 0)
        self.frame_23 = QFrame(self.Fbattery)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setFrameShape(QFrame.NoFrame)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_23)
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.label_84 = QLabel(self.frame_23)
        self.label_84.setObjectName(u"label_84")
        self.label_84.setFont(font2)

        self.horizontalLayout_16.addWidget(self.label_84)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_3)

        self.frame_24 = QFrame(self.frame_23)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setFrameShape(QFrame.NoFrame)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_24)
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(9, 0, 0, 0)
        self.cbPIR = QCheckBox(self.frame_24)
        self.cbPIR.setObjectName(u"cbPIR")
        self.cbPIR.setFont(font2)

        self.horizontalLayout_17.addWidget(self.cbPIR)


        self.horizontalLayout_16.addWidget(self.frame_24)


        self.verticalLayout_15.addWidget(self.frame_23)

        self.label_87 = QLabel(self.Fbattery)
        self.label_87.setObjectName(u"label_87")
        self.label_87.setFont(font1)
        self.label_87.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_15.addWidget(self.label_87)

        self.frame_27 = QFrame(self.Fbattery)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setFrameShape(QFrame.NoFrame)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_27)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.label_99 = QLabel(self.frame_27)
        self.label_99.setObjectName(u"label_99")
        font7 = QFont()
        font7.setFamilies([u"Inter"])
        font7.setPointSize(11)
        font7.setBold(True)
        self.label_99.setFont(font7)

        self.horizontalLayout_15.addWidget(self.label_99)

        self.SLbattery = QSlider(self.frame_27)
        self.SLbattery.setObjectName(u"SLbattery")
        sizePolicy6 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.SLbattery.sizePolicy().hasHeightForWidth())
        self.SLbattery.setSizePolicy(sizePolicy6)
        self.SLbattery.setMinimumSize(QSize(150, 0))
        self.SLbattery.setMinimum(0)
        self.SLbattery.setMaximum(100)
        self.SLbattery.setOrientation(Qt.Horizontal)
        self.SLbattery.setInvertedAppearance(False)
        self.SLbattery.setInvertedControls(False)
        self.SLbattery.setTickPosition(QSlider.NoTicks)

        self.horizontalLayout_15.addWidget(self.SLbattery)


        self.verticalLayout_15.addWidget(self.frame_27)


        self.verticalLayout_16.addWidget(self.Fbattery)

        self.Fsonar = QFrame(self.SYS)
        self.Fsonar.setObjectName(u"Fsonar")
        self.Fsonar.setFrameShape(QFrame.NoFrame)
        self.Fsonar.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.Fsonar)
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.label_85 = QLabel(self.Fsonar)
        self.label_85.setObjectName(u"label_85")
        self.label_85.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_18.addWidget(self.label_85)

        self.frame_6 = QFrame(self.Fsonar)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.NoFrame)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.label_86 = QLabel(self.frame_6)
        self.label_86.setObjectName(u"label_86")
        self.label_86.setFont(font7)

        self.horizontalLayout_14.addWidget(self.label_86)

        self.SLranger = QSlider(self.frame_6)
        self.SLranger.setObjectName(u"SLranger")
        sizePolicy6.setHeightForWidth(self.SLranger.sizePolicy().hasHeightForWidth())
        self.SLranger.setSizePolicy(sizePolicy6)
        self.SLranger.setMinimumSize(QSize(150, 0))
        font8 = QFont()
        font8.setFamilies([u"Inter"])
        font8.setPointSize(16)
        self.SLranger.setFont(font8)
        self.SLranger.setMinimum(20)
        self.SLranger.setMaximum(765)
        self.SLranger.setOrientation(Qt.Horizontal)

        self.horizontalLayout_14.addWidget(self.SLranger)


        self.verticalLayout_18.addWidget(self.frame_6)


        self.verticalLayout_16.addWidget(self.Fsonar)

        self.frame_20 = QFrame(self.SYS)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setFrameShape(QFrame.NoFrame)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_20)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_57 = QLabel(self.frame_20)
        self.label_57.setObjectName(u"label_57")

        self.horizontalLayout.addWidget(self.label_57)

        self.label_64 = QLabel(self.frame_20)
        self.label_64.setObjectName(u"label_64")
        font9 = QFont()
        font9.setFamilies([u"Inter"])
        font9.setPointSize(9)
        font9.setBold(True)
        self.label_64.setFont(font9)

        self.horizontalLayout.addWidget(self.label_64)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_4)


        self.verticalLayout_16.addWidget(self.frame_20)


        self.verticalLayout_17.addWidget(self.SYS)

        self.RECORD = QFrame(self.COL1)
        self.RECORD.setObjectName(u"RECORD")
        sizePolicy2.setHeightForWidth(self.RECORD.sizePolicy().hasHeightForWidth())
        self.RECORD.setSizePolicy(sizePolicy2)
        self.RECORD.setFont(font4)
        self.RECORD.setFrameShape(QFrame.Box)
        self.RECORD.setFrameShadow(QFrame.Raised)
        self.RECORD.setLineWidth(2)
        self.gridLayout_9 = QGridLayout(self.RECORD)
        self.gridLayout_9.setSpacing(4)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setContentsMargins(4, 0, 4, 0)
        self.PB_Play = QPushButton(self.RECORD)
        self.PB_Play.setObjectName(u"PB_Play")

        self.gridLayout_9.addWidget(self.PB_Play, 3, 1, 1, 1)

        self.label_8 = QLabel(self.RECORD)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_9.addWidget(self.label_8, 0, 1, 1, 1)

        self.PB_Record = QPushButton(self.RECORD)
        self.PB_Record.setObjectName(u"PB_Record")

        self.gridLayout_9.addWidget(self.PB_Record, 1, 0, 1, 1)

        self.line = QFrame(self.RECORD)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout_9.addWidget(self.line, 2, 0, 1, 1)

        self.label_3 = QLabel(self.RECORD)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font2)

        self.gridLayout_9.addWidget(self.label_3, 0, 0, 1, 1)

        self.line_2 = QFrame(self.RECORD)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.gridLayout_9.addWidget(self.line_2, 2, 1, 1, 1)

        self.SLspeed = QSlider(self.RECORD)
        self.SLspeed.setObjectName(u"SLspeed")
        self.SLspeed.setMinimum(10)
        self.SLspeed.setMaximum(2000)
        self.SLspeed.setSingleStep(50)
        self.SLspeed.setPageStep(50)
        self.SLspeed.setValue(500)
        self.SLspeed.setSliderPosition(500)
        self.SLspeed.setOrientation(Qt.Horizontal)

        self.gridLayout_9.addWidget(self.SLspeed, 4, 1, 1, 1)

        self.label_9 = QLabel(self.RECORD)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_9.addWidget(self.label_9, 4, 0, 1, 1)

        self.RecordFileName = QLineEdit(self.RECORD)
        self.RecordFileName.setObjectName(u"RecordFileName")

        self.gridLayout_9.addWidget(self.RecordFileName, 1, 1, 1, 1)

        self.PB_Load = QPushButton(self.RECORD)
        self.PB_Load.setObjectName(u"PB_Load")

        self.gridLayout_9.addWidget(self.PB_Load, 3, 0, 1, 1)

        self.label_89 = QLabel(self.RECORD)
        self.label_89.setObjectName(u"label_89")

        self.gridLayout_9.addWidget(self.label_89, 4, 2, 1, 1)


        self.verticalLayout_17.addWidget(self.RECORD)

        self.LOCO = QFrame(self.COL1)
        self.LOCO.setObjectName(u"LOCO")
        sizePolicy2.setHeightForWidth(self.LOCO.sizePolicy().hasHeightForWidth())
        self.LOCO.setSizePolicy(sizePolicy2)
        self.LOCO.setFont(font1)
        self.LOCO.setFrameShape(QFrame.Box)
        self.LOCO.setFrameShadow(QFrame.Raised)
        self.LOCO.setLineWidth(2)
        self.verticalLayout_9 = QVBoxLayout(self.LOCO)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(3, 0, 3, 3)
        self.frame_17 = QFrame(self.LOCO)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.NoFrame)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.label_36 = QLabel(self.frame_17)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setFont(font2)

        self.horizontalLayout_9.addWidget(self.label_36)


        self.verticalLayout_9.addWidget(self.frame_17)

        self.frame_21 = QFrame(self.LOCO)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setFrameShape(QFrame.NoFrame)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_21)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 5, 0, 0)
        self.widget_2 = QWidget(self.frame_21)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setFont(font1)
        self.gridLayout_4 = QGridLayout(self.widget_2)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(4, 0, 0, 0)
        self.label_50 = QLabel(self.widget_2)
        self.label_50.setObjectName(u"label_50")

        self.gridLayout_4.addWidget(self.label_50, 3, 1, 1, 1)

        self.label_42 = QLabel(self.widget_2)
        self.label_42.setObjectName(u"label_42")

        self.gridLayout_4.addWidget(self.label_42, 1, 0, 1, 1)

        self.label_37 = QLabel(self.widget_2)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setFont(font5)

        self.gridLayout_4.addWidget(self.label_37, 0, 1, 1, 1)

        self.label_45 = QLabel(self.widget_2)
        self.label_45.setObjectName(u"label_45")

        self.gridLayout_4.addWidget(self.label_45, 2, 2, 1, 1)

        self.label_48 = QLabel(self.widget_2)
        self.label_48.setObjectName(u"label_48")

        self.gridLayout_4.addWidget(self.label_48, 2, 1, 1, 1)

        self.label_49 = QLabel(self.widget_2)
        self.label_49.setObjectName(u"label_49")

        self.gridLayout_4.addWidget(self.label_49, 3, 0, 1, 1)

        self.label_47 = QLabel(self.widget_2)
        self.label_47.setObjectName(u"label_47")

        self.gridLayout_4.addWidget(self.label_47, 1, 2, 1, 1)

        self.label_39 = QLabel(self.widget_2)
        self.label_39.setObjectName(u"label_39")

        self.gridLayout_4.addWidget(self.label_39, 2, 0, 1, 1)

        self.label_41 = QLabel(self.widget_2)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setFont(font5)

        self.gridLayout_4.addWidget(self.label_41, 0, 2, 1, 1)

        self.label_46 = QLabel(self.widget_2)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setFont(font5)

        self.gridLayout_4.addWidget(self.label_46, 0, 0, 1, 1)

        self.label_51 = QLabel(self.widget_2)
        self.label_51.setObjectName(u"label_51")

        self.gridLayout_4.addWidget(self.label_51, 3, 2, 1, 1)

        self.label_38 = QLabel(self.widget_2)
        self.label_38.setObjectName(u"label_38")

        self.gridLayout_4.addWidget(self.label_38, 1, 1, 1, 1)


        self.verticalLayout_7.addWidget(self.widget_2)


        self.verticalLayout_9.addWidget(self.frame_21)


        self.verticalLayout_17.addWidget(self.LOCO)

        self.IMU = QFrame(self.COL1)
        self.IMU.setObjectName(u"IMU")
        sizePolicy2.setHeightForWidth(self.IMU.sizePolicy().hasHeightForWidth())
        self.IMU.setSizePolicy(sizePolicy2)
        self.IMU.setFrameShape(QFrame.Box)
        self.IMU.setFrameShadow(QFrame.Raised)
        self.IMU.setLineWidth(2)
        self.verticalLayout_3 = QVBoxLayout(self.IMU)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 3, 0)
        self.frame_7 = QFrame(self.IMU)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.NoFrame)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(3, 0, 2, 0)
        self.label_12 = QLabel(self.frame_7)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font2)

        self.horizontalLayout_3.addWidget(self.label_12)


        self.verticalLayout_3.addWidget(self.frame_7)

        self.frame_5 = QFrame(self.IMU)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFont(font1)
        self.frame_5.setFrameShape(QFrame.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_5)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(0)
        self.gridLayout_2.setVerticalSpacing(1)
        self.gridLayout_2.setContentsMargins(0, 5, 0, 5)
        self.iHeading = QLabel(self.frame_5)
        self.iHeading.setObjectName(u"iHeading")

        self.gridLayout_2.addWidget(self.iHeading, 0, 1, 1, 1)

        self.label_20 = QLabel(self.frame_5)
        self.label_20.setObjectName(u"label_20")

        self.gridLayout_2.addWidget(self.label_20, 4, 0, 1, 1)

        self.iPitch = QLabel(self.frame_5)
        self.iPitch.setObjectName(u"iPitch")

        self.gridLayout_2.addWidget(self.iPitch, 1, 1, 1, 1)

        self.label_13 = QLabel(self.frame_5)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_2.addWidget(self.label_13, 0, 0, 1, 1)

        self.label_19 = QLabel(self.frame_5)
        self.label_19.setObjectName(u"label_19")

        self.gridLayout_2.addWidget(self.label_19, 3, 0, 1, 1)

        self.label_16 = QLabel(self.frame_5)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout_2.addWidget(self.label_16, 2, 0, 1, 1)

        self.iRoll = QLabel(self.frame_5)
        self.iRoll.setObjectName(u"iRoll")

        self.gridLayout_2.addWidget(self.iRoll, 2, 1, 1, 1)

        self.label_15 = QLabel(self.frame_5)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout_2.addWidget(self.label_15, 1, 0, 1, 1)

        self.label_21 = QLabel(self.frame_5)
        self.label_21.setObjectName(u"label_21")

        self.gridLayout_2.addWidget(self.label_21, 5, 0, 1, 1)

        self.iTemp = QLabel(self.frame_5)
        self.iTemp.setObjectName(u"iTemp")

        self.gridLayout_2.addWidget(self.iTemp, 3, 1, 1, 1)

        self.iPressure = QLabel(self.frame_5)
        self.iPressure.setObjectName(u"iPressure")

        self.gridLayout_2.addWidget(self.iPressure, 4, 1, 1, 1)

        self.iAltitude = QLabel(self.frame_5)
        self.iAltitude.setObjectName(u"iAltitude")

        self.gridLayout_2.addWidget(self.iAltitude, 5, 1, 1, 1)


        self.verticalLayout_3.addWidget(self.frame_5)

        self.widget = QWidget(self.IMU)
        self.widget.setObjectName(u"widget")
        self.widget.setFont(font4)
        self.gridLayout_3 = QGridLayout(self.widget)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(4, 0, 0, 0)
        self.label_17 = QLabel(self.widget)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font5)

        self.gridLayout_3.addWidget(self.label_17, 0, 1, 1, 1)

        self.label_26 = QLabel(self.widget)
        self.label_26.setObjectName(u"label_26")

        self.gridLayout_3.addWidget(self.label_26, 1, 1, 1, 1)

        self.label_18 = QLabel(self.widget)
        self.label_18.setObjectName(u"label_18")

        self.gridLayout_3.addWidget(self.label_18, 2, 0, 1, 1)

        self.label_29 = QLabel(self.widget)
        self.label_29.setObjectName(u"label_29")

        self.gridLayout_3.addWidget(self.label_29, 4, 1, 1, 1)

        self.label_24 = QLabel(self.widget)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setFont(font5)

        self.gridLayout_3.addWidget(self.label_24, 0, 2, 1, 1)

        self.label_23 = QLabel(self.widget)
        self.label_23.setObjectName(u"label_23")

        self.gridLayout_3.addWidget(self.label_23, 1, 0, 1, 1)

        self.label_28 = QLabel(self.widget)
        self.label_28.setObjectName(u"label_28")

        self.gridLayout_3.addWidget(self.label_28, 4, 0, 1, 1)

        self.label_30 = QLabel(self.widget)
        self.label_30.setObjectName(u"label_30")

        self.gridLayout_3.addWidget(self.label_30, 4, 2, 1, 1)

        self.label_25 = QLabel(self.widget)
        self.label_25.setObjectName(u"label_25")

        self.gridLayout_3.addWidget(self.label_25, 2, 2, 1, 1)

        self.label_14 = QLabel(self.widget)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font5)

        self.gridLayout_3.addWidget(self.label_14, 0, 0, 1, 1)

        self.label_27 = QLabel(self.widget)
        self.label_27.setObjectName(u"label_27")

        self.gridLayout_3.addWidget(self.label_27, 1, 2, 1, 1)

        self.label_22 = QLabel(self.widget)
        self.label_22.setObjectName(u"label_22")

        self.gridLayout_3.addWidget(self.label_22, 2, 1, 1, 1)

        self.label_31 = QLabel(self.widget)
        self.label_31.setObjectName(u"label_31")

        self.gridLayout_3.addWidget(self.label_31, 3, 0, 1, 1)

        self.label_32 = QLabel(self.widget)
        self.label_32.setObjectName(u"label_32")

        self.gridLayout_3.addWidget(self.label_32, 3, 1, 1, 1)

        self.label_33 = QLabel(self.widget)
        self.label_33.setObjectName(u"label_33")

        self.gridLayout_3.addWidget(self.label_33, 3, 2, 1, 1)


        self.verticalLayout_3.addWidget(self.widget)


        self.verticalLayout_17.addWidget(self.IMU)

        self.GPS = QFrame(self.COL1)
        self.GPS.setObjectName(u"GPS")
        sizePolicy2.setHeightForWidth(self.GPS.sizePolicy().hasHeightForWidth())
        self.GPS.setSizePolicy(sizePolicy2)
        self.GPS.setFont(font1)
        self.GPS.setFrameShape(QFrame.Box)
        self.GPS.setFrameShadow(QFrame.Raised)
        self.GPS.setLineWidth(2)
        self.verticalLayout_8 = QVBoxLayout(self.GPS)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(3, 0, 3, 3)
        self.frame_12 = QFrame(self.GPS)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.NoFrame)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_11 = QLabel(self.frame_12)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font2)

        self.horizontalLayout_6.addWidget(self.label_11)


        self.verticalLayout_8.addWidget(self.frame_12)

        self.frame_14 = QFrame(self.GPS)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.NoFrame)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 6, 0, 0)
        self.frame_13 = QFrame(self.frame_14)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.NoFrame)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_13)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_7.addWidget(self.frame_13)

        self.frame_15 = QFrame(self.frame_14)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.NoFrame)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_15)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_7.addWidget(self.frame_15)


        self.verticalLayout_8.addWidget(self.frame_14)

        self.frame = QFrame(self.GPS)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame)
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gAccuracy = QLabel(self.frame)
        self.gAccuracy.setObjectName(u"gAccuracy")

        self.gridLayout_5.addWidget(self.gAccuracy, 2, 1, 1, 1)

        self.label_53 = QLabel(self.frame)
        self.label_53.setObjectName(u"label_53")

        self.gridLayout_5.addWidget(self.label_53, 4, 0, 1, 1)

        self.gNumSats = QLabel(self.frame)
        self.gNumSats.setObjectName(u"gNumSats")

        self.gridLayout_5.addWidget(self.gNumSats, 1, 1, 1, 1)

        self.label_44 = QLabel(self.frame)
        self.label_44.setObjectName(u"label_44")

        self.gridLayout_5.addWidget(self.label_44, 0, 0, 1, 1)

        self.gLong = QLabel(self.frame)
        self.gLong.setObjectName(u"gLong")
        self.gLong.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.gLong, 4, 1, 1, 1)

        self.label_52 = QLabel(self.frame)
        self.label_52.setObjectName(u"label_52")

        self.gridLayout_5.addWidget(self.label_52, 1, 0, 1, 1)

        self.gAlt = QLabel(self.frame)
        self.gAlt.setObjectName(u"gAlt")

        self.gridLayout_5.addWidget(self.gAlt, 5, 1, 1, 1)

        self.label_43 = QLabel(self.frame)
        self.label_43.setObjectName(u"label_43")

        self.gridLayout_5.addWidget(self.label_43, 3, 0, 1, 1)

        self.label_40 = QLabel(self.frame)
        self.label_40.setObjectName(u"label_40")

        self.gridLayout_5.addWidget(self.label_40, 2, 0, 1, 1)

        self.gLat = QLabel(self.frame)
        self.gLat.setObjectName(u"gLat")
        self.gLat.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.gLat, 3, 1, 1, 1)

        self.gQuality = QLabel(self.frame)
        self.gQuality.setObjectName(u"gQuality")

        self.gridLayout_5.addWidget(self.gQuality, 0, 1, 1, 1)

        self.label_54 = QLabel(self.frame)
        self.label_54.setObjectName(u"label_54")

        self.gridLayout_5.addWidget(self.label_54, 5, 0, 1, 1)

        self.label_56 = QLabel(self.frame)
        self.label_56.setObjectName(u"label_56")

        self.gridLayout_5.addWidget(self.label_56, 6, 0, 1, 1)

        self.gVariance = QLabel(self.frame)
        self.gVariance.setObjectName(u"gVariance")

        self.gridLayout_5.addWidget(self.gVariance, 6, 1, 1, 1)


        self.verticalLayout_8.addWidget(self.frame)

        self.frame_16 = QFrame(self.GPS)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.NoFrame)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.gridLayout_7 = QGridLayout(self.frame_16)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setHorizontalSpacing(0)
        self.gridLayout_7.setContentsMargins(0, 3, 0, 4)
        self.label_5 = QLabel(self.frame_16)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_7.addWidget(self.label_5, 3, 0, 1, 1)

        self.label_6 = QLabel(self.frame_16)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_7.addWidget(self.label_6, 5, 0, 1, 1)

        self.label_10 = QLabel(self.frame_16)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_7.addWidget(self.label_10, 7, 0, 1, 1)

        self.label_4 = QLabel(self.frame_16)
        self.label_4.setObjectName(u"label_4")
        sizePolicy7 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy7)

        self.gridLayout_7.addWidget(self.label_4, 1, 0, 1, 1)

        self.gLatBottom = QDoubleSpinBox(self.frame_16)
        self.gLatBottom.setObjectName(u"gLatBottom")
        sizePolicy8 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.gLatBottom.sizePolicy().hasHeightForWidth())
        self.gLatBottom.setSizePolicy(sizePolicy8)
        self.gLatBottom.setMinimumSize(QSize(100, 0))
        self.gLatBottom.setMaximumSize(QSize(120, 16777215))
        self.gLatBottom.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.gLatBottom.setDecimals(6)
        self.gLatBottom.setMinimum(-38.000000000000000)
        self.gLatBottom.setMaximum(-37.000000000000000)
        self.gLatBottom.setSingleStep(0.000010000000000)
        self.gLatBottom.setValue(-37.500000000000000)

        self.gridLayout_7.addWidget(self.gLatBottom, 1, 1, 1, 1, Qt.AlignRight)

        self.gLatMult = QSpinBox(self.frame_16)
        self.gLatMult.setObjectName(u"gLatMult")
        self.gLatMult.setMinimumSize(QSize(60, 0))
        self.gLatMult.setMaximumSize(QSize(60, 16777215))
        self.gLatMult.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.gLatMult.setMinimum(1)
        self.gLatMult.setMaximum(1000)
        self.gLatMult.setValue(800)
        self.gLatMult.setDisplayIntegerBase(10)

        self.gridLayout_7.addWidget(self.gLatMult, 3, 1, 1, 1, Qt.AlignRight)

        self.gLonLeft = QDoubleSpinBox(self.frame_16)
        self.gLonLeft.setObjectName(u"gLonLeft")
        self.gLonLeft.setMinimumSize(QSize(100, 0))
        self.gLonLeft.setMaximumSize(QSize(100, 16777215))
        self.gLonLeft.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.gLonLeft.setDecimals(6)
        self.gLonLeft.setMinimum(144.000000000000000)
        self.gLonLeft.setMaximum(145.000000000000000)
        self.gLonLeft.setSingleStep(0.000010000000000)
        self.gLonLeft.setValue(144.500000000000000)

        self.gridLayout_7.addWidget(self.gLonLeft, 5, 1, 1, 1)

        self.gLonMult = QSpinBox(self.frame_16)
        self.gLonMult.setObjectName(u"gLonMult")
        self.gLonMult.setMinimumSize(QSize(60, 0))
        self.gLonMult.setMaximumSize(QSize(60, 16777215))
        self.gLonMult.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.gLonMult.setMinimum(1)
        self.gLonMult.setMaximum(1000)
        self.gLonMult.setSingleStep(1)
        self.gLonMult.setValue(400)

        self.gridLayout_7.addWidget(self.gLonMult, 7, 1, 1, 1, Qt.AlignRight)


        self.verticalLayout_8.addWidget(self.frame_16)

        self.frame_8 = QFrame(self.GPS)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFont(font1)
        self.frame_8.setFrameShape(QFrame.NoFrame)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.frame_8)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setHorizontalSpacing(0)
        self.gridLayout_6.setVerticalSpacing(3)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.PB_MapPlot = QPushButton(self.frame_8)
        self.PB_MapPlot.setObjectName(u"PB_MapPlot")
        sizePolicy9 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.PB_MapPlot.sizePolicy().hasHeightForWidth())
        self.PB_MapPlot.setSizePolicy(sizePolicy9)

        self.gridLayout_6.addWidget(self.PB_MapPlot, 0, 0, 1, 1)

        self.PB_MapClear = QPushButton(self.frame_8)
        self.PB_MapClear.setObjectName(u"PB_MapClear")
        sizePolicy9.setHeightForWidth(self.PB_MapClear.sizePolicy().hasHeightForWidth())
        self.PB_MapClear.setSizePolicy(sizePolicy9)

        self.gridLayout_6.addWidget(self.PB_MapClear, 0, 1, 1, 1)

        self.label_34 = QLabel(self.frame_8)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.label_34, 1, 0, 1, 1)

        self.label_35 = QLabel(self.frame_8)
        self.label_35.setObjectName(u"label_35")
        sizePolicy10 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy10.setHorizontalStretch(0)
        sizePolicy10.setVerticalStretch(0)
        sizePolicy10.setHeightForWidth(self.label_35.sizePolicy().hasHeightForWidth())
        self.label_35.setSizePolicy(sizePolicy10)

        self.gridLayout_6.addWidget(self.label_35, 1, 1, 1, 1, Qt.AlignHCenter)

        self.lineEdit = QLineEdit(self.frame_8)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout_6.addWidget(self.lineEdit, 2, 0, 1, 1)

        self.lineEdit_2 = QLineEdit(self.frame_8)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.gridLayout_6.addWidget(self.lineEdit_2, 2, 1, 1, 1)


        self.verticalLayout_8.addWidget(self.frame_8)


        self.verticalLayout_17.addWidget(self.GPS)

        self.RC = QFrame(self.COL1)
        self.RC.setObjectName(u"RC")
        sizePolicy2.setHeightForWidth(self.RC.sizePolicy().hasHeightForWidth())
        self.RC.setSizePolicy(sizePolicy2)
        self.RC.setFrameShape(QFrame.Box)
        self.RC.setFrameShadow(QFrame.Raised)
        self.RC.setLineWidth(2)
        self.verticalLayout_2 = QVBoxLayout(self.RC)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(3, 0, 3, 0)
        self.frame_19 = QFrame(self.RC)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setFont(font3)
        self.frame_19.setFrameShape(QFrame.NoFrame)
        self.frame_19.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_19)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 7, 0)
        self.label_55 = QLabel(self.frame_19)
        self.label_55.setObjectName(u"label_55")
        self.label_55.setFont(font2)

        self.horizontalLayout_10.addWidget(self.label_55)

        self.BCH5 = QCheckBox(self.frame_19)
        self.BCH5.setObjectName(u"BCH5")
        font10 = QFont()
        font10.setFamilies([u"Inter"])
        font10.setPointSize(9)
        font10.setBold(False)
        self.BCH5.setFont(font10)

        self.horizontalLayout_10.addWidget(self.BCH5)

        self.BCH6 = QCheckBox(self.frame_19)
        self.BCH6.setObjectName(u"BCH6")
        self.BCH6.setFont(font10)

        self.horizontalLayout_10.addWidget(self.BCH6)


        self.verticalLayout_2.addWidget(self.frame_19)

        self.frame_32 = QFrame(self.RC)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setFont(font3)
        self.frame_32.setFrameShape(QFrame.NoFrame)
        self.frame_32.setFrameShadow(QFrame.Raised)
        self.gridLayout_13 = QGridLayout(self.frame_32)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.SL3 = QSlider(self.frame_32)
        self.SL3.setObjectName(u"SL3")
        self.SL3.setSingleStep(1)
        self.SL3.setValue(50)
        self.SL3.setOrientation(Qt.Vertical)

        self.gridLayout_13.addWidget(self.SL3, 0, 2, 1, 1)

        self.SL4 = QSlider(self.frame_32)
        self.SL4.setObjectName(u"SL4")
        self.SL4.setEnabled(True)
        self.SL4.setValue(50)
        self.SL4.setOrientation(Qt.Horizontal)

        self.gridLayout_13.addWidget(self.SL4, 0, 1, 1, 1)

        self.SL2 = QSlider(self.frame_32)
        self.SL2.setObjectName(u"SL2")
        self.SL2.setValue(50)
        self.SL2.setOrientation(Qt.Horizontal)

        self.gridLayout_13.addWidget(self.SL2, 0, 3, 1, 1)

        self.SL1 = QSlider(self.frame_32)
        self.SL1.setObjectName(u"SL1")
        self.SL1.setEnabled(True)
        self.SL1.setValue(50)
        self.SL1.setOrientation(Qt.Vertical)

        self.gridLayout_13.addWidget(self.SL1, 0, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.frame_32)

        self.frame_4 = QFrame(self.RC)
        self.frame_4.setObjectName(u"frame_4")
        font11 = QFont()
        font11.setFamilies([u"Inter"])
        font11.setPointSize(12)
        font11.setBold(True)
        self.frame_4.setFont(font11)
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, -1, 0)
        self.LCH1 = QLabel(self.frame_4)
        self.LCH1.setObjectName(u"LCH1")

        self.horizontalLayout_12.addWidget(self.LCH1)

        self.LCH4 = QLabel(self.frame_4)
        self.LCH4.setObjectName(u"LCH4")

        self.horizontalLayout_12.addWidget(self.LCH4)

        self.LCH3 = QLabel(self.frame_4)
        self.LCH3.setObjectName(u"LCH3")

        self.horizontalLayout_12.addWidget(self.LCH3)

        self.LCH2 = QLabel(self.frame_4)
        self.LCH2.setObjectName(u"LCH2")

        self.horizontalLayout_12.addWidget(self.LCH2)


        self.verticalLayout_2.addWidget(self.frame_4)

        self.frame_11 = QFrame(self.RC)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFont(font3)
        self.frame_11.setFrameShape(QFrame.NoFrame)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.frame_11.setLineWidth(-1)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.label_73 = QLabel(self.frame_11)
        self.label_73.setObjectName(u"label_73")

        self.horizontalLayout_13.addWidget(self.label_73)

        self.label_74 = QLabel(self.frame_11)
        self.label_74.setObjectName(u"label_74")

        self.horizontalLayout_13.addWidget(self.label_74)

        self.label_75 = QLabel(self.frame_11)
        self.label_75.setObjectName(u"label_75")

        self.horizontalLayout_13.addWidget(self.label_75)

        self.label_76 = QLabel(self.frame_11)
        self.label_76.setObjectName(u"label_76")

        self.horizontalLayout_13.addWidget(self.label_76)


        self.verticalLayout_2.addWidget(self.frame_11)

        self.frame_9 = QFrame(self.RC)
        self.frame_9.setObjectName(u"frame_9")
        font12 = QFont()
        font12.setFamilies([u"Inter"])
        font12.setPointSize(7)
        self.frame_9.setFont(font12)
        self.frame_9.setFrameShape(QFrame.NoFrame)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_77 = QLabel(self.frame_9)
        self.label_77.setObjectName(u"label_77")

        self.horizontalLayout_4.addWidget(self.label_77)

        self.label_79 = QLabel(self.frame_9)
        self.label_79.setObjectName(u"label_79")

        self.horizontalLayout_4.addWidget(self.label_79)

        self.label_78 = QLabel(self.frame_9)
        self.label_78.setObjectName(u"label_78")

        self.horizontalLayout_4.addWidget(self.label_78)

        self.label_80 = QLabel(self.frame_9)
        self.label_80.setObjectName(u"label_80")

        self.horizontalLayout_4.addWidget(self.label_80)


        self.verticalLayout_2.addWidget(self.frame_9)


        self.verticalLayout_17.addWidget(self.RC)


        self.horizontalLayout_2.addWidget(self.COL1)

        self.COL4 = QFrame(self.centralwidget)
        self.COL4.setObjectName(u"COL4")
        self.COL4.setFrameShape(QFrame.NoFrame)
        self.COL4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.COL4)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.frame_10 = QFrame(self.COL4)
        self.frame_10.setObjectName(u"frame_10")
        font13 = QFont()
        font13.setFamilies([u"Inter"])
        font13.setPointSize(14)
        font13.setBold(True)
        self.frame_10.setFont(font13)
        self.frame_10.setFrameShape(QFrame.NoFrame)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_10)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_26 = QFrame(self.frame_10)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setFrameShape(QFrame.NoFrame)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_26)
        self.horizontalLayout_19.setSpacing(0)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(0, -1, 0, 0)
        self.label_7 = QLabel(self.frame_26)
        self.label_7.setObjectName(u"label_7")
        font14 = QFont()
        font14.setFamilies([u"Inter"])
        font14.setPointSize(14)
        font14.setBold(True)
        font14.setItalic(False)
        self.label_7.setFont(font14)
        self.label_7.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_19.addWidget(self.label_7)


        self.gridLayout.addWidget(self.frame_26, 4, 1, 1, 1)

        self.ChartView3 = QChartView(self.frame_10)
        self.ChartView3.setObjectName(u"ChartView3")
        sizePolicy10.setHeightForWidth(self.ChartView3.sizePolicy().hasHeightForWidth())
        self.ChartView3.setSizePolicy(sizePolicy10)
        self.ChartView3.setMinimumSize(QSize(200, 200))
        self.ChartView3.setMaximumSize(QSize(200, 200))
        self.ChartView3.setFrameShape(QFrame.Box)
        self.ChartView3.setFrameShadow(QFrame.Raised)
        self.ChartView3.setLineWidth(2)

        self.gridLayout.addWidget(self.ChartView3, 3, 2, 1, 1)

        self.frame_33 = QFrame(self.frame_10)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setFrameShape(QFrame.NoFrame)
        self.frame_33.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.frame_33)
        self.horizontalLayout_23.setSpacing(0)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(0, 9, 0, 0)
        self.label = QLabel(self.frame_33)
        self.label.setObjectName(u"label")
        self.label.setFont(font14)
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_23.addWidget(self.label)


        self.gridLayout.addWidget(self.frame_33, 2, 1, 1, 1)

        self.label_81 = QLabel(self.frame_10)
        self.label_81.setObjectName(u"label_81")
        self.label_81.setFont(font2)
        self.label_81.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_81, 0, 1, 1, 1)

        self.RollGauge = QLabel(self.frame_10)
        self.RollGauge.setObjectName(u"RollGauge")
        self.RollGauge.setMinimumSize(QSize(200, 200))
        self.RollGauge.setFrameShape(QFrame.Box)
        self.RollGauge.setFrameShadow(QFrame.Raised)
        self.RollGauge.setLineWidth(2)
        self.RollGauge.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.RollGauge, 5, 2, 1, 1)

        self.ChartView2 = QChartView(self.frame_10)
        self.ChartView2.setObjectName(u"ChartView2")
        sizePolicy10.setHeightForWidth(self.ChartView2.sizePolicy().hasHeightForWidth())
        self.ChartView2.setSizePolicy(sizePolicy10)
        self.ChartView2.setMinimumSize(QSize(200, 200))
        self.ChartView2.setMaximumSize(QSize(200, 200))
        self.ChartView2.setFrameShape(QFrame.Box)
        self.ChartView2.setFrameShadow(QFrame.Raised)
        self.ChartView2.setLineWidth(2)

        self.gridLayout.addWidget(self.ChartView2, 3, 1, 1, 1)

        self.frame_34 = QFrame(self.frame_10)
        self.frame_34.setObjectName(u"frame_34")
        self.frame_34.setFrameShape(QFrame.NoFrame)
        self.frame_34.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_34)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 9, 0, 0)
        self.label_2 = QLabel(self.frame_34)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font14)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_8.addWidget(self.label_2)


        self.gridLayout.addWidget(self.frame_34, 2, 2, 1, 1)

        self.PitchGauge = QLabel(self.frame_10)
        self.PitchGauge.setObjectName(u"PitchGauge")
        self.PitchGauge.setMinimumSize(QSize(200, 200))
        self.PitchGauge.setFrameShape(QFrame.Box)
        self.PitchGauge.setFrameShadow(QFrame.Raised)
        self.PitchGauge.setLineWidth(2)
        self.PitchGauge.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.PitchGauge, 5, 1, 1, 1)

        self.frame_35 = QFrame(self.frame_10)
        self.frame_35.setObjectName(u"frame_35")
        self.frame_35.setFrameShape(QFrame.NoFrame)
        self.frame_35.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_24 = QHBoxLayout(self.frame_35)
        self.horizontalLayout_24.setSpacing(0)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(0, -1, 0, 0)
        self.label_72 = QLabel(self.frame_35)
        self.label_72.setObjectName(u"label_72")
        self.label_72.setFont(font14)
        self.label_72.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_24.addWidget(self.label_72)


        self.gridLayout.addWidget(self.frame_35, 6, 2, 1, 1)

        self.frame_28 = QFrame(self.frame_10)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_28)
        self.horizontalLayout_20.setSpacing(0)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.label_83 = QLabel(self.frame_28)
        self.label_83.setObjectName(u"label_83")
        self.label_83.setFont(font9)

        self.horizontalLayout_20.addWidget(self.label_83)

        self.PB_MagReset = QPushButton(self.frame_28)
        self.PB_MagReset.setObjectName(u"PB_MagReset")
        sizePolicy11 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy11.setHorizontalStretch(0)
        sizePolicy11.setVerticalStretch(0)
        sizePolicy11.setHeightForWidth(self.PB_MagReset.sizePolicy().hasHeightForWidth())
        self.PB_MagReset.setSizePolicy(sizePolicy11)
        self.PB_MagReset.setMaximumSize(QSize(40, 16777215))
        font15 = QFont()
        font15.setFamilies([u"Inter"])
        font15.setPointSize(11)
        font15.setBold(False)
        self.PB_MagReset.setFont(font15)

        self.horizontalLayout_20.addWidget(self.PB_MagReset)


        self.gridLayout.addWidget(self.frame_28, 6, 1, 1, 1)

        self.frame_25 = QFrame(self.frame_10)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setFrameShape(QFrame.NoFrame)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_25)
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, -1, 0, 0)
        self.label_71 = QLabel(self.frame_25)
        self.label_71.setObjectName(u"label_71")
        self.label_71.setFont(font14)
        self.label_71.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_18.addWidget(self.label_71)


        self.gridLayout.addWidget(self.frame_25, 4, 2, 1, 1)

        self.frame_36 = QFrame(self.frame_10)
        self.frame_36.setObjectName(u"frame_36")
        self.frame_36.setFrameShape(QFrame.Box)
        self.frame_36.setFrameShadow(QFrame.Raised)
        self.frame_36.setLineWidth(2)
        self.horizontalLayout_25 = QHBoxLayout(self.frame_36)
        self.horizontalLayout_25.setSpacing(0)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.ChartView4 = QChartView(self.frame_36)
        self.ChartView4.setObjectName(u"ChartView4")

        self.horizontalLayout_25.addWidget(self.ChartView4)


        self.gridLayout.addWidget(self.frame_36, 7, 1, 1, 1)

        self.label_82 = QLabel(self.frame_10)
        self.label_82.setObjectName(u"label_82")
        self.label_82.setFont(font2)
        self.label_82.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_82, 0, 2, 1, 1)

        self.CompassGauge = QLabel(self.frame_10)
        self.CompassGauge.setObjectName(u"CompassGauge")
        self.CompassGauge.setMinimumSize(QSize(200, 200))
        self.CompassGauge.setFrameShape(QFrame.Box)
        self.CompassGauge.setFrameShadow(QFrame.Raised)
        self.CompassGauge.setLineWidth(2)
        self.CompassGauge.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.CompassGauge, 7, 2, 1, 1)


        self.verticalLayout_13.addWidget(self.frame_10)

        self.frame_29 = QFrame(self.COL4)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setFrameShape(QFrame.NoFrame)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_29)
        self.horizontalLayout_21.setSpacing(0)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.label_88 = QLabel(self.frame_29)
        self.label_88.setObjectName(u"label_88")
        self.label_88.setFont(font11)

        self.horizontalLayout_21.addWidget(self.label_88)

        self.PB_GPSVarReset = QPushButton(self.frame_29)
        self.PB_GPSVarReset.setObjectName(u"PB_GPSVarReset")
        sizePolicy5.setHeightForWidth(self.PB_GPSVarReset.sizePolicy().hasHeightForWidth())
        self.PB_GPSVarReset.setSizePolicy(sizePolicy5)
        self.PB_GPSVarReset.setMinimumSize(QSize(14, 0))
        self.PB_GPSVarReset.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout_21.addWidget(self.PB_GPSVarReset)


        self.verticalLayout_13.addWidget(self.frame_29)

        self.frame_31 = QFrame(self.COL4)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setFrameShape(QFrame.Box)
        self.frame_31.setFrameShadow(QFrame.Raised)
        self.frame_31.setLineWidth(2)
        self.verticalLayout_6 = QVBoxLayout(self.frame_31)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.ChartView1 = QChartView(self.frame_31)
        self.ChartView1.setObjectName(u"ChartView1")
        font16 = QFont()
        font16.setFamilies([u"Inter"])
        font16.setPointSize(6)
        self.ChartView1.setFont(font16)
        self.ChartView1.setFrameShape(QFrame.NoFrame)
        self.ChartView1.setFrameShadow(QFrame.Raised)
        self.ChartView1.setLineWidth(2)

        self.verticalLayout_6.addWidget(self.ChartView1)


        self.verticalLayout_13.addWidget(self.frame_31)


        self.horizontalLayout_2.addWidget(self.COL4)

        self.COL3 = QFrame(self.centralwidget)
        self.COL3.setObjectName(u"COL3")
        sizePolicy1.setHeightForWidth(self.COL3.sizePolicy().hasHeightForWidth())
        self.COL3.setSizePolicy(sizePolicy1)
        self.COL3.setMaximumSize(QSize(800, 16777215))
        self.COL3.setFrameShape(QFrame.NoFrame)
        self.COL3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.COL3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.GPSmap = QLabel(self.COL3)
        self.GPSmap.setObjectName(u"GPSmap")
        sizePolicy10.setHeightForWidth(self.GPSmap.sizePolicy().hasHeightForWidth())
        self.GPSmap.setSizePolicy(sizePolicy10)
        self.GPSmap.setMinimumSize(QSize(700, 500))
        self.GPSmap.setFrameShape(QFrame.Box)
        self.GPSmap.setFrameShadow(QFrame.Raised)
        self.GPSmap.setLineWidth(2)
        self.GPSmap.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.GPSmap)

        self.frame_2 = QFrame(self.COL3)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Box)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.frame_2.setLineWidth(2)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.Video_widget = QVideoWidget(self.frame_2)
        self.Video_widget.setObjectName(u"Video_widget")
        sizePolicy6.setHeightForWidth(self.Video_widget.sizePolicy().hasHeightForWidth())
        self.Video_widget.setSizePolicy(sizePolicy6)
        self.Video_widget.setMinimumSize(QSize(700, 500))
        self.Video_widget.setMaximumSize(QSize(700, 500))

        self.horizontalLayout_5.addWidget(self.Video_widget)


        self.verticalLayout_4.addWidget(self.frame_2)


        self.horizontalLayout_2.addWidget(self.COL3)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1372, 25))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.PB_MapPlot.clicked.connect(self.actionGPS_Map.trigger)
        self.PB_MapClear.clicked.connect(self.actionGPS_Clear.trigger)
        self.PB_Play.clicked.connect(self.actionPlay.trigger)
        self.PB_Load.clicked.connect(self.actionLoad.trigger)
        self.PB_Record.clicked.connect(self.actionRecord.trigger)
        self.PB_CommsStop.clicked.connect(self.actionCommsStop.trigger)
        self.PB_MagReset.clicked.connect(self.actionMagReset.trigger)
        self.PB_GPSVarReset.clicked.connect(self.actionGPSVarReset.trigger)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Roverling Telemetry v2.18       Mark Makies", None))
        self.actionGPS_Map.setText(QCoreApplication.translate("MainWindow", u"GPS-Map", None))
        self.actionGPS_Clear.setText(QCoreApplication.translate("MainWindow", u"GPS-Clear", None))
        self.actionRecord.setText(QCoreApplication.translate("MainWindow", u"Record", None))
        self.actionLoad.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.actionPlay.setText(QCoreApplication.translate("MainWindow", u"Play", None))
        self.actionGPS_Reset.setText(QCoreApplication.translate("MainWindow", u"GPS-Reset", None))
        self.actionCommsStop.setText(QCoreApplication.translate("MainWindow", u"CommsStop", None))
        self.actionMagReset.setText(QCoreApplication.translate("MainWindow", u"MagReset", None))
        self.actionGPSVarReset.setText(QCoreApplication.translate("MainWindow", u"GPSVarReset", None))
        self.label_58.setText(QCoreApplication.translate("MainWindow", u"COMMS", None))
        self.PB_CommsStop.setText(QCoreApplication.translate("MainWindow", u"RUNNING", None))
        self.label_59.setText(QCoreApplication.translate("MainWindow", u"Pkt Count", None))
        self.Ppulse.setText(QCoreApplication.translate("MainWindow", u"P", None))
        self.label_69.setText(QCoreApplication.translate("MainWindow", u"GPS Sec", None))
        self.Gpulse.setText(QCoreApplication.translate("MainWindow", u"P", None))
        self.label_66.setText(QCoreApplication.translate("MainWindow", u"ROVER", None))
        self.label_70.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_63.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_67.setText(QCoreApplication.translate("MainWindow", u"SNR", None))
        self.label_65.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_61.setText(QCoreApplication.translate("MainWindow", u"RSSI", None))
        self.label_68.setText(QCoreApplication.translate("MainWindow", u"PARAM", None))
        self.label_62.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_60.setText(QCoreApplication.translate("MainWindow", u"BASE", None))
        self.label_84.setText(QCoreApplication.translate("MainWindow", u"SYSTEM", None))
        self.cbPIR.setText(QCoreApplication.translate("MainWindow", u" PIR ", None))
        self.label_87.setText(QCoreApplication.translate("MainWindow", u"Battery Level", None))
        self.label_99.setText(QCoreApplication.translate("MainWindow", u"50%", None))
        self.label_85.setText(QCoreApplication.translate("MainWindow", u"Sonar Ranger", None))
        self.label_86.setText(QCoreApplication.translate("MainWindow", u"600 cm", None))
        self.label_57.setText(QCoreApplication.translate("MainWindow", u"Status Bits : ", None))
        self.label_64.setText(QCoreApplication.translate("MainWindow", u"01010101 10101010", None))
        self.PB_Play.setText(QCoreApplication.translate("MainWindow", u"Stopped", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"File Name", None))
        self.PB_Record.setText(QCoreApplication.translate("MainWindow", u"Paused", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"RECORD", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.RecordFileName.setText("")
        self.PB_Load.setText(QCoreApplication.translate("MainWindow", u"Load", None))
        self.label_89.setText(QCoreApplication.translate("MainWindow", u"500 ms", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"LOCOMOTION", None))
        self.label_50.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"Velocity", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"LEFT", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"Power", None))
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"Current", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"RIGHT", None))
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"PARAM", None))
        self.label_51.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"IMU", None))
        self.iHeading.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Pressure", None))
        self.iPitch.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Heading", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Temp", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Roll", None))
        self.iRoll.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Pitch", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Altitude (calc)", None))
        self.iTemp.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.iPressure.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.iAltitude.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"CURRENT", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"X Max", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"OBS LIMITS", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"X Min", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Y Max", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Mag PARAM", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Y Min", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"GPS / GNSS", None))
        self.gAccuracy.setText(QCoreApplication.translate("MainWindow", u"gAccuracy", None))
        self.label_53.setText(QCoreApplication.translate("MainWindow", u"Longitude", None))
        self.gNumSats.setText(QCoreApplication.translate("MainWindow", u"gNumber", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"Quality", None))
        self.gLong.setText(QCoreApplication.translate("MainWindow", u"long", None))
        self.label_52.setText(QCoreApplication.translate("MainWindow", u"Num Sats", None))
        self.gAlt.setText(QCoreApplication.translate("MainWindow", u"alt", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"Latitude", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"Accuracy", None))
        self.gLat.setText(QCoreApplication.translate("MainWindow", u"lat", None))
        self.gQuality.setText(QCoreApplication.translate("MainWindow", u"gQuality", None))
        self.label_54.setText(QCoreApplication.translate("MainWindow", u"Altitude", None))
        self.label_56.setText(QCoreApplication.translate("MainWindow", u"Variance (x / y)", None))
        self.gVariance.setText(QCoreApplication.translate("MainWindow", u"variance", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Lat Multiplier", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Long Left", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Long Mult", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Lat Bottom", None))
        self.PB_MapPlot.setText(QCoreApplication.translate("MainWindow", u"Plot Point", None))
        self.PB_MapClear.setText(QCoreApplication.translate("MainWindow", u"Clear Map", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"Latitude", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"Longitude", None))
        self.lineEdit.setText(QCoreApplication.translate("MainWindow", u"-37.5", None))
        self.lineEdit_2.setText(QCoreApplication.translate("MainWindow", u"144.5", None))
        self.label_55.setText(QCoreApplication.translate("MainWindow", u"RC      ", None))
        self.BCH5.setText(QCoreApplication.translate("MainWindow", u"CH5 GEAR", None))
        self.BCH6.setText(QCoreApplication.translate("MainWindow", u"CH6 FLAP", None))
        self.LCH1.setText(QCoreApplication.translate("MainWindow", u"50%", None))
        self.LCH4.setText(QCoreApplication.translate("MainWindow", u"50%", None))
        self.LCH3.setText(QCoreApplication.translate("MainWindow", u"50%", None))
        self.LCH2.setText(QCoreApplication.translate("MainWindow", u"50%", None))
        self.label_73.setText(QCoreApplication.translate("MainWindow", u"CH1", None))
        self.label_74.setText(QCoreApplication.translate("MainWindow", u"CH4", None))
        self.label_75.setText(QCoreApplication.translate("MainWindow", u"CH3", None))
        self.label_76.setText(QCoreApplication.translate("MainWindow", u"CH2", None))
        self.label_77.setText(QCoreApplication.translate("MainWindow", u"THRO", None))
        self.label_79.setText(QCoreApplication.translate("MainWindow", u"ELVE", None))
        self.label_78.setText(QCoreApplication.translate("MainWindow", u"RUDD", None))
        self.label_80.setText(QCoreApplication.translate("MainWindow", u"AILE", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_81.setText(QCoreApplication.translate("MainWindow", u"Left Velocity          Current", None))
        self.RollGauge.setText(QCoreApplication.translate("MainWindow", u"Roll Gauge", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.PitchGauge.setText(QCoreApplication.translate("MainWindow", u"Pitch Gauge", None))
        self.label_72.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_83.setText(QCoreApplication.translate("MainWindow", u"Magnetic Field Strength", None))
        self.PB_MagReset.setText(QCoreApplication.translate("MainWindow", u"RST", None))
        self.label_71.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_82.setText(QCoreApplication.translate("MainWindow", u"Right Velocity          Current", None))
        self.CompassGauge.setText(QCoreApplication.translate("MainWindow", u"Compass", None))
        self.label_88.setText(QCoreApplication.translate("MainWindow", u"GPS Variance", None))
        self.PB_GPSVarReset.setText(QCoreApplication.translate("MainWindow", u"RST", None))
        self.GPSmap.setText(QCoreApplication.translate("MainWindow", u"GPS Map ", None))
    # retranslateUi

