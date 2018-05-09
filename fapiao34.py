from PyQt4.QtGui import *
from PyQt4.QtCore import *
class win(QWidget):
    def __init__(self):
        super(win, self).__init__()
        self.setWindowTitle("Fapiao Caculator")
        b1 = QPushButton("Start")
        b2 = QPushButton("Quit")
        self.le=[]
        lay=QGridLayout()
        l1=QLineEdit()
        l1.setFocus()
        for i in range(6):
            self.le.append(QLineEdit())
            lay.addWidget(self.le[i],[i,i-1][i%2],i%2)
            self.le[i].setValidator(QRegExpValidator(QRegExp("[0-9]?\d?\d(\.\d{1,2})?")))
            self.connect(self.le[i],SIGNAL("returnPressed()"),self.ccc)
        self.t3 = QTextEdit()
        self.t3.setReadOnly(True)
        self.focusNextPrevChild(True)
        lay.addWidget(self.t3,i+1,0,2,0)
        lay.addWidget(b1,i+3,0)
        lay.addWidget(b2,i+3,1)
        self.setLayout(lay)
        self.connect(b1, SIGNAL("clicked()"), self.aaa)
        self.connect(b2, SIGNAL("clicked()"), self.close)
    def aaa(self):
        A=[]
        for i in self.le:
            A.append(float(i.text()) if i.text() else 0)
            i.setText("")
        C=self.bbb(A)
        for i in range(len(C[0])):
            self.le[i].setText(str(C[0][i]))
    def bbb(self,A):
        print(A)
        from itertools import combinations
        B=[]
        for i in range(1,len(A)+1):
            B+=[sum(j) for j in combinations(A,i) if sum(j)<=600]
        self.t3.setText(str(max(B)))
        for i in range(1,len(A)+1):
            C=[j for j in combinations(A,i) if sum(j)==max(B)]
            if C:return C
    def ccc(self):
        self.focusNextPrevChild(True)
app = QApplication([])
w = win()
w.show()
app.exec_()
