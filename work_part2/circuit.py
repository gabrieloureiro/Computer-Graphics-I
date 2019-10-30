from OpenGL.GL import *
from work_part1 import obj
def draw_circuit():
    #rgb_wall_material = [44/255, 137/255, 142/255]
    rgb_gramado = [50/255, 205/255, 50/255]
    rgb_folhas = [50/255, 140/255, 50/255]
    rgb_terra = [151/255,105/255,79/255]
    rgb_madeira = [92/255, 51/255, 23/255]
    rgb_ferro = [168/255, 168/255, 168/255]
    rgb_cal = [1,1,1]
    rgb_asfalto = [76/255,76/255,76/255]
    rgb_lista = [217/255, 217/255, 25/255]
    
    asfalto_material = obj.Material(rgb_asfalto, rgb_asfalto, [0.3,0.3,0.3], 10)
    gramado_material = obj.Material(rgb_gramado, rgb_gramado, [0.3,0.3,0.3], 10)
    madeira_material = obj.Material(rgb_madeira,rgb_madeira, [0.3,0.3,0.3],10)
    cal_material = obj.Material(rgb_cal,rgb_cal, [0.3,0.3,0.3],10)
    terra_material = obj.Material(rgb_terra, rgb_terra, [0.1,0.1,0.1], 10)
    ferro_material = obj.Material(rgb_ferro, rgb_ferro, [0.3,0.3,0.3], 10)
    #espelho_material = obj.Material([0.8,0.8,0.8], [0,0,0], [0.8,0.8,0.8], 20)
    
    # CHÃO
    glPushMatrix()
    glScalef(150.,0.01, 200.)
    cube = obj.Obj().import_obj('../objects/cube_vn.obj', terra_material)
    draw_polygon(cube)
    glPopMatrix()

    # Campo
    glPushMatrix()
    cube = obj.Obj().import_obj('../objects/cube_vn.obj', gramado_material)
    glTranslatef(37 ,0., 52)
    glScalef(67, 0.02, 78)
    draw_polygon(cube)
    glPopMatrix()

     # Reta Esquerda
    glPushMatrix()
    cube = obj.Obj().import_obj('../objects/cube_vn.obj', cal_material)
    glTranslatef(37 ,0., 51)
    glScalef(67, 0.1, 1)
    draw_polygon(cube)
    glPopMatrix()
    
    # Reta Direita
    glPushMatrix()
    cube = obj.Obj().import_obj('../objects/cube_vn.obj', cal_material)
    glTranslatef(37 ,0., 130)
    glScalef(67, 0.1, 1)
    draw_polygon(cube)
    glPopMatrix()

    # Reta Inferior
    glPushMatrix()
    cube = obj.Obj().import_obj('../objects/cube_vn.obj', cal_material)
    glTranslatef(37 ,0., 51)
    glScalef(0.5, 0.1, 79)
    draw_polygon(cube)
    glPopMatrix()

    # Reta Central
    glPushMatrix()
    cube = obj.Obj().import_obj('../objects/cube_vn.obj', cal_material)
    glTranslatef(67 ,0., 51)
    glScalef(0.5, 0.1, 79)
    draw_polygon(cube)
    glPopMatrix()

    # Reta Superior
    glPushMatrix()
    cube = obj.Obj().import_obj('../objects/cube_vn.obj', cal_material)
    glTranslatef(104 ,0., 51)
    glScalef(0.5, 0.1, 79)
    draw_polygon(cube)
    glPopMatrix()



    # draw_car(positionInitial=[25.,0.05,50.])
    # draw_car(positionInitial=[53.,0.6,53.])
    draw_carUp()
    draw_carDown()
    draw_carUpEntry()
    # draw_car(color=[0.,0.,1], positionInitial=[57.,0.6,52.])
    # draw_car(positionInitial=[53.,0.6,53.])
    # draw_car(color=[0.,1.,0], positionInitial=[61.,0.6,54.])#x y z


    # Arquibancada:
    glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT, [0.1,0.05,0.05])
    glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, [0.8,0.8,0.8])
    glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, [0.7,0.7,0.7])
    glMaterialf(GL_FRONT_AND_BACK, GL_SHININESS, 3)
    glPushMatrix()
    glTranslatef(68, 0.05, 20)
    glScalef(2.5,1,2.5)
    objeto('objetos/grandstand.obj')
    glPopMatrix()

    #Asfalto
    glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT, rgb_asfalto)
    glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, rgb_asfalto)
    glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, rgb_asfalto)
    glMaterialf(GL_FRONT_AND_BACK, GL_SHININESS, 3)
    glPushMatrix()
    glTranslatef(22, 0.05, 110)
    glScalef(2.7,0.02,30)
    objeto('objetos/road.obj')
    glPopMatrix()

    #Linha do asfalto
    glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT, rgb_lista)
    glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, rgb_lista)
    glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, rgb_lista)
    glMaterialf(GL_FRONT_AND_BACK, GL_SHININESS, 3)
    glPushMatrix()
    glTranslatef(22, 0.05, 110)
    glScalef(0.2,0.05,30)
    objeto('objetos/road.obj')
    glPopMatrix()

    #Canteiro inferior
    glPushMatrix()
    glTranslatef(17, 1, 1)
    glScalef(1, 1, 180)
    cube = obj.Obj().import_obj('../objects/cube_vn.obj', ferro_material)
    draw_polygon(cube)
    glPopMatrix()

    #Canteiro superior
    glPushMatrix()
    glTranslatef(28, 1, 1)
    glScalef(1, 1, 130)
    cube = obj.Obj().import_obj('../objects/cube_vn.obj', ferro_material)
    draw_polygon(cube)
    glPopMatrix()

    #Folhas Arvore:
    glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT, rgb_folhas)
    glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, rgb_folhas)
    glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, rgb_folhas)
    glMaterialf(GL_FRONT_AND_BACK, GL_SHININESS, 3)
    glPushMatrix()
    glTranslatef(106, 0.1, 20)
    glScalef(1,0.5,1.5)
    objeto('objetos/MapleTreeLeaves.obj')
    glPopMatrix()

    # Caule Arvore:
    glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT, rgb_madeira)
    glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, rgb_madeira)
    glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, rgb_madeira)
    glMaterialf(GL_FRONT_AND_BACK, GL_SHININESS, 3)
    glPushMatrix()
    glTranslatef(106, 0.1, 20)
    glScalef(1,0.5,1.5)
    objeto('objetos/MapleTreeStem.obj')
    glPopMatrix()

    #Folhas Arvore2:
    glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT, rgb_folhas)
    glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, rgb_folhas)
    glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, rgb_folhas)
    glMaterialf(GL_FRONT_AND_BACK, GL_SHININESS, 3)
    glPushMatrix()
    glTranslatef(106, 0.1, 150)
    glScalef(1,0.5,1.5)
    objeto('objetos/MapleTreeLeaves.obj')
    glPopMatrix()

    # Caule Arvore2:
    glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT, rgb_madeira)
    glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, rgb_madeira)
    glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, rgb_madeira)
    glMaterialf(GL_FRONT_AND_BACK, GL_SHININESS, 3)
    glPushMatrix()
    glTranslatef(106, 0.1, 150)
    glScalef(1,0.5,1.5)
    objeto('objetos/MapleTreeStem.obj')
    glPopMatrix()

    #Cerca
    glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT, rgb_asfalto)
    glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, rgb_asfalto)
    glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, rgb_asfalto)
    glMaterialf(GL_FRONT_AND_BACK, GL_SHININESS, 3)
    glPushMatrix()
    glTranslatef(116, 0.03, 199)
    glScalef(10.7,1,10)
    #glRotatef(90,0,1,0)
    objeto('objetos/fance.obj')
    glPopMatrix()

    #Torre de madeira
    glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT, rgb_madeira)
    glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, rgb_madeira)
    glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, rgb_madeira)
    glMaterialf(GL_FRONT_AND_BACK, GL_SHININESS, 3)
    glPushMatrix()
    glTranslatef(77, 0.1, 150)
    glScalef(2,2,3)
    objeto('objetos/wooden_watch_tower2.obj')
    glPopMatrix()

    # #Bancos:
    # glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT, rgb_terra)
    # glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, rgb_terra)
    # glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, rgb_terra)
    # glMaterialf(GL_FRONT_AND_BACK, GL_SHININESS, 1)
    # glPushMatrix()
    # glTranslatef(68, 0.1, 130)
    # glScalef(0.02,0.02,0.07)
    # glRotatef(180,0,1,0)
    # objeto('objetos/Bench_HighRes.obj')
    # glPopMatrix()


    # Criando traves
    
    ##TRAVE TIME A VERTICAL ESQUERDA
    glPushMatrix()
    glTranslatef(40, 0, 75)
    glScalef(1, 5, 1)
    cube = obj.Obj().import_obj('../objects/cube_vn.obj', ferro_material)
    draw_polygon(cube)
    glPopMatrix()

    ##TRAVE TIME A VERTICAL DIREITA
    glPushMatrix()
    glTranslatef(40, 0, 105)
    glScalef(1, 5, 1)
    cube = obj.Obj().import_obj('../objects/cube_vn.obj', ferro_material)
    draw_polygon(cube)
    glPopMatrix()

    ##TRAVE TIME A HORIZONTAL
    glPushMatrix()
    glTranslatef(40, 5, 75)
    glScalef(1, 1, 31)
    cube = obj.Obj().import_obj('../objects/cube_vn.obj', ferro_material)
    draw_polygon(cube)
    glPopMatrix()


    ##TRAVE TIME B VERTICAL ESQUERDA
    glPushMatrix()
    glTranslatef(100, 0, 75)
    glScalef(1, 5, 1)
    cube = obj.Obj().import_obj('../objects/cube_vn.obj', ferro_material)
    draw_polygon(cube)
    glPopMatrix()

    ##TRAVE TIME A VERTICAL DIREITA
    glPushMatrix()
    glTranslatef(100, 0, 105)
    glScalef(1, 5, 1)
    cube = obj.Obj().import_obj('../objects/cube_vn.obj', ferro_material)
    draw_polygon(cube)
    glPopMatrix()

    ##TRAVE TIME A HORIZONTAL
    glPushMatrix()
    glTranslatef(100, 5, 75)
    glScalef(1, 1, 31)
    cube = obj.Obj().import_obj('../objects/cube_vn.obj', ferro_material)
    draw_polygon(cube)
    glPopMatrix()


    # # Tampo do Poste:
    # glPushMatrix()
    # glTranslatef(75., 11.06, 59.5)
    # glScalef(5, 0.05, 5)
    # cube = obj.Obj().import_obj('../objects/cube_vn.obj', espelho_material)
    # draw_polygon(cube)
    # glPopMatrix()
