#!/usr/bin/
# -*- coding: utf-8 -*-

#Field expressions:

import math

def Asym0(): 
	return lambda q,v,x: 0.
def AsymInf():
	return lambda q,v,x: q*q*q - q
def GP():
	return lambda q,v,x: -(v/x + q) + q/(x*x) + q*q*q

f=Asym0()
g=GP()
h=0.01

n=0.
N = 10.
i=0
ee = 1.
df = 0.
while i<16:
	j=0
	ee = ee*0.1
	t=True
	n=0.
	while (t and n<N):
		n+=1
		if (0.1*math.pi-df) < 0:
			print "se paso"
			df = df-ee
			t=False
		else : df += ee
		print df
		j+=1
	i+=1

while n<500.:
	x=0.001+n*h
#	print x,f(0.99,1.,x)-g(0.99,1.,x),f(0.99,1.,x),g(0.99,1.,x)
	n+=1