from scenario import *
import obj
import transformations as t

def circuit():
    objects = []

    # Cores dos Materiais & Componentes Especulares:
    specular_term = [1, 1, 1]
    specular_term2 = [0.3, 0.3, 0.3]
    rugose_term = [0.2, 0.2, 0.2]
    m = 10 

    rgb_asfalto = [0.50196078,0.50196078,0.50196078]
    rgb_gramado = [50/255, 205/255, 50/255]
    rgb_madeira = [92/255, 51/255, 23/255]
    rgb_vermelho_grena = [140/255, 23/255, 23/255]
    rgb_mostarda = [207/255, 181/255, 59/255]
    rgb_preto = [0, 0, 0]
    rgb_branco = [1,1,1]
    
    # Materiais:
    asfalto_material = obj.Material(rgb_asfalto, rgb_asfalto, specular_term2, m)
    gramado_material = obj.Material(rgb_gramado, rgb_gramado, specular_term, 10)
    madeira_material = obj.Material(rgb_madeira, rgb_madeira, specular_term, 2)

    # -- lc = linha de chegada -- #
    lc1_material = obj.Material(rgb_preto, rgb_preto, specular_term, m)
    lc2_material = obj.Material(rgb_branco, rgb_branco, specular_term, m)
    
    # -- p's = postes  -- #
    p1_material = obj.Material(rgb_vermelho_grena, rgb_vermelho_grena, specular_term, 2)
    p2_material = obj.Material(rgb_mostarda, rgb_mostarda, specular_term, 2)  

    
    # Chão
    scale = t.get_scale([150, 0.01, 150, 1])
    #translate = t.get_translation([-50, 0, -50]) #Centralizando o chao
    chao = obj.UnitSquare()
    chao.apply_material(gramado_material)
    chao.apply_transformation(scale)
    #chao.apply_transformation(translate)
    #chao.printVertices()
    objects.append(chao)

    # Reta Principal
    scale = t.get_scale([50, 0.05, 5, 1])
    translate = t.get_translation([50,0,50])
    r = obj.UnitSquare()
    r.apply_transformation(scale)
    r.apply_transformation(translate)
    r.printVertices()
    r.apply_material(asfalto_material)
    objects.append(r)

    print ("Reta Principal:")
    r.printVertices()

    # C1
    # Curva pos reta principal
    rotate = t.get_rotation(90, 'y')
    scale = t.get_scale([5, 0.05, 5, 1])
    translate = t.get_translation(r.vertices[2].coordinates[:3]) #Movimentando o triangulo para o fim da reta
    c = obj.UnitTriangle()
    c.apply_transformation(scale)
    c.apply_transformation(rotate)
    c.apply_transformation(translate)
    c.apply_material(asfalto_material)
    objects.append(c)

    # C2
    rotate = t.get_rotation(-90, 'y')
    scale = t.get_scale([5, 0.05, 5, 1])
    translate = t.get_translation(c.vertices[1].coordinates[:3])
    c = obj.UnitTriangle()
    c.apply_transformation(scale)
    c.apply_transformation(rotate)
    c.apply_transformation(translate)
    #c12.printVertices()
    c.apply_material(asfalto_material)
    objects.append(c)
    
    # C3
    rotate = t.get_rotation(90, 'y')
    scale = t.get_scale([5, 0.05, 5, 1])
    translate = t.get_translation(c.vertices[2].coordinates[:3])
    c = obj.UnitTriangle()
    c.apply_transformation(scale)
    c.apply_transformation(rotate)
    c.apply_transformation(translate)
    c.apply_material(asfalto_material)
    objects.append(c)

    # Reta pos principal
    scale = t.get_scale([5, 0.05, 10, 1])
    translate = t.get_translation(c.vertices[0].coordinates[:3])
    r = obj.UnitSquare()
    r.apply_transformation(scale)
    r.apply_transformation(translate)
    #r2.printVertices()
    r.apply_material(asfalto_material)
    objects.append(r)

    # Curva apos reta: 
    rotate = t.get_rotation(-90, 'y')
    scale = t.get_scale([5, 0.05, 5, 1])
    translate = t.get_translation(r.vertices[2].coordinates[:3]) #Movimentando o triangulo para o fim da reta
    c = obj.UnitTriangle()
    c.apply_transformation(scale)
    c.apply_transformation(rotate)
    c.apply_transformation(translate)
    c.apply_material(asfalto_material)
    objects.append(c)

    rotate = t.get_rotation(90, 'y')
    scale = t.get_scale([5, 0.05, 5, 1])
    translate = t.get_translation(c.vertices[2].coordinates[:3])
    c = obj.UnitTriangle()
    c.apply_transformation(scale)
    c.apply_transformation(rotate)
    c.apply_transformation(translate)
    c.apply_material(asfalto_material)
    objects.append(c)


    # Reta do lado oposto:
    scale = t.get_scale([5, 0.05, 5, 1])
    translate = t.get_translation(c.vertices[0].coordinates[:3])
    r = obj.UnitSquare()
    r.apply_transformation(scale)
    r.apply_transformation(translate)
    #r3.printVertices()
    r.apply_material(asfalto_material)
    objects.append(r)

    # Curva setor 03
    scale = t.get_scale([5, 0.05, 5, 1])
    translate = t.get_translation(r.vertices[1].coordinates[:3]) 
    c = obj.UnitTriangle()
    c.apply_transformation(scale)
    c.apply_transformation(translate)
    
    print ("Curva Setor 3")
    c.printVertices()
    c.apply_material(asfalto_material)
    objects.append(c)

    scale = t.get_scale([20, 0.05, 5, 1])
    translate = t.get_translation(c.vertices[0].coordinates[:3] - [20, 0, 0])
    r = obj.UnitSquare()
    r.apply_transformation(scale)
    r.apply_transformation(translate)
    r.apply_material(asfalto_material)
    objects.append(r)

    # Curva setor 04:
    rotate = t.get_rotation(-90, 'y')
    scale = t.get_scale([5, 0.05, 5, 1])
    translate = t.get_translation(r.vertices[0].coordinates[:3]) 
    c = obj.UnitTriangle()
    c.apply_transformation(scale)
    c.apply_transformation(rotate)
    c.apply_transformation(translate)
    #c.printVertices()
    c.apply_material(asfalto_material)
    objects.append(c)

    scale = t.get_scale([5, 0.05, 5, 1])
    translate = t.get_translation(c.vertices[1].coordinates[:3] - [0, 0, 5])
    r = obj.UnitSquare()
    r.apply_transformation(scale)
    r.apply_transformation(translate)
    #r.printVertices()
    r.apply_material(asfalto_material)
    objects.append(r)

    rotate = t.get_rotation(180, 'y')
    scale = t.get_scale([5, 0.05, 5, 1])
    translate = t.get_translation(r.vertices[3].coordinates[:3]) 
    c = obj.UnitTriangle()
    c.apply_transformation(scale)
    c.apply_transformation(rotate)
    c.apply_transformation(translate)
    #c.printVertices()
    c.apply_material(asfalto_material)
    objects.append(c)

    scale = t.get_scale([8, 0.05, 5, 1])
    translate = t.get_translation(c.vertices[1].coordinates[:3])
    r = obj.UnitSquare()
    r.apply_transformation(scale)
    r.apply_transformation(translate)
    #r.printVertices()
    r.apply_material(asfalto_material)
    objects.append(r)

    scale = t.get_scale([5, 0.05, 5, 1])
    translate = t.get_translation(r.vertices[3].coordinates[:3]) 
    c = obj.UnitTriangle()
    c.apply_transformation(scale)
    #c.apply_transformation(rotate)
    c.apply_transformation(translate)
    #c.printVertices()
    c.apply_material(asfalto_material)
    objects.append(c)


    scale = t.get_scale([5, 0.05, 5, 1])
    translate = t.get_translation(c.vertices[0].coordinates[:3] - [0, 0, 5])
    r = obj.UnitSquare()
    r.apply_transformation(scale)
    r.apply_transformation(translate)
    #r.printVertices()
    r.apply_material(asfalto_material)
    objects.append(r)

    rotate = t.get_rotation(90, 'y')
    scale = t.get_scale([5, 0.05, 5, 1])
    translate = t.get_translation(r.vertices[0].coordinates[:3]) 
    c = obj.UnitTriangle()
    c.apply_transformation(scale)
    c.apply_transformation(rotate)
    c.apply_transformation(translate)
    #c.printVertices()
    c.apply_material(asfalto_material)
    objects.append(c)

    scale = t.get_scale([10, 0.05, 5, 1])
    translate = t.get_translation(c.vertices[2].coordinates[:3] - [10, 0, 0])
    r = obj.UnitSquare()
    r.apply_transformation(scale)
    r.apply_transformation(translate)
    #r.printVertices()
    r.apply_material(asfalto_material)
    objects.append(r)



    # -- PRIMEIRA DIAGONAL DO CIRCUITO: -- #
    rotate = t.get_rotation(180, 'y')
    scale = t.get_scale([5, 0.05, 5, 1])
    translate = t.get_translation(r.vertices[1].coordinates[:3]) 
    d = obj.UnitTriangle()
    d.apply_transformation(scale)
    d.apply_transformation(rotate)
    d.apply_transformation(translate)
    #d11.printVertices()
    d.apply_material(asfalto_material)
    objects.append(d)

    translate = t.get_translation(d.vertices[2].coordinates[:3]) 
    d = obj.UnitTriangle()
    d.apply_transformation(scale)
    d.apply_transformation(translate)
    #d12.printVertices()
    d.apply_material(asfalto_material)
    objects.append(d)

    rotate = t.get_rotation(180, 'y')
    translate = t.get_translation(d.vertices[1].coordinates[:3]) 
    d = obj.UnitTriangle()
    d.apply_transformation(scale)
    d.apply_transformation(rotate)
    d.apply_transformation(translate)
    #d.printVertices()
    d.apply_material(asfalto_material)
    objects.append(d)

    translate = t.get_translation(d.vertices[2].coordinates[:3]) 
    d = obj.UnitTriangle()
    d.apply_transformation(scale)
    d.apply_transformation(translate)
    #d.printVertices()
    d.apply_material(asfalto_material)
    objects.append(d)

    rotate = t.get_rotation(180, 'y')
    translate = t.get_translation(d.vertices[1].coordinates[:3]) 
    d = obj.UnitTriangle()
    d.apply_transformation(scale)
    d.apply_transformation(rotate)
    d.apply_transformation(translate)
    #d.printVertices()
    d.apply_material(asfalto_material)
    objects.append(d)

    translate = t.get_translation(d.vertices[2].coordinates[:3]) 
    d = obj.UnitTriangle()
    d.apply_transformation(scale)
    d.apply_transformation(translate)
    #d.printVertices()
    d.apply_material(asfalto_material)
    objects.append(d)

    rotate = t.get_rotation(180, 'y')
    translate = t.get_translation(d.vertices[1].coordinates[:3]) 
    d = obj.UnitTriangle()
    d.apply_transformation(scale)
    d.apply_transformation(rotate)
    d.apply_transformation(translate)
    #d.printVertices()
    d.apply_material(asfalto_material)
    objects.append(d)

    translate = t.get_translation(d.vertices[2].coordinates[:3]) 
    d = obj.UnitTriangle()
    d.apply_transformation(scale)
    d.apply_transformation(translate)
    #d.printVertices()
    d.apply_material(asfalto_material)
    objects.append(d)

    # INFLEXAO DA DIAGONAL
    scale = t.get_scale([5, 0.05, 5, 1])
    translate = t.get_translation(d.vertices[0].coordinates[:3] - [5 ,0, 0])
    r = obj.UnitSquare()
    r.apply_transformation(scale)
    r.apply_transformation(translate)
    #r.printVertices()
    r.apply_material(asfalto_material)
    objects.append(r)

    # Iniciando a outra Diagonal
    rotate = t.get_rotation(-90, 'y')
    translate = t.get_translation(r.vertices[0].coordinates[:3]) 
    d = obj.UnitTriangle()
    d.apply_transformation(scale)
    d.apply_transformation(rotate)
    d.apply_transformation(translate)
    #d.printVertices()
    d.apply_material(asfalto_material)
    objects.append(d)

    rotate = t.get_rotation(90, 'y')
    translate = t.get_translation(d.vertices[1].coordinates[:3]) 
    d = obj.UnitTriangle()
    d.apply_transformation(scale)
    d.apply_transformation(rotate)
    d.apply_transformation(translate)
    #d.printVertices()
    d.apply_material(asfalto_material)
    objects.append(d)
    
    rotate = t.get_rotation(-90, 'y')
    translate = t.get_translation(d.vertices[2].coordinates[:3]) 
    d = obj.UnitTriangle()
    d.apply_transformation(scale)
    d.apply_transformation(rotate)
    d.apply_transformation(translate)
    #d.printVertices()
    d.apply_material(asfalto_material)
    objects.append(d)

    rotate = t.get_rotation(90, 'y')
    translate = t.get_translation(d.vertices[1].coordinates[:3]) 
    d = obj.UnitTriangle()
    d.apply_transformation(scale)
    d.apply_transformation(rotate)
    d.apply_transformation(translate)
    #d.printVertices()
    d.apply_material(asfalto_material)
    objects.append(d)

    rotate = t.get_rotation(-90, 'y')
    translate = t.get_translation(d.vertices[2].coordinates[:3]) 
    d = obj.UnitTriangle()
    d.apply_transformation(scale)
    d.apply_transformation(rotate)
    d.apply_transformation(translate)
    #d.printVertices()
    d.apply_material(asfalto_material)
    objects.append(d)

    rotate = t.get_rotation(90, 'y')
    translate = t.get_translation(d.vertices[1].coordinates[:3]) 
    d = obj.UnitTriangle()
    d.apply_transformation(scale)
    d.apply_transformation(rotate)
    d.apply_transformation(translate)
    #d.printVertices()
    d.apply_material(asfalto_material)
    objects.append(d)

    rotate = t.get_rotation(-90, 'y')
    translate = t.get_translation(d.vertices[2].coordinates[:3]) 
    d = obj.UnitTriangle()
    d.apply_transformation(scale)
    d.apply_transformation(rotate)
    d.apply_transformation(translate)
    #d.printVertices()
    d.apply_material(asfalto_material)
    objects.append(d)

    rotate = t.get_rotation(90, 'y')
    translate = t.get_translation(d.vertices[1].coordinates[:3]) 
    d = obj.UnitTriangle()
    d.apply_transformation(scale)
    d.apply_transformation(rotate)
    d.apply_transformation(translate)
    #d.printVertices()
    d.apply_material(asfalto_material)
    objects.append(d)

    # Termino
    scale = t.get_scale([5, 0.05, 5, 1])
    translate = t.get_translation(d.vertices[2].coordinates[:3] - [5 ,0, 0])
    r = obj.UnitSquare()
    r.apply_transformation(scale)
    r.apply_transformation(translate)
    #r.printVertices()
    r.apply_material(asfalto_material)
    objects.append(r)

    rotate = t.get_rotation(180, 'y')
    scale = t.get_scale([5, 0.05, 5, 1])
    translate = t.get_translation(r.vertices[1].coordinates[:3]) 
    c = obj.UnitTriangle()
    c.apply_transformation(scale)
    c.apply_transformation(rotate)
    c.apply_transformation(translate)
    c.apply_material(asfalto_material)
    objects.append(c)

    scale = t.get_scale([5, 0.05, 10, 1])
    translate = t.get_translation(c.vertices[2].coordinates[:3])
    r = obj.UnitSquare()
    r.apply_transformation(scale)
    r.apply_transformation(translate)
    r.apply_material(asfalto_material)
    objects.append(r)

    rotate = t.get_rotation(-90, 'y')
    scale = t.get_scale([5, 0.05, 5, 1])
    translate = t.get_translation(r.vertices[2].coordinates[:3]) 
    c = obj.UnitTriangle()
    c.apply_transformation(scale)
    c.apply_transformation(rotate)
    c.apply_transformation(translate)
    c.apply_material(asfalto_material)
    objects.append(c)

    translate = t.get_translation(c.vertices[0].coordinates[:3])
    r = obj.UnitSquare()
    r.apply_transformation(scale)
    r.apply_transformation(translate)
    r.apply_material(asfalto_material)
    objects.append(r)

    rotate = t.get_rotation(90, 'y')
    translate = t.get_translation(r.vertices[2].coordinates[:3]) 
    c = obj.UnitTriangle()
    c.apply_transformation(scale)
    c.apply_transformation(rotate)
    c.apply_transformation(translate)
    c.apply_material(asfalto_material)
    objects.append(c)

    translate = t.get_translation(c.vertices[0].coordinates[:3])
    r = obj.UnitSquare()
    r.apply_transformation(scale)
    r.apply_transformation(translate)
    r.apply_material(asfalto_material)
    objects.append(r)

    translate = t.get_translation(r.vertices[1].coordinates[:3]) 
    c = obj.UnitTriangle()
    c.apply_transformation(scale)
    c.apply_transformation(translate)
    c.apply_material(asfalto_material)
    objects.append(c)

    scale = t.get_scale([15, 0.05, 5, 1])
    translate = t.get_translation(c.vertices[0].coordinates[:3] - [15,0,0])
    r = obj.UnitSquare()
    r.apply_transformation(scale)
    r.apply_transformation(translate)
    r.apply_material(asfalto_material)
    objects.append(r)

    scale = t.get_scale([5, 0.05, 5, 1])
    rotate = t.get_rotation(-90, 'y')
    translate = t.get_translation(r.vertices[0].coordinates[:3]) 
    c = obj.UnitTriangle()
    c.apply_transformation(scale)
    c.apply_transformation(rotate)
    c.apply_transformation(translate)
    c.apply_material(asfalto_material)
    objects.append(c)

    #Ultima reta antes da ultima curva
    scale = t.get_scale([5, 0.05, 30, 1])
    translate = t.get_translation(c.vertices[1].coordinates[:3] - [0,0,30])
    r = obj.UnitSquare()
    r.apply_transformation(scale)
    r.apply_transformation(translate)
    r.apply_material(asfalto_material)
    objects.append(r)
    print("Ultima reta antes da ultima curva: ")
    r.printVertices()
    

    scale = t.get_scale([5, 0.05, 5, 1])
    rotate = t.get_rotation(180, 'y')
    translate = t.get_translation(r.vertices[3].coordinates[:3]) 
    c = obj.UnitTriangle()
    c.apply_transformation(scale)
    c.apply_transformation(rotate)
    c.apply_transformation(translate)
    c.apply_material(asfalto_material)
    objects.append(c)

    # Reta que liga a saida da curva com a pista principal
    scale = t.get_scale([22, 0.05, 5, 1])
    translate = t.get_translation(c.vertices[1].coordinates[:3])
    r = obj.UnitSquare()
    r.apply_transformation(scale)
    r.apply_transformation(translate)
    r.apply_material(asfalto_material)
    objects.append(r)

    print("Reta que liga a saida da curva com a pista principal")
    r.printVertices()

    # LINHA CHEGADA
    scale = t.get_scale([1.25, 0.06, 1.25, 1])
    translate = t.get_translation(r.vertices[3].coordinates[:3])
    r = obj.UnitSquare()
    r.apply_transformation(scale)
    r.apply_transformation(translate)
    r.apply_material(lc1_material)
    objects.append(r)
    
    translate = t.get_translation(r.vertices[1].coordinates[:3])
    r = obj.UnitSquare()
    r.apply_transformation(scale)
    r.apply_transformation(translate)
    r.apply_material(lc2_material)
    objects.append(r)
    
    translate = t.get_translation(r.vertices[1].coordinates[:3])
    r = obj.UnitSquare()
    r.apply_transformation(scale)
    r.apply_transformation(translate)
    r.apply_material(lc1_material)
    objects.append(r)
    
    translate = t.get_translation(r.vertices[1].coordinates[:3])
    r = obj.UnitSquare()
    r.apply_transformation(scale)
    r.apply_transformation(translate)
    r.apply_material(lc2_material)
    objects.append(r)
    
    '''
    ## Linha de Chegada:
    translate = t.get_translation(r.vertices[3].coordinates[:3])
    r = obj.UnitSquare()
    r.apply_transformation(scale)
    r.apply_transformation(translate)
    r.apply_material(lc2_material)
    objects.append(r)

    translate = t.get_translation(r.vertices[0].coordinates[:3] - [0,0,1.25])
    r = obj.UnitSquare()
    r.apply_transformation(scale)
    r.apply_transformation(translate)
    r.apply_material(lc1_material)
    objects.append(r)
    
    r = obj.UnitSquare()
    r.apply_transformation(scale)
    r.apply_transformation(translate)
    r.apply_material(lc2_material)
    objects.append(r)
    
    r = obj.UnitSquare()
    r.apply_transformation(scale)
    r.apply_transformation(translate)
    r.apply_material(lc1_material)
    objects.append(r)
    '''

    # -- Arquibancadas (GrandStand):
    # Arquibancada reta principal:
    scale = t.get_scale([40, 10, 10, 1])
    translate = t.get_translation([39,0.05,36])
    gs = obj.UnitGrandstand([140/255, 23/255, 23/255]) #Cor das arquibancadas    [1,1,1]
    gs.apply_transformation(scale)
    gs.apply_transformation(translate)
    print("Arquibancada Reta Principal:")
    gs.printVertices()
    objects.append(gs)

    # Cobertura Arquibancada reta principal:
    scale = t.get_scale([40, 2, 10, 1])
    translate = t.get_translation(gs.vertices[0].coordinates[:3] + [0,10,0])
    cobertura = obj.UnitSquare()
    cobertura.apply_transformation(scale)
    cobertura.apply_transformation(translate)
    print("Cobertura:")
    cobertura.printVertices()
    objects.append(cobertura)


    # Arquibancada reta antes principal:
    rotate = t.get_rotation(90, 'y')
    gs = obj.UnitGrandstand([207/255, 181/255, 59/255]) #Cor das arquibancadas  [1,1,1]
    gs.apply_transformation(rotate)
    #gs.printVertices()
    translate = t.get_translation([0,0,1])
    gs.apply_transformation(translate)
    #gs.printVertices()
    
    scale = t.get_scale([10, 10, 30, 1])
    gs.apply_transformation(scale)
      
    translate = t.get_translation([11,0,55])
    gs.apply_transformation(translate)
    #gs.printVertices()
    objects.append(gs)      

    # POSTE:
    scale = t.get_scale([3,1,3,1])
    translate = t.get_translation([32,0.05,45]) 
    base = obj.UnitSquare()
    base.apply_transformation(scale)
    base.apply_transformation(translate)

    scale = t.get_scale([1,10,1,1])
    translate = t.get_translation(base.vertices[0].coordinates[:3] + [1,1,1])
    poste = obj.UnitSquare()
    poste.apply_transformation(scale)
    poste.apply_transformation(translate)

    objects.append(base)
    objects.append(poste)

    print("Primeiro Poste:")
    poste.printVertices()

    
    # POSTE:
    scale = t.get_scale([3,1,3,1])
    translate = t.get_translation([85,0.05,45])
    base = obj.UnitSquare()
    base.apply_transformation(scale)
    base.apply_transformation(translate)

    scale = t.get_scale([1,10,1,1])
    translate = t.get_translation(base.vertices[0].coordinates[:3] + [1,1,1])
    poste = obj.UnitSquare()
    poste.apply_transformation(scale)
    poste.apply_transformation(translate)
       
    print ("Segundo Poste:")
    poste.printVertices()

    objects.append(base)
    objects.append(poste)
    
        
    return objects



