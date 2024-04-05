import pygame, sys #Importando el modulo de pygame (contiene varias librerias)
from pygame.locals import* #Importamos todas las librerias del modulo pygame

pygame.init()  #Inicializa el pygame

#Definir las propiedades de la ventana

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (135, 206, 250)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
BROWN = (165, 42, 42)
PINK = (255, 192, 203)


ventana = pygame.display.set_mode((1024,575))
pygame.display.set_caption("Jueguito")
icono = pygame.image.load("icono.png")
pygame.display.set_icon(icono)
fondo = pygame.image.load("fondo.png")
ventana.blit(fondo,(0,0))

# Dibujo del sol
pygame.draw.circle(ventana, YELLOW, (550, 50), 40)

# Dibujo de la casa
pygame.draw.rect(ventana, BLUE, [150, 200, 300, 200])  # Cuerpo de la casa
pygame.draw.polygon(ventana, RED, [(150, 200), (300, 100), (450, 200)])  # Techo
pygame.draw.rect(ventana, BLACK, [230, 300, 50, 100])  # Puerta
pygame.draw.circle(ventana, BLACK, (275, 250), 5)  # Ventana izquierda
pygame.draw.circle(ventana, BLACK, (375, 250), 5)  # Ventana derecha

# Dibujo el poste de la señal de tránsito
pygame.draw.rect(ventana, BLACK, [30, 50, 20, 300])
pygame.draw.circle(ventana, RED, (40, 120), 30)
pygame.draw.circle(ventana, YELLOW, (40, 240), 30)
pygame.draw.circle(ventana, GREEN, (40, 360), 30)


while True: #La ventana itera continuamente hasta que se cierre
    for evento in pygame.event.get():
        if evento.type == QUIT: #Si el evento es igual a salir

            pygame.quit() #Cierra mmodulo de pygame
            sys.exit() #Salir del programa o sistema

    pygame.display.update()  #Actualiza la ejecución de ventana