//
//  main.cpp
//  Cours de Base de la programation
//
//  Created by Mérové on 09/03/2021.
//

#include <iostream>
using namespace std;

int fonction(int A[10], int B[10])
{
    
    int t=0;
    for (int i=0; i<10; i++)
    if(A[i]==B[i]){
        t++;
        
    };
    return t;
}

int fonction2(int A[10],int B[10]){
    int a=0;
    for (int i=0; i<10; i++){
        for (int q=0; q<10; q++) {
            if (A[i]==B[q])
                a++;
            
    }
    }
    return a;
    
}

int suppression(int A,)




int main (){
    int A[]={0,2,3,6,1,2,8,3,5,9,9};
    int B[]={4,3,1,5,6,7,8,6,2,4,2};
    cout<<"l'indice est : "<<fonction(A,B)<<endl;
    cout<<"les valeur commun son : "<<fonction2(A,B)<<endl;

}



