import pygame, sys #Importando el modulo de pygame (contiene varias librerias)
from pygame.locals import* #Importamos todas las librerias del modulo pygame

pygame.init()  #Inicializa el pygame

#Definir las propiedades de la ventana
azul = (0, 43, 255)

ventana = pygame.display.set_mode((500,400))
pygame.display.set_caption("Jueguito")
ventana.fill(azul)
icono = pygame.image.load("icono.png")
pygame.display.set_icon(icono)

while True: #La ventana itera continuamente hasta que se cierre
    for evento in pygame.event.get():
        if evento.type == QUIT: #Si el evento es igual a salir
            pygame.quit() #Cierra mmodulo de pygame
            sys.exit() #Salir del programa o sistema

    pygame.display.update()  #Actualiza la ejecución de ventana