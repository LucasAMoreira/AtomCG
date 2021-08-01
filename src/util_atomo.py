from random import *
from math import *

'''
Este script possui rotinas auxiliares para o script desenho.py, como:

	- Retornar coordenadas para o núcleo (retornaPos)
	- Retornar arranjo de cores para os elétrons (retornaCor)
	- Retornar como os elétrons são distribuídos nas camadas (retornaCamadas)

'''

# Retorna arranjo com posições dos elementos do núcleo
# Retorna um arranjo 3 vezes maior que o número de elementos
# Outra solução possível seria retornar uma matriz nX3

def retornaPos(n):
	arr =[]
	
	if(n==15):
		# Interno  centro  trás  frente  direita esquerda cima   baixo
		posicoes=[0,0,0, 0,0,-4, 0,0,4, 5,0,0, -5,0,0,  0,5,0, 0,-5,0]
		# diagonais da esquerda
		posicoes=posicoes+[-3,-3,-3,  -3,-3,3, -3,3,3, -3,3,-3]
		# diagonais da direita
		posicoes=posicoes+[ 3,-3,-3,  3,-3,3, 3,3,3, 3,3,-3 ]
		return posicoes
	
	i=0
	while i<3*n:
		arr.append(randint(floor(-n/4),floor(n/4)));
		i=i+1
	return arr
	
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

		
		
		

