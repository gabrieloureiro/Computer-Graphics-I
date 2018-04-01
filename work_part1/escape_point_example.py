import sys
import copy
sys.path.append("..")
import transformations as t

from obj import *
from scenario import *


def one_escape_point():
    objects = []
    color = [178/255, 34/255, 34/255]
    color_material = Material(color, color, [0.8, 0.8, 0.8], 10)
    
    # Chão:
    scale = t.get_scale([10, 0.1, 10., 1])
    translate = t.get_translation([0.0, 0.0, 0.])
    translate_scale = t.compose([translate, scale])
    floor = UnitSquare()
    floor.apply_transformation(translate_scale)
    floor.apply_material(color_material)
    objects.append(floor)
    print("Chao:")
    floor.printVertices()

    # DIREITA
    translate = t.get_translation([10, 0.1, 0.])
    scale = t.get_scale([0.1, 10, 10, 1])
    translate_scale = t.compose([translate, scale])
    cube = UnitSquare()
    cube.apply_transformation(translate_scale)
    cube.apply_material(color_material)
    objects.append(cube)
    print("Lado direito:")
    cube.printVertices()

    # ESQUERDA
    translate = t.get_translation([-0.1, 0.1, 0.])
    scale = t.get_scale([0.1, 10, 10, 1])
    translate_scale = t.compose([translate, scale])
    cube = UnitSquare()
    cube.apply_transformation(translate_scale)
    cube.apply_material(color_material)
    objects.append(cube)
    print("Lado esquerdo:")
    cube.printVertices()

    # CIMA
    translate = t.get_translation([0, 10.1, 0])
    scale = t.get_scale([10, 0.1, 10, 1])
    translate_scale = t.compose([translate, scale])
    cube = UnitSquare()
    cube.apply_transformation(translate_scale)
    cube.apply_material(color_material)
    objects.append(cube)
    print("Cima:")
    cube.printVertices()

    # MEIO
    #translate = t.get_translation([0, 0, 0])
    scale = t.get_scale([10, 10.5, 0.1, 1])
    #translate_scale = t.compose([translate, scale])
    cube = UnitSquare()
    cube.apply_transformation(scale)
    cube.apply_material(color_material)
    objects.append(cube)
    print("Meio:")
    cube.printVertices()
    
    punctual_light = PunctualLightSource(intensity=[0.5, 0.5, 0.5], position=[5., 8., 20.])
    punctual_light2 = PunctualLightSource(intensity=[0.5, 0.5, 0.5], position=[20., 20., 5.])

    d = 0.3
    window_height = 1
    window_width = 1
    pixels_height = 200
    pixels_width = 200

    window = Window(window_width, window_height, d, pixels_width, pixels_height)

    # One escape point:
    po = [5., 15., 25, 1.0]
    look_at = [5., 15., 0, 1.0]
    a_vup = [5., 16, 0, 1.0]

    scenario = Scenario(objects=objects, light_sources=[punctual_light, punctual_light2],po=po, look_at=look_at, a_vup=a_vup, background_color=[0., 0., 0.],ambient_light=[0.5, 0.5, 0.5])

    scenario.render(window, threads=True, shadow=True, projection_type="PERSPECTIVE",oblique_angle=None, oblique_factor=None)


def two_escape_points():
    objects = []
    color = [178/255, 34/255, 34/255]
    color_material = Material(color, color, [0.8, 0.8, 0.8], 10)

    scale = t.get_scale([10, 10, 10., 1])
    translate = t.get_translation([0.0, 0.0, 0.])
    translate_scale = t.compose([translate, scale])
    cube = UnitSquare()
    cube.apply_transformation(translate_scale)
    cube.apply_material(color_material)
    objects.append(cube)


    punctual_light = PunctualLightSource(intensity=[0.5, 0.5, 0.5], position=[20., 20., 5.])

    d = 1
    window_height = 1
    window_width = 1
    pixels_height = 200
    pixels_width = 200

    window = Window(window_width, window_height, d, pixels_width, pixels_height)

    # Two escape points
    po = [30., 30., 5, 1.0]
    look_at = [5., 5., 5, 1.0]
    a_vup = [5., 5, 6., 1.0]

    scenario = Scenario(objects=objects, light_sources=[punctual_light],po=po, look_at=look_at, a_vup=a_vup, background_color=[0., 0., 0.],ambient_light=[0.5, 0.5, 0.5])

    scenario.render(window, threads=True, shadow=True, projection_type="PERSPECTIVE",oblique_angle=None, oblique_factor=None)


def three_escape_points():
    objects = []
    color = [178/255, 34/255, 34/255]
    color_material = Material(color, color, [0.8, 0.8, 0.8], 10)

    scale = t.get_scale([10, 10, 10., 1])
    translate = t.get_translation([0.0, 0.0, 0.])
    translate_scale = t.compose([translate, scale])
    cube = UnitSquare()
    cube.apply_transformation(translate_scale)
    cube.apply_material(color_material)
    objects.append(cube)

    punctual_light = PunctualLightSource(intensity=[0.5, 0.5, 0.5], position=[20., 20., 5.])

    d = 1
    window_height = 1
    window_width = 1
    pixels_height = 200
    pixels_width = 200

    window = Window(window_width, window_height, d, pixels_width, pixels_height)

    # Three escape points
    po = [20., 20., 20., 1.0]
    look_at = [10., 10., 10, 1.0]
    a_vup = [10., 12, 10, 1.0]

    scenario = Scenario(objects=objects, light_sources=[punctual_light],po=po, look_at=look_at, a_vup=a_vup, background_color=[0., 0., 0.],ambient_light=[0.5, 0.5, 0.5])

    scenario.render(window, threads=True, shadow=True, projection_type="PERSPECTIVE",oblique_angle=None, oblique_factor=None)


def main():
    #one_escape_point()
    two_escape_points()
    #three_escape_points()


if __name__ == '__main__':
    main()