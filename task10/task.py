from random import randint
import random
n = int(input("Введите n: "))
list0 = []
for i in range(n):
    list0.append(random.randint(0,1))
print(list0)
k=0
for i in range(n):
    if list0[i]==0:
        k+=1
r=n-k
if r<k:
    print(int(r))
else:
    print(int(k))