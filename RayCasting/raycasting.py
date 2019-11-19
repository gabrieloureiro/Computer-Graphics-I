# Importar arquivos do projeto.
from python.raycaster.auxi import RGB
from python.raycaster.light import FocalLight, FarLight, SpotLight
from python.raycaster.object import Material, Texture
from python.raycaster.object.surface import *
from python.raycaster.physics import *
from python.raycaster.scene import Scene, Observer
# Importar bibliotecas.
from PIL import Image, ImageDraw, ImageTk
import time
import tkinter as tk

print ("\n#######################################################################\n\t\t\tEQUIPE 01:\n\n>>> Executando Projeto RayCasting... Por favor, aguarde a renderização.\n\n#######################################################################")

# Cores
mode = 'RGB'
colors = {
    "white": (255, 255, 255),
    "black": (0, 0, 0),
    "light_blue": (100, 149, 237),
    "dark_blue": (50, 50, 200),
    "navy_blue": (0, 0, 128),
    "light_green": (46, 204, 113),
    "dark_green": (24, 102, 56),
    "red": (255, 0, 0),
    "orange": (255, 165, 0),
    "yellow": (247, 202, 24),
    "brown": (94, 77, 41),
    "magenta": (202, 31, 123),
    "wood": (92, 51, 23),
    "leaf": (5, 255, 5),
    "plastic_red":(255, 13, 66)
}

# Configurações
resolution = (500, 500)
image = Image.new(mode=mode, size=resolution)
pen = ImageDraw.Draw(image)

# Cenário
'''
                                        VISÃO PANORÂMICA FRONTAL
'''
observer = Observer.a(Point(155, 40, 75), Point(140, 30, 60), resolution, size=(99,99))

'''
                                        VISÃO DO FUNDO DO CENÁRIO
'''
#observer = Observer.a(Point(-40, 40, 75), Point(-20, 30, 60), resolution, size=(99,99))

'''
                                        VISÃO SUPERIOR AO CENÁRIO
'''
#observer = Observer.a(Point(55, 150, 35), Point(55, 120, 35), resolution, size=(99,99))

'''
                                        VISÃO SUPERIOR AO CAMPO
'''
#observer = Observer.a(Point(55, 60, 35), Point(55, 30, 35), resolution, size=(99,99))
'''
'''
#Instânciando cenário
scene = Scene()
background_color = colors["light_blue"]

''' 
>   >   >   >   >   >   >   >   >   >   OBJETOS   <   <   <   <   <   <   <   <   <   <   <   
'''

'''
#                    $$                 CHÃO DO CENÁRIO
'''
scene.add_obj("Chão", Material(
    Plane(Point(0, 0, 0), Vector(0, 1, 0)),
    Texture(amb_color=RGB(0, 0, 0), dif_color=RGB(94, 77, 41), spe_color=RGB(94, 77, 41), shine=0.85)))

'''
#                    $$                 CAMPO
'''
#
'''
#                    $$                 TRAVE 1
'''
scene.add_obj("Trave_1_Esq", Material(
    Cylinder(Point(30, 0, 30),Vector(0,6.5,0),1, 0.5),
    Texture(amb_color=RGB(255, 255, 255), dif_color=RGB(255, 255, 255), spe_color=RGB(255, 255, 255), shine=0.78)))

scene.add_obj("Trave_1_Dir", Material(
    Cylinder(Point(30, 0, 40),Vector(0,6.5,0),1, 0.5),
    Texture(amb_color=RGB(255, 255, 255), dif_color=RGB(255, 255, 255), spe_color=RGB(255, 255, 255), shine=0.78)))

scene.add_obj("Trave_1_Sup", Material(
    Cylinder(Point(30, 6.25, 30),Vector(0,0,10),1, 0.5),
    Texture(amb_color=RGB(255, 255, 255), dif_color=RGB(255, 255, 255), spe_color=RGB(255, 255, 255), shine=0.78)))

'''
#                    $$                 TRAVE 2
'''
scene.add_obj("Trave_2_Esq", Material(
    Cylinder(Point(80, 0, 30),Vector(0,6.5,0),1, 0.5),
    Texture(amb_color=RGB(255, 255, 255), dif_color=RGB(255, 255, 255), spe_color=RGB(255, 255, 255), shine=0.78)))

