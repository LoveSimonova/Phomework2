import math
S = int(input("Введите S: "))
P = int(input("Введите P: "))
D=pow(S,2)-4*P
y1=(S+math.sqrt(D))/2
y2=(S-math.sqrt(D))/2
if (y2>0)&(int(y2)==y2):
    x=S-y2
    if(x>0):
        print(x,y2)
elif (y1>0)&(int(y1)==y1):
    x=S-y1
    if(x>0):
        print(x,y1)