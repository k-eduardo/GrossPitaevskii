# -*- coding: utf-8 -*-

def RK42ODE(g):
	f = (lambda x, f, df:df)
	return lambda t, x, dx, dt: (lambda k11,k12: (lambda k21,k22: (lambda k31,k32: (lambda k41,k42 : [(k41+2*k31+2*k21+k11)/6,(k42+2*k32+2*k22+k12)/6] )(dt*f(t + dt,x + k31,dx + k32),dt*g(t + dt,x+k31,dx+k32)) )(dt*f(t+dt/2,x+k21/2,dx+k22/2),dt*g(t+dt/2,x+k21/2,dx+k22/2)))(dt*f(t+dt/2,x+k11/2,dx+k12/2),dt*g(t+dt,x+k11/2,dx+k12/2)))(dt*f(t,x,dx),dt*g(t,x,dx))
def RK4(f):
    return lambda t, y, dt: (lambda dy1: (lambda dy2: (lambda dy3: (lambda dy4: (dy1 + 2*dy2 + 2*dy3 + dy4)/6)( dt * f(t+dt,y+dy3)))( dt * f( t + dt/2, y + dy2/2 ) ))( dt * f( t + dt/2, y + dy1/2 ) ))( dt * f( t       , y         ) )

#Expresiones para el "campo vectorial"

def Asym0(): 
	return lambda x,q: 0.001
def AsymInf():
	return lambda x,q,v: (-q + q*q*q)
def GP():
	return lambda x,q,v: (-v*x - q*x*x + q + q*q*q*x*x)/(x*x)

#Pruebas

def prueba(f):
	return (lambda x,y :(
		lambda z,a : (
			lambda q,w: (f(x,f(y,f(z,f(a,f(q,w))))))
			)("\n","Suerte.") )
			("una ","prueba.") )