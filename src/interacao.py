from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from util_atomo import*
from desenho import *
from anima import*

'''

Este Script possui tudo o que é relacionado à interação com o usuário
(no caso apenas a função 'mouse')

'''

# Caso o usuário clique na cena com o botão direito do mouse,
# a função 'anima' (do script 'anima.py') será invocada,
# animando os elétrons
def mouse(botao,estado,x,y):

	if(botao==GLUT_RIGHT_BUTTON):
		if(estado==GLUT_DOWN):
			anima()
			
	glutPostRedisplay();	



