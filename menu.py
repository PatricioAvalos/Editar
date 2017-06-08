# -*- coding: utf-8 -*-

"Importacion de librerias"
import random, pygame,sys,mainTAE
from pygame.locals import *
from constantes.Cons import *



#Clase para las opciones
class Opcion:
    
    def __init__(self, fuente, titulo, x, y, paridad, funcion_asignada):
        self.imagen_normal = fuente.render(titulo, 1, (0, 0, 0))
        self.imagen_destacada = fuente.render(titulo, 1, (200, 0, 0))
        self.image = self.imagen_normal
        self.rect = self.image.get_rect()
        self.rect.x = 500 * paridad
        self.rect.y = y
        self.funcion_asignada = funcion_asignada
        self.x = float(self.rect.x)

    def actualizar(self):
        #AJUSTE X OPCIONES
        destino_x = 550
        self.x += (destino_x - self.x) / 5.0
        self.rect.x = int(self.x)

    def imprimir(self, screen):
        screen.blit(self.image, self.rect)

    def destacar(self, estado):
        if estado:
            self.image = self.imagen_destacada
        else:
            self.image = self.imagen_normal

    def activar(self):
        self.funcion_asignada()

#Clase para el cursor
class Cursor:

    def __init__(self, x, y, dy):
        self.image = pygame.image.load('Data/Menu/cursor2.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.y_inicial = y
        self.dy = dy
        self.y = 0
        self.seleccionar(0)

    def actualizar(self):
        self.y += (self.to_y - self.y) / 10.0
        self.rect.y = int(self.y)

    def seleccionar(self, indice):
        self.to_y = self.y_inicial + indice * self.dy

    def imprimir(self, screen):
        screen.blit(self.image, self.rect)

#Clase Menu
class Menu:
    "Representa un menú con opciones para un juego"
    
    def __init__(self, opciones):
        self.opciones = []
        fuente = pygame.font.Font('Data/Menu/dejavu.ttf', 40)
        #AJUSTE POSICION CURSOR
        x = ALTOPANTALLA - 60
        #AJUSTE ALTURA OPCIONES
        y = ANCHOPANTALLA/4
        paridad = 1
        #y = posicion cursor
        self.cursor = Cursor(x - 30, y+10, 50)

        for titulo, funcion in opciones:
            self.opciones.append(Opcion(fuente, titulo, x, y, paridad, funcion))
            y += 50
            if paridad == 1:
                paridad = -1
            else:
                paridad = 1

        self.seleccionado = 0
        self.total = len(self.opciones)
        self.mantiene_pulsado = False

    def actualizar(self):
        """Altera el valor de 'self.seleccionado' con los direccionales."""
        k = pygame.key.get_pressed()

        if not self.mantiene_pulsado:
            if k[K_UP]:
                self.seleccionado -= 1
                
                "Ejecucion de sonido"
                x = pygame.mixer.Sound('Data/Sonidos/beepop.ogg')
                x.play()
            
            elif k[K_DOWN]:
                self.seleccionado += 1
                
                "Ejecucion de sonido"
                y = pygame.mixer.Sound('Data/Sonidos/beepop.ogg')
                y.play()
            
            elif k[K_z]:
                # Invoca a la función asociada a la opción.
                self.opciones[self.seleccionado].activar()
                pygame.mixer.music.stop()
                MusicaFondo()

        # procura que el cursor esté entre las opciones permitidas
        if self.seleccionado < 0:
            self.seleccionado = 0
        elif self.seleccionado > self.total - 1:
            self.seleccionado = self.total - 1
        
        self.cursor.seleccionar(self.seleccionado)

        # indica si el usuario mantiene pulsada alguna tecla.
        self.mantiene_pulsado = k[K_UP] or k[K_DOWN] or k[K_z]

        self.cursor.actualizar()
     
        for o in self.opciones:
            o.actualizar()

    def imprimir(self, screen):
        """Imprime sobre 'screen' el texto de cada opción del menú."""

        self.cursor.imprimir(screen)

        for opcion in self.opciones:
            opcion.imprimir(screen)

def comenzar_nuevo_juego():
    "Ejecucion de sonido de confirmacion"
    pygame.mixer.music.stop()
    z = pygame.mixer.Sound('Data/Sonidos/aceptarop.ogg')
    z.play()
    
    "Ejecucion Juego"
    mainTAE.main(tiker)

def controles():
    "Ejecucion de sonido de confirmacion"
    z = pygame.mixer.Sound('Data/Sonidos/aceptarop.ogg')
    z.play()
    
    "Ejecucion Controles"
    GJ1()
    

def creditos():   
    "Ejecucion de sonido de confirmacion"
    z = pygame.mixer.Sound('Data/Sonidos/aceptarop.ogg')
    z.play()
    "Ejecucion Creditos"
    vcreditos()
    
def salir_del_programa():
    "Ejecucion de sonido de confirmacion"
    z = pygame.mixer.Sound('Data/Sonidos/aceptarop.ogg')
    z.play()
    
    "Ejecucion de cierre del Juego"
    pygame.quit()
    sys.exit()

"Main: Menu"
if __name__ == '__main__':

    salir = False
    opciones = [
        ("Jugar", comenzar_nuevo_juego),
        ("Controles", controles),
        ("Creditos", creditos),
        ("Salir", salir_del_programa)
        ]

    pygame.font.init()
    pygame.mixer.init()
    MusicaFondo()
    screen = pygame.display.set_mode((ANCHOPANTALLA, ALTOPANTALLA))
    fondo = pygame.image.load("Data/Menu/fondo.png").convert()
    menu = Menu(opciones)
   
    while not salir:

        for e in pygame.event.get():
            if e.type == QUIT:
                pygame.quit()
                sys.exit()
                salir = True
                break

        screen.blit(fondo, (0, 0))
        menu.actualizar()
        menu.imprimir(screen)
        
        pygame.display.flip()
        pygame.time.delay(10)
