from PyQt5.QtWidgets import *
class win(QWidget):
    def __init__(self):
        super(win, self).__init__()
        b1 = QPushButton("Start")
        b2 = QPushButton("Quit")
        self.le=[]
        lay=QGridLayout()
        for i in range(6):
            self.le.append(QLineEdit())
            lay.addWidget(self.le[i],[i,i-1][i%2],i%2)
        self.t3 = QTextEdit()
        lay.addWidget(self.t3,i+1,0,2,0)
        lay.addWidget(b1,i+3,0)
        lay.addWidget(b2,i+3,1)
        self.setLayout(lay)
        b1.clicked.connect(self.aaa)
        b2.clicked.connect(self.close)
    def aaa(self):
        self.le[0].setText("10")
app = QApplication([])
w = win()
w.show()
app.exec_()