def draw_carUpEntry(color=[0,0,1], positionInitial=[30.,0.5,160.]):
    glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT, color)
    glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, color)
    glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, color)
    glMaterialf(GL_FRONT_AND_BACK, GL_SHININESS, 3)
    glPushMatrix()
    glTranslatef(positionInitial[0], positionInitial[1], positionInitial[2])
    glScalef(1.8,1,5)
    glMatrixMode(GL_MODELVIEW);
    glRotatef(230,0,1,0)
    objeto('objetos/ferrari.obj')
    glPopMatrix()

def draw_carUp(color=[0,1,0], positionInitial=[25.,0.5,70.]):
    glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT, color)
    glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, color)
    glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, color)
    glMaterialf(GL_FRONT_AND_BACK, GL_SHININESS, 3)
    glPushMatrix()
    glTranslatef(positionInitial[0], positionInitial[1], positionInitial[2])
    glScalef(1.8,1,5)
    glMatrixMode(GL_MODELVIEW);
    glRotatef(180,0,1,0)
    objeto('objetos/ferrari.obj')
    glPopMatrix()
    
def draw_carDown(color=[1,0,0], positionInitial=[20,0.5,30.]):
    glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT, color)
    glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, color)
    glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, color)
    glMaterialf(GL_FRONT_AND_BACK, GL_SHININESS, 3)
    glPushMatrix()
    glTranslatef(positionInitial[0], positionInitial[1], positionInitial[2])
    glScalef(1.4,1,5)
    glMatrixMode(GL_MODELVIEW);
    #glRotatef(180,0,1,0)
    objeto('objetos/ferrari.obj')
    glPopMatrix()

