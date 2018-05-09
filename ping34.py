from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
import threading
from subprocess import Popen,PIPE

class Ping(threading.Thread):
    def __init__(self, ip_address):
        threading.Thread.__init__(self)
        self.ip = ip_address
        self.ret=0
    def run(self):
        p = Popen(['ping','-n','1',self.ip],shell=True,stdout = PIPE,stderr=PIPE)
        self.ret=p.stdout.read().decode('gb2312').find('100%')
        return self.ret

class win(QWidget):
    def __init__(self,A,B):
        super(win, self).__init__()
        self.A=A
        self.B=B
        self.setWindowFlags(Qt.WindowCloseButtonHint)
        self.setWindowTitle('PING')
        self.lay=QGridLayout()
        self.le=[]
        self.k=0
        self.win2=hello(self)
        for i in range(len(self.A)):
            self.le.append(QPushButton())
            self.lay.addWidget(self.le[i],i/7,i%7)
            self.le[i].setText('\n'.join(self.A[i]))
            self.le[i].clicked.connect(self.bbb)
        self.setLayout(self.lay)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.aaa)
        self.timer.start(100)

    def center(self):
        scr=QDesktopWidget().screenGeometry()
        wnd=self.geometry()
        zb1=(scr.width()-wnd.width())/2
        zb2=(scr.height()-wnd.height())/2
        self.move(zb1,zb2)

    def aaa(self):
        pp=Ping(self.A[self.k][2]);pp.start();pp.join()
        if pp.ret>0:
            self.le[self.k].setStyleSheet("QPushButton {background-color: #ff0000 }")
        else:
            self.le[self.k].setStyleSheet("QPushButton {background-color: #00ff00 }" "QPushButton:pressed { background-color: yellow }")
        self.k=self.k+1
        if self.k==len(self.A):
            self.timer.stop()

    def keyPressEvent(self, QKeyEvent):
        if QKeyEvent.key()==Qt.Key_Escape:
            self.close()

    def bbb(self):
        self.win2.setWindowModality(Qt.ApplicationModal)
        self.win2.t1.setText(self.B[self.le.index(self.sender())])
        self.win2.show()

class hello(QWidget):
    def __init__(self,win1):
        super(hello, self).__init__()
        self.setWindowFlags(Qt.WindowCloseButtonHint)
        self.win1=win1
        self.t1=QTextEdit("")
        self.l=QGridLayout()
        self.l.addWidget(self.t1,0,0,1,2)
        self.setLayout(self.l)

    def keyPressEvent(self, QKeyEvent):
        if QKeyEvent.key()==Qt.Key_Escape:
            self.close()

