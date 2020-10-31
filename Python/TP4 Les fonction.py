# C1
# from random import*
# liste=[]
# max=randint(0,100)
# for i in range(2,max):
#     a=randint(0,10000)
#     liste.append(a)
# liste=sorted(liste)
# len(liste)
# b=liste[-1]
# print(liste)
# print("le nombre le plus grande est : ",b)

# C2
from random import*

liste1 = []
liste2 = []
liste3 = []
max1 = randint(1, 20)
for i in range(2, max1):
    a = randint(1, 10)
    liste1.append(a)
max2 = randint(2, 20)
for x in range(2, max2):
    c = randint(1, 10)
    liste2.append(c)
liste1 = sorted(liste1)
liste2 = sorted(liste2)
print("la premier liste est:", liste1)
print("la deuxieme liste est : ", liste2)
if len(liste1)>len(liste2):
    for i in range(len(liste2)):
        q = liste1[i]
        b = liste2[i]
        if q == b:
            liste3.append(q)
    if len(liste3) == 0:
        print("aucun nombre n'est pareille")
    else:
        print(liste3)
else:
    for i in range(len(liste1)):
        q = liste1[i]
        b = liste2[i]
        if q == b:
            liste3.append(q)
    if len(liste3) == 0:
        print("aucun nombre n'est pareille")
    else:
        print(liste3)
