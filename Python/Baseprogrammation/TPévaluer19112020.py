from math import*
# def distance(A,B):
#     ladistance=sqrt((A[0]-B[0])**2+(A[1]-B[1])**2)
#     print(ladistance)
# distance([2,3],[3,5])
# I/B
# def identique(L,A):
#     i=0
#     while i<len(L):
#         ladistance=sqrt((L[i]-A[0])**2+(L[i+1]-A[1])**2)
#         i=i+2
#         if ladistance<0.0001:
#             print("les deux point L et A sont identique")
#         print("les deux point ne sont pas identique")
# identique([2,3],[3,5])
# I/C
# def indice_du_point_le_plus_loin(LP,C):
#     liste=[]
#     i=0
#     while i<len(LP):
#         ladistance=sqrt((LP[i]-C[0]) ** 2+(LP[i+1]-C[1]) ** 2)
#         liste.append(ladistance)
#         i=i+2
#     list.sort(liste)
#     print(liste)
#     print(liste[len(liste)-1])
#indice_du_point_le_plus_loin([9,8,5,4,8,5],[3,5])
#
# I/D
# def Ordonner(LP):
#     O=[0,0]
#     liste=[]
#     i=0
#     while i<len(LP):
#         ladistance=sqrt((LP[i]-O[0]) ** 2+(LP[i+1]-O[1]) ** 2)
#         liste.append(ladistance)
#         i=i+2
#     list.sort(liste)
#     print(liste)
#     print(liste[len(liste)-1])
# Ordonner([9,8,5,4,8,5])

# I/E
# Ordonner([2,2,3,3,6,6,4,4,10,10,1,1,-11,-11])
# I/F
# def chercher(L,A):
#     identique(L,A)
# chercher([2,2,3,3,6,6,4,4,10,10,1,1,-11,-11],[6,6])

def point_commun(Liste1,Liste2):
    listecommun=[]
    for i in range(liste1):
        for a in range(liste2):
            if i==a:
                listecommun.append[i]
    print(listecommun)
point_commun([2,2,3,3,6,6,4,4,10,10,1,1,-11,-11],[2,3,1,1,2,3,2,1,3,2])

def compter(N, L):
    Nombre = 0
    L1 = []
    affectation = 0
    for i in range(1, N+1):
        for j in range(len(L)):
            if i == L[j]:
                Nombre += 1
        L1.append(Nombre)
        affectation += Nombre
        Nombre=0
    comparaison = len(L)*N
    return L1, comparaison, affectation