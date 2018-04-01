import math
import time
import matplotlib.pyplot as plt
import numpy as np

import world_camera_transformations as wct

class Window(object):
    def __init__(self, width, height, distance, pixels_width, pixels_height):
        self.width = width
        self.height = height
        self.distance = distance
        self.pixels_width = pixels_width
        self.pixels_height = pixels_height
        self.delta_x = width / pixels_width
        self.delta_y = height / pixels_height

    def get_pij(self, i, j):
        y_i = (self.height - self.delta_y) / 2 - (i * self.delta_y)
        x_i = (-self.width + self.delta_x) / 2 + (j * self.delta_x)
        return np.array([x_i, y_i, -self.distance])


class Scenario(object):
    def __init__(self, objects=[], light_sources=[], po=None, look_at=None,
                 a_vup=None, background_color=[0.0, 0.0, 0.0], ambient_light=[1.0, 1.0, 1.0]):
        """
        :param objects: array dos objetos pertencentes ao cenário
        :param light_sources: array das fontes luminosas do cenário
        :param po: ponto do olho do observador
        :param look_at: look at do observador point
        :param a_vup: a_viewUp do observador
        """
        self._objects = objects
        self._light_sources = light_sources
        self._background_color = background_color
        self._ambient_light = np.array(ambient_light)

        # Camera:
        self._po = po
        self._look_at = look_at
        self._a_vup = a_vup

    def render(self, window, threads=True, shadow=False, projection_type="PERSPECTIVE",
               oblique_angle=None, oblique_factor=None):

        """
            Renderizador
        """

        params = {'threads': threads, 'shadow': shadow, 'projection_type': projection_type,'oblique_angle': oblique_angle, 'oblique_factor': oblique_factor}

        # Montando o cenário
        scenario = self._ray_casting(window, **params)
        
        plt.imshow(scenario)
        plt.show()

    

    

    def _ray_casting(self, window, threads=True, shadow=False, projection_type="CABINET", oblique_angle=0.0, oblique_factor=0.0):

        """
            Ray Casting para reenderizar ambiente;

            :return: matrix with scenario pixels rgb
        """

        print("Ray_casting()...")
        startOperation = time.time()

        self._world_to_camera()

        oblique, oblique_factor = self._get_obliqueOptions(projection_type, oblique_factor)

        if threads:
            import pymp
            pymp.config.nested = True
            matrixPixels = pymp.shared.array((window.pixels_width, window.pixels_height, 3))

            # Abrindo quatro laços simultâneos, com controle de concorrência:
            with pymp.Parallel(4) as p1:
                for i in p1.range(window.pixels_height):
                    for j in range(window.pixels_width):
                        matrixPixels[i][j] = self._ray_casting_per_pixel(window.get_pij(i, j), shadow, oblique, oblique_factor,oblique_angle)
        
        # Sem threads:
        else:
            p = np.ones((window.pixels_width, window.pixels_height, 3))
            for i in range(window.pixels_height):
                for j in range(window.pixels_width):
                    matrixPixels[i][j] = self._ray_casting_per_pixel(window.get_pij(i, j), shadow, oblique, oblique_factor,oblique_angle)

        # Pegando o RGB maximo, pois valores passarão de 1 (0..255)
        max_rgb = np.amax(np.amax(matrixPixels, axis=0), axis=0)

        endOperation = time.time()
        print("Finish: ", endOperation - startOperation)

        return matrixPixels / [max(1, max_rgb[0]), max(1, max_rgb[1]), max(1, max_rgb[2])]

    

    def _ray_casting_per_pixel(self, pij, shadow, oblique=False, oblique_factor=0., oblique_angle=0.):
        """
            Ray casting para cada pixel
        """

        if oblique:
            r0 = pij
            d = np.array([-oblique_factor * math.cos(math.radians(oblique_angle)),
                          -oblique_factor * math.sin(math.radians(oblique_angle)),
                          -1])
            d /= np.linalg.norm(d)
        else:
            r0 = np.zeros(3) #(0,0,0)
            d = pij

        p_int, intersected_face = self._get_intersection(r0, d)

        # Se não teve ponto de interseção:
        # !Atualizar para checar o y de mundo!
        if p_int is None:
            return self._background_color

        else:
            return self._determine_color(r0, p_int, intersected_face, shadow)


    def _determine_color(self, r0, p_int, intersected_face, shadow=True):
        """
            Retorna a cor do pixel RGB
            :param r0: origem do raio
            :param p_int: ponto de interceção
            :param intersected_face: face interceptada pelo raio
            :param shadow: se True, utilizar mecanismo de sombreamento
            :return: RGB do Pij
        """
        pij_color = intersected_face.material.k_a_rgb * self._ambient_light
        for light_source in self._light_sources:

            if shadow:
                l_int, l_face = self._get_intersection(p_int, light_source.get_l(p_int), 0, intersected_face)

                if l_int is not None:
                    continue

                else:
                    pij_color += light_source.get_total_intensity(r0, intersected_face, p_int)
            else:
                pij_color += light_source.get_total_intensity(r0, intersected_face, p_int)

        return pij_color

    def _get_intersection(self, r0, d, t_limit=1, face_int=None):
        objects_with_aura_touched = self._objects_aura_intercepted(r0, d)
        return self._get_intersected_face(objects_with_aura_touched, r0, d, t_limit, face_int)

    def _is_ray_touches_aura(self, obj, r0, d):
        """
        Retorna true ou falso se o raio tem interação com a Aura do Obj;
        :param r0: origem do raio
        :param obj: obj a ser analisado
        :param d: raio propriamente dito
        :return: true ou false
        """
        vertices = np.array([vertex.coordinates for vertex in obj.vertices])
        min_x = min(vertices[:, 0])
        max_x = max(vertices[:, 0])
        min_y = min(vertices[:, 1])
        max_y = max(vertices[:, 1])
        min_z = min(vertices[:, 2])
        max_z = max(vertices[:, 2])

        center = np.array([(max_x + min_x)/2, (max_y + min_y)/2, (max_z + min_z)/2])
        dx = abs(max_x) + abs(min_x)
        dy = abs(max_y) + abs(min_y)
        dz = abs(max_z) + abs(min_z)

        radius = max(dx, dy, dz)/2

        a = (d).dot(d)
        b = -2 * d.dot(r0-center)
        c = (r0-center).dot(r0-center) - math.pow(radius, 2)
        return math.pow(b, 2) - 4 * a * c >= 0
            
        '''        
        c = obj.center
        r = obj.radius

        a = d.dot(d)
        b = -2 * d.dot(r0 - c)
        c = (r0 - c).dot(r0 - c) - r ** 2

        return b ** 2 - 4 * a * c >= 0
        '''
    def _objects_aura_intercepted(self, r0, d):
        """
            Retorna uma lista com os objetos que tiveram a Aura tocada pelo raio
            :return: []
        """
        return [obj for obj in self._objects if self._is_ray_touches_aura(obj, r0, d)]

    def _find_t(self, face, r0, d):
        p1 = face.vertices[0].coordinates[:3]
        n = face.normal[:3]

        n_dot_d = np.dot(n, d[:3])
        if n_dot_d >= 0:
            return -1

        return n.dot(p1-r0)/n_dot_d

    def _get_intersected_face(self, objects, r0, d, t_limit=1, face_int=None):
        """
            Retorna qual face teve interação com o raio
        """
        
        t_min = float('inf') # Numero pequeno
        intersected_face = (None, None)

        for object_ in objects:
            for face in [f for f in object_.faces if f is not face_int]:
                t = self._find_t(face, r0, d)

                if t < t_limit or (t_limit == 1 and t > t_min) or (t_limit == 0 and t > 1):
                    continue

                # ray and plane intersection point
                p = r0 + (t * d)

                # now we want to check if this point is inside the face
                if face.is_in_triangle(p):
                    t_min = t
                    intersected_face = (p, face)
                    if t_limit == 0:
                        return intersected_face

        return intersected_face
    
    def _get_obliqueOptions(self, projection_type, oblique_factor):
        """
            Configurações Iniciais para projeções;
            return: 
        """
        projections = {
            'PERSPECTIVE': (False, oblique_factor),
            'CABINET': (True, .5),
            'CAVALIER': (True, 1.),
            'OBLIQUE': (True, oblique_factor),
            'ORTHOGRAPHIC': (True, 0.)
        }
        if projection_type not in projections:
            exit()
        else:
            return projections[projection_type]
    def _world_to_camera(self):
        
        wc_matrix = wct.get_world_camera_matrix(self._po, self._look_at, self._a_vup)
        for object_ in self._objects:
            for vertex in object_.vertices:
                vertex.coordinates = wc_matrix.dot(vertex.coordinates)[:3]
            object_.calculate_normals()

        for light_source in self._light_sources:
            if type(light_source) is not InfinityLightSource:
                light_source.position = wc_matrix.dot(light_source.position)

    
    
    def _camera_to_world(self):
        cw_matrix = wct.get_camera_world_matrix(self._po, self._look_at, self._a_vup)

        for object_ in self._objects:
            for vertex in object_.vertices:
                vertex.coordinates = cw_matrix.dot(vertex.coordinates)
            object_.calculate_normals()

        for light_source in self._light_sources:
            light_source.position = cw_matrix.dot(light_source.position)


