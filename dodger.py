import pygame, random , sys
from pygame.locals import *

#variabelen
scherm_breedte = 1000
scherm_hoogte = 1000
tekstkleur = (255, 255, 255)

#functie voor eindigen spel
def eindigen():
    pygame.quit()
    sys.exit()

#functie tekst
def tekst(tekst, font, oppervlak, x, y):
    tekstobject = font.render(tekst, 1, tekstkleur)
    tekstvak = tekstobject.get_rect()
    tekstvak.topleft = (x, y)
    oppervlak.blit(tekstobject, tekstvak)

#functie startscherm
def klikscherm():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                eindigen()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    eindigen()
                return

#functie otte raakt slechterik
def boem(plaatje_raakvlak, slechterik):
    for b in slechterik:
        if plaatje_raakvlak.colliderect(b['rect']):
            return True
    return False

#scherm en in-game klok
pygame.init()
ingameklok = pygame.time.Clock()
scherm = pygame.display.set_mode((scherm_breedte, scherm_hoogte))
pygame.display.set_caption('Dodger')
pygame.mouse.set_visible(False)

font = pygame.font.SysFont(None, 48)

#plaatjes
otte_plaatje = pygame.image.load('ottertje2.png')
plaatje_raakvlak = otte_plaatje.get_rect()
plaatje_slechterik = pygame.image.load('mariothwomp.png')

#geluid
gameovergeluid = pygame.mixer.Sound('gameover.wav')
pygame.mixer.music.load('background2.mid')

#startscherm display + speler moet klikken
tekst('Dodger', font, scherm, (scherm_breedte / 3) + 70, (scherm_hoogte / 3))
tekst('Klik om te beginnen', font, scherm, (scherm_breedte / 3) - 10, (scherm_hoogte / 3) + 70)
tekst('Door: Joris, Otte, Lucas en Hugo', font, scherm, (scherm_breedte / 3) - 100, (scherm_hoogte / 3) + 140)
pygame.display.update()
klikscherm()

top_score = 0

#start van het spel
while True:
    slechterik = []
    score = 0
    plaatje_raakvlak.topleft = (scherm_breedte / 2, scherm_hoogte - 50)
    moveLeft = moveRight = moveUp = moveDown = False
    reverseCheat = slowCheat = False
    slechterik_toevoegen = 0
    pygame.mixer.music.play(-1, 0.0)

    while True: 
        score += 1 

        for event in pygame.event.get():
            if event.type == QUIT:
                eindigen()

            if event.type == KEYDOWN:
                if event.key == ord('z'):
                    reverseCheat = True
                if event.key == ord('x'):
                    slowCheat = True
                if event.key == K_LEFT or event.key == ord('a'):
                    moveRight = False
                    moveLeft = True
                if event.key == K_RIGHT or event.key == ord('d'):
                    moveLeft = False
                    moveRight = True
                if event.key == K_UP or event.key == ord('w'):
                    moveDown = False
                    moveUp = True
                if event.key == K_DOWN or event.key == ord('s'):
                    moveUp = False
                    moveDown = True

            if event.type == KEYUP:
                if event.key == ord('z'):
                    reverseCheat = False
                    score = 0
                if event.key == ord('x'):
                    slowCheat = False
                    score = 0
                if event.key == K_ESCAPE:
                        eindigen()

                if event.key == K_LEFT or event.key == ord('a'):
                    moveLeft = False
                if event.key == K_RIGHT or event.key == ord('d'):
                    moveRight = False
                if event.key == K_UP or event.key == ord('w'):
                    moveUp = False
                if event.key == K_DOWN or event.key == ord('s'):
                    moveDown = False

            if event.type == MOUSEMOTION:
                # If the mouse moves, move the player where the cursor is.
                plaatje_raakvlak.move_ip(event.pos[0] - plaatje_raakvlak.centerx, event.pos[1] - plaatje_raakvlak.centery)
