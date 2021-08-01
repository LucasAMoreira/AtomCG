from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from desenho import*

'''
Script responsável pela animação da cena.

'''

# Move os elétrons por cerca de 10 segundos.
# Para fazer isso, basicamente invoca o método 'desenhaAtomo' (do script 'desenho.py')
# mudando o parâmetro i, que é usado para calcular a posição do elétron 
# (ver 'desenhaAtomo' para mais detalhes)		
def anima():
	
	tempoInicial=glutGet(GLUT_ELAPSED_TIME)
	tempoFinal=tempoInicial+10000
	tempoAtual=glutGet(GLUT_ELAPSED_TIME)
	i=0
	while (tempoAtual<tempoFinal):
		desenhaAtomo(i)
		#Quanto mais rápido i cresce, mais rápido é o movimento dos elétrons 		
		i=i+0.1
		tempoAtual=glutGet(GLUT_ELAPSED_TIME)
	tempo=0	

