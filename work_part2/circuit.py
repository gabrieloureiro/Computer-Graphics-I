from OpenGL.GL import *
from work_part1 import obj
def draw_circuit():
    #rgb_wall_material = [44/255, 137/255, 142/255]
    rgb_gramado = [50/255, 205/255, 50/255]
    rgb_folhas = [50/255, 140/255, 50/255]
    rgb_terra = [107/255,66/255,38/255]
    rgb_ferro = [168/255, 168/255, 168/255]
    rgb_campo = [1,1,1]
    gramado_material = obj.Material(rgb_gramado, rgb_gramado, [0.3,0.3,0.3], 10)
    campo_material = obj.Material(rgb_campo,rgb_campo, [0.3,0.3,0.3],10)
    caminho_material = obj.Material(rgb_terra, rgb_terra, [0.3,0.3,0.3], 10)
    ferro_material = obj.Material(rgb_ferro, rgb_ferro, [0.3,0.3,0.3], 10)
    #espelho_material = obj.Material([0.8,0.8,0.8], [0,0,0], [0.8,0.8,0.8], 20)
    
    # CHÃO
    glPushMatrix()
    glScalef(150.,0.01, 150.)
    cube = obj.Obj().import_obj('../objects/cube_vn.obj', gramado_material)
    draw_polygon(cube)
    glPopMatrix()

     # Reta Esquerda
    glPushMatrix()
    cube = obj.Obj().import_obj('../objects/cube_vn.obj', campo_material)
    glTranslatef(37 ,0., 51)
    glScalef(67, 0.5, 0.5)
    draw_polygon(cube)
    glPopMatrix()
    
    # Reta Direita
    glPushMatrix()
    cube = obj.Obj().import_obj('../objects/cube_vn.obj', campo_material)
    glTranslatef(37 ,0., 130)
    glScalef(67, 0.5, 0.5)
    draw_polygon(cube)
    glPopMatrix()

    # Reta Inferior
    glPushMatrix()
    cube = obj.Obj().import_obj('../objects/cube_vn.obj', campo_material)
    glTranslatef(37 ,0., 51)
    glScalef(0.5, 0.5, 79)
    draw_polygon(cube)
    glPopMatrix()

    # Reta Central
    glPushMatrix()
    cube = obj.Obj().import_obj('../objects/cube_vn.obj', campo_material)
    glTranslatef(67 ,0., 51)
    glScalef(0.5, 0.5, 79)
    draw_polygon(cube)
    glPopMatrix()

    # Reta Superior
    glPushMatrix()
    cube = obj.Obj().import_obj('../objects/cube_vn.obj', campo_material)
    glTranslatef(104 ,0., 51)
    glScalef(0.5, 0.5, 79)
    draw_polygon(cube)
    glPopMatrix()

    # draw_goalVertical(positionInitial=[53.,5,57])
    # draw_goalHorizontal(positionInitial=[53.,5,56.5])
    # draw_goalVertical(positionInitial=[53.,5,140])

    # draw_car(positionInitial=[53.,0.6,53.])
    # draw_car(color=[0.,0.,1], positionInitial=[57.,0.6,52.])
    # draw_car(positionInitial=[53.,0.6,53.])
    # draw_car(color=[0.,1.,0], positionInitial=[61.,0.6,54.])#x y z


    # Arquibancada:
    glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT, [0.1,0.05,0.05])
    glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, [0.8,0.8,0.8])
    glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, [0.7,0.7,0.7])
    glMaterialf(GL_FRONT_AND_BACK, GL_SHININESS, 3)
    glPushMatrix()
    glTranslatef(68, 0.05, 33)
    glScalef(2,0.4,1)
    objeto('objetos/grandstand.obj')
    glPopMatrix()
    glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT, [0.1,0.05,0.05])
    glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, [0.8,0.8,0.8])
    glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, [0.7,0.7,0.7])
    glMaterialf(GL_FRONT_AND_BACK, GL_SHININESS, 3)
    glPushMatrix()
    glTranslatef(68, 0.1, 20)
    glScalef(2,0.9,1)
    objeto('objetos/grandstand.obj')
    glPopMatrix()

    #Folhas Arvore:
    glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT, rgb_folhas)
    glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, rgb_folhas)
    glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, rgb_folhas)
    glMaterialf(GL_FRONT_AND_BACK, GL_SHININESS, 3)
    glPushMatrix()
    glTranslatef(104, 0.1, 20)
    glScalef(1,0.5,1.5)
    objeto('objetos/MapleTreeLeaves.obj')
    glPopMatrix()

    # Caule Arvore:
    glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT, rgb_terra)
    glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, rgb_terra)
    glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, rgb_terra)
    glMaterialf(GL_FRONT_AND_BACK, GL_SHININESS, 3)
    glPushMatrix()
    glTranslatef(104, 0.1, 20)
    glScalef(1,0.5,1.5)
    objeto('objetos/MapleTreeStem.obj')
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
    cube = obj.Obj().import_obj('../objects/cube_vn.obj', caminho_material)
    draw_polygon(cube)
    glPopMatrix()

    ##TRAVE TIME A VERTICAL DIREITA
    glPushMatrix()
    glTranslatef(40, 0, 105)
    glScalef(1, 5, 1)
    cube = obj.Obj().import_obj('../objects/cube_vn.obj', caminho_material)
    draw_polygon(cube)
    glPopMatrix()

    ##TRAVE TIME A HORIZONTAL
    glPushMatrix()
    glTranslatef(40, 5, 75)
    glScalef(1, 1, 31)
    cube = obj.Obj().import_obj('../objects/cube_vn.obj', caminho_material)
    draw_polygon(cube)
    glPopMatrix()


    ##TRAVE TIME B VERTICAL ESQUERDA
    glPushMatrix()
    glTranslatef(100, 0, 75)
    glScalef(1, 5, 1)
    cube = obj.Obj().import_obj('../objects/cube_vn.obj', caminho_material)
    draw_polygon(cube)
    glPopMatrix()

    ##TRAVE TIME A VERTICAL DIREITA
    glPushMatrix()
    glTranslatef(100, 0, 105)
    glScalef(1, 5, 1)
    cube = obj.Obj().import_obj('../objects/cube_vn.obj', caminho_material)
    draw_polygon(cube)
    glPopMatrix()

    ##TRAVE TIME A HORIZONTAL
    glPushMatrix()
    glTranslatef(100, 5, 75)
    glScalef(1, 1, 31)
    cube = obj.Obj().import_obj('../objects/cube_vn.obj', caminho_material)
    draw_polygon(cube)
    glPopMatrix()


    # # Tampo do Poste:
    # glPushMatrix()
    # glTranslatef(75., 11.06, 59.5)
    # glScalef(5, 0.05, 5)
    # cube = obj.Obj().import_obj('../objects/cube_vn.obj', espelho_material)
    # draw_polygon(cube)
    # glPopMatrix()


# def draw_car(color=[1,0.,0.], positionInitial=[0.,0.6,0.]):
#     glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT, color)
#     glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, color)
#     glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, color)
#     glMaterialf(GL_FRONT_AND_BACK, GL_SHININESS, 10)
#     glPushMatrix()
#     glTranslatef(positionInitial[0], positionInitial[1], positionInitial[2])
#     glRotatef(0,0,1,0)
#     glScalef(0.06,0.06,0.06)
#     objeto('objetos/10502_Football_Goalpost_v1_L3.obj')
#     glPopMatrix()

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
