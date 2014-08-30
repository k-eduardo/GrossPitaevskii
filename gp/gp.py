#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from lib import *
import inspect
from math import isnan

vel1 = 0.58556722913132 #con el cambio de ode en x=0.1


f , df, dx, L = 0.0, 0.4, 0.001, 100.
x = 0.0
n, N = 0, abs(L/dx)
xlineal = 0.005

xtoinf = AsymInf()
xint = GP()

H = RK42ODE(xint)
G = RK42ODE(xtoinf)

i=0
ee = 1.
dfi = df
precision = 16

while i<precision:
	j=0
	trigger = True
	ee = ee*0.1
	while (j<10 and trigger):
		dff = dfi
		dfi += ee
		print 'i = '+str(i)+', j = '+str(j)+', df es '+'{0:.16f}'.format(dfi)
		t = True
		while t:
			x,f,df,n=0.,0.,dfi,0
			while n<N:
				if (x<xlineal):
					x,f = x + dx, f + df*dx
				elif (x>=xlineal):
					x,f,df=x+dx,f+H(x,f,df,dx)[0],df+H(x,f,df,dx)[1]
				else:
					x,f,df=x+dx,f+G(x,f,df,dx)[0],df+G(x,f,df,dx)[1]
				n+=1
			if isnan(f):
				print "se paso"
				dfi = dfi-ee
				dff = dfi-ee
				trigger = False
				if n==1:
					sys.exit("Dos NAN seguidos")
			t = False
		j+=1
	x,f,df,m=0.,0.,dff,0
	archivo = 'data.GP.%i' % (i+1)
	print archivo
	A = open(archivo,'w')
	while m<N:
		if (x<xlineal):
			x,f = x + dx, f + df*dx
		elif (x>=xlineal):
			x,f,df=x+dx,f+H(x,f,df,dx)[0],df+H(x,f,df,dx)[1]
		else:
			x,f,df=x+dx,f+G(x,f,df,dx)[0],df+G(x,f,df,dx)[1]
		A.write(str(x)+' '+str(f)+' '+str(df)+'\n')
		m+=1
	x,f,df = 0.,0.,dfi
	i+=1




options = ['yes','y','Yes','YES','si','Si','Sí','sí','yep','Yep','Y','']

if not (int(N) - N == 0):
	tmp = "yes"
	print "\nI could't create the mesh with the space step you suggested"
	print N
	tmpp = dx*int(N)
	tmp = str(raw_input ("May I use L = " + str(tmpp) + " instead? (yes,no)[yes]: "))
	if tmp in options:
		L = int(dx*N)
		N = int(N)
	else:
		sys.exit("\nFatal Error: Cannot continue if N is not an integer.\n")