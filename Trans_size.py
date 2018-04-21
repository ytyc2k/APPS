from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
class win(QWidget):
    def __init__(self,A,B):
        super(win, self).__init__()
        b1 = QPushButton("Start")
        b2 = QPushButton("Quit")
        self.le=[]
        self.A=A
        self.B=B
        lay=QGridLayout()
        for i in range(14):
            self.le.append(QLineEdit())
            lay.addWidget(self.le[i], i / 4, i % 4)
        self.le[0].setText(str(self.A) + 'm')
        self.le[1].setText(str(self.B) + 'm')
        self.le[2].setEnabled(0)
        self.t3 = QTextEdit()
        lay.addWidget(self.t3,i+1,0,2,0)
        lay.addWidget(b1,i+3,0)
        lay.addWidget(b2,i+3,1)
        self.setLayout(lay)
        b1.clicked.connect(self.trans)
        b2.clicked.connect(self.close)

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()
    def trans(self):
        self.le[2].setText(str('%5.2f'%(self.A*self.B))+'m2')
        self.le[3].setText(str(self.A*self.B*10.76)+'sqft')
        self.le[4].setText(str(self.B*100)+'cm')

app = QApplication([])
w = win(5.2,2.6)
w.show()
app.exec_()