import pygame
import sys

# Inicializar Pygame
pygame.init()

# Definir colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)

# Configurar la pantalla
width, height = 400, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Señal de Tránsito")

# Bucle principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Limpiar la pantalla
    screen.fill(WHITE)

    # Dibujar el poste
    pygame.draw.rect(screen, BLACK, [180, 50, 40, 400])

    # Dibujar el círculo rojo
    pygame.draw.circle(screen, RED, (200, 120), 30)

    # Dibujar el círculo amarillo
    pygame.draw.circle(screen, YELLOW, (200, 240), 30)

    # Dibujar el círculo verde
    pygame.draw.circle(screen, GREEN, (200, 360), 30)

    # Actualizar la pantalla
    pygame.display.flip()

# Salir de Pygame
pygame.quit()
sys.exit()
