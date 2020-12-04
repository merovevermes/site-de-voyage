# def plus_grand(L,d,f):
#     ind=d
#     for j in range(d,f+1):
#         if L[j]<L[ind]:
#             ind=j
#     return ind
#
# def tri_selection_rec(tL,d):
#     if d==tL:
#         return
#     else:
#         ind=plus_grand(L,d,len(L)-1)
#         tmp=L[ind]
#         L[ind]=L[d]
#         L[d]=tmp
#         tri_selection_rec(tL,d+1)
#
# if __name__ == "__main__":
#     L=[2,10,8,22,5,44]
#     i = 0
#     tri_selection_rec(len(L),0)
#     print(L)

# def Estpremier(N):
#     listediviseur=[]
#     for i in range(1,N+1):
#         if N%i==0:
#             listediviseur.append(i)
#     if len(listediviseur)==2:
#         print ("Le nombre est premier et il as ", listediviseur,"comme diviseur")
#     else :
#         print ("Le nombre n'est pas premier et il as ", listediviseur,"comme diviseur")
# Estpremier(3)

def recursive(N,M):
    listepremier=[]
    for a in range(N,M):
        listediviseur=[]
        for t in range(1,a+1):
            if a%t==0:
                listediviseur.append(t)
        if len(listediviseur)==2:
            listepremier.append(a)
    for b in range (len(listepremier)):
        listesomme=[]
        resultat=[]
        listesomme.append(1/b)
        resultat.append(sum(listesomme))
    print(resultat)
recursive(0,10)

