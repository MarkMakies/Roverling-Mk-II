import sys
import random
import math
import paho.mqtt.client as mqtt

from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QStatusBar
from PySide6.QtCore import (QDateTime, QPointF, Qt, QRect, QPoint, Signal, QObject,
                            QTimer)
from PySide6.QtCharts import (QChart, QChartView, QLineSeries, QAreaSeries, 
                            QPieSeries, QPieSlice)
from PySide6.QtGui import (QPainter, QPixmap, QPen, QColor, QTransform, 
                            QImage, QGradient, QFont, QPolygon, QBrush)
from PySide6.QtMultimedia import (QAudio, QAudioOutput, QMediaFormat,
                                  QMediaPlayer)
from PySide6.QtMultimediaWidgets import QVideoWidget

from ui import Ui_MainWindow

MQTTClientID =      'RoverTelemetry'
MQTTBroker =        '192.168.2.100'
MQTTTopic =         'DEV/RV/Packet'
from Secrets import MQTTUser, MQTTPassword

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.statusBar = QStatusBar()
        self.setStatusBar(self.ui.statusBar)

        canvas = QPixmap(200, 200)
        canvas.fill(Qt.white)
        self.ui.RollGauge.setPixmap(canvas)
        self.ui.PitchGauge.setPixmap(canvas)
        self.ui.CompassGauge.setPixmap(canvas)

        canvas = QPixmap(700,500)
        canvas.fill(Qt.green)
        self.ui.GPSmap.setPixmap(canvas)

        self.ui.GPS.setStyleSheet('background-color : Yellow')
        self.ui.COMMS.setStyleSheet('background-color : Yellow')
        self.ui.PB_Record.setStyleSheet('background-color : Yellow')
        self.ui.PB_CommsStop.setStyleSheet('background-color : LawnGreen')

        td = QDateTime.currentDateTime()
        fn = td.toString('yyyyMMdd-hh:mm') + '.rv2'    #MM
        #fn = 'GPS-test1.rv2'
        self.ui.RecordFileName.setText(fn)

        self.mediaPlayer = QMediaPlayer()
        #self.mediaPlayer.setSource('walk1.mp4')
        #url = 'tcp/h264://192.168.2.20:10001'
        
        #supportedFileFormats:
        #['video/ogg', 'video/x-ms-wmv', 'video/x-msvideo', 'video/mp4', 'video/quicktime', 'audio/mp4', 
        # 'video/webm', 'audio/aac', 'audio/x-ms-wma', 'video/x-matroska', 'audio/x-wav', 'audio/flac']

        self.mediaPlayer.setVideoOutput(self.ui.Video_widget)
        self.mediaPlayer.play()

        # signals to free functions  (slot)
        self.ui.actionPlay.triggered.connect(PktPlayStart)
        self.ui.actionRecord.triggered.connect(PktRecord)
        self.ui.actionLoad.triggered.connect(PktLoad)

        self.ui.actionGPS_Reset.triggered.connect(ResetSliders)
        self.ui.actionGPS_Map.triggered.connect(ManualMap)
        self.ui.actionGPS_Clear.triggered.connect(Init_Map)
        self.ui.actionCommsStop.triggered.connect(CommsStopStart)
        self.ui.actionMagReset.triggered.connect(MagReset)
        self.ui.actionGPSVarReset.triggered.connect(GPSVarReset)

        self.ui.timerPulse = QTimer(self)
        self.ui.timerPulse.setSingleShot(True)

        self.ui.timerPulse.singleShot(100, InitGUI)
        self.ui.timerPulse.singleShot(2000, CheckComms)

class MqttSyncObj(QObject):       # For my thread syncing
    NewPacket = Signal(str)

def ResetSliders():
    win.sl_gtop.setValue(0)
    win.sl_gbottom.setValue(0)
    win.sl_gleft.setValue(0)
    win.sl_gright.setValue(0)

def Init_Map():
    gHeight = 500
    gWidth = 700
    canvas = win.GPSmap.pixmap()   
    p = QPainter(canvas)
    p.drawImage(QRect(0,0,700,500), QImage('map1.JPG'))
    p.end()
    win.GPSmap.setPixmap(canvas)

    from Secrets import LAT_A, LON_A
    win.gLatBottom.setValue(LAT_A)
    win.gLatMult.setValue(940)
    win.gLonLeft.setValue(LON_A)
    win.gLonMult.setValue(540)

