import copy

import transformations as t
from obj import *
from scenario import *


def main():
    d = 1
    window_height = 1
    window_width = 1
    pixels_height = 200
    pixels_width = 200

    objects = []

    scale = t.get_scale([100., 0.1, 100., 1])
    floor = UnitSquare()
    floor.apply_transformation(scale)
    objects.append(floor)

    rgb_red = [1, 0, 0]
    red_material = Material(rgb_red, rgb_red, [1,1,1], 1)

    translate = t.get_translation([50, 0, 50])
    scale = t.get_scale([1, 3, 1, 1])
    scale_translate = t.compose([translate, scale])
    cube = UnitSquare()
    cube.apply_transformation(scale_translate)
    cube.apply_material(red_material)
    print("Cube")
    cube.printVertices()
    objects.append(cube)

    #punctual_light = PunctualLightSource(intensity=[1., 1., 1.], position=[50.5, 5, 50.5])
    punctual_light = PunctualLightSource(intensity=[1., 1., 1.], position=[50.5, 1.5, 48.5])

    # Observador atrás do objeto, luz à frente do objeto
    #po = [50.5, 4, 60.5, 1.0]

    # Observador na frente do Objeto, e atrás da luz
    po = [50.5,4,40.05,1.0]
    
    look_at = [50.5, 0., 50.5, 1.0]
    a_vup = [50.5, 20, 50.5, 1.0]


    scenario = Scenario(objects=objects, light_sources=[punctual_light],po=po, look_at=look_at, a_vup=a_vup, background_color=[0., 0., 0.],ambient_light=[0.1, 0.1, 0.1])

    window = Window(window_width, window_height, d, pixels_width, pixels_height)

    scenario.render(window, threads=True, shadow=True, projection_type="PERSPECTIVE", oblique_angle=None, oblique_factor=None)

if __name__ == '__main__':
    main()