#include <iostream>
#include <fstream>
#include <math.h>


using namespace std;

int main()
{
    FILE *f = NULL;
    float input [100]={0};
    float aire_minimal ;
    float aire_maximal;
    float x1,y1,x2,y2,x3,y3,y4,x4;
    float dist1,dist2,dist3,dist4;
    float longueur,largeur;
    float semi_perimetre;
    float aire_gift;
    f=fopen("test.txt","r");





    if(f==NULL){

cout << "Impossible d'ouvrir le fichier " << endl;


}
else{

fscanf(f, "%f %f %f %f %f %f %f %f %f %f %f %f %f %f %f %f  ", &input[0], &input[1], &input[2],&input[3],&input[4],&input[5],&input[6],&input[7],&input[8],&input[9],&input[10],&input[11],&input[12],&input[13],&input[14],&input[15]);

if(input[0]==3){

   x1=input[1];
   y1=input[2];
   x2=input[3];
   y2=input[4];
   x3=input[5];
   y3=input[6];




  dist1=sqrt(((x2-x1)*(x2-x1)) + ((y2-y1)*(y2-y1)));
  dist2=sqrt((x2-x3)*(x2-x3) + (y2-y3)*(y2-y3));
  dist3=sqrt((x1-x3)*(x1-x3) + (y1-y3)*(y1-y3));



  if(dist1>dist2 && dist1>dist3){

    longueur=dist1;
  }else if(dist2>dist3 && dist2>dist1){

    longueur=dist2;
  }else if(dist3>dist2 && dist3>dist1){

    longueur=dist3;
  }


  semi_perimetre=(dist1+dist2+dist3)/2;
  aire_gift=sqrt(semi_perimetre*(semi_perimetre-dist1)*(semi_perimetre-dist2)*(semi_perimetre-dist3));

  largeur = aire_gift*2/longueur;

aire_minimal= ceil(longueur * largeur) ;
aire_maximal= ceil((longueur*longueur/2)) ;



cout << "Gift1 : " << endl;
cout << "Min_area : " <<aire_minimal*1000<< endl;

cout << "Max_area : " <<aire_maximal*1000<< endl;

cout<<" " <<endl;

}
if(input[7]==4){

    x1=input[8];
   y1=input[9];
   x2=input[10];
   y2=input[11];
   x3=input[12];
   y3=input[13];
   x4=input[14];
   y4=input[15];


   dist1=sqrt(((x2-x1)*(x2-x1)) + ((y2-y1)*(y2-y1)));
  dist2=sqrt((x2-x3)*(x2-x3) + (y2-y3)*(y2-y3));
  dist3=sqrt((x1-x4)*(x1-x4) + (y1-y4)*(y1-y4));
  dist4=sqrt((x4-x3)*(x4-x3) + (y4-y3)*(y4-y3));

  longueur=max(max(dist1,dist2),max(dist3,dist4));
  largeur=min(min(dist1,dist2),min(dist3,dist4));

  aire_minimal=longueur*largeur;
  aire_maximal=aire_minimal*2;

  cout << "Gift2 : " << endl;
cout << "Min_area : " <<aire_minimal*1000<< endl;

cout << "Max_area : " <<aire_maximal*1000<< endl;

}




}


    return 0;
}
