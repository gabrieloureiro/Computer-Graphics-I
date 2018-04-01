from OpenGL.GL import *
from work_part1 import obj
def draw_circuit():
    #rgb_wall_material = [44/255, 137/255, 142/255]
    rgb_gramado = [50/255, 205/255, 50/255]
    rgb_asfalto = [76/255,76/255,76/255]
    gramado_material = obj.Material(rgb_gramado, rgb_gramado, [0.3,0.3,0.3], 10)
    asfalto_material = obj.Material(rgb_asfalto, rgb_asfalto, [0.3,0.3,0.3], 10)
    espelho_material = obj.Material([0.8,0.8,0.8], [0,0,0], [0.8,0.8,0.8], 20)
    
    # CHÃO
    glPushMatrix()
    glScalef(150., 0.01, 150.)
    cube = obj.Obj().import_obj('../objects/cube_vn.obj', gramado_material)
    draw_polygon(cube)
    glPopMatrix()

    # Reta Principal
    glPushMatrix()
    cube = obj.Obj().import_obj('../objects/cube_vn.obj', asfalto_material)
    glTranslatef(49.1 ,0., 51)
    glScalef(50.9, 0.05, 3.8)
    draw_polygon(cube)
    glPopMatrix()
    
    # C1.1
    glPushMatrix()
    glTranslatef(100,0,55)
    glRotatef(90,0,1,0) #Rotacionando 90 em y
    glScalef(5, 0.05, 5)
    draw_unitTriangle(asfalto_material)
    glPopMatrix()
    
    # C1.2
    glPushMatrix()
    glTranslatef(103.8,0,55) #Trazendo para a origem o triangulo
    glRotatef(-90,0,1,0) #Rotacionando 270 em y
    glScalef(5,0.05,5)
    draw_unitTriangle(asfalto_material)
    glPopMatrix()

    # C1.3
    glPushMatrix()
    glTranslatef(103.8,0,58.8)
    glRotatef(90,0,1,0) #Rotacionando 90 em y
    glScalef(5, 0.05, 5)
    draw_unitTriangle(asfalto_material)
    glPopMatrix()

    # Reta pos Principal
    glPushMatrix()
    cube = obj.Obj().import_obj('../objects/cube_vn.obj', asfalto_material)
    glTranslatef(103.9 ,0., 58.9)
    glScalef(4, 0.05, 20)
    draw_polygon(cube)
    glPopMatrix()

        
    # C2.1
    glPushMatrix()
    glTranslatef(103.9,0,79)
    #glRotatef(90,0,1,0) #Rotacionando 90 em y
    glScalef(5, 0.05, 5)
    draw_unitTriangle(asfalto_material)
    glPopMatrix()

    # Reta pos reta pos Principal
    glPushMatrix()
    cube = obj.Obj().import_obj('../objects/cube_vn.obj', asfalto_material)
    glTranslatef(99 ,0., 78.9)
    glScalef(5, 0.05, 4)
    draw_polygon(cube)
    glPopMatrix()

    # C3.1
    glPushMatrix()
    glTranslatef(99,0,79)
    glRotatef(-90,0,1,0) #Rotacionando 270 em y
    glScalef(5, 0.05, 5)
    draw_unitTriangle(asfalto_material)
    glPopMatrix()
    
    # C3.2
    glPushMatrix()
    glTranslatef(95,0,79)
    glRotatef(90,0,1,0) #Rotacionando 90 em y
    glScalef(5, 0.05, 5)
    draw_unitTriangle(asfalto_material)
    glPopMatrix()

    # C3.3
    glPushMatrix()
    glTranslatef(95,0,75.1)
    glRotatef(-90,0,1,0) #Rotacionando 270 em y
    glScalef(5, 0.05, 5)
    draw_unitTriangle(asfalto_material)
    glPopMatrix()
            
    # C3.4
    glPushMatrix()
    glTranslatef(91.1,0,75.1)
    glRotatef(90,0,1,0) #Rotacionando 90 em y
    glScalef(5, 0.05, 5)
    draw_unitTriangle(asfalto_material)
    glPopMatrix()

    # C3.5
    glPushMatrix()
    glTranslatef(91.1,0,71.1)
    glRotatef(-90,0,1,0) #Rotacionando 270 em y
    glScalef(5, 0.05, 5)
    draw_unitTriangle(asfalto_material)
    glPopMatrix()
            
    # C3.6
    glPushMatrix()
    glTranslatef(87.1,0,71.1)
    glRotatef(90,0,1,0) #Rotacionando 90 em y
    glScalef(5, 0.05, 5)
    draw_unitTriangle(asfalto_material)
    glPopMatrix()


    # Reta pos reta pos pos Principal
    glPushMatrix()
    cube = obj.Obj().import_obj('../objects/cube_vn.obj', asfalto_material)
    glTranslatef(57.1 ,0., 67.1)
    glScalef(30, 0.05, 4)
    draw_polygon(cube)
    glPopMatrix()
    
    # C4.1
    glPushMatrix()
    glTranslatef(57.1,0,71.1)
    glRotatef(180,0,1,0) #Rotacionando 270 em y
    glScalef(5, 0.05, 5)
    draw_unitTriangle(asfalto_material)
    glPopMatrix()
            
    # C4.2
    glPushMatrix()
    glTranslatef(53.1,0,71.1)
    #glRotatef(90,0,1,0) #Rotacionando 90 em y
    glScalef(5, 0.05, 5)
    draw_unitTriangle(asfalto_material)
    glPopMatrix()

    # C4.3
    glPushMatrix()
    glTranslatef(53.1,0,75.1)
    glRotatef(180,0,1,0) #Rotacionando 270 em y
    glScalef(5, 0.05, 5)
    draw_unitTriangle(asfalto_material)
    glPopMatrix()
            
    # C4.4
    glPushMatrix()
    glTranslatef(49.1,0,75.1)
    #glRotatef(90,0,1,0) #Rotacionando 90 em y
    glScalef(5, 0.05, 5)
    draw_unitTriangle(asfalto_material)
    glPopMatrix()

    # C4.5
    glPushMatrix()
    glTranslatef(49.1,0,75.1)
    glRotatef(-90,0,1,0) #Rotacionando 270 em y
    glScalef(5, 0.05, 5)
    draw_unitTriangle(asfalto_material)
    glPopMatrix()

    # Reta antes reta Principal
    glPushMatrix()
    cube = obj.Obj().import_obj('../objects/cube_vn.obj', asfalto_material)
    glTranslatef(45.3 ,0., 54.9)
    glScalef(3.8, 0.05, 20.2 )
    draw_polygon(cube)
    glPopMatrix()

    # C5.1
    glPushMatrix()
    glTranslatef(49.1,0,54.9)
    glRotatef(180,0,1,0) #Rotacionando 270 em y
    glScalef(5, 0.05, 5)
    draw_unitTriangle(asfalto_material)
    glPopMatrix()

    draw_car(positionInitial=[53.,0.6,53.])
    draw_car(color=[0.,0.,1], positionInitial=[57.,0.6,52.])

    # Arquibancada:
    glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT, [0.1,0.05,0.05])
    glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, [0.8,0.8,0.8])
    glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, [0.7,0.7,0.7])
    glMaterialf(GL_FRONT_AND_BACK, GL_SHININESS, 3)
    glPushMatrix()
    glTranslatef(75, 0.05, 40)
    glScalef(2,0.4,1)
    objeto('objetos/grandstand.obj')
    glPopMatrix()

    # Criando Poste de Iluminação do Circuito
    glPushMatrix()
    glTranslatef(75, 0.05, 60)
    glScalef(3, 11, 3)
    cube = obj.Obj().import_obj('../objects/cube_vn.obj', asfalto_material)
    draw_polygon(cube)
    glPopMatrix()

    # Tampo do Poste:
    glPushMatrix()
    glTranslatef(75., 11.06, 59.5)
    glScalef(5, 0.05, 5)
    cube = obj.Obj().import_obj('../objects/cube_vn.obj', espelho_material)
    draw_polygon(cube)
    glPopMatrix()


def draw_car(color=[1,0.,0.], positionInitial=[0.,0.6,0.]):
    glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT, color)
    glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, color)
    glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, color)
    glMaterialf(GL_FRONT_AND_BACK, GL_SHININESS, 10)
    glPushMatrix()
    glTranslatef(positionInitial[0], positionInitial[1], positionInitial[2])
    glRotatef(90,0,1,0)
    glScalef(0.5,0.5,0.5)
    objeto('objetos/Ferrari.obj')
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
