#include <iostream>
#include "Header.h"
#include <cstdlib>
#include <vector>
#include <stdio.h>
#include <algorithm>
using namespace std;


int main() {
    int Div,i,a,longeur;
    cout<<"veuillez saisir un nombre pour afficher ses divisieur\n";
    cin>>Div;
    int Tableaux[Div];
    for (i; i<Div; i++) {
        if (Div%i==0){
            Tableaux[i]=i;
            longeur++;
            
        }
    }
    sort(Tableaux)
    cout<<"les diviseur de "<<Div<<" sont : ";
    for (a;a<Div; a++)
    {
        if (Tableaux[a]!=0)
            cout<<Tableaux[a];
    }
    if (longeur==2){
        cout<<"le nombre est premier";
    }
        
}
