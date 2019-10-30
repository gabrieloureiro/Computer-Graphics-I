from OpenGL.GL import *
from OpenGL.GLU import *
from PyQt5.QtWidgets import QOpenGLWidget
from circuit import draw_circuit
#from scenario.scenario import

class GLWidget(QOpenGLWidget):
    def __init__(self, parent=None):
        super(GLWidget, self).__init__(parent)


    def initializeGL(self):
        glClearColor(25/255, 25/255, 122/255, 1) # cor de background        
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_NORMALIZE)
        glEnable(GL_LIGHTING)

        #### Luz Principal ####
        '''
        glEnable(GL_LIGHT0)
        glLightfv(GL_LIGHT0, GL_AMBIENT, [0.9, 0.9, 0.9, 1.0])
        glLightfv(GL_LIGHT0, GL_DIFFUSE, [0.7, 0.7, 0.7, 1.0])
        glLightfv(GL_LIGHT0, GL_SPECULAR, [1., 1., 1., 1.0])
        glLightfv(GL_LIGHT0, GL_POSITION, [76.5, 11, 55, 1.0])
        '''
        
        glEnable(GL_LIGHT0)
        glLightfv(GL_LIGHT0, GL_AMBIENT, [0.9, 0.9, 0.9, 1.0])
        glLightfv(GL_LIGHT0, GL_DIFFUSE, [0.7, 0.7, 0.7, 1.0])
        glLightfv(GL_LIGHT0, GL_SPECULAR, [1., 1., 1., 1.0])
        glLightfv(GL_LIGHT0, GL_POSITION, [76.5, 11, 55, 1.0])

        #######################

        
        ######## Luz Spotlight #######

        # posicao da luz pontual inicial
        glLightfv(GL_LIGHT0, GL_POSITION, [60, 11, 40, 1.0]);#[76.5, 11, 55.5, 1.0] posicao da luz pontual inicial
        glLightfv(GL_LIGHT0, GL_SPOT_DIRECTION, [68, 0.05, 45]) # [40,4,51]); #direcao da spotlight
        glLightf(GL_LIGHT0, GL_SPOT_EXPONENT, 0); #concentracao da luz, maior abre mais
        glLightf(GL_LIGHT0, GL_SPOT_CUTOFF, 90); # angulo de iluminaçao da spotlight
        glEnable(GL_LIGHTING);
        glEnable(GL_LIGHT0);
        
        
        ###############
        
        '''
        glPushMatrix()
        
        glLightfv(GL_LIGHT0, GL_POSITION,  [76.5, 11, 55.5,0, 0] )
        glLightfv(GL_LIGHT0, GL_AMBIENT, [1, 1, 1, 1])
        glLightfv(GL_LIGHT0, GL_DIFFUSE, [1, 1, 1, 1])
        glLightfv(GL_LIGHT0, GL_SPECULAR, [1.,1., 1., 1.0])
        glEnable(GL_LIGHT0)

        glLightf(GL_LIGHT0, GL_SPOT_CUTOFF, 60); # angulo de abertura
        glLightfv(GL_LIGHT0, GL_SPOT_DIRECTION, (0, 0, -1, 0)) # direção 
        glLightf(GL_LIGHT0, GL_SPOT_EXPONENT, 30) # força de foco
        glPopMatrix()
        '''
        
        glLightModelfv(GL_LIGHT_MODEL_AMBIENT, [0.1, 0.1, 0.1])
        glEnable(GL_CULL_FACE) #Habilitado o Back Face Culling
        glFrontFace(GL_CCW)
        glShadeModel(GL_SMOOTH)


    def resizeGL(self, width, height):
        glViewport(0, 0, width, height)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        
        '''Projeção Perspectiva'''
        #gluPerspective(20, width / height, 0.5, 100)
        
        '''Projeção Ortogonal'''
        #glOrtho(-15, 15, -2, 15, 5, 80)
        
        '''Projeção Obliqua e Paralelas'''
        glFrustum(-35, 50, -6, 8, 5, 60) #xmin, xmax,ymin,ymax,near,far
        #gluPerspective(45, (width/height), 5, 60)

        
        
        '''VISTAS '''
        '''Vista Proxima Entrada Circuito'''
        gluLookAt(37,37,50, 50,0,50, 0,1,0)#gabriel
        #gluLookAt(35,20,51, 55,1,54, 0,1,0)
        '''Vista Superior'''
        #gluLookAt(40,85,60, 50,5,50, 0,1,0)
        '''Vista Arquibancada'''
        #gluLookAt(68,4,40, 65,0.1,100, 0,3,2)

    def paintGL(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

        draw_circuit()

        
  
       