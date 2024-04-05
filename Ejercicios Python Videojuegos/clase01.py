import pygame

#Inicialización de Python0
pygame.init()

# Pantalla - ventana
W, H = 860, 484
PANTALLA = pygame.display.set_mode((W, H))
pygame.display.set_caption('Animación Personaje')
icono=pygame.image.load('icono.png')
pygame.display.set_icon(icono)

# Fondo del juego
fondo = pygame.image.load('bosque.jpeg')

# Carga de imagen para personaje posición quieto
quieto = pygame.image.load('imagenes/espadachin/quieto/quieto1.png')

# Carga de imágenes para personaje caminar a la derecha	
caminaDerecha = [pygame.image.load('imagenes/espadachin/derecha/walk_der1.png'),
				pygame.image.load('imagenes/espadachin/derecha/walk_der2.png'),
				pygame.image.load('imagenes/espadachin/derecha/walk_der3.png'),
				pygame.image.load('imagenes/espadachin/derecha/walk_der4.png'),
				pygame.image.load('imagenes/espadachin/derecha/walk_der5.png'),
				pygame.image.load('imagenes/espadachin/derecha/walk_der6.png'),
				pygame.image.load('imagenes/espadachin/derecha/walk_der7.png'),
				pygame.image.load('imagenes/espadachin/derecha/walk_der8.png')]

# Carga de imágenes para personaje caminar a la izquierda
caminaIzquierda = [pygame.image.load('imagenes/espadachin/izquierda/walk_izq1.png'),
				pygame.image.load('imagenes/espadachin/izquierda/walk_izq2.png'),
				pygame.image.load('imagenes/espadachin/izquierda/walk_izq3.png'),
				pygame.image.load('imagenes/espadachin/izquierda/walk_izq4.png'),
				pygame.image.load('imagenes/espadachin/izquierda/walk_izq5.png'),
				pygame.image.load('imagenes/espadachin/izquierda/walk_izq6.png'),
				pygame.image.load('imagenes/espadachin/izquierda/walk_izq7.png'),
				pygame.image.load('imagenes/espadachin/izquierda/walk_izq8.png')]

# Carga de imágenes para personaje saltar	
salta = [pygame.image.load('imagenes/espadachin/saltar/saltar1.png'),
		 pygame.image.load('imagenes/espadachin/saltar/saltar2.png'),
		 pygame.image.load('imagenes/espadachin/saltar/saltar3.png'),
		 pygame.image.load('imagenes/espadachin/saltar/saltar4.png'),
		 pygame.image.load('imagenes/espadachin/saltar/saltar5.png'),
		 pygame.image.load('imagenes/espadachin/saltar/saltar6.png'),
		 pygame.image.load('imagenes/espadachin/saltar/saltar7.png'),
		 pygame.image.load('imagenes/espadachin/saltar/saltar8.png')]

# Variables de posición y movimiento del personaje
x = 0
px = 50
py = 290
ancho = 40
velocidad = 10

# Control de FPS
reloj = pygame.time.Clock()

# Variable para salto inicializar
salto = False
# Contador de salto inicializar
cuentaSalto = 10 #Controlar la altura y la duración del salto del personaje

# Variables dirección
izquierda = False
derecha = False

# Pasos
cuentaPasos = 0

# Movimiento
def recarga_pantalla():
	# Variables globales
	global cuentaPasos
	global x

	# Fondo en movimiento
	x_relativa = x % fondo.get_rect().width
	PANTALLA.blit(fondo, (x_relativa - fondo.get_rect().width, 0))
	if x_relativa < W:
		PANTALLA.blit(fondo, (x_relativa, 0))
	x -= 5

	# Contador de pasos y actualización de animaciones según dirección
	if cuentaPasos + 1 >= 8:
		cuentaPasos = 0
	# Si Movimiento a la izquierda muestra animaciones
	if izquierda:
		PANTALLA.blit(caminaIzquierda[cuentaPasos // 1], (int(px), int(py)))
		cuentaPasos += 1

		# Si Movimiento a la derecha, muestra animaciones
	elif derecha:
		PANTALLA.blit(caminaDerecha[cuentaPasos // 1], (int(px), int(py)))
		cuentaPasos += 1

	elif salto + 1 >= 8:
		PANTALLA.blit(salta[cuentaPasos // 1], (int(px), int(py)))
		cuentaPasos += 1

	else:
		PANTALLA.blit(quieto,(int(px), int(py)))

ejecuta = True

# Bucle de acciones y controles
while ejecuta:
	# FPS
	reloj.tick(18)

	# Bucle del juego
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			ejecuta = False

	# Opción tecla pulsada
	keys = pygame.key.get_pressed()

	# Tecla A - Movimiento a la izquierda
	if keys[pygame.K_a] and px > velocidad:
		px -= velocidad #decremento de la velocidad
		izquierda = True
		derecha = False

	# Tecla D - Movimiento a la derecha
	elif keys[pygame.K_d] and px < 850 - velocidad - ancho:
		px += velocidad
		izquierda = False
		derecha = True

	# Personaje quieto
	else:
		izquierda = False
		derecha = False
		cuentaPasos = 0

	# Tecla W - Movimiento hacia arriba
	if keys[pygame.K_w] and py > 100:
		py -= velocidad

	# Tecla S - Moviemiento hacia abajo
	if keys[pygame.K_s] and py < 300:
		py += velocidad

	# Tecla SPACE - Salto
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

	# Actualización de la ventana
	pygame.display.update()
	
	#Llamada a la función de actualización de la ventana
	recarga_pantalla()

# Salida del juego
pygame.quit()