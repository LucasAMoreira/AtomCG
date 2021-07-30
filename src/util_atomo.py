from random import *
from math import *

width=500;
length=500;

f = width/length;

a=7
j=-50
'''
def retornaPos(n):
	posicoes =[]
	i=1
	# Talvez imaginar como uma matriz 3D
	while i<=n:
		
		posicoes.append(-1);
		posicoes.append(-1);
		posicoes.append(0);
		
		
		if n%i==0:
			posicoes.append(c);
			posicoes.append(sin(i)*i);
			posicoes.append(0-i);
		if n%i==1:
			posicoes.append(5);
			posicoes.append(5);
			posicoes.append(5);
		if n%i==2:
			posicoes.append(0);
			posicoes.append(5);
			posicoes.append(5);
		if n%i==3:
			posicoes.append(10);
			posicoes.append(10);
			posicoes.append(10); 
		
		i=i+1
	return posicoes
'''


'''
def retornaPos(n):
	posicoes = []
	x=n/2
	i=0	
	while i<n:
		if(i<n/3):
			posicoes.append(i*4-x)
			posicoes.append(0)
			posicoes.append(0)
		if(i>=n/3 and i<2*n/3):
			posicoes.append((i-n/3)*4-x)
			posicoes.append(4)
			posicoes.append(0)
		if(i>=2*n/3):
			posicoes.append((i-2*n/3)*4-x)
			posicoes.append(8)
			posicoes.append(0)
		i=i+1
	return posicoes
'''

def retornaPos(n):
	posicoes =[]
	i=0
	while i<n:
		posicoes.append(cos(i)*i);
		posicoes.append(sin(i)*i);
		posicoes.append(randint(floor(-n),floor(n)));
		i=i+1
	return posicoes



	
# Recebe númeron n 
# Retorna n combinações Float de cores
def retornaCor(n):
	arr =[]
	i=0
	while i<3*n:
		arr.append(random());
		i=i+1
	return arr
	
# Recebe o número de elétrons do átomo	
# Retorna arranjo com o número de eletrons em cada camada
def retornaCamadas(n):
	
	numEletrons = [0,0,0,0,0,0,0]
	
	i=0
	while i<n:
		if i<2:# Camada K (máx 2)
			numEletrons[0]=numEletrons[0]+1
		if i>=2 and i<10:# Camada L (máx 8)
			numEletrons[1]=numEletrons[1]+1
		if i>=10 and i<26:# Camada M (máx 18)
			numEletrons[2]=numEletrons[2]+1
		if i>=26 and i<50:# Camada N (máx 32)
			numEletrons[3]=numEletrons[3]+1
			
		if i>=50 and i<82:# Camada O (máx 32)
			numEletrons[4]=numEletrons[4]+1
		if i>=82 and i<100:# Camada P (máx 18)
			numEletrons[5]=numEletrons[5]+1
		if i>=100 and i<108:# Camada Q (máx 8)
			numEletrons[6]=numEletrons[6]+1	
		
		i=i+1
	return numEletrons;

		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
