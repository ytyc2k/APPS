import re
Dict={'m':1.0,'ft':0.3048,'cm':0.01,'inch':0.0254}
ForegnExchange={'$':1.0,'Y':5.0}
def Trs2Meter(DigitalStr): # Trs2Meter('120cm') result:1.2
    return float(re.findall("\d+\.?\d*", DigitalStr)[0])*Dict[re.findall("[a-z]+", DigitalStr)[0]]
def Trs2Dollar(PriceStr): # Trs2Dollar('5.5Y') result:1.1
    return float(re.findall("\d+\.?\d*", PriceStr)[0])/ForegnExchange[PriceStr[-1]]

class pjt():
    def __init__(self,Item):
        self.RealArea=Trs2Meter(RealSize[0])*Trs2Meter(RealSize[1])
        self.ItemArea=Trs2Meter(Item[0])*Trs2Meter(Item[1])
        self.ItemPrice=Trs2Dollar(Item[2])
    def GotTotalPrice(self):
        print(self.RealArea/self.ItemArea*self.ItemPrice)

RealSize=['5.2m','2.6m']
WallPaper_Taobao=pjt(['10m','53cm','58Y'])
WallPaper_Taobao.GotTotalPrice()
WallPaper_Amazon1=pjt(['17.7inch','19.7ft','34.9$'])
WallPaper_Amazon1.GotTotalPrice()
WallPaper_Amazon2=pjt(['33ft','1.74ft','19.99$'])
WallPaper_Amazon2.GotTotalPrice()
WallPaper_Amazon3=pjt(['20.8inch','393.7inch','29.99$'])
WallPaper_Amazon3.GotTotalPrice()
RealSize=['3m','7m']
WallPaper_Amazon3=pjt(['18inch','18inch','7.99$'])
WallPaper_Amazon3.GotTotalPrice()