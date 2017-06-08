Agrega:

def MusicaFondo():
    //Cambialo por la direccion del mp3
    pygame.mixer.music.load("musica/axe.mp3")
    pygame.mixer.music.play(-1)

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
    