def ManualMap():
    lat = float(win.lineEdit.text())
    long = float(win.lineEdit_2.text())
    Map(lat, long, -1)

def Map(Lat, Lon, Qual):
    
    Width = 700     # x, longitude
    Height = 500    # y, latitude

    LatBottom = win.gLatBottom.value() 
    LatMult = win.gLatMult.value()
    LatY = Height - ((Lat - LatBottom) * LatMult * Height)

    LonLeft = win.gLonLeft.value() 
    LonMult = win.gLonMult.value()
    LonX = (Lon - LonLeft) * LonMult * Width

    canvas = win.GPSmap.pixmap()   
    p = QPainter(canvas)  

    pen = QPen()
    pen.setWidth(4)
    if Qual == -1: 
        pen.setColor(QColor('white'))
    elif Qual == 1:
        pen.setColor(QColor('yellow'))
    else:
        pen.setColor(QColor('red'))

    p.setPen(pen)    

    if Qual != 0 :
        p.drawPoint(LonX, LatY)
        win.GPS.setStyleSheet('background-color : None')
    else:
        win.GPS.setStyleSheet('background-color : Yellow')

    p.end()
    win.GPSmap.setPixmap(canvas)

def Init_CompassGauge():
    canvas = win.CompassGauge.pixmap()
    
    p = QPainter(canvas)
    p.fillRect(0, 0, 200, 200, QColor('lightgrey'))
    p.translate(100,100)
    pen = QPen()
 
    # draw ticks
    pen.setWidth(2)
    pen.setColor(QColor('white'))
    p.setPen(pen)     

    for i in range(0, 24):
        p.drawLine(90, 0, 100, 0)
        p.rotate(15.0)

    #p.drawEllipse(-91, -91, 182, 182)

    p.end()
    win.CompassGauge.setPixmap(canvas)

def Init_RollGauge():
    canvas = win.RollGauge.pixmap()
    
    p = QPainter(canvas)
    p.fillRect(0, 0, 200, 200, QColor('lightgrey'))
    p.translate(100,100)
    pen = QPen()
 
    # draw ticks
    pen.setWidth(2)
    pen.setColor(QColor('white'))
    p.setPen(pen)     
    tick1 = -250
    tick2 = 250

    p.save()
    p.rotate(-30)
    p.drawLine(tick1, 0, tick2, 0)
    p.rotate(15)
    p.drawLine(tick1, 0, tick2, 0)
    p.rotate(15)
    p.drawLine(tick1, 0, tick2, 0)
    p.rotate(15)
    p.drawLine(tick1, 0, tick2, 0)
    p.rotate(15)
    p.drawLine(tick1, 0, tick2, 0)
    p.restore()

    #p.drawEllipse(-91, -91, 182, 182)

    p.end()
    win.RollGauge.setPixmap(canvas)

def Init_PitchGauge():
    canvas = win.PitchGauge.pixmap()
    
    p = QPainter(canvas)
    p.fillRect(0, 0, 200, 200, QColor('lightgrey'))
    p.translate(100,100)
    pen = QPen()
 
    # draw ticks
    pen.setWidth(2)
    pen.setColor(QColor('white'))
    p.setPen(pen)     
    tick1 = -250
    tick2 = 250

    p.save()
    p.rotate(-30)
    p.drawLine(tick1, 0, tick2, 0)
    p.rotate(15)
    p.drawLine(tick1, 0, tick2, 0)
    p.rotate(15)
    p.drawLine(tick1, 0, tick2, 0)
    p.rotate(15)
    p.drawLine(tick1, 0, tick2, 0)
    p.rotate(15)
    p.drawLine(tick1, 0, tick2, 0)
    p.restore()

    #p.drawEllipse(-91, -91, 182, 182)

    p.end()
    win.PitchGauge.setPixmap(canvas)

