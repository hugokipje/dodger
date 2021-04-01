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

#startscherm display + speler moet klikken
tekst('Dodger', font, scherm, (scherm_breedte / 3) + 70, (scherm_hoogte / 3))
tekst('Klik om te beginnen', font, scherm, (scherm_breedte / 3) - 10, (scherm_hoogte / 3) + 70)
tekst('Door: Joris, Otte, Lucas en Hugo', font, scherm, (scherm_breedte / 3) - 100, (scherm_hoogte / 3) + 140)
pygame.display.update()
klikscherm()
