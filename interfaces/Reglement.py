import pygame

from gestionnaires.Affichage import Affichage
from gestionnaires.Evenement import Evenement

from utils import Constantes


class Reglement:
    TITRE = (26, 188, 156)  # Turquoise
    SOUS_TITRE = (41, 128, 185)  # Bleu
    DESCRIPTION = (255, 255, 255)  # Blanc
    TOUCHE = (0, 0, 0)  # Noir

    def __init__(self, menu):
        self.montrer = False
        self.__menu = menu
        self.__background = pygame.image.load("res/img/interfaces/accueil/accueil-background.png")
        Affichage().enregistrer(self)
        Evenement().enregistrer(pygame.KEYUP, self)

    def affichage(self, ecran):
        if self.montrer:
            ecran.blit(self.__background, (-490, 0))

            # Titre
            font = pygame.font.Font("res/fonts/Comfortaa-Bold.ttf", 60)
            texte = font.render("Règles", True, self.TITRE)
            ecran.blit(texte, (Constantes.LARGEUR / 2 - texte.get_width() / 2, 20))

            # Objectif
            font = pygame.font.Font("res/fonts/Comfortaa-Bold.ttf", 36)
            ecran.blit(font.render("Objectif", True, self.SOUS_TITRE), (50, 110))
            font = pygame.font.Font("res/fonts/Comfortaa-Bold.ttf", 20)
            ecran.blit(font.render("Soyez le dernier en vie en utilisant les", True, self.DESCRIPTION), (50, 160))
            ecran.blit(font.render("courants ascendants et descendants", True, (155, 89, 182)), (455, 160))
            ecran.blit(font.render("pour changer", True, self.DESCRIPTION), (860, 160))
            ecran.blit(font.render("d'étages. Vous disposez également d'une", True, self.DESCRIPTION), (50, 187))
            ecran.blit(font.render("compétence unique", True, (230, 126, 34)), (490, 187))
            ecran.blit(font.render(", propre à chaque dinosaure.", True, self.DESCRIPTION), (705, 187))
            ecran.blit(
                font.render("Evitez les obstacles et courez, la caméra se déplace en fonction du joueur en première",
                            True, self.DESCRIPTION), (50, 214))
            ecran.blit(
                font.render("position. Si vous sortez de l'écran (à gauche) vous perdez une vie et réapparaissez au",
                            True, self.DESCRIPTION), (50, 241))
            ecran.blit(font.render("centre de l'écran. Vous ne possédez que", True, self.DESCRIPTION), (50, 268))
            ecran.blit(font.render("5 vies", True, (231, 76, 60)), (485, 268))
            ecran.blit(font.render(".", True, self.DESCRIPTION), (550, 268))

            # Commandes
            font = pygame.font.Font("res/fonts/Comfortaa-Bold.ttf", 36)
            ecran.blit(font.render("Commandes", True, self.SOUS_TITRE), (50, 320))
            font = pygame.font.Font("res/fonts/Comfortaa-Bold.ttf", 26)
            ecran.blit(font.render("Joueur 1", True, self.DESCRIPTION), (350, 370))
            ecran.blit(font.render("Joueur 2", True, self.DESCRIPTION), (750, 370))
            font = pygame.font.Font("res/fonts/Comfortaa-Bold.ttf", 22)
            ecran.blit(font.render("Déplacements", True, self.DESCRIPTION), (50, 480))
            ecran.blit(font.render("Compétence", True, self.DESCRIPTION), (50, 650))
            touche = pygame.image.load("res/img/interfaces/regles/touche.png")
            font = pygame.font.Font("res/fonts/NotoSansJP-Bold.otf", 45)

            # Joueur 1
            ecran.blit(touche, (370, 430))  # Haut
            ecran.blit(touche, (370, 505))  # Bas
            ecran.blit(touche, (290, 505))  # Gauche
            ecran.blit(touche, (450, 505))  # Droite
            ecran.blit(touche, (370, 630))  # Compétence
            ecran.blit(font.render(self.nom_touche(Constantes.TOUCHES[0]['sauter']), True, self.TOUCHE), (390, 425))  # Haut
            # ecran.blit(font.render(pygame.key.name(Constantes.TOUCHES[0]['']), True, self.TOUCHE), (370, 505))  # Bas
            ecran.blit(font.render(self.nom_touche(Constantes.TOUCHES[0]['aller_gauche']), True, self.TOUCHE), (307, 495))  # Gauche
            ecran.blit(font.render(self.nom_touche(Constantes.TOUCHES[0]['aller_droite']), True, self.TOUCHE), (470, 500))  # Droite
            ecran.blit(font.render(self.nom_touche(Constantes.TOUCHES[0]['competence']), True, self.TOUCHE), (377, 630))  # Compétence

            # Joueur 2
            ecran.blit(touche, (770, 430))  # Haut
            ecran.blit(touche, (770, 505))  # Bas
            ecran.blit(touche, (690, 505))  # Gauche
            ecran.blit(touche, (850, 505))  # Droite
            ecran.blit(touche, (770, 630))  # Compétence
            ecran.blit(font.render(self.nom_touche(Constantes.TOUCHES[1]['sauter']), True, self.TOUCHE), (785, 425))  # Haut
            # ecran.blit(font.render(pygame.key.name(Constantes.TOUCHES[0]['']), True, self.TOUCHE), (370, 505))  # Bas
            ecran.blit(font.render(self.nom_touche(Constantes.TOUCHES[1]['aller_gauche']), True, self.TOUCHE), (700, 500))  # Gauche
            ecran.blit(font.render(self.nom_touche(Constantes.TOUCHES[1]['aller_droite']), True, self.TOUCHE), (865, 500))  # Droite
            ecran.blit(font.render(self.nom_touche(Constantes.TOUCHES[1]['competence']), True, self.TOUCHE), (773, 627))  # Compétence

            font = pygame.font.Font("res/fonts/Comfortaa-Bold.ttf", 20)
            texte = font.render("ESC pour retourner au menu principal", True, self.DESCRIPTION)
            ecran.blit(texte, (Constantes.LARGEUR / 2 - texte.get_width() / 2, 740))

    def evenement(self, evenement):
        if self.montrer and evenement.key == pygame.K_ESCAPE:
            self.montrer = False
            self.__menu.montrer = True

    def nom_touche(self, touche):
        touches = {
            pygame.K_RIGHT: '→',
            pygame.K_LEFT: '←',
            pygame.K_UP: '↑',
            pygame.K_DOWN: '↓',
            pygame.K_RSHIFT: 'R⇧',
            pygame.K_LSHIFT: 'L⇧'
        }
        if touche in touches.keys():
            return touches[touche]
        else:
            return pygame.key.name(touche).upper()