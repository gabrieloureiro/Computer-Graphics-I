import sys
sys.path.append("..")

import transformations as t
import copy
import obj
from scenario import *


def main():
    rgb_vermelho_grena = [140/255, 23/255, 23/255]
    material = obj.Material(rgb_vermelho_grena, rgb_vermelho_grena, [0.8,0.8,0.8], 2)
    
    d = 0.00001
    window_height = 10
    window_width = 10
    pixels_height = 300
    pixels_width = 300

    objects = []
    cube = obj.Obj().import_obj('../objects/cube.obj')

    cube.apply_material(material)
    # s = t.get_scale_matrix([3., 0.1, 4., 1])
    # floor = copy.deepcopy(cube)
    # floor.apply_transformation(s)
    # objects.append(floor)

    # T = t.get_translation_matrix([1, 0, 2])
    # cube2 = copy.deepcopy(cube)
    # cube2.apply_material(obj.Material([0, 0, 0], [0, 0, 0], [0, 0, 0], 1))
    # cube2.apply_transformation(T)
    objects.append(cube)

    # punctual_light = PunctualLightSource(intensity=[1., 1., 1.], position=[1.5, 1.2, 0.1])

    po = [0.5, 0.5, 2.5, 1.0]
    look_at = [0.5, 0.5, 0.5, 1.0]
    a_vup = [0.5, 2, 0.5, 1.0]

    p = "PERSPECTIVE"
    ob = "OBLIQUE"
    cb = "CABINET"
    cv = "CAVALIER"
    ort = "ORTHOGRAPHIC"

    projection_type = ob

    scenario = Scenario(objects=objects, light_sources=[],po=po, look_at=look_at, a_vup=a_vup, background_color=[0.1, 0.1, 0.1],ambient_light=[0.8, 0.8, 0.8])

    window = Window(window_width, window_height, d, pixels_width, pixels_height)

    scenario.render(window, threads=True, shadow=False, projection_type=projection_type, oblique_angle=45, oblique_factor=1)


if __name__ == '__main__':
    main()