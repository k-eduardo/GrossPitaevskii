//péndulo complicado método runge kutta de cuarto orden 11/03/10
//x de la teoría son y en este programa

#include<stdio.h>
#include<math.h>

//aquí están los parámetros del sustema
#define k 0.2
#define m 1
#define g 9.78
#define l 9.78
#define fo 1.5*m*l
#define wo 1

//aquí las definiciones de las variables con las que trabaja el programa y las funciones
#define a g/l
#define b fo/(m*l)
#define q k/m
#define g1(y1,y2,t) (y2)
#define g2(y1,y2,t) (-y1/t + y1/(t*t) - y1 + y1*y1*y1)

#define P 10000 // periodos que se quieran calcular (T=2pi)

main(){
printf("\na es %lf b es %lf q es %lf\n\n",a,b,q);
double h=-0.1;
int pr;
double xx;
int i,n;
n=400/0.1;
int mm=h*n/(2*M_PI);
double x[n],v[n],t=400.,y1,y2;
double k11,k12,k21,k22,k31,k32,k41,k42;

//Condiciones iniciales

x[0]=1.;
v[0]=0.;
y1=x[0];
y2=v[0];

for(i=0;i<n;i++){
// Algoritmo RK-4

printf("%lf, %lf\n", t,x[i]);

k11 = g1(y1,y2,t);
k12 = g2(y1,y2,t);

k21=g1(y1 + h*k11/2,y2 + h*k12/2,t + h/2);
k22=g2(y1 + h*k11/2,y2 + h*k12/2,t + h/2);

k31 = g1(y1 + h*k21/2,y2 + h*k22/2,t + h/2);
k32 = g2(y1 + h*k21/2,y2 + h*k22/2,t + h/2);

k41 = g1(y1 + h*k31,y2 + h*k32,t + h);
k42 = g2(y1 + h*k31,y2 + h*k32,t + h);

y1 = y1 + h * (k11 + 2*k21 + 2*k31 + k41)/6;
y2 = y2 + h * (k12 + 2*k22 + 2*k32 + k42)/6;

x[i+1] = y1;
v[i+1] = y2;
t = t+h;



}
FILE *out=fopen("rk4.dat","w");
FILE *po=fopen("poincare.dat","w");
t=400.;
for(i=0;i<=n;i++){
xx=x[i];
fprintf(out,"%lf\t%lf\t%lf\n",t,xx,v[i]);
t=t+h;
}
fclose(out);
}