scene.add_obj("Trave_2_Dir", Material(
    Cylinder(Point(80, 0, 40),Vector(0,6.5,0),1, 0.5),
    Texture(amb_color=RGB(255, 255, 255), dif_color=RGB(255, 255, 255), spe_color=RGB(255, 255, 255), shine=0.78)))

scene.add_obj("Trave_2_Sup", Material(
    Cylinder(Point(80, 6.25, 30),Vector(0,0,10),1, 0.5),
    Texture(amb_color=RGB(255, 255, 255), dif_color=RGB(255, 255, 255), spe_color=RGB(255, 255, 255), shine=0.78)))
'''
#                    $$                 MARCAÇÕES DO CAMPO
'''
scene.add_obj("Linha_Inf", Material(
    Cylinder(Point(15,-0.1,15),Vector(80,0,0),0.1, 0.17),
    Texture(amb_color=RGB(255, 255, 255), dif_color=RGB(255, 255, 255), spe_color=RGB(255, 255, 255), shine=1)))

scene.add_obj("Linha_Sup", Material(
    Cylinder(Point(15,-0.1,55),Vector(80,0,0),0.1, 0.17),
    Texture(amb_color=RGB(255, 255, 255), dif_color=RGB(255, 255, 255), spe_color=RGB(255, 255, 255), shine=1)))

scene.add_obj("Linha_Esq", Material(
    Cylinder(Point(15,-0.1,15),Vector(0,0,40),0.1, 0.17),
    Texture(amb_color=RGB(255, 255, 255), dif_color=RGB(255, 255, 255), spe_color=RGB(255, 255, 255), shine=1)))

scene.add_obj("Linha_Central", Material(
    Cylinder(Point(55,-0.1,15),Vector(0,0,40),0.1, 0.17),
    Texture(amb_color=RGB(255, 255, 255), dif_color=RGB(255, 255, 255), spe_color=RGB(255, 255, 255), shine=1)))

scene.add_obj("Linha_Dir", Material(
    Cylinder(Point(95,-0.1,15),Vector(0,0,40),0.1, 0.17),
    Texture(amb_color=RGB(255, 255, 255), dif_color=RGB(255, 255, 255), spe_color=RGB(255, 255, 255), shine=1)))

'''
#                    $$                 BOLA
'''
scene.add_obj("Bola", Material(
    Sphere(Point(35, 1.1, 43), 1),
    Texture(amb_color=RGB(66, 13, 66), dif_color=RGB(127, 127, 127), spe_color=RGB(178, 78, 178), shine=0.78)))

'''
#                    $$                 ÁRVORE FRONDOSA
'''
scene.add_obj("Folhas_Arvore_1", Material(
    Cone(Point(10, 8, 70),Point(10,15,70), 5),
    Texture(amb_color=RGB(5, 255, 5), dif_color=RGB(1, 255, 1), spe_color=RGB(230, 255, 230), shine=0.58)))

scene.add_obj("Tronco_Arvore_1", Material(
    Cylinder(Point(10, 0, 70),Vector(0,8,0),1,3),
    Texture(amb_color=RGB(92, 51, 23), dif_color=RGB(92, 51, 23), spe_color=RGB(92, 51, 23), shine=0.78)))
'''
#                    $$                 ÁRVORE SECA
'''
scene.add_obj("Tronco_Arvore_2", Material(
    Cylinder(Point(10, 0, 10),Vector(0,8,0),1,3),
    Texture(amb_color=RGB(92, 51, 23), dif_color=RGB(92, 51, 23), spe_color=RGB(92, 51, 23), shine=0.78)))
'''
#                    $$                 CERCA
'''
'''
#Colunas
'''
scene.add_obj("Cerca_Fundo_Lat", Material(
    Cylinder(Point(0, 0, 0),Vector(0,13,0),1,1),
    Texture(amb_color=RGB(130,130,130), dif_color=RGB(160,160,160), spe_color=RGB(180,180,180), shine=0.40)))

scene.add_obj("Cerca_Fundo_Arq", Material(
    Cylinder(Point(0, 0, 80),Vector(0,13,0),1,1),
    Texture(amb_color=RGB(130,130,130), dif_color=RGB(160,160,160), spe_color=RGB(180,180,180), shine=0.40)))