class LightSource(object):
    def __init__(self, intensity, position, direction=None):
        """
        :param intensity: light source intensity, between 0 and 1
        """
        self.intensity = np.array(intensity)
        self.position = np.append(position, [1])
        if direction is not None:
            self.direction = np.array(direction)/np.linalg.norm(direction)
        else:
            self.direction = None

    def get_l(self, p_int):
        return self.position[:3] - p_int

    def get_vectors(self, r0, face, p_int):
        """
        Return the unitary vectors n, l, u and r
        :param r0: origin of ray
        :param face: face intersected by the ray
        :param p_int: point intersected
        :return:
        """
        n_u = face.normal[:3]

        l = self.position[:3] - p_int
        l_u = (l / np.linalg.norm(l))

        v = r0-p_int
        v_u = (v / np.linalg.norm(v))

        r = 2 * (np.dot(l_u, n_u)) * n_u - l_u

        return n_u, l_u, v_u, r

    def get_total_intensity(self, r0, face, p_int):
        """
        Return the sum of the diffuse and specular term
        :param r0: origin of ray
        :param face: face intersected by the ray
        :param p_int: point intersected
        :return:
        """
        n, l, v, r = self.get_vectors(r0, face, p_int)

        k_d_rgb = face.material.k_d_rgb
        k_e_rgb = face.material.k_e_rgb

        diffuse_term = n.dot(l)
        if not diffuse_term > 0:
            return 0

        specular_term = np.dot(v, r)
        specular_term = max(0, specular_term ** face.material.attenuation)

        i_obj = (((k_d_rgb * self.intensity) * diffuse_term) +
                 ((k_e_rgb * self.intensity) * specular_term))

        return i_obj


