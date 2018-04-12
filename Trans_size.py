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
        for i in range(6):
            self.le.append(QLineEdit())
            lay.addWidget(self.le[i],[i,i-1][i%2],i%2)
        self.le[0].setText(str(self.A) + 'm')
        self.le[1].setText(str(self.B) + 'm')
        self.t3 = QTextEdit()
        lay.addWidget(self.t3,i+1,0,2,0)
        lay.addWidget(b1,i+3,0)
        lay.addWidget(b2,i+3,1)
        self.setLayout(lay)
        b1.clicked.connect(self.aaa)
        b2.clicked.connect(self.close)

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()

    def aaa(self):
        self.le[2].setText(str('%5.2f'%(self.A*self.B))+'m2')
        self.le[3].setText(str(self.B*100)+'cm')

app = QApplication([])
w = win(5.2,2.6)
w.show()
app.exec_()