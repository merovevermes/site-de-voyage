from random import *
# # 1 a)

# liste=[]
# a=int(input("veuillez saisir un nombre minoré :"))
# b=int(input("vueiller saisir un nombre majoré :"))
# nombre=int(input("veuillez saisir n nombre de fois"))
# for i in range(nombre) :
#     x=randint(a,b)
#     liste.append(x)
# print(liste)
# # b)
# w=int(input("donner une valeur : "))
# if w in liste :
#     print("Présent dans le liste à l'indice...")
# else :
#     print("Absent de la liste")
# # c)
# maxi=liste[0]
# for i in liste:
#     if i >= maxi:
#         maxi = i
# print("la valeur maximum est :",maxi)
# min=liste[0]
# for i in liste:
#     if i <= min:
#         min=i
# print("la valeur minimum est :" ,min)
# somme=sum(liste)
# nombre=len(liste)
# moyenne=somme/nombre
# print("la moyenne des valeur est :", moyenne)

# 2)
# liste=[]
# nombremaximum=int(input("veuillez saisir un nombre de réiteration: "))
# for i in range (nombremaximum):
#     nombrealeatoire=randint(1,2)
#     liste.append(nombrealeatoire)
# print(liste)
# print(sorted(liste))
# 2.2=
# liste=[]
# nombremaximum=int(input("veuillez saisir un nombre de réiteration: "))
# for i in range (nombremaximum):
#     nombrealeatoire=randint(1,3)
#     liste.append(nombrealeatoire)
# print(liste)
# print(sorted(liste))
# # 3)
# liste1 =[]
# liste2=[]
# a=int(input("veuillez saisir un minoré :"))
# b=int(input("veuillez saisir un majauré : "))
# nombredefois=int(input("veuillez saisir un nombre de fois :"))
#
# for i in range(nombredefois):
#     nombre1=randint(a,b)
#     nombre2 = randint(a,b)
#     liste1.append(nombre1)
#     liste2.append(nombre2)
# print(liste1)
# print(liste2)
#
# # 3.2) je n'ai pas compris la consigne
# # 3.3)
# liste3=[]
# print(sorted(liste1+liste2))
# 4.1)
import string
import random
longeur=int(input("choisir un nombre entre 4 et 12 caractere : "))
mdp="".join(random.choice(string.ascii_letters+string.digits+string.punctuation) for i in range(longeur))
if len(mdp)>4:
    if len(mdp)<12:
        if "="or","or"_"or "&" or"?" or "#" or "*" or  "$" or "@" or "{" or "}" or"+" or "(" or ")" or ":" or  "," or ";" or "!" or '"' or "'" or "." or "e" in mdp:
            if " "not in mdp:
                print("le mots de passe est :", mdp)
print("invalide")
# le programme ne marche pas parce que il ne prend pas en compte la ligne 76

suitedechiffre="".join(random.choice(string.ascii_letters+string.digits)for i in range(randint(5,10)))
print("veuillez saisir : ",suitedechiffre)
saisiehumain=str(input("saisir ce que on vous demende :")
if saisiehumain==suitedechiffre:
    print("le mots de passe est validé")

#     invalid syntax a la ligne 85 mais je ne comprend pas pk