scene.add_obj("Cerca_Frente_Arq", Material(
    Cylinder(Point(135, 0, 80),Vector(0,13,0),1,1),
    Texture(amb_color=RGB(130,130,130), dif_color=RGB(160,160,160), spe_color=RGB(180,180,180), shine=0.40)))

scene.add_obj("Cerca_Frente_Lat", Material(
    Cylinder(Point(135, 0, 0),Vector(0,13,0),1,1),
    Texture(amb_color=RGB(130,130,130), dif_color=RGB(160,160,160), spe_color=RGB(180,180,180), shine=0.40)))

scene.add_obj("Cerca_Frente_1", Material(
    Cylinder(Point(135, 0, 35),Vector(0,13,0),1,1),
    Texture(amb_color=RGB(130,130,130), dif_color=RGB(160,160,160), spe_color=RGB(180,180,180), shine=0.40)))

scene.add_obj("Cerca_Frente_2", Material(
    Cylinder(Point(155, 0, 35),Vector(0,13,0),1,0.5),
    Texture(amb_color=RGB(130,130,130), dif_color=RGB(160,160,160), spe_color=RGB(180,180,180), shine=0.40)))
'''
#Fundo
'''

scene.add_obj("Cerca_Fundo_H1", Material(
    Cylinder(Point(0,-0.1,0),Vector(0,0,80),0.1, 0.17),
    Texture(amb_color=RGB(130,130,130), dif_color=RGB(160,160,160), spe_color=RGB(180,180,180), shine=0.40)))
    
scene.add_obj("Cerca_Fundo_H2", Material(
    Cylinder(Point(0,1,0),Vector(0,0,80),0.1, 0.17),
    Texture(amb_color=RGB(130,130,130), dif_color=RGB(160,160,160), spe_color=RGB(180,180,180), shine=0.40)))

scene.add_obj("Cerca_Fundo_H3", Material(
    Cylinder(Point(0,2,0),Vector(0,0,80),0.1, 0.17),
    Texture(amb_color=RGB(130,130,130), dif_color=RGB(160,160,160), spe_color=RGB(180,180,180), shine=0.40)))

scene.add_obj("Cerca_Fundo_H4", Material(
    Cylinder(Point(0,3,0),Vector(0,0,80),0.1, 0.17),
    Texture(amb_color=RGB(130,130,130), dif_color=RGB(160,160,160), spe_color=RGB(180,180,180), shine=0.40)))

scene.add_obj("Cerca_Fundo_H5", Material(
    Cylinder(Point(0,4,0),Vector(0,0,80),0.1, 0.17),
    Texture(amb_color=RGB(130,130,130), dif_color=RGB(160,160,160), spe_color=RGB(180,180,180), shine=0.40)))

scene.add_obj("Cerca_Fundo_H6", Material(
    Cylinder(Point(0,5,0),Vector(0,0,80),0.1, 0.17),
    Texture(amb_color=RGB(130,130,130), dif_color=RGB(160,160,160), spe_color=RGB(180,180,180), shine=0.40)))

scene.add_obj("Cerca_Fundo_H7", Material(
    Cylinder(Point(0,6,0),Vector(0,0,80),0.1, 0.17),
    Texture(amb_color=RGB(130,130,130), dif_color=RGB(160,160,160), spe_color=RGB(180,180,180), shine=0.40)))

scene.add_obj("Cerca_Fundo_H8", Material(
    Cylinder(Point(0,7,0),Vector(0,0,80),0.1, 0.17),
    Texture(amb_color=RGB(130,130,130), dif_color=RGB(160,160,160), spe_color=RGB(180,180,180), shine=0.40)))

scene.add_obj("Cerca_Fundo_H9", Material(
    Cylinder(Point(0,8,0),Vector(0,0,80),0.1, 0.17),
    Texture(amb_color=RGB(130,130,130), dif_color=RGB(160,160,160), spe_color=RGB(180,180,180), shine=0.40)))

scene.add_obj("Cerca_Fundo_H10", Material(
    Cylinder(Point(0,9,0),Vector(0,0,80),0.1, 0.17),
    Texture(amb_color=RGB(130,130,130), dif_color=RGB(160,160,160), spe_color=RGB(180,180,180), shine=0.40)))

