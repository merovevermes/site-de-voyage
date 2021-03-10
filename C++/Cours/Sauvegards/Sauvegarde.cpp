//
//  Sauvegarde.cpp
//  Cours
//
//  Created by Mérové on 11/02/2021.
//

//#include "Sauvegarde.hpp"
//int main(){
//    int nombre;
//    int valeur_absolue;
//    std::cout<<"veuillez saisir la valeur"<<std::endl;
//    std::cin>>nombre;
//    std::cout<<"la valeur est :" << nombre <<std::endl;
//    if (nombre>=0)
//    {
//    std::cout<<"le resultat est : "<< nombre <<std::endl;
//    }
//    if (nombre<=0) {
//
//    valeur_absolue=nombre-(2*nombre);
//    std::cout<<"le resultat est :" <<valeur_absolue<<std::endl;
//    return 0;
//    }
//    int x;
//    int y;
//    int temp;
//    std::cout<<"veuillez saisir une valeur pour x  : ";
//    std::cin>>x;
//    std::cout<<"veuillez saisir une valeur pour y : ";
//    std::cin>>y;
//    std::cout<<"la valeur de x est : "<<x<<" et la valeur de y est : "<<y<<std::endl;
//    temp=x;
//    x=y;
//    y=temp;
//    std::cout<<"la valeur de x est maintenant : "<<x<<" et la valeur de y est maintenant : "<<y<<std::endl;
//    int a,b,c,temp;
//    std::cout<<"veuillez saisir une valeur pour a  : ";
//    std::cin>>a;
//    std::cout<<"veuillez saisir une valeur pour b : ";
//    std::cin>>b;
//    std::cout<<"veuillez saisir une valeur pour c : ";
//    std::cin>>c;
//    std::cout<<"la valeur de a est : "<<a<<",la valeur de b est:"<<b<<" et la valeur de c est : "<<c<<std::endl;
//    if (a<b) {
//        temp=b;
//        b=a;
//        a=temp;
//    }
//    if (b<c) {
//        temp=c;
//        c=b;
//        b=temp;
//    }
//    std::cout<<"la valeur de a est maintenant : "<<a<<" la valeur de b est maintenant : "<<b<<" et la valeur de c est "<<c<<std::endl;
//

//int N;
//std::cout<<"veullez saisir la taille du tableau"<<std::endl;
//std::cin>>N;
//
//double Tableau[N];
//int i=0;
//for (i=0; i<N; i++) {
//    int valeur=rand();
//    std::cout<<"la valeur est "<<valeur<<std::endl;
//    Tableau[i]=valeur;
//    valeur=0;}
//double somme(0);
//for (int q(0) ; q<N ; q++){
//        somme+=Tableau[q];}
//std::cout<<"la somme est donc "<<somme<<std::endl;
//somme/=N;
//std::cout<<"la moyenne est donc" <<somme<<std::endl;
//return 0;

//}








//vector<int> Tableaux(0);
//int A=1,quantité=0,i=0;
//while (A>0) {
//    cout<<"veuillez saisir la valeur du nombre"<<endl;
//    cin>>A;
//    for (int i(1); i>0; i++) {
//        Tableaux[i]=A;
//    }
//    quantité++;
//    cout<<quantité<<endl;
//
//}
//for (int a(1); a<i; a++) {
//    cout<<"voici le contenut du tableaux"<<Tableaux[a]<<endl;
//        }
//
//cout<<"la quantité est "<<quantité<<endl;
//cout<<"la valleur est négative"<<endl;







//cout<<"veuillez rentré votre caractere";
//char ascii;
//cin>>ascii;
//int caractere=ascii;
//cout<<"votre caractere est : "<<caractere;







//cout<<"veuillez rentré votre caractere";
//char ascii;
//cin>>ascii;
//while (ascii!='#') {
//    cout<<"veuillez rentré votre caractere\n";
//    char ascii;
//    cin>>ascii;
//    int caractere=ascii;
//    cout<<"votre caractere est : "<<caractere<<"\n";
//    if (ascii=='#'){
//        break;
//    }
//}
//cout<<"on s'arrete la"<<"\n";




//int A,B,C,delta;
//cout<<"Veuillez saisir la variable A : ";
//cin>>A;
//cout<<"Veuillez saisir la variable B : ";
//cin>>B;
//cout<<"Veuillez saisir la variable C : ";
//cin>>C;
//cout<<"le programme va résoudre A*x^2+B*x+C=0\n";
//delta=(B*B)-(4*(A*C));
//cout<<"Delta est égale a :" <<delta<<"\n";
//if (delta<0) {
//    cout<<"L'equation n'admets aucun solution \n";
//}
//if (delta==0) {
//    int solution = -B/(2*A);
//    cout<<"la solution de l'equation est : "<<solution<<"\n";
//}
//if (delta>0) {
//    int solution1,solution2;
//    solution1=(-B+sqrt(delta))/(2*A);
//    solution2=(-B-sqrt(delta))/(2*A);
//    cout<<"Les solutioin de l'equation est : "<<solution1<<" et "<< solution2<<"\n";
//
//}