def CompassGauge(deg):
    Init_CompassGauge()
    win.label_72.setText('HDG  ' + str(deg) + u'\N{DEGREE SIGN}')

    canvas = win.CompassGauge.pixmap()
    p = QPainter(canvas)
    pen = QPen() 
    brush = QBrush()
   
    p.translate(100,100)
    p.rotate(deg)
    p.drawImage(QRect(-90, -90, 180, 180), QImage('RovTop6.png'))
    
    arrow = QPolygon([QPoint(0, -87), QPoint(-20, -67), QPoint(20, -67)])
    brush.setColor(QColor('green'))
    brush.setStyle(Qt.SolidPattern)
    p.setBrush(brush)
    p.drawConvexPolygon(arrow)

    #p.rotate(-deg)
    #p.setPen(QColor('DarkGreen'))
    #p.setFont(QFont('Roboto', 24, QFont.Bold))
    #ss = 'HDG  ' + str(deg) + u'\N{DEGREE SIGN}'
    #p.drawText(-70,92, ss)

    p.end()
    win.CompassGauge.setPixmap(canvas)

def RollGauge(deg):
    lean = False
    Init_RollGauge()

    canvas = win.RollGauge.pixmap()
    p = QPainter(canvas)
    pen = QPen() 
    brush = QBrush()

    p.translate(100,100)
    p.rotate(deg)
    p.drawImage(QRect(-90, -90, 180, 180), QImage('RovBack3.png'))

    left_arrow = QPolygon([QPoint(-67, -20), QPoint(-67, 20), QPoint(-87, 0)])
    right_arrow = QPolygon([QPoint(67, -20), QPoint(67, 20), QPoint(87, 0)])
    if abs(deg) < 5:
        brush.setColor(QColor('green'))
        lean = False
    else:
        brush.setColor(QColor('red'))
        lean = True
    brush.setStyle(Qt.SolidPattern)
    p.setBrush(brush)
    p.drawConvexPolygon(left_arrow)
    p.drawConvexPolygon(right_arrow)

    win.label_71.setText('ROLL  ' + str(deg) + u'\N{DEGREE SIGN}')

    if lean:
        win.frame_25.setStyleSheet('background-color : Yellow')
    else:
        win.frame_25.setStyleSheet('background-color : none')

    #p.setFont(QFont('Roboto', 24, QFont.Bold))
    #ss = 'ROLL  ' + str(abs(int(deg))) + u'\N{DEGREE SIGN}'
    #p.drawText(-74,92, ss)

    p.end()
    win.RollGauge.setPixmap(canvas)

def PitchGauge(deg):
    lean = False
    Init_PitchGauge()
    canvas = win.PitchGauge.pixmap()
    p = QPainter(canvas)
    pen = QPen() 
    brush = QBrush()

    p.translate(100,100)
    p.rotate(deg)
    p.drawImage(QRect(-90, -90, 180, 180), QImage('RovSide3.png'))

    left_arrow = QPolygon([QPoint(-67, -20), QPoint(-67, 20), QPoint(-87, 0)])
    right_arrow = QPolygon([QPoint(67, -20), QPoint(67, 20), QPoint(87, 0)])
    if abs(deg) < 5:
        brush.setColor(QColor('green'))
        lean = False
    else:
        brush.setColor(QColor('red'))
        lean = True
    brush.setStyle(Qt.SolidPattern)
    p.setBrush(brush)
    p.drawConvexPolygon(left_arrow)
    p.drawConvexPolygon(right_arrow)

    win.label_7.setText('PITCH  ' + str(deg) + u'\N{DEGREE SIGN}')
    if lean:
        win.frame_26.setStyleSheet('background-color : Yellow')
    else:
        win.frame_26.setStyleSheet('background-color : none')


    p.end()
    win.PitchGauge.setPixmap(canvas)

def InitGUI():
    Init_RollGauge()
    Init_PitchGauge()
    Init_CompassGauge()
    Init_Map()

    RollGauge(0)
    PitchGauge(0)
    CompassGauge(0)
    
def MQTT_cb(client, userdata, msg):
    #topic = msg.topic
    message = msg.payload.decode()  
    MqttSync.NewPacket.emit(message)

