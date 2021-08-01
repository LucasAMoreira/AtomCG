from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from util_atomo import*

'''
Script com rotinas responsáveis por:
	- desenhar o átomo
	- Posicionar observador
	- Iluminar cena
'''



# -------------------------
# -------------------------

numeroMassa=40
numeroEletrons=10

# -------------------------
# -------------------------


# Tamanho da janela
width=500;
length=500;

f = width/length;

angulo=30

# retorna arranjo de combinações de cores
coresc=retornaCor(numeroEletrons)
cores = retornaCor(numeroMassa) 

# retorna arranjo com posições dos elementos do núcleo
arr=retornaPos(numeroMassa)

# Classe Eletron. 
# Seu construtor recebe como parâmetro as coordenadas para translada-lo.
# Usa o método do OpenGL 'glutSolidSphere',
class Eletron:

	def __init__(self,x,y,z):
		self.x=x;
		self.y=y;
		self.z=z;
		
		glTranslated(x,y,z)
		self.particula=glutSolidSphere(1.0,50,80);
		return


#Recebe como parâmetro o número de massa n e desenha um núcleo
def fazNucleo(n):
	i=0
	while i<3*n:
		matrizesOriginais()
		glTranslated(arr[i],arr[i+1],arr[i+2]);
		#glColor3f(cores[i],cores[i+1],cores[i+2])
		glColor3f(1.0,0.0,0.0)
		glutSolidSphere(3.0,50,8);
		#esfera(n)									
		i=i+3
	matrizesOriginais()
	return

#Recebe como parâmetro o número de eletrons e um número K representando o deslocamento deles
#Retorna um arranjo de eletrons
def fazCamadaEletrons(n,k):

	i=0;
	j=0;
	eletrons=[]
	
	camadas = retornaCamadas(n)
	
	while j<len(camadas):
		distancia=20+(j*5)
		
		while i<camadas[j]:
			glColor(coresc[j],coresc[(j)+1],coresc[(j)+2])
		
			# Define coordenadas do eletron atual
			rad=(2*pi)/camadas[j]		
			x = (sin((rad*i)+k+j)*distancia)
			y = 1
			z = (cos((rad*i)+k+j)*distancia)
			
			#Rotacionamos algumas camadas para elas transladarem em volta do núcleo
			#de forma diferente das demais camadas
			if j%2==0:
				glRotate(45,1.0,0.0,0.0)
			
			if j%2==1:
				glRotate(15,1.0,0.0,0.0)	
			# Cria eletron							 
			eletron=Eletron(x,y,z)	
			
			# Adiciona eletron no arranjo eletrons				
			eletrons.append(eletron)
			
			# Limpa matriz (Para a rotação dos eletrons ficar correta)
			matrizesOriginais()
			i=i+1
		matrizesOriginais()
		i=0
		j=j+1
		
	return eletrons



# Desenha o átomo
# Recebe como parâmetro um número i que será usado para
# calcular a posição do elétron	
def desenhaAtomo(i):
	visualizacao()
	
	nucleo=fazNucleo(numeroMassa)
	
	eletrons=fazCamadaEletrons(numeroEletrons,i)

	glutSwapBuffers();

	
# Inicializa matriz de projeção 
def visualizacao():
	# Inicializa matriz de projeção
	glMatrixMode(GL_PROJECTION);	
	glLoadIdentity();
	# Limpa buffer de cores	
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
	
# Inicializa matriz do modelo
# Define posições na cena
def matrizesOriginais():	
		
	#Perspectiva: angulo, altura, distancia corte mais perto, distancia fundo
	gluPerspective(angulo, f,0.4,400);
	
	#Toda futura operação vai afetar o desenho -> GL_MODELVIEW
	glMatrixMode(GL_MODELVIEW);
	glLoadIdentity();
	
	#define (x,y,z) da camera, (x,y,z) do objeto e (x,y,z) do vetor de cima da cena
	gluLookAt(0,80,200, 0, 0, 0, 0, 1, 0);
	
	
# Baseado no método 'inicializa' do tutorial "Utilizando luzes"
# Disponível em: https://www.inf.pucrs.br/~manssour/OpenGL/Iluminacao.html
def inicializa():
	
	luzAmbiente = [0.2,0.2,0.2,1.0]
	luzDifusa = [0.7,0.7,0.7,1.0]
	luzEspecular = [1.0,1.0,1.0,1.0]
	posicaoLuz = [0.0,50.0,50.0,1.0]
	
	especularidade=[1.0,1.0,1.0,1.0]; 
	especMaterial = 60;
		
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
	
		
	desenhaAtomo(0)