def draw_polygon(obj):
    for face in obj.faces:
        glMaterialfv(GL_FRONT, GL_AMBIENT, face.material.k_a_rgb)
        glMaterialfv(GL_FRONT, GL_DIFFUSE, face.material.k_d_rgb)
        glMaterialfv(GL_FRONT, GL_SPECULAR, face.material.k_e_rgb)
        glMaterialf(GL_FRONT, GL_SHININESS, face.material.attenuation)

        glBegin(GL_POLYGON)
        for vertex in face.vertices:
            glNormal3fv(vertex.normal)
            glVertex3fv(vertex.coordinates[:3])
        glEnd()


def draw_unitTriangle(material):
    #color = (0.6,0,0)

    glMaterialfv(GL_FRONT, GL_AMBIENT, material.k_a_rgb)
    glMaterialfv(GL_FRONT, GL_DIFFUSE, material.k_d_rgb)
    glMaterialfv(GL_FRONT, GL_SPECULAR, material.k_e_rgb)
    glMaterialf(GL_FRONT, GL_SHININESS, material.attenuation)
    
    vertices = (
        (0,0,0),
        (0,0,1),
        (1,0,0),
        (0,1,0)
    )

    faces = (
        (0,1,3),
        (0,3,2),
        (0,2,1),
        (1,2,3)
    )


    glBegin(GL_TRIANGLES)
    for face in faces:
        for vertex in face:
            glVertex3fv(vertices[vertex])
    
    glEnd()
    
   

