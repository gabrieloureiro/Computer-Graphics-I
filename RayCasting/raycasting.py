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
    "magenta": (202, 31, 123)
}

# Configurações
resolution = (500, 500)
image = Image.new(mode=mode, size=resolution)
pen = ImageDraw.Draw(image)

# Cenário
observer = Observer.a(Point(20, 60, -20), Point(35, 30, 0), resolution, size=(99,99))
'''
                                        VISÃO SUPERIOR AO CAMPO
'''
#observer = Observer.a(Point(55, 60, 35), Point(55, 30, 35), resolution, size=(99,99))
'''
'''

scene = Scene()
background_color = colors["light_blue"]

''' OBJETOS '''

'''
                                        CHÃO DO CENÁRIO
'''
scene.add_obj("Chão", Material(
    Plane(Point(0, 0, 0), Vector(0, 1, 0)),
    Texture(amb_color=RGB(0, 0, 0), dif_color=RGB(94, 77, 41), spe_color=RGB(94, 77, 41), shine=0.85)))

'''
                                        CAMPO
'''
#DANTAS IMPLEMENTA O QUADRADOOOOOOOOOOOOOOOOOO
'''
                                        TRAVE 1
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
                                        TRAVE 2
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
                                        MARCAÇÕES DO CAMPO
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
                                        BOLA
'''
scene.add_obj("Bola", Material(
    Sphere(Point(35, 1.1, 43), 1),
    Texture(amb_color=RGB(66, 13, 66), dif_color=RGB(127, 127, 127), spe_color=RGB(178, 78, 178), shine=0.78)))

'''
                                        ÁRVORE 1
'''
scene.add_obj("Folhas_Arvore_1", Material(
    Cone(Point(10, 8, 15),Point(10,15,15), 5),
    Texture(amb_color=RGB(5, 255, 5), dif_color=RGB(1, 255, 1), spe_color=RGB(230, 255, 230), shine=0.58)))

scene.add_obj("Tronco_Arvore_1", Material(
    Cylinder(Point(10, 0, 15),Vector(0,8,0),1,3),
    Texture(amb_color=RGB(92, 51, 23), dif_color=RGB(92, 51, 23), spe_color=RGB(92, 51, 23), shine=0.78)))
'''
'''

# scene.add_light("Luz Focal", FocalLight(
#     origin=Point(50, 0, 35),
#     amb_light=RGB(10, 10, 6), dif_light=RGB(100, 100, 30), spe_light=RGB(180, 180, 48)))

scene.add_light("Luz Far", FarLight(
    direction=Vector(0, -10, 1),
    amb_light=RGB(30, 30, 40), dif_light=RGB(60, 60, 100), spe_light=RGB(90, 90, 120)))

scene.add_light("Luz Spot", SpotLight(
    origin=Point(55, 15, 35), direction=Vector(0, -14, 0), angle=60,
    amb_light=RGB(50, 25, 25), dif_light=RGB(255, 100, 100), spe_light=RGB(255, 120, 120)))

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
