# ~ ex1
# a= int(input("donner un entier positif inférieur à 100 :"))
# while a>100:
# 	a=int(input("donner un entier positif inféreur à 100 :"))
# print("tout va bien")
#
#
#
#
#
#
#
#
# ~ ex2
# m=int(input("donner le nombre de la table de multiplication entre 2 et 9 : "))
# while m<2 or m>9:
# 	m=int(input("donner le nombre de la table de multiplication entre 2 et 9 :"))
# for i in range (11):
# 	r=m*i
# 	print(r)
#
#
#
# ~ ex 3
# ~ A)
# ~ som=0
# ~ cont=0
# ~ n=int(input())
# ~ while(n!=0)
# 	~ som+=n
# 	~ cont+=1
# 	~ n=int(intput))
# ~ print(som/cont)
#
# ~ autre facon de le faire
#
# a=int(input("donner un nombre pour faire la moyene des 4 nombre. Si c'est un 0 cela s'arrete"))
# b=int(input("donner un nombre pour faire la moyene des 4 nombre. Si c'est un 0 cela s'arrete"))
# c=int(input("donner un nombre pour faire la moyene des 4 nombre. Si c'est un 0 cela s'arrete"))
# d=int(input("donner un nombre pour faire la moyene des 4 nombre. Si c'est un 0 cela s'arrete"))
# while a!=0 and b!=0 and c!=0 and d!=0 :
# 	r=a+b+c+d
# 	r=r/4
# 	print(r)
# 	a=int(input("donner un nombre pour faire la moyene des 4 nombre. Si c'est un 0 cela s'arrete"))
# 	b=int(input("donner un nombre pour faire la moyene des 4 nombre. Si c'est un 0 cela s'arrete"))
# 	c=int(input("donner un nombre pour faire la moyene des 4 nombre. Si c'est un 0 cela s'arrete"))
# 	d=int(input("donner un nombre pour faire la moyene des 4 nombre. Si c'est un 0 cela s'arrete"))
#
# print("on arrete la")
#
# ~ B)
# ~ som=0
# ~ cont=0
# ~ n=int(input())
# ~ min=n
# ~ max=n
# ~ while(n!=0)
# 	~ som+=n
# 	~ cont+=1
# 	~ if(n<min):
# 		~ min=n
# 	~ if(n>max):
# 		~ max=n
# 	~ n=int(input())
# ~ print(som/cont)
# ~ print("maxi",max,"mini",min)s
#
# ~ ex4
# ~ som_imp=0
# ~ som_p=0
# ~ cont_p=0
# ~ cont_imp=0
# ~ n=int(input())
# ~ while(n!=0):
# 	~ if(n%2==0):
# 		~ som_p+=n
# 		~ cont_p+=1
# 	~ else:
# 		~ som_imp+=n
# 		~ cont_imp+=1
# 	~ n=int(input())
# ~ if(cont_p>0):
# 	~ print("La moyenne paire est:",som_p/cont_p)
# ~ else:
# 	~ print("0")
# ~ if(cont_imp>0):
# 	~ print("La moyenne impaire est:",som_imp/cont_imp)
# ~ else:
# 	~ print("0")
#
# ~ ex 5
# ~ A)
# ~ a=1
# ~ while(a!=42):
# 	~ a=int(input())
# 	~ if(a<42):
# 		~ print("superieur")
# 	~ elif(a>42):
# 		~ print("inferieur")
# ~ print ("bravo")
# ~ B)
# ~ from random import*
# ~ prix=randint(1,100)
# ~ n=1
# ~ a=int(input("quels est le prix"))
# ~ while(a!=prix):
# 	~ a=int(input())
# 	~ if(a<prix):
# 		~ print("superieur")
# 	~ elif(a>prix):
# 		~ print("inferieur")
# ~ print("bravo")
#  ex6
# ~ largeur=int(input("veuiller saisir la largeur du rectangle"))
# ~ longeur=int(input("veuiller saisir la longeur du rectangle"))
# ~ centre=largeur-2
# ~ print("*"*largeur)
# ~ for i in range(longeur-1):
# 	~ print("*",""*centre,"*")
# ~ print("*"*largeur)
#
# taille=int(input("veuiller saisir la taille de la forme"))
# taille1=taille
# taille2=taille
# for i in range(taille1):
# 	debut=i+1
# 	millieu=taille1*2-i*2
# 	print(debut*" ","*",millieu*" ","*")
# for a in range(taille2):
# 	debut=taille2-a
# 	millieu=a*2
# 	print(debut*" ","*",millieu*" ","*")
#  je n'ai pas compris ce que était un factorielle d'un entier
