from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from desenho import*
from interacao import*
	
numeroEletrons = 108	
numeroMassa = 8
	
glutInit();
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH);
glutInitWindowSize(width,length)
janela = glutCreateWindow("Atomo CG")
glutDisplayFunc(inicializa);
glutMouseFunc(mouse);
glutMainLoop()
