# coding: cp936
__author__ = 'YangTong'
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import threading
from subprocess import Popen,PIPE
import time

class bt(QPushButton):
    def __init__(self,k):
        super(bt, self).__init__()
        if 'Y' in k:
            self.setStyleSheet("QPushButton {background-color: grey }")
        elif len(k.split())>=2 or k[0]=='2' or k[0]=='3' or k[0]=='4':
            self.setStyleSheet("QPushButton {background-color: #00ff00 }")
        elif k[0]=='X' and 'P1' in k or 'P3' in k:
            self.setStyleSheet("QPushButton {background-color: red }")
        elif k[0]=='X' or (len(k.split())==1 and k[0]!='2' and k[0]!='3' and k[0]!='4'):
            self.setStyleSheet("QPushButton {background-color: yellow }")
class win(QWidget):
    def __init__(self,A):
        super(win, self).__init__()
        self.A=[[str(i[0])+':'+str(i[1]),i[3]] for i in A if i[1]!='None']
        self.B=[i[6] for i in A if i[1]!='None']
        self.C=['\n'.join(i).replace('None\n','') for i in A if i[1]!='None']
        self.setWindowFlags(Qt.WindowCloseButtonHint)
        self.setWindowTitle('PING')
        self.lay=QGridLayout()
        self.le=[]
        self.k=0
        self.t=time.time()
        self.win2=hello(self)
        for i in range(len(self.A)):
            self.le.append(bt(self.B[i]))
            self.lay.addWidget(self.le[i],i/10,i%10)
            self.le[i].setText('\n'.join(self.A[i]))
            self.le[i].clicked.connect(self.bbb)
        self.setLayout(self.lay)

    def center(self):
        scr=QDesktopWidget().screenGeometry()
        wnd=self.geometry()
        zb1=(scr.width()-wnd.width())/2
        zb2=(scr.height()-wnd.height())/2
        self.move(zb1,zb2)

    def keyPressEvent(self, QKeyEvent):
        if QKeyEvent.key()==Qt.Key_Escape:
            self.close()

    def bbb(self):
        self.win2.setWindowModality(Qt.ApplicationModal)
        self.win2.t1.setText(self.C[self.le.index(self.sender())])
        self.win2.show()

class hello(QWidget):
    def __init__(self,win1):
        super(hello, self).__init__()
        self.setWindowFlags(Qt.WindowCloseButtonHint)
        self.win1=win1
        self.t1=QTextEdit("")
        self.t1.setStyleSheet(
                              "QTextEdit {color: blue;"
                              "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, "
                              "stop:0 rgba(0, 180, 190, 200), "
                              "stop:1 rgba(255, 255, 255, 255));}"
                              )
        self.l=QGridLayout()
        self.l.addWidget(self.t1,0,0,1,2)
        self.setLayout(self.l)

    def keyPressEvent(self, QKeyEvent):
        if QKeyEvent.key()==Qt.Key_Escape:
            self.close()

from openpyxl import load_workbook
work_book=load_workbook("//21.12.121.64/信息技术部共享/yangtong/系统应用/服务器/服务器清单.xlsx")
work_sheet=work_book.get_sheet_by_name("Sheet1")
tmp=[]
s=0
for i in range(len(work_sheet.rows)):
    tmp.append([str(j[i].value) for j in work_sheet.columns])
    s=s+len(tmp[i][6].split())

app = QApplication([])
w = win(tmp[1:])
w.show()
w.center()
app.exec_()
