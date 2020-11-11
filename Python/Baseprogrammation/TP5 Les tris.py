# I.1/I.2
# def
#
def triebulle(N):
    compteur=0
    while compteur<1:
        for i in range(len(N)-1):
            for i in range(len(N)-1):
                if N[i]>N[i+1]:
                    cache=N[i+1]
                    N[i+1]=N[i]
                    N[i]=cache
                    print(N)
                else:
                    compteur+=1


# triebulle([564,987,62432,6574,626587,5,654,687,54,87,541,21,654,654,3241,4])
# II
# programme fait par moi même
# def triedirect(N):
#     for i in range(0,2*len(N)):
#         for a in range (len(N))
#             if N[i+1]<=N[i]:
#                 tmp=N[i+1]
#                 N[i+1]=N[i]
#                 N[i]=tmp
#             print(N)
# triedirect([4, 8, 4, 7, 5, 2, 1])
# je n'y suis pas arriver

# programme trouver sur internet pour realiser la suite des exercice
def tri_direct(tab):
    for i in range(len(tab)):
        min=i
        for j in range(i+1,len(tab)):
            if tab[min]>tab[j]:
                min=j
        tmp=tab[i]
        tab[i]=tab[min]
        tab[min]=tmp
    print(tab)


# II.1,2,3
def indice_max(tab,N):
    for i in range(len(tab)):
        min=i
        for j in range(i+1,len(tab)):
            if tab[min]>tab[j]:
                min=j
        tmp=tab[i]
        tab[i]=tab[min]
        tab[min]=tmp
    print(tab)
    print(tab[N])


# III
# debut=time.time()
# for w in range(100):
#     liste=[random.randint(10000,100000) for i in range (100)]
#     tri_direct(liste)
# fin=time.time()
# print(fin-debut)
# pour tribulle : 21.859536170959473
# pour triedirect : 0.24970555305480957


# IV
# a- la boucle while est préférable. l'arrete se porte sur deux élement esque il est égale a 11 ou esque il est inférieur a 5.
# b-
# version for
def est_dans_listefor(L,n):
    for i in range(len(L)):
        if L[i] == n:
            print("vrai")
        print("faux")


# version while
def est_dans_listewhile(L,n):
    i=0
    while L[i] != n:
        print("Faux")
        i+=1
    print("Vrai")
# IV.2 il va renvoyer vrai car 22 appartient bien a la liste de liste
# le chiffre n'appartient pas a la liste par consequence le programme ne peut pas renvoyer vrai

def est_dans_liste_trié(L,n):
    i=0
    while L[i]<=n:
        print("le chiffre est inferieur a 5")
        i+=1
    print("les chiffre au dessus sont touse suppérieur a 5")



def recherche_dichotomiqeu(t, v):
    x = 0
    y = len(t)
    if y == 0:
      return False
    while True:
        m = (x + y) // 2
        if x == m:
          return t[x] == v
        if t[m] > v:
            y = m
        else:
            x = m
    return t[x] == v


# on peut calculer comme on la fait plus haut le temps d'exectuion des algo de tri