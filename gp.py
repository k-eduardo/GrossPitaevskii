#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

dx = 0.1
dt = 0.1
L = 400
N = L/dx







options = ['yes','y','Yes','YES','si','Si','Sí','sí','yep','Yep','Y','']

if not (int(N) - N == 0):
	tmp = "yes"
	print "\nI could't divide the mesh with the space step you suggested"
	print N
	tmpp = dx*int(N)
	print tmpp
	tmp = str(raw_input ("May I use L = " + str(tmpp) + " instead? (yes,no)[yes] "))
	if tmp in options:
		L = int(dx*N)
		N = int(N)
	else:
		sys.exit("\nFatal Error: Cannot continue if N is not an integer.\n")
