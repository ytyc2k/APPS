from tkinter import *
from time import sleep
w=Tk()
w.title('Game')
w.geometry("351x351")
FM=Frame(w)

GameStr="1234578*6"
btns=[Button(FM,text=GameStr[i],bg="yellow",height = 6, width = 12,font=('Helvetica', '12')) for i in range(9)]
for i in range(9):
    btns[i].grid(column=i%3+1,row=i//3+1)
FM.pack(side="top", fill="x")

x = GameStr.find(num)
k = GameStr.find('*')
i = x // 3
j = x % 3

up = 3 * (i - 1) + j
if (i - 1 < 0): up = 9
dn = 3 * (i + 1) + j
if (i + 1 > 2): dn = 9
lf = 3 * i + j - 1
if (j - 1 < 0): lf = 9
rt = 3 * i + j + 1
if (j + 1 > 2): rt = 9
if (k == up or k == dn or k == lf or k == rt):
    GameStr=GameStr.replace('*','9')
    GameStr=GameStr.replace(num,'*')
    GameStr=GameStr.replace('9',num)
for i in range(9):
    btns[i].config(text=GameStr[i])
if (GameStr == "12345678*"):
    print("YOU WON!!!")
w.mainloop()
