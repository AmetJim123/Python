import pygame
import random
import math
from pygame import mixer

# Inicializar pygame
pygame.init()

# Crear la pantalla
pantalla = pygame.display.set_mode((1400, 933))

# Título e icono
pygame.display.set_caption("Invasión espacial UwU")
icono = pygame.image.load("extraterrestre.png")
pygame.display.set_icon(icono)
fondo = pygame.image.load('fondo.jpg')

# Agregar música
mixer.music.load('MusicaFondo.mp3')
mixer.music.set_volume(0.2)
mixer.music.play(-1)

# Variables jugador
img_jugador = pygame.image.load("tank.png")
jugador_x = 668
jugador_y = 836
jugador_x_cambio = 0

# Variables enemigo
img_enemigo = []
enemigo_x = []
enemigo_y = []
enemigo_x_cambio = []
enemigo_y_cambio = []
cantidad_enemigos = 10

for e in range(cantidad_enemigos):
    img_enemigo.append(pygame.image.load("extraterrestre.png"))
    enemigo_x.append(random.randint(0, 1336))
    enemigo_y.append(0)
    enemigo_x_cambio.append(2)
    enemigo_y_cambio.append(50)


# Variables proyectil
img_proyectil = pygame.image.load("misil.png")
proyectil_x = 0
proyectil_y = 836
proyectil_x_cambio = 0
proyectil_y_cambio = 6
proyectil_visible = False

# Puntaje
puntaje = 0
fuente = pygame.font.Font('freesansbold.ttf', 32)
texto_x = 10
texto_y = 10

# Texto final del juego
fuente_final = pygame.font.Font('freesansbold.ttf', 80)

# Intentos
vidas = 5

    
def texto_final():
    mi_fuente_final = fuente_final.render('PERDISTE', True, (255, 255, 255))
    pantalla.blit(mi_fuente_final, (500, 375))


def mostrar_puntaje(x, y):
    texto = fuente.render(f'Puntaje: {puntaje}', True, (255, 255, 255))
    pantalla.blit(texto, (x, y))


# Función disparar proyectil
def disparar_proyectil(x, y):
    global proyectil_visible
    proyectil_visible = True
    pantalla.blit(img_proyectil, (x + 16, y + 10))


# Función detectar colisiones
def hay_colision(x_1, y_1, x_2, y_2):
    distancia = math.sqrt(math.pow(x_2 - x_1, 2) + math.pow(y_2 - y_1, 2))
    if distancia < 27:
        return True
    else:
        return False


# Función jugador
def jugador(x, y):
    pantalla.blit(img_jugador, (x, y))


# Función enemigo
def enemigo(x, y, ene):
    pantalla.blit(img_enemigo[ene], (x, y))


# Loop del Juego
se_ejecuta = True
while se_ejecuta:

    # imagen fondo de pantalla
    pantalla.blit(fondo, (0, 0))

    # Iterar eventos
    for evento in pygame.event.get():

        # Evento cerrar
        if evento.type == pygame.QUIT:
            se_ejecuta = False

        # Evento presionar teclas
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                jugador_x_cambio = -1.5
            if evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 1.5
            if evento.key == pygame.K_SPACE and not proyectil_visible:
                sonido_proyectil = mixer.Sound('disparo.mp3')
                sonido_proyectil.play()
                proyectil_x = jugador_x
                disparar_proyectil(proyectil_x, proyectil_y)
        # Evento soltar flechas
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 0

    # Modificar movimiento jugador
    jugador_x += jugador_x_cambio

    # Mantener dentro de bordes jugador
    if jugador_x <= 0:
        jugador_x = 0
    elif jugador_x >= 1336:
        jugador_x = 1336

    # Modificar ubicación del enemigo
    for e in range(cantidad_enemigos):

        # Fin del juego
        if enemigo_y[e] > 836:
            vidas -= 1
            if vidas == 0:
                for k in range(cantidad_enemigos):
                    enemigo_y[k] = 1000
                texto_final()

        enemigo_x[e] += enemigo_x_cambio[e]

        # Mantener dentro de bordes al enemigo
        if enemigo_x[e] <= 0:
            enemigo_x_cambio[e] = 2
            enemigo_y[e] += enemigo_y_cambio[e]
        elif enemigo_x[e] >= 1336:
            enemigo_x_cambio[e] = -2.
            enemigo_y[e] += enemigo_y_cambio[e]

        # Colision
        colision = hay_colision(enemigo_x[e], enemigo_y[e], proyectil_x, proyectil_y)
        if colision:
            sonido_colision = mixer.Sound('Golpe.mp3')
            sonido_colision.play()
            proyectil_y = 836
            proyectil_visible = False
            puntaje += 1
            enemigo_x[e] = random.randint(0, 1336)
            enemigo_y[e] = 0
            if 20 < puntaje > 10:
                enemigo_y[e] = 200
            elif 30 > puntaje > 20:
                enemigo_x_cambio[e] = 20
                enemigo_y[e] = 300
            elif 40 > puntaje > 30:
                enemigo_x_cambio[e] = 30
                enemigo_y[e] = 400

        if puntaje == 100:
            se_ejecuta = False

        enemigo(enemigo_x[e], enemigo_y[e], e)
    # Movimiento proyectil
    if proyectil_visible:
        disparar_proyectil(proyectil_x, proyectil_y)
        proyectil_y -= proyectil_y_cambio

    # Mantener dentro de borde al proyectil
    if proyectil_y <= -64:
        proyectil_y = 836
        proyectil_visible = False

    jugador(jugador_x, jugador_y)
    mostrar_puntaje(texto_x, texto_y)

    # Actualizar
    pygame.display.update()
