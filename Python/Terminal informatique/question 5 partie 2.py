def is_jumeaux(a,x):
    liste=[]
    for a in range(1,10000):
        for x in range (1,10000):    
            if (a==x+2):
                 liste.append(a,x)
            return(liste,"sont des nombre premier jumeaux")
            print(a,x , " ne sont pas des nombre premier jumeaux")
