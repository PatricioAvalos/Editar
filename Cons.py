# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 13:58:48 2017

@author: matia
"""
import pygame, sys, os, menu 

#Importacion de animaciones
import shooting, creditos, gameover_j1, gameover_j2

from pygame.locals import *

FPS = 30
RelojFPS = pygame.time.Clock()

ALTOPANTALLA=600
ANCHOPANTALLA=1300

DIR_IMAGEN="imagenes"

viejo1_tiker=0
viejo2_tiker=0
caja_tiker=0
bala_tiker=0
tiker=[viejo1_tiker,viejo2_tiker,caja_tiker,bala_tiker]

cronometro=[0,0,0,0,0,0,0,0]

TAMtorre=9
SEPERACIONtorres=600
PosTorre1=ANCHOPANTALLA/2-SEPERACIONtorres/2-120
PosTorre2=ANCHOPANTALLA/2+SEPERACIONtorres/2
ALTOTORRE=60
ANCHOTORRE=120

ALTOVIEJO=60
ANCHOVIEJO=30

ALTURACALLE=ALTOPANTALLA-100
LISTAMATERIALES=[("madera",),("cemento",),("fierro",),("ladrillo",)]
numeroLISTAMATERIALES=len(LISTAMATERIALES)

LISTAPISOS=[("piso1.png",1,300),("piso2.png",2,200),("piso3.png",3,100)]
numeroLISTAPISOS=len(LISTAPISOS)
LISTACANONES=[("cañon1.png",1),("cañon2.png",2)]
numeroLISTACANONES=len(LISTACANONES)
LISTABALAS=[("bala1T1.png","bala2T1","bala3T1"),("bala1T2.png","bala2T2","bala3T2")]
numeroLISTABALAS=len(LISTABALAS)

def cargar_imagen(nombre, dir_imagen, alpha=False):
    ruta = os.path.join(dir_imagen, nombre)
    try:
        image = pygame.image.load(ruta)
    except:
        print("Error, no se puede cargar la imagen: " + ruta)
        sys.exit(1)
    if alpha is True:
        image = image.convert_alpha()
    else:
        image = image.convert()
    return image
pantalla= pygame.display.set_mode((ANCHOPANTALLA,ALTOPANTALLA))

#video shooting stars
def videoshoo():
    video1 = shooting.video()
    pygame.mixer.init()
    pygame.mixer.music.load("Shooting.ogg")
    pygame.mixer.music.play(-1)
    clock = pygame.time.Clock()
    x = True
    while x:
        pantalla.fill((0,0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key==K_x:
                    pygame.mixer.quit()
                    x = False
        video1.update()
        pygame.display.flip()
        clock.tick(60)
    pantalla.fill((0,0,0))

#video creditos
def vcreditos():
    video1 = creditos.video()
    pygame.mixer.music.stop()
    pygame.mixer.init()
    effect = pygame.mixer.Sound('sound.ogg')
    effect.play()
    clock = pygame.time.Clock()
    x = True
    while x:
        pantalla.fill((0,0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key==K_x:
                    
                    effect.stop()
                    x = False
        video1.update()
        pygame.display.flip()
        clock.tick(60)
    pantalla.fill((0,0,0))

#Gameover J1
def GJ1():
    vgj1 = gameover_j1.video()
    pygame.mixer.init()
    pygame.mixer.music.load("musica/gameover.ogg")
    pygame.mixer.music.play(-1)
    clock = pygame.time.Clock()
    x = True
    while x:
        pantalla.fill((0,0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key==K_r:
                    pygame.mixer.music.stop()
                    x = False
        vgj1.update()
        pygame.display.flip()
        clock.tick(60)
    pantalla.fill((0,0,0))

#Gameover J2
def GJ2():
    vgj2 = gameover_j2.video()
    pygame.mixer.init()
    pygame.mixer.music.load("musica/gameover.ogg")
    pygame.mixer.music.play(-1)
    clock = pygame.time.Clock()
    x = True
    while x:
        pantalla.fill((0,0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key==K_r:
                    pygame.mixer.music.stop()
                    x = False
        vgj2.update()
        pygame.display.flip()
        clock.tick(60)
    pantalla.fill((0,0,0))

def MusicaFondo():
    pygame.mixer.music.load("musica/axe.mp3")
    pygame.mixer.music.play(-1)
