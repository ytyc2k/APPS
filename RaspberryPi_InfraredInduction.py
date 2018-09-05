import RPi.GPIO as G
from time import sleep
G.setmode(G.BOARD)
G.setup(40,G.IN)
G.setup(35,G.OUT)
def flash():
   for i in range(10):
      G.output(35,0);sleep(0.1)
      G.output(35,1);sleep(0.1)
while True:
    inv=G.input(40)
    if inv == False:
        flash()
        while inv == False:
            inv=G.input(40)