scene.add_obj("Cerca_Fundo_H11", Material(
    Cylinder(Point(0,10,0),Vector(0,0,80),0.1, 0.17),
    Texture(amb_color=RGB(130,130,130), dif_color=RGB(160,160,160), spe_color=RGB(180,180,180), shine=0.40)))

scene.add_obj("Cerca_Fundo_H12", Material(
    Cylinder(Point(0,11,0),Vector(0,0,80),0.1, 0.17),
    Texture(amb_color=RGB(130,130,130), dif_color=RGB(160,160,160), spe_color=RGB(180,180,180), shine=0.40)))

scene.add_obj("Cerca_Fundo_H13", Material(
    Cylinder(Point(0,12,0),Vector(0,0,80),0.1, 0.17),
    Texture(amb_color=RGB(130,130,130), dif_color=RGB(160,160,160), spe_color=RGB(180,180,180), shine=0.40)))
'''
#Lateral
'''
scene.add_obj("Cerca_Fundo_Lat_H1", Material(
    Cylinder(Point(0,-0.1,0),Vector(135,0,0),0.1, 0.17),
    Texture(amb_color=RGB(130,130,130), dif_color=RGB(160,160,160), spe_color=RGB(180,180,180), shine=0.40)))
    
scene.add_obj("Cerca_Fundo_Lat_H2", Material(
    Cylinder(Point(0,1,0),Vector(135,0,0),0.1, 0.17),
    Texture(amb_color=RGB(130,130,130), dif_color=RGB(160,160,160), spe_color=RGB(180,180,180), shine=0.40)))

scene.add_obj("Cerca_Fundo_Lat_H3", Material(
    Cylinder(Point(0,2,0),Vector(135,0,0),0.1, 0.17),
    Texture(amb_color=RGB(130,130,130), dif_color=RGB(160,160,160), spe_color=RGB(180,180,180), shine=0.40)))

scene.add_obj("Cerca_Fundo_Lat_H4", Material(
    Cylinder(Point(0,3,0),Vector(135,0,0),0.1, 0.17),
    Texture(amb_color=RGB(130,130,130), dif_color=RGB(160,160,160), spe_color=RGB(180,180,180), shine=0.40)))

scene.add_obj("Cerca_Fundo_Lat_H5", Material(
    Cylinder(Point(0,4,0),Vector(135,0,0),0.1, 0.17),
    Texture(amb_color=RGB(130,130,130), dif_color=RGB(160,160,160), spe_color=RGB(180,180,180), shine=0.40)))

scene.add_obj("Cerca_Fundo_Lat_H6", Material(
    Cylinder(Point(0,5,0),Vector(135,0,0),0.1, 0.17),
    Texture(amb_color=RGB(130,130,130), dif_color=RGB(160,160,160), spe_color=RGB(180,180,180), shine=0.40)))

scene.add_obj("Cerca_Fundo_Lat_H7", Material(
    Cylinder(Point(0,6,0),Vector(135,0,0),0.1, 0.17),
    Texture(amb_color=RGB(130,130,130), dif_color=RGB(160,160,160), spe_color=RGB(180,180,180), shine=0.40)))

scene.add_obj("Cerca_Fundo_Lat_H8", Material(
    Cylinder(Point(0,7,0),Vector(135,0,0),0.1, 0.17),
    Texture(amb_color=RGB(130,130,130), dif_color=RGB(160,160,160), spe_color=RGB(180,180,180), shine=0.40)))

scene.add_obj("Cerca_Fundo_Lat_H9", Material(
    Cylinder(Point(0,8,0),Vector(135,0,0),0.1, 0.17),
    Texture(amb_color=RGB(130,130,130), dif_color=RGB(160,160,160), spe_color=RGB(180,180,180), shine=0.40)))

scene.add_obj("Cerca_Fundo_Lat_H10", Material(
    Cylinder(Point(0,9,0),Vector(135,0,0),0.1, 0.17),
    Texture(amb_color=RGB(130,130,130), dif_color=RGB(160,160,160), spe_color=RGB(180,180,180), shine=0.40)))

scene.add_obj("Cerca_Fundo_Lat_H11", Material(
    Cylinder(Point(0,10,0),Vector(135,0,0),0.1, 0.17),
    Texture(amb_color=RGB(130,130,130), dif_color=RGB(160,160,160), spe_color=RGB(180,180,180), shine=0.40)))

