import pygame
import sys

# Iniciar pygame
pygame.init()

# Tamaño de la ventana
ancho, alto = 1080, 720
ventana = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption('Ejercicio Animación Zombie')
icono = pygame.image.load('icono zombie.png')
pygame.display.set_icon(icono)

# Cargar imágenes
fondo = pygame.image.load('fondo_zombie.png')
personajeQuieto = pygame.image.load('img zombie/idle1.png')
personajeQuieto = pygame.transform.scale(personajeQuieto, (40, 60))  # Redimensionar el personaje
derecha = [pygame.image.load('img zombie/Run1_derecha.png'),
           pygame.image.load('img zombie/Run2_derecha.png'),
           pygame.image.load('img zombie/Run3_derecha.png'),
           pygame.image.load('img zombie/Run4_derecha.png'),
           pygame.image.load('img zombie/Run5_derecha.png'),
           pygame.image.load('img zombie/Run6_derecha.png'),
           pygame.image.load('img zombie/Run7_derecha.png'),
           pygame.image.load('img zombie/Run8_derecha.png'),
           pygame.image.load('img zombie/Run9_derecha.png'),
           pygame.image.load('img zombie/Run10_derecha.png')]
izquierda = [pygame.image.load('img zombie/Run1_izquierda.png'),
             pygame.image.load('img zombie/Run2_izquierda.png'),
             pygame.image.load('img zombie/Run3_izquierda.png'),
             pygame.image.load('img zombie/Run4_izquierda.png'),
             pygame.image.load('img zombie/Run5_izquierda.png'),
             pygame.image.load('img zombie/Run6_izquierda.png'),
             pygame.image.load('img zombie/Run7_izquierda.png'),
             pygame.image.load('img zombie/Run8_izquierda.png'),
             pygame.image.load('img zombie/Run9_izquierda.png'),
             pygame.image.load('img zombie/Run10_izquierda.png')]
salto = [pygame.image.load('img zombie/Jump1.png'),
         pygame.image.load('img zombie/Jump2.png'),
         pygame.image.load('img zombie/Jump3.png'),
         pygame.image.load('img zombie/Jump4.png'),
         pygame.image.load('img zombie/Jump5.png'),
         pygame.image.load('img zombie/Jump6.png'),
         pygame.image.load('img zombie/Jump7.png')]

# Coordenadas y variables del personaje
px, py = 50, 290
velocidad = 10
cuentaPasos = 0
cuentaSalto = 8
salto_activo = False
direccion = "quieto"  # Puede ser "derecha", "izquierda" o "quieto"

def recarga_ventana():
    global cuentaPasos
    global ventana
    global px, py
    global fondo

    ventana.blit(fondo, (0, 0))
    
    if direccion == "derecha":
        ventana.blit(derecha[cuentaPasos // 1], (px, py))
    elif direccion == "izquierda":
        ventana.blit(izquierda[cuentaPasos // 1], (px, py))
    elif salto_activo:
        ventana.blit(salto[cuentaPasos // 1], (px, py))
    else:
        ventana.blit(personajeQuieto, (px, py))
    
    cuentaPasos += 1
    pygame.display.update()

# Bucle principal del juego
ejecutar = True
while ejecutar:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ejecutar = False

    # Teclas presionadas
    keys = pygame.key.get_pressed()

    # Movimiento del personaje
    if keys[pygame.K_a] or keys[pygame.K_KP4] or keys[pygame.K_LEFT]:
        px -= velocidad
        direccion = "izquierda"
    elif keys[pygame.K_d] or keys[pygame.K_KP6] or keys[pygame.K_RIGHT]:
        px += velocidad
        direccion = "derecha"
    elif keys[pygame.K_SPACE] or keys[pygame.K_KP8] or keys[pygame.K_UP]:
        if not salto_activo:
            salto_activo = True
    else:
        direccion = "quieto"
        cuentaPasos = 0

    # Salto
    if salto_activo:
        if cuentaSalto >= -8:
            neg = 1
            if cuentaSalto < 0:
                neg = -1
            py -= (cuentaSalto ** 2) * 0.5 * neg
            cuentaSalto -= 1
        else:
            cuentaSalto = 8
            salto_activo = False

    recarga_ventana()

pygame.quit()
sys.exit()
