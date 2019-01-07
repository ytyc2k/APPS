y=0
P=350
K=P
R=1.08
AGE=46
while P>0:
    y = y + 1;P = K;A = []
    for x in range(AGE,100):
        if x>=65:
            S=P*R-y+10
        else:
            S=P*R-y
        P=S
        A.append(int(P))
        if P<0:
            print(x,P,y)
            print(A)
            break

y=y-1;P = K;A = []
for x in range(AGE,100):
    if x>=65:
        S=P*R-y+10
    else:
        S=P*R-y
    P=S
    A.append(int(P))
print(y)
print(A)
