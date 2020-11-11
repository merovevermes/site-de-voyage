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
# from random import*
#
# liste1 = []
# liste2 = []
# liste3 = []
# max1 = randint(1, 20)
# for i in range(2, max1):
#     a = randint(1, 10)
#     liste1.append(a)
# max2 = randint(2, 20)
# for x in range(2, max2):
#     c = randint(1, 10)
#     liste2.append(c)
# liste1 = sorted(liste1)
# liste2 = sorted(liste2)
# print("la premier liste est:", liste1)
# print("la deuxieme liste est : ", liste2)
# if len(liste1)>len(liste2):
#     for i in range(len(liste2)):
#         q = liste1[i]
#         b = liste2[i]
#         if q == b:
#             liste3.append(q)
#     if len(liste3) == 0:
#         print("aucun nombre n'est pareille")
#     else:
#         print(liste3)
# else:
#     for i in range(len(liste1)):
#         q = liste1[i]
#         b = liste2[i]
#         if q == b:
#             liste3.append(q)
#     if len(liste3) == 0:
#         print("aucun nombre n'est pareille")
#     else:
#         print(liste3)

# C4
# nombre1 = int(input("veuillez saisir un nombre :"))
# nombre2 = int(input("veuillez saisir un deuxieme nombre :"))
#
# def PGCD(nombre1, nombre2):
#     listediviseur1 = []
#     listediviseur2 = []
#     listediviseurcommun = []
#     for i in range(1, nombre1):
#         if nombre1 % i == 0:
#             listediviseur1.append(i)
#     print("voici les diviseur du nombre 1 :", listediviseur1)
#     for a in range(1, nombre2):
#         if nombre2 % a == 0:
#             listediviseur2.append(a)
#     print("Voici les diviseur du nombre 2 :", listediviseur2)
#
#     if len(listediviseur1) > len(listediviseur2):
#         for n in range(len(listediviseur1)):
#             q = listediviseur1[n]
#             for k in range(len(listediviseur2)):
#                 p = listediviseur2[k]
#                 if q == p:
#                     listediviseurcommun.append(p)
#         if len(listediviseurcommun) == 0:
#             print("il n'y a aucun diviseur commun")
#         else:
#             print("les diviseur commun sont: ", listediviseurcommun)
#     else:
#         for n in range(len(listediviseur1)):
#             q = listediviseur1[n]
#             for k in range(len(listediviseur2)):
#                 p = listediviseur2[k]
#                 if q == p:
#                     listediviseurcommun.append(p)
#         if len(listediviseurcommun) == 0:
#             print("il n'y a aucun diviseur commun")
#         else:
#             print("les diviseur commun sont: ", listediviseurcommun)
#     pgcd = len(listediviseurcommun)
#     pgcd = pgcd - 1
#     print("le pgcd est :",listediviseurcommun[pgcd])
#
# #######le PGCD de 18 et 12 est 6 et non pas 4########
#
#
# PGCD(nombre1,nombre2)

# D1
from math import *
# def fonction(a,b,c):
#     delta = b*b-4*a*c
#     if delta > 0:
#         racineDeDelta = math.sqrt(delta)
#         retour = [(-b - racineDeDelta) / (2 * a), (-b + racineDeDelta) / (2 * a)]
#     elif delta < 0:
#         retour = []
#     else:
#         retour = [-b / (2 * a)]
#     print(retour)
# fonction(2,1,6)

 # version amelioré ->
 # from math import *
 # def fonction(a,b,c):
 #     delta=b**2-4*a*c
 #
 #     if delta>0:
 #         racine = sqrt(delta)
 #         x1=(-b-racine/(2*a))
 #         x2=(-b+racine/(2*a))
 #         print("delta est positif donc 2 solution")
 #         print("la premier solution est : ",x1)
 #         print("la deuxieme solution est : ",x2)
 #     else:
 #         if delta==0:
 #             x0=-b/(2*a)
 #             print("delta est egale a 0 donc il n'y a que 1 solution")
 #             print("la solution est :",x0)
 #         else:
 #             print("Pas de solution dans l'espace des réels")
 #
 # fonction(2,3,9/8)
