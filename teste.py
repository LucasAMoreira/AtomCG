from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from util_atomo import*

width=500;
length=500;

f = width/length;

a=7
j=-50


arr=[]

arr.append(cos(0)*30)
arr.append(0)
arr.append(sin(0)*50)

parada=False

def mouse(botao,estado,x,y):
	if(botao==GLUT_LEFT_BUTTON):
		if(estado==GLUT_DOWN):
			print("HO HO HO")
			gluLookAt(x,y,200, 0, 0, 0, 0, 1, 0);
	glutPostRedisplay();

class Eletron:

	def __init__(self,matriz,x,y,z):
		self.x=x;
		self.y=y;
		self.z=z;
		self.matriz=matriz;
		glColor3f(0.0,0.0,1.0)
		glTranslated(x,y,z)
		self.particula=glutSolidSphere(1.0,50,80);
		return




#Recebe como parâmetro o número de massa n e desenha um núcleo
def fazNucleo(n):
	i=0
	while i<3*n:
		glTranslated(arr[i],arr[i+1],arr[i+2]);
		glColor3f(cores[i],cores[i+1],cores[i+2])
		glutSolidSphere(4.0,50,8);									
		i=i+3
	return

#Recebe como parâmetro a matriz usada para calcular a translacao e o número de eletrons
#Retorna um arranjo de eletrons
def fazCamadaEletrons(matriz,n,k):

	i=0;
	metade=i/2
	eletrons=[]
	while i<n:
		x=(sin(k+i)*30)-(i)
		y=0
		z=(cos(k+i)*30)-(i)
		matriz		
		eletron=Eletron(matriz,x,y,z)
		eletrons.append(eletron)
		i=i+1
		metade=i/2
		
	return eletrons


def animaEletrons(eletrons,i):
	j=0
	novoseletrons=[]
	while j<len(eletrons):
		eletron=eletrons[j]
		matriz=eletron.matriz
		xantigo=eletron.x;
		zantigo=eletron.z;
		xnovo=xantigo
		znovo=zantigo
		novoeletron=Eletron(eletron.matriz,xnovo,0,znovo);
		novoseletrons.append(novoeletron)
		j=j+1
	return novoseletrons

	
def desenhaAtomo(i):
	matriz=visualizacao()
	
	nucleo=fazNucleo(7)
	matriz
	eletrons=fazCamadaEletrons(matriz,8,i)
	#eletrons=animaEletrons(eletrons,i)

	glutSwapBuffers();
	'''
	
		
	while i<len(eletrons):
		eletrons[i].particula
		i=i+1
	
	glutSwapBuffers();
	'''
'''
def anima():
	matriz=visualizacao()
	nucleo=fazNucleo(7)
	glutSwapBuffers();
	
	
	movimentaEletrons(fazCamadaEletrons(matriz,8));
	glutSwapBuffers();
	
	while i<len(eletrons):
		eletrons[i].particula
		i=i+1
	glutSwapBuffers();
'''	
	
	
def anima():
	i=0
	while (True and parada==False):
		desenhaAtomo(i)		
		i=i+0.01	
	
def movimentaEletrons(eletrons):
	i=0
	while(True):
		'''
		j=0
		while(j<len(eletrons)):
			eletrons[j].x=1#eletrons[j].x+cos(i)
			eletrons[j].z=1#eletrons[j].z+sin(i)			
			j=j+1
		'''
		j=0
		while j<len(eletrons):
			x=cos(i)*30#eletrons[j].x+cos(i)
			z=sin(i)*50#eletrons[j].z+sin(i)
			glTranslated(x,0,z)
			eletrons[j].particula
			j=j+1
		i=i+0.01
		glutSwapBuffers();

'''
def animaAtomo():
	desenhaAtomo(0)
	
	i=0
	while True:
		desenhaAtomo(i)
		i=i+0.01		
'''
def visualizacao():
	#Toda futura operação vai afetar a câmera
	glMatrixMode(GL_PROJECTION);	
	glLoadIdentity();
		
	#Perspectiva: angulo, altura, distancia corte mais perto, distancia fundo
	gluPerspective(45, f,0.1,500);
	
	#Toda futura operação vai afetar o desenho
	glMatrixMode(GL_MODELVIEW);
	matriz=glLoadIdentity();
	
	#define (x,y,z) da camera, (x,y,z) do objeto e (x,y,z) do vetor de cima da cena
	gluLookAt(0,80,200, 0, 0, 0, 0, 1, 0);
		
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
	glColor3f(1.0,0.0,0.0)

	return matriz


def inicializa():
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
	
	anima();

def posicoes(n,i):
	x=2
	y=2
	xoriginal=cos(0)*30
	yoriginal=sin(0)*50
	posicoes=[]
	i=0
	while x!=xoriginal and y!=yoriginal:
		posicoes.append(cos(i)*30)
		posicoes.append(0)
		posicoes.append(sin(i)*50)
		i=i+0.01
	return posicoes
		
arr=retornaPos(a)
cores = retornaCor(a)
	
glutInit();
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH);
glutInitWindowSize(width,length)
janela = glutCreateWindow("Atomo")
glutDisplayFunc(inicializa);
glutMouseFunc(mouse);

print(arr[20])
glutMainLoop()


