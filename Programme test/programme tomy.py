# from math import *
# xA=float(input("Donner la valeur de xA"))
# yA=float(input("Donner la valeur de yA"))
# xB=float(input("Donner la valeur de xB"))
# yB=float(input("Donner la valeur de yB"))
# xC=float(input("Donner la valeur de xC"))
# yC=float(input("Donner la valeur de yC"))
# def distance1(xA,yA,xB,yB):
#     x1=xA-xB
#     y1=yA-yB
#
#     res=sqrt(x1**2 + y1**2)
#     return res
# r1=distance1(xA,yA,xB,yB)
# print("[AB] =",r1)
# def distance2(xA,yA,xC,yC):
#     x2=xA-xC
#     y2=yA-yC
#     res=sqrt(x2**2 + y2**2)
#     return res
# r2=distance2(xA,yA,xC,yC)
# print("[AC] =",r2)
# def distance3(xB,yB,xC,yC):
#     x3=xB-xC
#     y3=yB-yC
#     res=sqrt(x3**2 + y3**2)
#     return res
# r3=distance3(xB,yB,xC,yC)
# print("[BC] =",r3)
# if r1**2==r2**2+r3**2:
#     print("vrai")
# elif r2**2==r1**2+r3**2:
#     print("vrai")
# elif r3**2==r1**2+r2**2:
#     print("vrai")
# else:
#     print("faux")


from math import sqrt

def distanceAB(xA, yA, xB, yB):
    xAB = xA - xB
    yAB = yA-yB
    resAB = sqrt(xAB**2 +yAB**2)
    return resAB**2
def distanceAC(xA,yA,xC,yC):
    xAC = xA-xC
    yAC = yA-yC
    resAC = sqrt(xAC**2 + yAC**2)
    return resAC**2
def distanceBC(xB,yB,xC,yC):
    xBC = xB-xC
    yBC = yB-yC
    resBC = sqrt(xBC**2 + yBC**2)
    return resBC**2
xA=int(input("veuillez saisir xA : "))
yA=int(input("veuillez saisir yA : "))
xB=int(input("veuillez saisir xB : "))
yB=int(input("veuillez saisir yB : "))
xC=int(input("veuillez saisir xC : "))
yC=int(input("veuillez saisir yC : "))
if distanceAB(xA, yA, xB, yB)+ distanceAC(xA ,yA ,xC ,yC) == distanceBC(xB ,yB ,xC ,yC):
    print ("c'est un triangle rectangle")
else :
    print("ce n'est pas un triangle rectangle")