def nombre_diviseur(i):
    return len(diviseur(i))
def diviseur(i):
    liste=[]
    for x in range(1,i+1):
        if(i%x)==0:
            liste.append(x)
    return(liste)
for i in range(1,10000):
    if nombre_diviseur(i)==2:
        print (i)
