from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

# QUAL é o TAMANHO dos POLÍGONOS?
	
def esfera(n):
	glMatrixMode(GL_PROJECTION)
	i=0
	d=0.25
	f=0.5
	x=0.0
	y=0.0
	z=0.0
	while i<n:
		x=x*i
		y=y*i
		z=z*i
		glLoadIdentity()
		glBegin(GL_POLYGON)
		glVertex3f(x,y,z)
		glVertex3f(x+d,y+d,z+d)
		glVertex3f(x+f,y+f,z+f)
		glEnd();
		i=i+1
		
def inicio():
	glColor3f(1.0,0.0,0.0)
	esfera(2)	
	glutSwapBuffers()
	
glutInit();
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH);
glutInitWindowSize(500,500)
janela = glutCreateWindow("Atomo CG")
glutDisplayFunc(inicio);
glutMainLoop()
