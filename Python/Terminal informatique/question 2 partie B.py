def nombre_diviseur(i):
    return len(diviseur(i))
def diviseur(i):
    liste=[]
    for x in range(1,i+1):
        if(i%x)==0:
            liste.append(x)
    return(liste)
for i in range(1,1000):
    print (i,nombre_diviseur(i))