scene.add_obj("Cerca_Fundo_Lat_H12", Material(
    Cylinder(Point(0,11,0),Vector(135,0,0),0.1, 0.17),
    Texture(amb_color=RGB(130,130,130), dif_color=RGB(160,160,160), spe_color=RGB(180,180,180), shine=0.40)))

scene.add_obj("Cerca_Fundo_Lat_H13", Material(
    Cylinder(Point(0,12,0),Vector(135,0,0),0.1, 0.17),
    Texture(amb_color=RGB(130,130,130), dif_color=RGB(160,160,160), spe_color=RGB(180,180,180), shine=0.40)))

'''
#Frente
'''
scene.add_obj("Cerca_Frente_H1", Material(
    Cylinder(Point(135,-0.1,80),Vector(0,0,-45),0.1, 0.17),
    Texture(amb_color=RGB(130,130,130), dif_color=RGB(160,160,160), spe_color=RGB(180,180,180), shine=0.40)))
    
scene.add_obj("Cerca_Frente_H2", Material(
    Cylinder(Point(135,1,80),Vector(0,0,-45),0.1, 0.17),
    Texture(amb_color=RGB(130,130,130), dif_color=RGB(160,160,160), spe_color=RGB(180,180,180), shine=0.40)))

scene.add_obj("Cerca_Frente_H3", Material(
    Cylinder(Point(135,2,80),Vector(0,0,-45),0.1, 0.17),
    Texture(amb_color=RGB(130,130,130), dif_color=RGB(160,160,160), spe_color=RGB(180,180,180), shine=0.40)))

scene.add_obj("Cerca_Frente_H4", Material(
    Cylinder(Point(135,3,80),Vector(0,0,-45),0.1, 0.17),
    Texture(amb_color=RGB(130,130,130), dif_color=RGB(160,160,160), spe_color=RGB(180,180,180), shine=0.40)))

scene.add_obj("Cerca_Frente_H5", Material(
    Cylinder(Point(135,4,80),Vector(0,0,-45),0.1, 0.17),
    Texture(amb_color=RGB(130,130,130), dif_color=RGB(160,160,160), spe_color=RGB(180,180,180), shine=0.40)))

scene.add_obj("Cerca_Frente_H6", Material(
    Cylinder(Point(135,5,80),Vector(0,0,-45),0.1, 0.17),
    Texture(amb_color=RGB(130,130,130), dif_color=RGB(160,160,160), spe_color=RGB(180,180,180), shine=0.40)))

scene.add_obj("Cerca_Frente_H7", Material(
    Cylinder(Point(135,6,80),Vector(0,0,-45),0.1, 0.17),
    Texture(amb_color=RGB(130,130,130), dif_color=RGB(160,160,160), spe_color=RGB(180,180,180), shine=0.40)))

scene.add_obj("Cerca_Frente_H8", Material(
    Cylinder(Point(135,7,80),Vector(0,0,-45),0.1, 0.17),
    Texture(amb_color=RGB(130,130,130), dif_color=RGB(160,160,160), spe_color=RGB(180,180,180), shine=0.40)))

scene.add_obj("Cerca_Frente_H9", Material(
    Cylinder(Point(135,8,80),Vector(0,0,-45),0.1, 0.17),
    Texture(amb_color=RGB(130,130,130), dif_color=RGB(160,160,160), spe_color=RGB(180,180,180), shine=0.40)))

scene.add_obj("Cerca_Frente_H10", Material(
    Cylinder(Point(135,9,80),Vector(0,0,-45),0.1, 0.17),
    Texture(amb_color=RGB(130,130,130), dif_color=RGB(160,160,160), spe_color=RGB(180,180,180), shine=0.40)))

scene.add_obj("Cerca_Frente_H11", Material(
    Cylinder(Point(135,10,80),Vector(0,0,-45),0.1, 0.17),
    Texture(amb_color=RGB(130,130,130), dif_color=RGB(160,160,160), spe_color=RGB(180,180,180), shine=0.40)))

scene.add_obj("Cerca_Frente_H12", Material(
    Cylinder(Point(135,11,80),Vector(0,0,-45),0.1, 0.17),
    Texture(amb_color=RGB(130,130,130), dif_color=RGB(160,160,160), spe_color=RGB(180,180,180), shine=0.40)))

