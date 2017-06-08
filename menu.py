class Menu:
    "Representa un menú con opciones para un juego"
    
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
