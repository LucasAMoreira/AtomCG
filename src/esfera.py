from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from math import *

# QUAL é o TAMANHO dos POLÍGONOS?

'''	
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
		glBegin()
		glVertex3f(x,y,z)
		glVertex3f(x+d,y+d,z+d)
		glVertex3f(x+f,y+f,z+f)
		glEnd();
		i=i+1
'''

def visualizacao():
	#Toda futura operação vai afetar a câmera
	matriz=glMatrixMode(GL_PROJECTION);	
	glLoadIdentity();
		
	#Perspectiva: angulo, altura, distancia corte mais perto, distancia fundo
	gluPerspective(45, 1,0.1,500);
	
	#Toda futura operação vai afetar o desenho -> GL_MODELVIEW
	glMatrixMode(GL_MODELVIEW);
	glLoadIdentity();
	
	#define (x,y,z) da camera, (x,y,z) do objeto e (x,y,z) do vetor de cima da cena
	gluLookAt(0,80,200, 0, 0, 0, 0, 1, 0);
		
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

def esfera(n):
	i=0
	maximo=2*pi
	zoom=30

	glBegin(GL_POLYGON)
	while i<maximo:
		x=cos(i)*zoom
		y=sin(i)*zoom
		z=0.0		
		glVertex3f(x,y,z)
		glVertex3f(z,y,x)
		glVertex3f(y,z,x)						
		i=i+0.10
	glEnd();
	'''
	glVertex3f(cos(0.25)/2,sin(0.25)/2,0.0)
	glVertex3f(cos(0.50)/2,sin(0.50)/2,0.0)
	glVertex3f(cos(0.75)/2,sin(0.75)/2,0.0)
	'''
	
		
def inicio():

	visualizacao()

	luzAmbiente = [0.2,0.2,0.2,1.0]
	luzDifusa = [0.7,0.7,0.7,1.0]
	luzEspecular = [1.0,1.0,1.0,1.0]
	posicaoLuz = [0.0,50.0,50.0,1.0]
	
	especularidade=[1.0,1.0,1.0,1.0]; 
	especMaterial = 100;

	# Cor de fundo
	glClearColor(0.0, 0.0, 0.0, 1.0)
		
	glShadeModel(GL_SMOOTH);

	glMaterialfv(GL_FRONT,GL_SPECULAR, especularidade);

	glMateriali(GL_FRONT,GL_SHININESS,especMaterial);

	glLightModelfv(GL_LIGHT_MODEL_AMBIENT, luzAmbiente);

	glLightfv(GL_LIGHT0, GL_AMBIENT, luzAmbiente); 
	glLightfv(GL_LIGHT0, GL_DIFFUSE, luzDifusa );
	glLightfv(GL_LIGHT0, GL_SPECULAR, luzEspecular );
	glLightfv(GL_LIGHT0, GL_POSITION, posicaoLuz );

	#Habilita a definição da cor do material a partir da cor corrente
	glEnable(GL_COLOR_MATERIAL);
	#Habilita o uso de iluminação
	glEnable(GL_LIGHTING);  
	# Habilita a luz de número 0
	glEnable(GL_LIGHT0);
	# Habilita o depth-buffering
	glEnable(GL_DEPTH_TEST);
	
	

	glColor3f(0.0,1.0,0.0)
	esfera(2)	
	glutSwapBuffers()

glutInit();
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH);
glutInitWindowSize(500,500)
janela = glutCreateWindow("Atomo CG")
glutDisplayFunc(inicio);
glutMainLoop()


