def plus_grand(L,d,f):
    ind=d
    for j in range(d,f+1):
        if L[j]<L[ind]:
            ind=j
    return ind

def tri_selection_rec(tL,d):
    if d==tL:
        return
    else:
        ind=plus_grand(L,d,len(L)-1)
        tmp=L[ind]
        L[ind]=L[d]
        L[d]=tmp
        tri_selection_rec(tL,d+1)

if __name__ == "__main__":
    L=[2,10,8,22,5,44]
    i = 0
    tri_selection_rec(len(L),0)
    print(L)