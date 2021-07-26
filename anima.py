from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from random import *
from math import *

width=500;
length=500;

f = width/length;

a=7
j=-50

i=0

def desenha():
	glutSolidSphere(20.0,50,80);
	
	
def translacao():
	i=0;
	while i<60:
		glClear(GL_COLOR_BUFFER_BIT)
		glBegin(GL_POINTS)
		glTranslate(0,0,i)
		glutSolidSphere(5.0,50,80)
		i=i+1
	i=0	
	return


def visualizacao():
	#Toda futura operação vai afetar a câmera
	glMatrixMode(GL_PROJECTION);	
	glLoadIdentity();
		
	#Perspectiva: angulo, altura, distancia corte mais perto, distancia fundo
	gluPerspective(45, f,0.1,500);
	
	#Toda futura operação vai afetar o desenho
	glMatrixMode(GL_MODELVIEW);
	glLoadIdentity();
	
	#define (x,y,z) da camera, (x,y,z) do objeto e (x,y,z) do vetor de cima da cena
	gluLookAt(0,80,200, 0, 0, 0, 0, 1, 0);
		
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
	glColor3f(1.0,0.0,0.0)

	desenha()

def anima(i):
	visualizacao()
	glTranslate(cos(i)*30,0,sin(i)*50)
	glutSolidSphere(1.0,50,80)
	glutSwapBuffers();
	i=0	

def inicializa():
	i=0
	while i<10:
		anima(i)
		i=i+0.01
	i=0
	luzAmbiente = [0.2,0.2,0.2,1.0]
	luzDifusa = [0.7,0.7,0.7,1.0]
	luzEspecular = [1.0,1.0,1.0,1.0]
	posicaoLuz = [0.0,50.0,50.0,1.0]
	
	especularidade=[1.0,1.0,1.0,1.0]; 
	especMaterial = 60;

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
	
	
glutInit();
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH);
glutInitWindowSize(width,length)
janela = glutCreateWindow("Atomo")
inicializa()
glutDisplayFunc(inicializa);
glutMainLoop()




