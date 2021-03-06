import random

import pygame
import sys
import pygame.time as time
from gestionnaires.Evenement import *
from gestionnaires.Images import Images
from gestionnaires.Maj import *
from interfaces.Intro import Intro
from interfaces.Ecran import Ecran
from utils.Constantes import *

pygame.init()
random.seed()

ecran = pygame.display.set_mode(TAILLE)
pygame.display.set_caption("Dino Tempest")
icon = Images().charger_image("res/img/fenetre/icon2.png")
pygame.display.set_icon(icon)

intro = Intro()

clock = time.Clock()
gestionnaire_evenements = Evenement()
maj = Maj()
affichage = Ecran(ecran)

while 1:
    for evenement in pygame.event.get():
        if evenement.type == pygame.QUIT:
            sys.exit()
        else:
            gestionnaire_evenements.maj(evenement.type, evenement)

    delta = clock.tick(MAX_IPS) / 1000
    maj.maj(delta)

    ecran.fill(FOND)
    affichage.affichage(ecran)
    pygame.display.flip()
