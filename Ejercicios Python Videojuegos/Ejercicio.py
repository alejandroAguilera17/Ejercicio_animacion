import pygame

# iniciar python
pygame.init()

# ventana
ancho, alto= 1024, 461
ventana= pygame.display.set_mode((ancho, alto))
pygame.display.set_caption('Ejercicio Animación Zombie')
icono=pygame.image.load('icono zombie.png')
pygame.display.set_icon(icono)

# fondo
fondo = pygame.image.load('fondo_zombie.jpg')

# personaje quieto
personajeQuieto = pygame.image.load('img zombie/idle1.png')

# personaje camina hacia la derecha
derecha = [pygame.image.load('img zombie/Run1_derecha.png'),
		   pygame.image.load('img zombie/Run2_derecha.png'),
		   pygame.image.load('img zombie/Run3_derecha.png'),
		   pygame.image.load('img zombie/Run4_derecha.png'),
		   pygame.image.load('img zombie/Run5_derecha.png'),
		   pygame.image.load('img zombie/Run6_derecha.png'),
		   pygame.image.load('img zombie/Run7_derecha.png'),
		   pygame.image.load('img zombie/Run8_derecha.png'),
		   pygame.image.load('img zombie/Run9_derecha.png'),
		   pygame.image.load('img zombie/Run10_derecha.png'),]

# personaje camina hacia la izquierda
izquierda = [pygame.image.load('img zombie/Run1_izquierda.png'),
		   pygame.image.load('img zombie/Run2_izquierda.png'),
		   pygame.image.load('img zombie/Run3_izquierda.png'),
		   pygame.image.load('img zombie/Run4_izquierda.png'),
		   pygame.image.load('img zombie/Run5_izquierda.png'),
		   pygame.image.load('img zombie/Run6_izquierda.png'),
		   pygame.image.load('img zombie/Run7_izquierda.png'),
		   pygame.image.load('img zombie/Run8_izquierda.png'),
		   pygame.image.load('img zombie/Run9_izquierda.png'),
		   pygame.image.load('img zombie/Run10_izquierda.png'),]

# personaje salta
salto = [pygame.image.load('img zombie/Jump1.png'),
		   pygame.image.load('img zombie/Jump2.png'),
		   pygame.image.load('img zombie/Jump3.png'),
		   pygame.image.load('img zombie/Jump4.png'),
		   pygame.image.load('img zombie/Jump5.png'),
		   pygame.image.load('img zombie/Jump6.png'),
		   pygame.image.load('img zombie/Jump7.png'),]

# Variables de posición y movimiento del personaje
x = 0
px = 50
py = 50
ancho = 40
velocidad = 10

# Control de FPS
reloj = pygame.time.Clock()

salto = False
# Contador de salto inicializar

cuentaSalto = 8 #Controlar la altura y la duración del salto del personaje

# Variables de inicio

izquierda = False
derecha = False

cuentaPasos = 0

# Variables globales
def recarga_ventana():
	global cuentaPasos
	global x

# Fondo en movimiento
	x_relativa = x % fondo.get_rect().width
	ventana.blit(fondo, (x_relativa - fondo.get_rect().width, 0))
	if x_relativa < ancho:
		ventana.blit(fondo, (x_relativa, 0))
	x -= 5

	# Contador de pasos y actualización de animaciones según dirección
	if cuentaPasos + 1 >= 8:
		cuentaPasos = 0
	# Si Movimiento a la izquierda muestra animaciones
	if izquierda:
		ventana.blit(izquierda[cuentaPasos // 1], (int(px), int(py)))
		cuentaPasos += 1

		# Si Movimiento a la derecha, muestra animaciones
	elif derecha:
		ventana.blit(derecha[cuentaPasos // 1], (int(px), int(py)))
		cuentaPasos += 1

	elif salto + 1 >= 8:
		ventana.blit(salto[cuentaPasos // 1], (int(px), int(py)))
		cuentaPasos += 1

	else:
		ventana.blit(personajeQuieto,(int(px), int(py)))

ejecuta = True

while ejecuta:
        
    # FPS
    reloj.tick(18)

    #bucle
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                ejecuta = False

    # Opción tecla pulsada
    keys = pygame.key.get_pressed()


    # Tecla A,Tecla 4, flecha izq - Movimiento a la izquierda
    if  (keys[pygame.K_a] or keys[pygame.K_KP4] or keys[pygame.K_LEFT]) and px > velocidad:
        px -= velocidad
        izquierda = True
        derecha = False

    # Tecla D o Tecla 6 - Movimiento a la derecha
    elif (keys[pygame.K_d] or keys[pygame.K_KP6] or keys[pygame.K_RIGHT]) and px < 900 - velocidad - ancho:
        px += velocidad
        izquierda = False
        derecha = True


    # Tecla W - Movimiento hacia arriba
    if keys[pygame.K_w] or keys[pygame.K_UP] and py > 100:
        py -= velocidad


    # Tecla S o Tecla 2 - Movimiento hacia abajo
    if keys[pygame.K_s] or keys[pygame.K_DOWN] and py < 300:
        py += velocidad

    # personaje quieto
    else:
          izquierda = False
          derecha = False
          cuentaPasos = 0

    # Tecla SPACE o Tecla 8 - Salto
    if not salto:
        if keys[pygame.K_SPACE]:
            salto = True
            izquierda = False
            derecha = False
            cuentaPasos = 0
    else:
        if cuentaSalto >= -10:
            py -= (cuentaSalto * abs(cuentaSalto)) * 0.5
            cuentaSalto -= 1
        else:
            cuentaSalto = 10
            salto = False

    
    #Llamada a la función de actualización de la ventana
    recarga_ventana()

    # Actualización de la ventana
    pygame.display.update()

# salir del juego
pygame.quit()