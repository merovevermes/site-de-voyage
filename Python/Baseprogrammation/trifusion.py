import time
from random import*
def fusion(lg,ld):
    aux=[]
    indice_lg=0
    indice_ld=0
    while (indice_lg <len(lg) and indice_ld < len(ld)):
        if lg[indice_lg] < ld[indice_ld]:
            aux.append(lg[indice_lg])
            indice_lg+=1
        else:
            aux.append(ld[indice_ld])
            indice_ld+=1
    if indice_lg<len(lg):
        aux=aux+lg[indice_lg:]
    if indice_ld<len(ld):
        aux=aux+ld[indice_ld:]
    return aux


def tri_fusion(_liste):
    taille=len(_liste)
    if taille > 1:
        m=taille//2
        liste_gauche=tri_fusion(_liste[:m])
        liste_droite=tri_fusion(_liste[m:])
        return fusion(liste_gauche,liste_droite)
    else:
        return _liste
_liste=[]
t=time.time()
for i in range (1000):
    _liste.append(randint(0,100))
print(_liste)
tri_fusion(_liste)
b = time.time()
print(b-t)