class PunctualLightSource(LightSource):
    def __init__(self, intensity, position):
        """
        :param intensity: light source intensity, between 0 and 1
        :param position: position x,y,z of the light source
        """
        super().__init__(intensity, position, None)


class SpotLightSource(LightSource):
    def __init__(self, intensity, position, direction, theta):
        """
        :param intensity: light source intensity, between 0 and 1
        :param position: position x,y,z of the light source
        :param direction: direction vector of the light
        :param theta: limit angle at which light from source can be seen
        """
        super().__init__(intensity, position, direction)
        self.theta = theta

    def get_total_intensity(self, r0, face, p_int):
        """
        Return the sum of the diffuse and specular term
        :param face: face intersected by the ray
        :param p_int: point intersected
        :return:
        """
        n, l, v, r = self.get_vectors(r0, face, p_int)

        k_d_rgb = face.material.k_d_rgb
        k_e_rgb = face.material.k_e_rgb

        spot_intensity = self.direction.dot(-l)
        if spot_intensity < math.cos(math.radians(self.theta)):
            spot_intensity = 0

        diffuse_term = spot_intensity * n.dot(l)
        if not diffuse_term > 0:
            return 0

        specular_term = spot_intensity * np.dot(v, r)
        specular_term = max(0, specular_term ** face.material.attenuation)

        i_obj = (((k_d_rgb * self.intensity) * diffuse_term) +
                 ((k_e_rgb * self.intensity) * specular_term))

        return i_obj


class InfinityLightSource(LightSource):
    def __init__(self, intensity, direction):
        """
        :param intensity: light source intensity, between 0 and 1
        :param direction: direction vector of the light
        """
        super().__init__(intensity=intensity, position=None, direction=direction)

    def get_l(self, p_int):
        return -self.direction

    def get_vectors(self, r0, face, p_int):
        """
        Return the unitary vectors n, l, u and r
        :param r0: origin of ray
        :param face: face intersected by the ray
        :param p_int: point intersected
        :return:
        """
        n_u = face.normal[:3]

        l = -self.direction
        l_u = (l / np.linalg.norm(l))

        v = r0-p_int
        v_u = (v / np.linalg.norm(v))

        r = 2 * (np.dot(l_u, n_u)) * n_u - l_u

        return n_u, l_u, v_u, r