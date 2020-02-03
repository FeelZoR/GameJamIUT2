import pygame
from gestionnaires.Affichage import *
from gestionnaires.Maj import *
from gestionnaires.Evenement import *
from utils.Animation import Animation


class Joueur:
    TAILLE_IMAGE = [24 * 5, 24 * 5]

    def __init__(self):
        self.sprite = pygame.image.load('res/img/dino-jaune.png')
        self.rect = self.sprite.get_rect()
        self.vitesse = 300
        self.deplacement = [0, 0]

        self.anim_attente = Animation(0, 0, Joueur.TAILLE_IMAGE[0], Joueur.TAILLE_IMAGE[1], 4, 0.2)
        self.anim_deplacement = Animation(4, 0, Joueur.TAILLE_IMAGE[0], Joueur.TAILLE_IMAGE[1], 6, 0.2)
        self.anim_attaque = Animation(10, 0, Joueur.TAILLE_IMAGE[0], Joueur.TAILLE_IMAGE[1], 3, 0.2)
        self.anim_degat = Animation(13, 0, Joueur.TAILLE_IMAGE[0], Joueur.TAILLE_IMAGE[1], 4, 0.2)
        self.anim_accroupi = Animation(18, 0, Joueur.TAILLE_IMAGE[0], Joueur.TAILLE_IMAGE[1], 6, 0.2)

        evenement = Evenement()
        evenement.enregistrer(pygame.KEYDOWN, self)
        evenement.enregistrer(pygame.KEYUP, self)
        Affichage().enregistrer(self)
        Maj().enregistrer(self)

    def evenement(self, evenement):
        if evenement.type == pygame.KEYDOWN:
            if evenement.key == pygame.K_q:
                self.deplacement[0] -= 1
            elif evenement.key == pygame.K_d:
                self.deplacement[0] += 1

        else:  # KEYUP
            if evenement.key == pygame.K_q:
                self.deplacement[0] += 1
            elif evenement.key == pygame.K_d:
                self.deplacement[0] -= 1

    def maj(self, delta):
        self.anim_accroupi.ajouter_temps(delta)
        self.rect = self.rect.move(self.vitesse * self.deplacement[0] * delta,
                                   self.vitesse * self.deplacement[1] * delta)

    def affichage(self, ecran):
        ecran.blit(self.sprite, self.rect, self.anim_accroupi.recuperer_image())
