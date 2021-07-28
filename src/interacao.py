from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from util_atomo import*

def mouse(botao,estado,x,y):
	if(botao==GLUT_LEFT_BUTTON):
		if(estado==GLUT_DOWN):
			print("HO HO HO")
			gluLookAt(x,y,200, 0, 0, 0, 0, 1, 0);
	glutPostRedisplay();