scene.add_obj("Cerca_Frente_H13", Material(
    Cylinder(Point(135,12,80),Vector(0,0,-45),0.1, 0.17),
    Texture(amb_color=RGB(130,130,130), dif_color=RGB(160,160,160), spe_color=RGB(180,180,180), shine=0.40)))

'''
PORTÃO
'''
scene.add_obj("Cerca_Portao_H1", Material(
    Cylinder(Point(155,-0.1,35),Vector(-20,0,-35),0.1, 0.17),
    Texture(amb_color=RGB(130,130,130), dif_color=RGB(160,160,160), spe_color=RGB(180,180,180), shine=0.40)))
    
scene.add_obj("Cerca_Portao_H2", Material(
    Cylinder(Point(155,1,35),Vector(-20,0,-35),0.1, 0.17),
    Texture(amb_color=RGB(130,130,130), dif_color=RGB(160,160,160), spe_color=RGB(180,180,180), shine=0.40)))

scene.add_obj("Cerca_Portao_H3", Material(
    Cylinder(Point(155,2,35),Vector(-20,0,-35),0.1, 0.17),
    Texture(amb_color=RGB(130,130,130), dif_color=RGB(160,160,160), spe_color=RGB(180,180,180), shine=0.40)))

scene.add_obj("Cerca_Portao_H4", Material(
    Cylinder(Point(155,3,35),Vector(-20,0,-35),0.1, 0.17),
    Texture(amb_color=RGB(130,130,130), dif_color=RGB(160,160,160), spe_color=RGB(180,180,180), shine=0.40)))

scene.add_obj("Cerca_Portao_H5", Material(
    Cylinder(Point(155,4,35),Vector(-20,0,-35),0.1, 0.17),
    Texture(amb_color=RGB(130,130,130), dif_color=RGB(160,160,160), spe_color=RGB(180,180,180), shine=0.40)))

scene.add_obj("Cerca_Portao_H6", Material(
    Cylinder(Point(155,5,35),Vector(-20,0,-35),0.1, 0.17),
    Texture(amb_color=RGB(130,130,130), dif_color=RGB(160,160,160), spe_color=RGB(180,180,180), shine=0.40)))

scene.add_obj("Cerca_Portao_H7", Material(
    Cylinder(Point(155,6,35),Vector(-20,0,-35),0.1, 0.17),
    Texture(amb_color=RGB(130,130,130), dif_color=RGB(160,160,160), spe_color=RGB(180,180,180), shine=0.40)))

scene.add_obj("Cerca_Portao_H8", Material(
    Cylinder(Point(155,7,35),Vector(-20,0,-35),0.1, 0.17),
    Texture(amb_color=RGB(130,130,130), dif_color=RGB(160,160,160), spe_color=RGB(180,180,180), shine=0.40)))

scene.add_obj("Cerca_Portao_H9", Material(
    Cylinder(Point(155,8,35),Vector(-20,0,-35),0.1, 0.17),
    Texture(amb_color=RGB(130,130,130), dif_color=RGB(160,160,160), spe_color=RGB(180,180,180), shine=0.40)))

scene.add_obj("Cerca_Portao_H10", Material(
    Cylinder(Point(155,9,35),Vector(-20,0,-35),0.1, 0.17),
    Texture(amb_color=RGB(130,130,130), dif_color=RGB(160,160,160), spe_color=RGB(180,180,180), shine=0.40)))

scene.add_obj("Cerca_Portao_H11", Material(
    Cylinder(Point(155,10,35),Vector(-20,0,-35),0.1, 0.17),
    Texture(amb_color=RGB(130,130,130), dif_color=RGB(160,160,160), spe_color=RGB(180,180,180), shine=0.40)))

scene.add_obj("Cerca_Portao_H12", Material(
    Cylinder(Point(155,11,35),Vector(-20,0,-35),0.1, 0.17),
    Texture(amb_color=RGB(130,130,130), dif_color=RGB(160,160,160), spe_color=RGB(180,180,180), shine=0.40)))

scene.add_obj("Cerca_Portao_H13", Material(
    Cylinder(Point(155,12,35),Vector(-20,0,-35),0.1, 0.17),
    Texture(amb_color=RGB(130,130,130), dif_color=RGB(160,160,160), spe_color=RGB(180,180,180), shine=0.40)))

