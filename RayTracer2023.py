import pygame
from pygame.locals import *

from rt import RayTracer
from figures import *
from lights import *
from materials import *


width = 512
height = 512

pygame.init()

screen = pygame.display.set_mode((width,height),pygame.DOUBLEBUF|pygame.HWACCEL|pygame.HWSURFACE)
screen.set_alpha(None)

raytracer = RayTracer(screen)
raytracer.rtClearColor(0.25,0.25,0.25)

brick = Material(diffuse=(1,0.4,0.4),spec=8,Ks=0.01)
grass = Material(diffuse=(0.4,1,0.4),spec=32,Ks=0.1)
water = Material(diffuse=(0.4,0.4,1),spec=256,Ks=0.2)

#Materials
snow = Material(diffuse=(1,1,1),spec=8,Ks=0.01)
button = Material(diffuse=(0,0,0),spec=32,Ks=0.1)
carrot = Material(diffuse=(1,int(163/255),0),spec=256,Ks=0.2)
seed = Material(diffuse=(0.5,0.5,0.5),spec=8,Ks=0.01)

#Esferas
#Cuerpo
raytracer.scene.append(Sphere(position=(0,-1.5,-5),radius=1,material=snow))
raytracer.scene.append(Sphere(position=(0,0,-5),radius=0.8,material=snow))
raytracer.scene.append(Sphere(position=(0,1,-5),radius=0.6,material=snow))

#Botones
raytracer.scene.append(Sphere(position=(0,-1,-3),radius=0.15,material=button))
raytracer.scene.append(Sphere(position=(0,-0.4,-3),radius=0.1,material=button))
raytracer.scene.append(Sphere(position=(0,0,-3),radius=0.1,material=button))

#Nariz
raytracer.scene.append(Sphere(position=(0,0.7,-3),radius=0.1,material=carrot))

#Boca
raytracer.scene.append(Sphere(position=(0.06,0.5,-3),radius=0.04,material=seed))
raytracer.scene.append(Sphere(position=(-0.06,0.5,-3),radius=0.04,material=seed))
raytracer.scene.append(Sphere(position=(0.15,0.55,-3),radius=0.04,material=seed))
raytracer.scene.append(Sphere(position=(-0.15,0.55,-3),radius=0.04,material=seed))

#Ojos
raytracer.scene.append(Sphere(position=(0.14,0.8,-3),radius=0.06,material=snow))
raytracer.scene.append(Sphere(position=(-0.14,0.8,-3),radius=0.06,material=snow))
raytracer.scene.append(Sphere(position=(0.09,0.55,-2),radius=0.02,material=button))
raytracer.scene.append(Sphere(position=(-0.09,0.55,-2),radius=0.02,material=button))

#Luces
raytracer.lights.append(AmbientLight(intensity=0.1))
raytracer.lights.append(DirectionalLight(direction=(-1,-1,-1),intensity=0.7))
#raytracer.lights.append(PointLight(point=(2.5,0,-5),intensity=1, color=(1,0,1)))

isRunning = True
while isRunning:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			isRunning = False
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				isRunning = False
	
	raytracer.rtClear()
	raytracer.rtRender()
	pygame.display.flip()

pygame.quit()