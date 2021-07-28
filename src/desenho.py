from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from util_atomo import*

width=500;
length=500;

f = width/length;

a=7
j=-50

'''
arr=[]
arr.append(cos(0)*30)
arr.append(0)
arr.append(sin(0)*50)
'''

parada=False


class Eletron:

	def __init__(self,x,y,z):
		self.x=x;
		self.y=y;
		self.z=z;
		
		glTranslated(x,y,z)
		self.particula=glutSolidSphere(1.0,50,80);
		return

	def translada(x,y,z):
		glColor3f(0.0,0.0,1.0)
		glTranslated(x,y,z)
		self.particula=glutSolidSphere(1.0,50,80);



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
def fazCamadaEletrons(n,k):

	i=0;
	eletrons=[]
	while i<n:
		'''
		#define coordenadas
		x=(sin(k+i)*30)-3*(i*sin(k))
		y=0
		z=(cos(k+i)*30)-3*(i*cos(k))
		'''
		
		rad=(2*pi)/n
		
		x=(sin((rad*i)+k)*30)-3*(i*sin(k))
		y=0
		z=(cos((rad*i)+k)*30)-3*(i*cos(k))
				
		
		#matriz identidade
		#matriz=glLoadIdentity();
		
		#Cria eletron
		glColor3f(0.0,0.0,1.0)
					 
		eletron=Eletron(x,y,z)	
		
		# Adiciona eletron no arranjo eletrons				
		eletrons.append(eletron)
		i=i+1
		
	return eletrons




	
def desenhaAtomo(i):
	visualizacao()
	
	nucleo=fazNucleo(7)
	
	eletrons=fazCamadaEletrons(3,i)
	#eletrons=animaEletrons(eletrons,i)

	glutSwapBuffers();

		
def anima():
	i=0
	while (True and parada==False):
		desenhaAtomo(i)		
		i=i+0.01	
	

def visualizacao():
	#Toda futura operação vai afetar a câmera
	matriz=glMatrixMode(GL_PROJECTION);	
	glLoadIdentity();
		
	#Perspectiva: angulo, altura, distancia corte mais perto, distancia fundo
	gluPerspective(45, f,0.1,500);
	
	#Toda futura operação vai afetar o desenho -> GL_MODELVIEW
	glMatrixMode(GL_MODELVIEW);
	glLoadIdentity();
	
	#define (x,y,z) da camera, (x,y,z) do objeto e (x,y,z) do vetor de cima da cena
	gluLookAt(0,80,200, 0, 0, 0, 0, 1, 0);
		
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
	glColor3f(1.0,0.0,0.0)

	

	

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

		
arr=retornaPos(a)
cores = retornaCor(a)

print("OOOOOOOPA")
print(cos(6.28))


