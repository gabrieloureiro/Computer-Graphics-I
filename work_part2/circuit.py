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
    rgb_detento = [217/255, 135/255, 25/255]
    rgb_lixeira = [35/255, 107/255, 142/255]
    rgb_verde_lixo = [33/255, 94/255, 33/255]
    rgb_vermelho = [1,0,0]
    rgb_azul = [0,0,1]
    azul_material = obj.Material(rgb_azul, rgb_azul, [0.3,0.3,0.3], 10)
    vermelho_material = obj.Material(rgb_vermelho, rgb_vermelho, [0.3,0.3,0.3], 10)
    gramado_material = obj.Material(rgb_gramado, rgb_gramado, [0.3,0.3,0.3], 10)
    madeira_material = obj.Material(rgb_madeira,rgb_madeira, [0.3,0.3,0.3],10)
    cal_material = obj.Material(rgb_cal,rgb_cal, [0.3,0.3,0.3],10)
    terra_material = obj.Material(rgb_terra, rgb_terra, [0.1,0.1,0.1], 10)
    ferro_material = obj.Material(rgb_ferro, rgb_ferro, [0.3,0.3,0.3], 10)
    espelho_material = obj.Material([0.8,0.8,0.8], [0,0,0], [0.8,0.8,0.8], 20)
    

    # OBJETOS QUE COMPÕEM O CENÁRIO

    # Chão
    glPushMatrix()
    glScalef(150.,0.01, 200.)
    cube = obj.Obj().import_obj('../objects/cube_vn.obj', terra_material)
    draw_polygon(cube)
    glPopMatrix()

    # Campo
    glPushMatrix()
    cube = obj.Obj().import_obj('../objects/cube_vn.obj', gramado_material)
    glTranslatef(65 ,0., 52)
    glScalef(40, 0.02, 78)
    draw_polygon(cube)
    glPopMatrix()

     # Reta Esquerda
    glPushMatrix()
    cube = obj.Obj().import_obj('../objects/cube_vn.obj', cal_material)
    glTranslatef(65 ,0., 51)
    glScalef(40, 0.1, 1)
    draw_polygon(cube)
    glPopMatrix()
    
    # Reta Direita
    glPushMatrix()
    cube = obj.Obj().import_obj('../objects/cube_vn.obj', cal_material)
    glTranslatef(65 ,0., 130)
    glScalef(40, 0.1, 1)
    draw_polygon(cube)
    glPopMatrix()

    # Reta Inferior
    glPushMatrix()
    cube = obj.Obj().import_obj('../objects/cube_vn.obj', cal_material)
    glTranslatef(65 ,0., 51)
    glScalef(0.5, 0.1, 79)
    draw_polygon(cube)
    glPopMatrix()

    # Reta Central
    glPushMatrix()
    cube = obj.Obj().import_obj('../objects/cube_vn.obj', cal_material)
    glTranslatef(86 ,0., 51)
    glScalef(0.5, 0.1, 79)
    draw_polygon(cube)
    glPopMatrix()

    # Reta Superior
    glPushMatrix()
    cube = obj.Obj().import_obj('../objects/cube_vn.obj', cal_material)
    glTranslatef(105 ,0., 51)
    glScalef(0.5, 0.1, 79)
    draw_polygon(cube)
    glPopMatrix()

    # Carro 01 - Dentro do Terreno
    glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT, [0,0,0])
    glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, [0,0,0])
    glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, [0,0,0])
    glMaterialf(GL_FRONT_AND_BACK, GL_SHININESS, 3)
    glPushMatrix()
    glTranslatef(58.,4.3,175.)
    glScalef(1,1.8,2)
    glRotatef(90,0,1,0)
    objeto('objetos/camaro.obj')
    glPopMatrix()

    # Carro 02 - saindo no terreno
    glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT, [0.1,0.05,0.05])
    glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, [0.8,0.8,0.8])
    glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, [0.7,0.7,0.7])
    glMaterialf(GL_FRONT_AND_BACK, GL_SHININESS, 3)
    glPushMatrix()
    glTranslatef(29.,4.3,75.)
    glScalef(1,1.8,2)
    glRotatef(193,0,1,0)
    objeto('objetos/camaro.obj')
    glPopMatrix()

    # Sirene 01
    glPushMatrix()
    glTranslatef(55.5, 6, 172)
    glScalef(3, 1, 3)
    cube = obj.Obj().import_obj('../objects/cube_vn.obj', vermelho_material)
    draw_polygon(cube)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(55.5, 6, 175)
    glScalef(3, 1, 3)
    cube = obj.Obj().import_obj('../objects/cube_vn.obj', azul_material)
    draw_polygon(cube)
    glPopMatrix()

    # Sirene 02
    glPushMatrix()
    glTranslatef(29, 6, 72)
    glScalef(3, 1, 3)
    cube = obj.Obj().import_obj('../objects/cube_vn.obj', vermelho_material)
    draw_polygon(cube)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(29, 6, 75)
    glScalef(3, 1, 3)
    cube = obj.Obj().import_obj('../objects/cube_vn.obj', azul_material)
    draw_polygon(cube)
    glPopMatrix()

    # Arquibancada:
    glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT, rgb_madeira)
    glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, rgb_madeira)
    glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, rgb_madeira)
    glMaterialf(GL_FRONT_AND_BACK, GL_SHININESS, 3)
    glPushMatrix()
    glTranslatef(71, 0.05, 25)
    glScalef(2.108,1,1.8)
    objeto('objetos/grandstand.obj')
    glPopMatrix()

    #Asfalto
    glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT, rgb_asfalto)
    glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, rgb_asfalto)
    glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, rgb_asfalto)
    glMaterialf(GL_FRONT_AND_BACK, GL_SHININESS, 3)
    glPushMatrix()
    glTranslatef(22, 0.01, 99)
    glScalef(2.7,0.02,23)
    objeto('objetos/road.obj')
    glPopMatrix()

    #Linha do asfalto
    glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT, rgb_lista)
    glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, rgb_lista)
    glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, rgb_lista)
    glMaterialf(GL_FRONT_AND_BACK, GL_SHININESS, 3)
    glPushMatrix()
    glTranslatef(22, 0.01, 99)
    glScalef(0.2,0.05,23)
    objeto('objetos/road.obj')
    glPopMatrix()

    #Canteiro inferior
    glPushMatrix()
    glTranslatef(15, 0.01, 1)
    glScalef(1, 1, 192)
    cube = obj.Obj().import_obj('../objects/cube_vn.obj', ferro_material)
    draw_polygon(cube)
    glPopMatrix()

    #Canteiro superior
    glPushMatrix()
    glTranslatef(28, 0.06, 116)
    glScalef(1, 1, 80)
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

    # # Folhas Arvore2:
    # glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT, rgb_folhas)
    # glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, rgb_folhas)
    # glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, rgb_folhas)
    # glMaterialf(GL_FRONT_AND_BACK, GL_SHININESS, 3)
    # glPushMatrix()
    # glTranslatef(106, 0.1, 150)
    # glScalef(1,0.5,1.5)
    # objeto('objetos/MapleTreeLeaves.obj')
    # glPopMatrix()

    # Caule Arvore2:
    glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT, rgb_madeira)
    glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, rgb_madeira)
    glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, rgb_madeira)
    glMaterialf(GL_FRONT_AND_BACK, GL_SHININESS, 3)
    glPushMatrix()
    glTranslatef(106, 0.1, 173)
    glScalef(1,0.5,1.5)
    objeto('objetos/MapleTreeStem.obj')
    glPopMatrix()

    # Cerca direita
    glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT, rgb_ferro)
    glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, rgb_ferro)
    glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, rgb_ferro)
    glMaterialf(GL_FRONT_AND_BACK, GL_SHININESS, 3)
    glPushMatrix()
    glTranslatef(75.7, 0.01, 199)
    glScalef(5,0.7,10)
    #glRotatef(90,0,1,0)
    objeto('objetos/fance.obj')
    glPopMatrix()

    # Portão
    glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT, rgb_ferro)
    glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, rgb_ferro)
    glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, rgb_ferro)
    glMaterialf(GL_FRONT_AND_BACK, GL_SHININESS, 3)
    glPushMatrix()
    glTranslatef(28.8, 0.01, 75)
    glScalef(1.7,0.7,6.8)
    glRotatef(90,0,1,0)
    objeto('objetos/military_fence_gate.obj')
    glPopMatrix()

    # Cerca Fundo
    glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT, rgb_ferro)
    glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, rgb_ferro)
    glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, rgb_ferro)
    glMaterialf(GL_FRONT_AND_BACK, GL_SHININESS, 3)
    glPushMatrix()
    glTranslatef(112, 0.01, 98.2)
    glScalef(4,0.7,12.5)
    glRotatef(90,0,1,0)
    objeto('objetos/fance.obj')
    glPopMatrix()

    # Cerca Esquerda
    glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT, rgb_ferro)
    glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, rgb_ferro)
    glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, rgb_ferro)
    glMaterialf(GL_FRONT_AND_BACK, GL_SHININESS, 3)
    glPushMatrix()
    glTranslatef(75.7, 0.01, 0)
    glScalef(5,0.7,10)
    #glRotatef(90,0,1,0)
    objeto('objetos/fance.obj')
    glPopMatrix()

    #Torre do vigia
    glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT, rgb_ferro)
    glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, rgb_ferro)
    glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, rgb_ferro)
    glMaterialf(GL_FRONT_AND_BACK, GL_SHININESS, 3)
    glPushMatrix()
    glTranslatef(40.7, 0.01, 74)
    glScalef(2,2.6,3)
    glRotatef(180,0,1,0)
    objeto('objetos/wooden_watch_tower2.obj')
    glPopMatrix()

    # Detento 1
    glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT, rgb_detento)
    glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, rgb_detento)
    glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, rgb_detento)
    glMaterialf(GL_FRONT_AND_BACK, GL_SHININESS, 3)
    glPushMatrix()
    glTranslatef(90, 0.1, 155)
    glScalef(1.5,1,2.7)
    glRotatef(270,0,1,0)
    objeto('objetos/male.obj')
    glPopMatrix()

    # Detento 2
    glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT, rgb_detento)
    glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, rgb_detento)
    glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, rgb_detento)
    glMaterialf(GL_FRONT_AND_BACK, GL_SHININESS, 3)
    glPushMatrix()
    glTranslatef(75, 0.1, 75)
    glScalef(1.5,1,2.7)
    glRotatef(90,0,1,0)
    objeto('objetos/male.obj')
    glPopMatrix()

    # Bola
    glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT, [0,0,0])
    glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, [0,0,0])
    glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, [0,0,0])
    glMaterialf(GL_FRONT_AND_BACK, GL_SHININESS, 3)
    glPushMatrix()
    glTranslatef(90, 2, 80)
    glScalef(1,1,1.5)
    #glRotatef(90,0,1,0)
    objeto('objetos/Ball.obj')
    glPopMatrix()

    # Lixeira Azul
    glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT, rgb_lixeira)
    glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, rgb_lixeira)
    glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, rgb_lixeira)
    glMaterialf(GL_FRONT_AND_BACK, GL_SHININESS, 1)
    glPushMatrix()
    glTranslatef(40, 0.05, 50)
    glScalef(0.03,0.03,0.1)
    glRotatef(90,0,1,0)
    objeto('objetos/trash.obj')
    glPopMatrix()

    # Lixeira Verde
    glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT, rgb_verde_lixo)
    glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, rgb_verde_lixo)
    glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, rgb_verde_lixo)
    glMaterialf(GL_FRONT_AND_BACK, GL_SHININESS, 1)
    glPushMatrix()
    glTranslatef(40, 0.05, 20)
    glScalef(0.03,0.03,0.1)
    glRotatef(90,0,1,0)
    objeto('objetos/trash.obj')
    glPopMatrix()


    # Quadrado para refletor torre > campo
    glPushMatrix()
    glTranslatef(40.7, 19, 74)
    glScalef(0, 2, 2)
    cube = obj.Obj().import_obj('../objects/cube_vn.obj', cal_material)
    draw_polygon(cube)
    glPopMatrix()

    # # Detento 3
    # glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT, rgb_detento)
    # glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, rgb_detento)
    # glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, rgb_detento)
    # glMaterialf(GL_FRONT_AND_BACK, GL_SHININESS, 3)
    # glPushMatrix()
    # glTranslatef(50, 0.1, 90)
    # glScalef(0.09,0.015,1.05)
    # glRotatef(180,0,1,1)
    # objeto('objetos/male.obj')
    # glPopMatrix()


    #Banco Up Left:
    glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT, rgb_verde_lixo)
    glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, rgb_verde_lixo)
    glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, rgb_verde_lixo)
    glMaterialf(GL_FRONT_AND_BACK, GL_SHININESS, 1)
    glPushMatrix()
    glTranslatef(108.5, 0.1, 75)
    glScalef(0.08,0.04,0.12)
    glRotatef(270,0,1,0)
    objeto('objetos/Bench_HighRes.obj')
    glPopMatrix()

    #Banco Up Right:
    glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT, rgb_vermelho)
    glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, rgb_vermelho)
    glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, rgb_vermelho)
    glMaterialf(GL_FRONT_AND_BACK, GL_SHININESS, 1)
    glPushMatrix()
    glTranslatef(108.5, 0.1, 118)
    glScalef(0.08,0.04,0.12)
    glRotatef(270,0,1,0)
    objeto('objetos/Bench_HighRes.obj')
    glPopMatrix()
    

    ##TRAVE INFERIOR - VERTICAL ESQUERDA
    glPushMatrix()
    glTranslatef(67, 0, 75)
    glScalef(1, 5, 1)
    cube = obj.Obj().import_obj('../objects/cube_vn.obj', ferro_material)
    draw_polygon(cube)
    glPopMatrix()

    ##TRAVE INFERIOR - VERTICAL DIREITA
    glPushMatrix()
    glTranslatef(67, 0, 105)
    glScalef(1, 5, 1)
    cube = obj.Obj().import_obj('../objects/cube_vn.obj', ferro_material)
    draw_polygon(cube)
    glPopMatrix()

    ##TRAVE INFERIOR - HORIZONTAL
    glPushMatrix()
    glTranslatef(67, 5, 75)
    glScalef(1, 1, 31)
    cube = obj.Obj().import_obj('../objects/cube_vn.obj', ferro_material)
    draw_polygon(cube)
    glPopMatrix()


    ##TRAVE SUPERIOR - VERTICAL ESQUERDA
    glPushMatrix()
    glTranslatef(100, 0, 75)
    glScalef(1, 5, 1)
    cube = obj.Obj().import_obj('../objects/cube_vn.obj', ferro_material)
    draw_polygon(cube)
    glPopMatrix()

    ##TRAVE SUPERIOR - VERTICAL DIREITA
    glPushMatrix()
    glTranslatef(100, 0, 105)
    glScalef(1, 5, 1)
    cube = obj.Obj().import_obj('../objects/cube_vn.obj', ferro_material)
    draw_polygon(cube)
    glPopMatrix()

    ##TRAVE SUPERIOR - HORIZONTAL
    glPushMatrix()
    glTranslatef(100, 5, 75)
    glScalef(1, 1, 31)
    cube = obj.Obj().import_obj('../objects/cube_vn.obj', ferro_material)
    draw_polygon(cube)
    glPopMatrix()

# Função polígonos 
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

# Função triângulo unitário
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