'''
#Lateral da arquibancada
'''
scene.add_obj("Cerca_Arq_H1", Material(
    Cylinder(Point(0,-0.1,80),Vector(135,0,0),0.1, 0.17),
    Texture(amb_color=RGB(130,130,130), dif_color=RGB(160,160,160), spe_color=RGB(180,180,180), shine=0.40)))
    
scene.add_obj("Cerca_Arq_H2", Material(
    Cylinder(Point(0,1,80),Vector(135,0,0),0.1, 0.17),
    Texture(amb_color=RGB(130,130,130), dif_color=RGB(160,160,160), spe_color=RGB(180,180,180), shine=0.40)))

scene.add_obj("Cerca_Arq_H3", Material(
    Cylinder(Point(0,2,80),Vector(135,0,0),0.1, 0.17),
    Texture(amb_color=RGB(130,130,130), dif_color=RGB(160,160,160), spe_color=RGB(180,180,180), shine=0.40)))

scene.add_obj("Cerca_Arq_H4", Material(
    Cylinder(Point(0,3,80),Vector(135,0,0),0.1, 0.17),
    Texture(amb_color=RGB(130,130,130), dif_color=RGB(160,160,160), spe_color=RGB(180,180,180), shine=0.40)))

scene.add_obj("Cerca_Arq_H5", Material(
    Cylinder(Point(0,4,80),Vector(135,0,0),0.1, 0.17),
    Texture(amb_color=RGB(130,130,130), dif_color=RGB(160,160,160), spe_color=RGB(180,180,180), shine=0.40)))

scene.add_obj("Cerca_Arq_H6", Material(
    Cylinder(Point(0,5,80),Vector(135,0,0),0.1, 0.17),
    Texture(amb_color=RGB(130,130,130), dif_color=RGB(160,160,160), spe_color=RGB(180,180,180), shine=0.40)))

scene.add_obj("Cerca_Arq_H7", Material(
    Cylinder(Point(0,6,80),Vector(135,0,0),0.1, 0.17),
    Texture(amb_color=RGB(130,130,130), dif_color=RGB(160,160,160), spe_color=RGB(180,180,180), shine=0.40)))

scene.add_obj("Cerca_Arq_H8", Material(
    Cylinder(Point(0,7,80),Vector(135,0,0),0.1, 0.17),
    Texture(amb_color=RGB(130,130,130), dif_color=RGB(160,160,160), spe_color=RGB(180,180,180), shine=0.40)))

scene.add_obj("Cerca_Arq_H9", Material(
    Cylinder(Point(0,8,80),Vector(135,0,0),0.1, 0.17),
    Texture(amb_color=RGB(130,130,130), dif_color=RGB(160,160,160), spe_color=RGB(180,180,180), shine=0.40)))

scene.add_obj("Cerca_Arq_H10", Material(
    Cylinder(Point(0,9,80),Vector(135,0,0),0.1, 0.17),
    Texture(amb_color=RGB(130,130,130), dif_color=RGB(160,160,160), spe_color=RGB(180,180,180), shine=0.40)))

scene.add_obj("Cerca_Arq_H11", Material(
    Cylinder(Point(0,10,80),Vector(135,0,0),0.1, 0.17),
    Texture(amb_color=RGB(130,130,130), dif_color=RGB(160,160,160), spe_color=RGB(180,180,180), shine=0.40)))

scene.add_obj("Cerca_Arq_H12", Material(
    Cylinder(Point(0,11,80),Vector(135,0,0),0.1, 0.17),
    Texture(amb_color=RGB(130,130,130), dif_color=RGB(160,160,160), spe_color=RGB(180,180,180), shine=0.40)))

scene.add_obj("Cerca_Arq_H13", Material(
    Cylinder(Point(0,12,80),Vector(135,0,0),0.1, 0.17),
    Texture(amb_color=RGB(130,130,130), dif_color=RGB(160,160,160), spe_color=RGB(180,180,180), shine=0.40)))

'''
                    $$                  Alarme
'''
scene.add_obj("Alarme", Material(
    Sphere(Point(120, 5, 55), 1.5),
    Texture(amb_color=RGB(255, 13, 66), dif_color=RGB(255, 127, 127), spe_color=RGB(255, 78, 178), shine=0.78)))
