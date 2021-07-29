from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from util_atomo import*
from desenho import *

def mouse(botao,estado,x,y):
	if(botao==GLUT_LEFT_BUTTON):
		if(estado==GLUT_DOWN):
			gluLookAt(50,80,200, x, y, 0, 0, 1, 0);
	if(botao==GLUT_RIGHT_BUTTON):
		if(estado==GLUT_DOWN):
			anima()
	glutPostRedisplay();
