from random import *
from math import *

width=500;
length=500;

f = width/length;

a=7
j=-50


def retornaPos(n):
	arr =[]
	i=0
	while i<3*n:
		arr.append(randint(floor(-n/4),floor(n/4)));
		i=i+1
	return arr
	
def retornaCor(n):
	arr =[]
	i=0
	while i<3*n:
		arr.append(random());
		i=i+1
	return arr


