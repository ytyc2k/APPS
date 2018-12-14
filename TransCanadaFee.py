import re
fd = open ('TransCanadaFee.txt','r')
ss=[]
for line in fd:
    ss+=re.findall(r"\d+.\d+(?=  人民币)", line.replace(',',''))
print(sum([float(i) for i in ss]))