'''
>   >   >   >   >   >   >   >   >   >   FONTES DE LUZ
'''
scene.add_light("Sol", FarLight(
    direction=Vector(0, -10, 35),
    amb_light=RGB(0, 10, 44), dif_light=RGB(150, 150, 150), spe_light=RGB(255, 255, 255)))


scene.add_light("Luz Spot", SpotLight(
    origin=Point(55, 15, 35), direction=Vector(0, -14, 0), angle=60,
    amb_light=RGB(50, 25, 25), dif_light=RGB(255, 100, 100), spe_light=RGB(255, 120, 120)))

# scene.add_light("Alarme", FocalLight(
#     origin=Point(120, 5, 55),
#     amb_light=RGB(215, 10, 6), dif_light=RGB(215, 10, 6), spe_light=RGB(215, 10, 6)))


#     amb_light=RGB(215, 10, 6), dif_light=RGB(215, 100, 30), spe_light=RGB(215, 130, 48)))


'''
>>>     EXECUÇÃO DO RAYCAST
'''
# Executar o raycast e desenhar na tela.
for y_index in range(resolution[1]):
    for x_index in range(resolution[0]):
        line = observer.shoot(x_index, y_index)
        min_coef = None
        min_obj = None

        for obj_name in scene.objects:
            # Check if visibility is enabled for that object.
            if scene.objects[obj_name][1]:
                result = scene.objects[obj_name][0].surface.intersection(line)
                if result and (min_coef is None or result < min_coef):
                    min_coef = result
                    min_obj = obj_name

        if min_obj:
            color = RGB(0, 0, 0)
            for light_name in scene.lights:
                color += scene.lights[light_name][0].illuminate(scene.objects[min_obj][0], line(min_coef), observer)
        else:
            # Cor a ser desenhada = cor do plano de fundo.
            color = RGB(0, 0, 0)
            for light_name in scene.lights:
                color += RGB(0, 0, 128) * scene.lights[light_name][0].amb_light

        pen.point((x_index, y_index), color.tuple)

# Save image.
image_path = '../Debug/'
image_name = time.strftime("%Y-%m-%d %H-%M-%S") + '.png'
image.save(image_path + image_name)


# Setup.
def onclick(event):
    print("\n>>>@>>>@>>>\nClique: ({0}, {1})\n".format(event.x, event.y))
    line = observer.shoot(event.x, event.y)
    min_coef = None
    min_obj = None

    for obj_name in scene.objects:
        # Check if visibility is enabled for that object.
        if scene.objects[obj_name][1]:
            result = scene.objects[obj_name][0].surface.intersection(line)
            if result and (min_coef is None or result < min_coef):
                min_coef = result
                min_obj = obj_name

            p = line(result) if result is not None else None
            print("{0} ('{1}', {2}) @ {3} {4}\n".format(
                obj_name,
                scene.objects[obj_name][0].surface.__class__.__name__,
                "Visível" if scene.objects[obj_name][1] else "Invisível",
                "Ponto: ({0:0.2f}, {1:0.2f}, {2:0.2f})".format(p.x, p.y, p.z) if p is not None else None,
                "Coef: {0:0.5f}".format(result) if result is not None else "")
            )

    if min_obj:
        color = RGB(0, 0, 0)
        for light_name in scene.lights:
            color += scene.lights[light_name][0].illuminate(scene.objects[min_obj][0], line(min_coef), observer)
        print("Interseção: {0}, Cor: {1}\n".format(min_obj, color))
    else:
        # Cor a ser desenhada = cor do plano de fundo.
        color = RGB(0, 0, 0)
        for light_name in scene.lights:
            color += RGB(0, 0, 128) * scene.lights[light_name][0].amb_light
        print("Interseção: Plano de Fundo, Cor: {0}\n".format(color))


root = tk.Tk()
root.title("RayCaster >>> EQUIPE_O1")
root.bind("<Button-1>", onclick)
canvas = tk.Canvas(master=root, width=resolution[0], height=resolution[1])
canvas.pack()
# Carregar imagem na janela.
photo_image = ImageTk.PhotoImage(image, master=root)
photo_id = canvas.create_image((0, 0), image=photo_image, anchor=tk.NW)
# Abrir janela.
root.mainloop()