def ProcessPacket(m):
    global Hmin, Hmax, Vmin, Vmax 
    #print(Mode)
    if Mode == 'Recording':
        SavePkt(m)

    global count
    count += 1

    # decode this messy format
    Seconds = int(m.split(',')[0][1:])
    Latitude = float(m.split(',')[1][2:])
    Longitude = float(m.split(',')[2][1:][:-1])
    Quality = int(m.split(',')[3])
    NumSats = int(m.split(',')[4])
    Accuracy = float(m.split(',')[5])
    Altitude = float(m.split(',')[6])
    LeftVel = float(m.split(',')[7])
    RightVel = float(m.split(',')[8])
    LeftCur = float(m.split(',')[9])
    RightCur = float(m.split(',')[10])
    LeftPWM = float(m.split(',')[11])
    RightPWM = float(m.split(',')[12])
    ch1 = int(m.split(',')[13])
    ch2 = int(m.split(',')[14])
    ch3 = int(m.split(',')[15])
    ch4 = int(m.split(',')[16])
    ch5 = int(m.split(',')[17])
    ch6 = int(m.split(',')[18])
    AccelX = float(m.split(',')[19])
    AccelY = float(m.split(',')[20])
    AccelZ = float(m.split(',')[21])
    GyrolX = float(m.split(',')[22])
    GyroY = float(m.split(',')[23])
    GyroZ = float(m.split(',')[24])
    MagX = float(m.split(',')[25])
    MagY = float(m.split(',')[26])
    MagZ = float(m.split(',')[27])
    Temp = float(m.split(',')[28])
    Pressure = float(m.split(',')[29])
    RoverSNR = float(m.split(',')[30])
    RoverRSSI = float(m.split(',')[31])
    Sonar = float(m.split(',')[32])
    BatPercent = int(m.split(',')[33])
    StatusByte1 = int(m.split(',')[34])
    StatusByte2 = int(m.split(',')[35][:-1])
    GatewaySNR = float(m.split(',')[36])
    GatewayRSSI = float(m.split(',')[37])

    '''print(Seconds, Latitude, Longitude, Quality, NumSats, Accuracy, Altitude,
        LeftVel,RightVel,LeftCur,RightCur,LeftPWM,RightPWM,ch1,ch2,ch3,ch4,ch5,ch6,
        AccelX,AccelY,AccelZ, GyrolX,GyroY,GyroZ,MagX,MagY,MagZ,Temp, Pressure,        
        RoverSNR, RoverRSSI, Sonar, BatPercent, StatusByte1, StatueByte2, GatewaySNR,
        GatewayRSSI)'''

    #print(Latitude, Longitude, Quality, NumSats, Accuracy, Altitude)
    #print(ch1, ch2, ch3, ch4, ch5, ch6)

    # GPS      
    win.gQuality.setText(str(Quality))
    win.gNumSats.setText(str(NumSats))
    win.gAccuracy.setText(str(Accuracy) +' m')

    win.gLat.setText('{:.7f}'.format(Latitude) + '   ')
    win.gLong.setText('{:.7f}'.format(Longitude) + '   ')
    
    win.gAlt.setText('{:.1f}'.format(Altitude) +' m')
    if not(Latitude == -37 and Longitude == 144):
        Map(Latitude, Longitude, Quality)

        #GNSS variance - used on line tools to work out metres between these points
        from Secrets import LAT_B, LAT_C, LON_B, LON_C
        vmult = 120 / (LAT_B - LAT_C)
        hmult = 161 / (LON_B -LON_C)

        LatBottom = win.gLatBottom.value() 

        Vmeters = (Latitude - win.gLatBottom.value()) * vmult
        Hmeters = (Longitude - win.gLonLeft.value()) * hmult

        if Vmin == 0:
            Vmin, Vmax = Vmeters, Vmeters
        else:
            Vmin = min(Vmin, Vmeters)
            Vmax = max(Vmax, Vmeters)

        if Hmin == 0:
            Hmin, Hmax = Hmeters, Hmeters
        else:
            Hmin = min(Hmin, Hmeters)
            Hmax = max(Hmax, Hmeters)

        win.gVariance.setText(str(round((Hmax - Hmin),2)) + ' / ' + str(round((Vmax - Vmin),2)))

        GPSVarianceChart(Hmeters, Vmeters, 0,0)
        
    #IMU
    Heading = CalcHeading(MagX, MagY)
    CompassGauge(Heading)

    Pitch, Roll = CalcAttitude(AccelX, AccelY, AccelZ)
    PitchGauge(Pitch)
    RollGauge(Roll)

    win.iHeading.setText(str(int(Heading)))
    win.iRoll.setText(str(Roll)+ u'\N{DEGREE SIGN}')
    win.iPitch.setText(str(Pitch)+ u'\N{DEGREE SIGN}')

    win.iTemp.setText(str(int(Temp)) + ' ' + u'\N{DEGREE SIGN}' + 'C')
    win.iPressure.setText(str(int(Pressure)) +  ' hPa')
    win.iAltitude.setText(str(CalcPressAlt(Pressure, Temp)) + ' m')
   
    # Locomotion
    win.label_38.setText(str(round(LeftVel,1)) + u' ms\u207b\u00b9')
    win.label_47.setText(str(round(RightVel,1)) + u' ms\u207b\u00b9')
    win.label_48.setText(str(int(round(LeftCur*100,0))*10) + ' mA')
    win.label_45.setText(str(int(round(RightCur*100,0))*10) + ' mA')
    win.label_50.setText(str(int(LeftPWM/ 2**16 * 100)) + ' %')
    win.label_51.setText(str(int(RightPWM/ 2**16 * 100)) + ' %')

    # Telemetry
    win.label_70.setText(str(int(GatewayRSSI)) + ' dBm')
    win.label_65.setText(str(int(GatewaySNR))   + ' dB')
    win.label_63.setText(str(int(RoverRSSI)) + ' dBm')
    win.label_62.setText(str(int(RoverSNR))   + ' dB')

    if (GatewayRSSI < -90 or RoverRSSI < -90 or GatewaySNR < 0 or RoverSNR < 0):
        win.Fsignal.setStyleSheet('background-color : Yellow')
    elif (GatewaySNR < 0 or RoverSNR < 0 or GatewaySNR < -5 or RoverSNR < -5):
        win.Fsignal.setStyleSheet('background-color : Red')
    else:
        win.Fsignal.setStyleSheet('background-color : None')

    win.Ppulse.setText(str(count))
    win.Ppulse.setStyleSheet('background-color : LawnGreen')  
    win.timerPulse.singleShot(200, PpulseOff)

    ss = str(Seconds//60) + ':' + str(Seconds%60)
    if win.Gpulse.text() != ss:
        win.Gpulse.setText(ss)
        win.Gpulse.setStyleSheet('background-color : LawnGreen')  
        win.timerPulse.singleShot(200, GpulseOff)

    # Battery
    win.SLbattery.setValue(BatPercent)
    win.label_99.setText(str(BatPercent) + ' %')
    if BatPercent < 25 :
        win.Fbattery.setStyleSheet('background-color : Red')
    elif BatPercent < 33 :
        win.Fbattery.setStyleSheet('background-color : Yellow')
    else:
        win.Fbattery.setStyleSheet('background-color : None')

    # Sonar / PIR
    win.label_86.setText(str(int(Sonar/10)) + ' cm')
    win.SLranger.setValue(int(Sonar/10))
    if Sonar < 500 :  # mm
        win.Fsonar.setStyleSheet('background-color : orange')
    else:
       win.Fsonar.setStyleSheet('background-color : None') 

    sb1 = '{0:08b}'.format(StatusByte1)
    sb2 = '{0:08b}'.format(StatusByte2)
    win.label_64.setText(sb2 + ' ' + sb1)
    if StatusByte1 & 1:
        win.cbPIR.setChecked(True)
        win.frame_24.setStyleSheet('background-color : orange')
    else:
        win.cbPIR.setChecked(False)
        win.frame_24.setStyleSheet('background-color : none')
    # RC
    win.SL1.setValue(ch1)
    win.SL2.setValue(ch2)
    win.SL3.setValue(ch3)
    win.SL4.setValue(ch4)

    win.LCH1.setText(str(ch1))
    win.LCH2.setText(str(ch2))
    win.LCH3.setText(str(ch3))
    win.LCH4.setText(str(ch4))

    if ch5 > 75:
        win.BCH5.setChecked(True)
    else:
        win.BCH5.setChecked(False)

    if ch6 > 75:
        win.BCH6.setChecked(True)
        win.RC.setStyleSheet('background-color : paleturquoise')
    else:
        win.BCH6.setChecked(False)
        win.RC.setStyleSheet('background-color : none')

    time = QDateTime.currentDateTime()
    timeDisplay = time.toString('hh:mm:ss')

    messBar = timeDisplay #+ '  Count: ' + str(count) + ' GPS Seconds:' + str(Seconds) 
    win.statusBar.showMessage(messBar)
    
    VelCharts(LeftVel, LeftCur, win.ChartView2)
    VelCharts(RightVel, RightCur, win.ChartView3)



def PpulseOff():
    win.Ppulse.setStyleSheet('none')

def GpulseOff():
    win.Gpulse.setStyleSheet('none')

def CheckComms():
    global PrevCount    
    if count == PrevCount:
        win.COMMS.setStyleSheet('background-color : yellow')
        win.GPS.setStyleSheet('background-color : yellow')
    else:
        win.COMMS.setStyleSheet('background-color : none')
    PrevCount = count
    win.timerPulse.singleShot(2000, CheckComms)

def CalcPressAlt(P, T):
    P = P * 100 # HPa to Pa
    alt = int((( ((101325/P) ** (1/5.257)) -1)*(T+273.15))/0.0065)
    return alt

def CalcAttitude(X, Y, Z):#return pitch, roll in deg
    rollOffset = 1.9
    pitchOffset = 1.1
    roll = round(math.degrees(math.atan2(-X, Z)) + rollOffset,1) 
    pitch = round(math.degrees(math.atan2(Y, math.sqrt(X**2 + Z**2))) + pitchOffset,1)
    return roll, pitch

def CalcHeading(X, Y):  # return degrees true north at my location
    global nXmax, nXmin, nYmax, nYmin
  
    MagVarianceChart(X, Y)
    Xmin = -440   
    Xmax =  78
    Ymin = -200
    Ymax =  283

    Xmid = (Xmax + Xmin) / 2
    Ymid = (Ymax + Ymin) / 2
    X = X * 1000
    Y = Y * 1000
    X1 = (X - Xmid) / (Xmax - Xmin) * 2
    Y1 = (Y - Ymid) / (Ymax - Ymin) * 2
    declination = math.radians((11 + 29/60)) # Woodend 11deg 29min
    magnetic_field_direction = math.atan2(Y1, X1)
    Heading = magnetic_field_direction + declination
    Heading = (int(math.degrees(Heading)) + 360) % 360

    win.label_26.setText(str(Xmin))
    win.label_22.setText(str(Xmax))
    win.label_32.setText(str(Ymin))
    win.label_29.setText(str(Ymax))

    if X > nXmax: nXmax = int(X)
    if X < nXmin: nXmin = int(X)
    if Y > nYmax: nYmax = int(Y)
    if Y < nYmin: nYmin = int(Y)

    win.label_27.setText(str(nXmin))
    win.label_25.setText(str(nXmax))
    win.label_33.setText(str(nYmin))
    win.label_30.setText(str(nYmax))

    return(Heading)

def MagReset():
    global series_Mag
    series_Mag = QLineSeries()

def MagVarianceChart(x,y):
    pen = QPen()
    pen.setWidth(2)
    pen.setColor(QColor('peru'))
    series_Mag.setPen(pen)

    series_Mag.append(QPointF(x, y))
    chart = QChart()
    chart.addSeries(series_Mag)
    chart.createDefaultAxes()  
    chart.setContentsMargins(-68,-28,-45,-43)
    chart.legend().setVisible(False)
    win.ChartView4.setContentsMargins(0,0,0,0)
    win.ChartView4.setChart(chart)
    win.ChartView4.show()
    pass


def VelCharts(vl, cl, cht):
    Vmax, Vwarn = 2.5, 2
    Imax, Iwarn = 2, 1


    if cht == win.ChartView2:
        win.label.setText(str(round(vl,1)) + u' ms\u207b\u00b9' +
            '        ' + str(round(cl,1)) + ' A' )
        if vl > Vwarn:
            win.frame_33.setStyleSheet('background-color : Yellow')
        else:
            win.frame_33.setStyleSheet('background-color : none')
    elif cht == win.ChartView3:
        win.label_2.setText(str(round(vl,1)) + u' ms\u207b\u00b9' +
            '        ' + str(round(cl,1)) + ' A' )
        if vl > Vwarn:
            win.frame_34.setStyleSheet('background-color : Yellow')
        else:
            win.frame_34.setStyleSheet('background-color : none')

    vl = abs(vl)
    cl = abs(cl)

    chart = QChart()
    # outer ring
    donut = QPieSeries()
    slc = QPieSlice('',1)
    donut.append(slc)
    donut.setHoleSize(0.98)
    donut.setPieSize(1)
    donut.setPieStartAngle(-150)
    donut.setPieEndAngle(150)
    chart.addSeries(donut)
    # second outer ring
    donut = QPieSeries()
    slc = QPieSlice('',1)
    donut.append(slc)
    donut.setHoleSize(0.76)
    donut.setPieSize(0.78)
    donut.setPieStartAngle(-150)
    donut.setPieEndAngle(150)
    chart.addSeries(donut)
    # second outer ring
    donut = QPieSeries()
    slc = QPieSlice('',1)
    donut.append(slc)
    donut.setHoleSize(0.56)
    donut.setPieSize(0.58)
    donut.setPieStartAngle(-150)
    donut.setPieEndAngle(150)
    chart.addSeries(donut)

    # velocity
    donut = QPieSeries()
    slc = QPieSlice(str(round(vl,1)),vl)
    if vl <= Vwarn:
        slc.setColor(QColor('cornflowerblue'))
    else:
        slc.setColor(QColor('lightcoral'))
    slc.setBorderColor(QColor('black'))
    donut.append(slc)
    slc = QPieSlice('',Vmax - vl)
    slc.setColor(QColor('white'))
    slc.setBorderColor(QColor('black'))
    donut.append(slc)
    donut.setHoleSize(0.80)
    donut.setPieSize(0.96)
    donut.setPieStartAngle(-150)
    donut.setPieEndAngle(150)
    chart.addSeries(donut)

    # current / torque
    donut = QPieSeries()
    slc = QPieSlice(str(round(cl,1)),cl)
    if cl <= Iwarn:
        slc.setColor(QColor('mediumaquamarine'))
    else:
        slc.setColor(QColor('crimson'))
    slc.setBorderColor(QColor('black'))
    donut.append(slc)
    slc = QPieSlice('',Imax - cl)
    slc.setColor(QColor('white'))
    slc.setBorderColor(QColor('black'))
    donut.append(slc)

    donut.setHoleSize(0.60)
    donut.setPieSize(0.74)
    donut.setPieStartAngle(-150)
    donut.setPieEndAngle(150)
    chart.addSeries(donut)

    brush = QBrush()
    brush.setColor(QColor('lightgrey'))
    brush.setStyle(Qt.SolidPattern)
    chart.setBackgroundBrush(brush)


    chart.createDefaultAxes()   
    chart.setContentsMargins(-20,-20,-15,-20)
    chart.legend().setVisible(False)
    cht.setContentsMargins(0,0,0,0)
    cht.setRenderHint(QPainter.Antialiasing)
    #chart.setAnimationOptions(QChart.AllAnimations)
    cht.setChart(chart)
    cht.show()

def GPSVarReset():
    global series_GPS
    series_GPS = QLineSeries()

def GPSVarianceChart(n,x,y,z):
    pen = QPen()
    pen.setWidth(2)
    pen.setColor(QColor('steelblue'))
    series_GPS.setPen(pen)

    series_GPS.append(QPointF(n,x))
   # series_1.append(QPointF(n,y))
   # series_2.append(QPointF(n,z))
    #series_GPS.setName("Batman")

    chart = QChart()
    chart.addSeries(series_GPS)
    #  chart.addSeries(series_1)
    #  chart.addSeries(series_2)
    #chart.setTitle("Simple areachart example")

    chart.createDefaultAxes()
   
    chart.setContentsMargins(-30,-30,-25,-30)
    chart.legend().setVisible(False)

    win.ChartView1.setContentsMargins(0,0,0,0)
    win.ChartView1.setChart(chart)

    win.ChartView1.show()

def PktRecord():
    if win.PB_Record.text() == 'Paused':
        RecordStart()
    else:
        RecordStop()

def PktLoad():
    global LoadedPackets
    RecordStop()
    CommsStop()
    fname2 = win.RecordFileName.text()
    myfile = open(fname2, 'r')
    #myfile = open('20231018-12:34.rv2', 'r')
    LoadedPackets = myfile.readlines()
    win.label_9.setText('0/' + str(len(LoadedPackets)))
    #win.SLpackets.setMaximum(len(LoadedPackets) - 1)
    #win.SLpackets.setValue(0)

def PktPlayStart():
    global PktCount 
    if win.PB_Play.text() == 'Stopped':
        if len(LoadedPackets) > 0:
            win.PB_Play.setText('Playing')
            InitGUI()
            win.PB_Play.setStyleSheet('background-color : LawnGreen')
            PktCount = 0
            win.timerPulse.singleShot(win.SLspeed.value(), PktPlay)
            win.label_89.setText(str(win.SLspeed.value()) + ' ms')

    else:
        win.PB_Play.setText('Stopped')
        win.PB_Play.setStyleSheet('background-color : none')

def PktPlay():
    global PktCount
    if win.PB_Play.text() == 'Playing':
        win.label_9.setText(str(PktCount) + '/' + str(len(LoadedPackets)))
        ProcessPacket(LoadedPackets[PktCount])
        PktCount += 1
        if PktCount < len(LoadedPackets):
            win.timerPulse.singleShot(win.SLspeed.value(), PktPlay)
            win.label_89.setText(str(win.SLspeed.value()/10) + ' ms')  #MM
        else:
            win.PB_Play.setStyleSheet('background-color : none')

def SavePkt(m):
    myfile = open(fname, 'a')
    myfile.write(m + '\n')
    myfile.close()

def CommsStopStart():
    if win.PB_CommsStop.text() == 'STOPPED':
        CommsStart()
    else:
        CommsStop()

def RecordStart():
    global Mode, fname
    win.PB_Record.setText('Recording')
    win.PB_Record.setStyleSheet('background-color : LawnGreen')
    Mode = 'Recording'
    fname = win.RecordFileName.text()
    myfile = open(fname, 'a')

def RecordStop():
    global Mode
    win.PB_Record.setText('Paused')
    win.PB_Record.setStyleSheet('background-color : yellow')
    Mode = 'Paused'

def CommsStart():
    win.PB_CommsStop.setText('RUNNING')
    win.PB_CommsStop.setStyleSheet('background-color : LawnGreen')
    client.loop_start()

def CommsStop():
    win.PB_CommsStop.setText('STOPPED')
    win.PB_CommsStop.setStyleSheet('background-color : Red')
    client.loop_stop()


################# 
MqttSync = MqttSyncObj()    # provides MQTT thread sync with Qt framework
MqttSync.NewPacket.connect(ProcessPacket)

Mode = 'Paused'

count = 0
PktCount = 0
PrevCount = 0
ii = 0
Hmin, Hmax, Vmin, Vamx = 0, 0, 0, 0

series_GPS = QLineSeries()
series_1 = QLineSeries()
series_2 = QLineSeries()
series_Mag = QLineSeries()

nXmax, nXmin, nYmax, nYmin = 0, 0, 0, 0

MqttSync = MqttSyncObj()
MqttSync.NewPacket.connect(ProcessPacket)

client = mqtt.Client(MQTTClientID)
client.username_pw_set(MQTTUser, MQTTPassword)
client.connect(MQTTBroker)
client.on_message = MQTT_cb
client.subscribe(MQTTTopic)


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    win = window.ui
    window.show()

#    t = threading.Thread(target=InitGUI)   # Init GUI elements
#    t.start()

    client.loop_start()     # runs loop in another thread
    x = app.exec()
    #print('stop', x)
    client.loop_stop()
    sys.exit(0)
