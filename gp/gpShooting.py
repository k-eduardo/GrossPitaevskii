#!/usr/bin/python
# -*- coding: utf-8 -*-

def F():
	beta = 1-2*a
	alfa = 1/(2-1.2599)
	f = lambda q,x: (-beta + x*x/4. + alfa * q*q/(x*x))*q if int(x) is not 0 else 0.
	return f

a = 1/(2-1.2599)
b = 1-2*a

v = 0.
q = 1.
x = 0.
L = 10.
h = 0.01


N = int(abs(L/h))
n=0

c1,c4 = a/2,a/2
c2, c3 = (a+b)/2,(a+b)/2
d1,d3 = a,a
d2,d4 = b,0.

f = F()

while (n<N):
	v1 = v + c1*h*f(q,x)
	q1 = q + d1*h*v1
	x1 = x + d1*h

	v2 = v1 + c2*h*f(q1,x1)
	q2 = q1 + d2*h*v2
	x2 = x1 + d2*h

	v3 = v2 + c3*h*f(q2,x2)
	q3 = q2 + d3*h*v3
	x3 = x2 + d3*h

	v = v3 + c4*h*f(q3,x3)
	q = q3 + d4*h*v
	x = x + h

	n+=1
	print x,q,v



