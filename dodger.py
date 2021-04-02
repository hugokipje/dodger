import pygame, random , sys
from pygame.locals import *

#variabelen
scherm_breedte = 1000
scherm_hoogte = 1000
tekstkleur = (255, 255, 255)
achtergrond = (21, 67, 96)
min_grootte_slechterik = 10
max_grootte_slechterik = 40
min_snelheid_slechterik = 1
max_snelheid_slechterik = 8
frequentie_slechteriken = 6
snelheid_otte = 5
fps = 60

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
                #je kan nu ook met muis besturen
                plaatje_raakvlak.move_ip(event.pos[0] - plaatje_raakvlak.centerx, event.pos[1] - plaatje_raakvlak.centery)

        pygame.mouse.set_pos(plaatje_raakvlak.centerx, plaatje_raakvlak.centery)        

        #zorgen dat het beweegt
        if moveLeft and plaatje_raakvlak.left > 0:
            plaatje_raakvlak.move_ip(-1 * snelheid_otte, 0)
        if moveRight and plaatje_raakvlak.right < scherm_breedte:
            plaatje_raakvlak.move_ip(snelheid_otte, 0)
        if moveUp and plaatje_raakvlak.top > 0:
            plaatje_raakvlak.move_ip(0, -1 * snelheid_otte)
        if moveDown and plaatje_raakvlak.bottom < scherm_hoogte:
            plaatje_raakvlak.move_ip(0, snelheid_otte)

        #nieuwe slechteriken
        if not reverseCheat and not slowCheat:
            slechterik_toevoegen += 1
        if slechterik_toevoegen == frequentie_slechteriken:
            slechterik_toevoegen = 0
            slechterik_grootte = random.randint(min_grootte_slechterik, max_grootte_slechterik)
            nieuwe_slechterik = {'rect': pygame.Rect(random.randint(0, scherm_breedte-slechterik_grootte), 0 - slechterik_grootte, slechterik_grootte, slechterik_grootte),
                         'speed': random.randint(min_snelheid_slechterik, max_snelheid_slechterik),
                         'surface': pygame.transform.scale(plaatje_slechterik, (slechterik_grootte, slechterik_grootte)),
                         }

            slechterik.append(nieuwe_slechterik)

        #zorgen dat slechteriken bewegen
        for b in slechterik:
            if not reverseCheat and not slowCheat:
                b['rect'].move_ip(0, b['speed'])
            elif reverseCheat:
                b['rect'].move_ip(0, -5)
            elif slowCheat:
                b['rect'].move_ip(0, 1)

        #zorgen dat slechteriken verdwijnen
        for b in slechterik[:]:
            if b['rect'].top > scherm_hoogte:
                slechterik.remove(b)

        scherm.fill(achtergrond)

        #score + top-score
        tekst('Score: %s' % (score), font, scherm, 10, 0)
        tekst('Top Score: %s' % (top_score), font, scherm, 10, 40)

        #goeierik tekenen
        scherm.blit(otte_plaatje, plaatje_raakvlak)

        #slechterik tekenen
        for b in slechterik:
            scherm.blit(b['surface'], b['rect'])

        pygame.display.update()

        #goeierik raakt slechterik
        if boem(plaatje_raakvlak, slechterik):
            if score > top_score:
                top_score = score 
            break

        ingameklok.tick(fps)

    #game-over + scherm daarvoor
    pygame.mixer.music.stop()
    gameovergeluid.play()

    tekst('GAME OVER :-(', font, scherm, (scherm_breedte / 3), (scherm_hoogte / 3))
    tekst('Klik om opnieuw te beginnen', font, scherm, (scherm_breedte / 3) - 80, (scherm_hoogte / 3) + 50)
    pygame.display.update()
    klikscherm()

    gameovergeluid.stop()