def main():
    d = 0.2
    #d = 1
    window_height = 1
    window_width = 1
    pixels_height = 200
    pixels_width = 200

    objects = circuit()

    lights = []
    
    # Luz do Poste 1
    punctual_light = PunctualLightSource(intensity=[1., 1., 1.], position=[34, 11.2, 50])
    lights.append(punctual_light)
    #spot_light = SpotLightSource(intensity=[1, 1, 1], position=[33, 11.1, 48], direction=[33, 0, 55], theta=15)
    #lights.append(spot_light)

    # Luz do Poste 2
    punctual_light = PunctualLightSource(intensity=[1., 1., 1.], position=[88, 11.2, 50])
    lights.append(punctual_light)
    #spot_light = SpotLightSource(intensity=[1, 1, 1], position=[86, 11.1, 48], direction=[86, 5, 55], theta=15)
    #lights.append(spot_light)
    
    # Posições do Observador:
    # VISTA SUPERIOR, X POSITIVO PARA ESQUERDA Oo
    #po = [50,60,50, 1.]
    #look_at = np.array([50,0,50, 1.])
    #a_vup = look_at + [-2,0,2, 0]
    
    # VISTA RETA PRINCIPAL ANTES PRIMEIRO POSTE:
    po = [27, 2, 53]
    look_at = np.array([38, 1, 53])
    a_vup = look_at + [0, 1, 0.]

    # VISTA ARQUIBANCADA:
    #po = [44,6,44]
    #look_at = np.array([45, 1, 48])
    #a_vup = look_at + [0, 1, 0.]

    p = "PERSPECTIVE"
    #ob = "OBLIQUE"
    #cb = "CABINET"
    #cv = "CAVALIER"
    #ort = "ORTHOGRAPHIC"

    projection_type = p

    scenario = Scenario(objects=objects, light_sources=lights,po=po, look_at=look_at, a_vup=a_vup, background_color=[5/255, 154/255, 244/255],ambient_light=[0., 0., 0.])

    window = Window(window_width, window_height, d, pixels_width, pixels_height) 

    scenario.render(window=window, threads=True, shadow=True, projection_type=projection_type, oblique_angle=45, oblique_factor=1)

    
if __name__ == '__main__':
    main()
