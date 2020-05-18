#include <iostream>
#include <fstream>
#include <math.h>

using namespace std;

int main()
{
    FILE *f = NULL;
    float input [100]={0};
    float nbr_segment ;
    float temps;
    float x1,y1,z1,w1,x,y,z,w;
    float constance;

    f=fopen("input1.txt","r");





    if(f==NULL){

cout << "Impossible d'ouvrir le fichier " << endl;


}
else{


fscanf(f, " %f %f %f %f %f %f %f %f %f %f   ", &input[0], &input[1], &input[2],&input[3],&input[4],&input[5],&input[6],&input[7],&input[8],&input[9]);

nbr_segment = input[0];

if(nbr_segment==3){

temps=input[1];
   x=input[2];
   x1=input[3];
   y=input[4];
   y1=input[5];
   z=input[6];
   z1=input[7];


   constance=((temps*x*y*z)-(y*z*x1)-(x*y1*z)-(x*y*z1))/(y*z)+(z*x)+(x*y);



}
else
    if(nbr_segment==4){

      temps=input[1];
   x=input[2];
   x1=input[3];
   y=input[4];
   y1=input[5];
   z=input[6];
   z1=input[7];
   w=input[8];
   w1=input[9];

 constance=((temps*x*y*z)-(y*z*x1)-(x*y1*z)-(x*y*z1))/(y*z)+(z*x)+(x*y);


    }
}

cout << "la constante c est : "<< constance<< endl;
return 0;
}
