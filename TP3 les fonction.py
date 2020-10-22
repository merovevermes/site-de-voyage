# import math
# def distance(xA,yA,xB,yB):
#     x=xA-xB
#     y=yA-yB
#     res=sqrt(x2+y2)
#     return res
# ifname=="main" :\
#     r=distance(1,-2,3,5)
# print(r)

# A.1
# from math import *
# def distance(xA,yA,xB,yB):
#         x=xA-xB
#         y=yA-yB
#         res=sqrt(x2 + y2)
#         return res
# if name=="main":
#         r=distance(1,-2,3,5)
# #         print(r)
# A.2

# from math import sqrt
# def distanceAB(xA, yA, xB, yB):
#     xAB = xA - xB
#     yAB = yA-yB
#     resAB = sqrt(xAB  2 +yAB  2)
#     return resAB2
# def distanceAC(xA,yA,xC,yC):
#     xAC = xA-xC
#     yAC = yA-yC
#     resAC = sqrt(xAC  2 + yAC  2)
#     return resAC2
# def distanceBC(xB,yB,xC,yC):
#     xBC = xB-xC
#     yBC = yB-yC
#     resBC = sqrt(xBC  2 + yBC  2)
#     return resBC2
#
# if distanceAB(1,5,8,7)+ distanceAC(4,89,45,5) == distanceBC(1456,4,9874,651):
#     print ("c'est un triangle rectangle")
# else :
#     print("ce n'est pas un triangle rectangle")
# A.3

# from math import sqrt
#
# def distanceAB(xA, yA, xB, yB):
#     xAB = xA - xB
#     yAB = yA-yB
#     resAB = sqrt(xAB  2 +yAB  2)
#     return resAB2
# def distanceAC(xA,yA,xC,yC):
#     xAC = xA-xC
#     yAC = yA-yC
#     resAC = sqrt(xAC  2 + yAC  2)
#     return resAC2
# def distanceBC(xB,yB,xC,yC):
#     xBC = xB-xC
#     yBC = yB-yC
#     resBC = sqrt(xBC  2 + yBC  2)
#     return resBC2
# xA=int(input("veuillez saisir xA : "))
# yA=int(input("veuillez saisir yA : "))
# xB=int(input("veuillez saisir xB : "))
# yB=int(input("veuillez saisir yB : "))
# xC=int(input("veuillez saisir xC : "))
# yC=int(input("veuillez saisir yC : "))
# if distanceAB(xA, yA, xB, yB)+ distanceAC(xA ,yA ,xC ,yC) == distanceBC(xB ,yB ,xC ,yC):
#     print ("c'est un triangle rectangle")
# else :
#     print("ce n'est pas un triangle rectangle")

# nombre=int(input("veuillez saisir votre nombre"))
# liste=[]
# for i in range(1,nombre+1):
#     a=nombre%i
#     if a==0:
#         liste.append(i)
# if len(liste)==2:
#     print("le nombre est premier")
# else:
#     print("le nombre n'est pas premier")

N=int(input("Veuillez saisir le nombre N "))
M=int(input("Veuillez saisir le nombre M "))
liste=[]
listedesnombrepremier=[]
def nombre_premier(N,M):
    for i in range (N,M):
        for a in range(1,M+1):
            x=i%a
            if x==0:
                liste.append(a)
        if len(liste)==2:
            listedesnombrepremier.append(i)
    print(listedesnombrepremier)
nombre_premier(N,M)

# le dernier programme ne marche pas et je ne sais pas pourquoi ?