def converte(valor):
    return int(valor[0:valor.find('/')])

def objeto(path, cor=None):
    if cor is None: 
        cor = (0.6, 0.6, 0.6)
    
    vertices = []
    faces_triangulares = []
    faces_quadriculares = []

    with open(path) as meu_arquivo:
        
        for linha in meu_arquivo:
            valores = linha.split()

            if len(valores) == 4 and valores[0] == 'v':
                vertices.append((float(valores[1]), float(valores[2]), float(valores[3])))
            
            elif len(valores) == 4 and valores[0] == 'f':
                v1 = converte(valores[1]) - 1
                v2 = converte(valores[2]) - 1
                v3 = converte(valores[3]) - 1
                faces_triangulares.append((v1, v2, v3))

            elif len(valores) == 5 and valores[0] == 'f':
                v1 = converte(valores[1]) - 1
                v2 = converte(valores[2]) - 1
                v3 = converte(valores[3]) - 1
                v4 = converte(valores[4]) - 1
                faces_quadriculares.append((v1, v2, v3, v4))

    vertices = tuple(vertices)
    faces_triangulares = tuple(faces_triangulares)
    faces_quadriculares = tuple(faces_quadriculares)

    glBegin(GL_TRIANGLES)
    for face in faces_triangulares:
        #glColor3fv(cor)
        for vertice in face:
            glVertex3fv(vertices[vertice])
    glEnd()
    
    glBegin(GL_QUADS)
    for face in faces_quadriculares:
        #glColor3fv(cor)
        for vertice in face:
            glVertex3fv(vertices[vertice])
    glEnd()
