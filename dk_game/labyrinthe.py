import pygame
from pygame.locals import *

from classes import *
from constantes import *
import time





pygame.init()

# Ouverture de la fenêtre Pygame (carré : largeur = hauteur)
fenetre = pygame.display.set_mode((cote_fenetre, cote_fenetre))
# Icone
icone = pygame.image.load(image_icone)
pygame.display.set_icon(icone)
# Titre
pygame.display.set_caption(titre_fenetre)

# BOUCLE PRINCIPALE
continuer = 1
while continuer:
    # Chargement et affichage de l'écran d'accueil
    accueil = pygame.image.load(image_accueil).convert()
    fenetre.blit(accueil, (0, 0))

    # Rafraichissement
    pygame.display.flip()

    # On remet ces variables à 1 à chaque tour de boucle
    continuer_jeu = 1
    continuer_accueil = 1

    # BOUCLE D'ACCUEIL
    while continuer_accueil:

        # Limitation de vitesse de la boucle
        pygame.time.Clock().tick(30)

        for event in pygame.event.get():

            # Si l'utilisateur quitte, on met les variables
            # de boucle à 0 pour n'en parcourir aucune et fermer
            if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                continuer_accueil = 0
                continuer_jeu = 0
                continuer = 0
                # Variable de choix du niveau
                choix = 0

            elif event.type == KEYDOWN:
                # Lancement du niveau 1
                if event.key == K_F1:
                    continuer_accueil = 0  # On quitte l'accueil
                    choix = 'l1'  # On définit le niveau à charger
                # Lancement du niveau 2
                elif event.key == K_F2:
                    continuer_accueil = 0
                    choix = 'l2'
                # Lancement du niveau 3
                elif event.key == K_F3:
                    continuer_accueil = 0
                    choix = 'l3'

    # on vérifie que le joueur a bien fait un choix de niveau
    # pour ne pas charger s'il quitte
    fond = pygame.image.load(image_fond).convert()
    if choix != 0:
        # Chargement du fond

        # Génération d'un niveau à partir d'un fichier
        niveau = Niveau(choix)
        niveau.generer()
        niveau.afficher(fenetre)

        # Création de Donkey Kong
        pc = Perso(niveau)

    # BOUCLE DE JEU
    while continuer_jeu:

        # Limitation de vitesse de la boucle
        pygame.time.Clock().tick(30)

        for event in pygame.event.get():

            # Si l'utilisateur quitte, on met la variable qui continue le jeu
            # ET la variable générale à 0 pour fermer la fenêtre
            if event.type == QUIT:
                continuer_jeu = 0
                continuer = 0

            elif event.type == KEYDOWN:
                # Si l'utilisateur presse Echap ici, on revient seulement au menu
                if event.key == K_ESCAPE:
                    continuer_jeu = 0

                # Touches de déplacement de Donkey Kong
                elif event.key == K_RIGHT:
                    pc.travel(RIGHT)
                elif event.key == K_LEFT:
                    pc.travel(LEFT)
                elif event.key == K_UP:
                    pc.travel(UP)
                elif event.key == K_DOWN:
                    pc.travel(DOWN)

        # Affichages aux nouvelles positions
        fenetre.blit(fond, (0, 0))
        niveau.afficher(fenetre)

        fenetre.blit(pc.image, (pc.case_x * taille_sprite, pc.case_y * taille_sprite))  # plus besoin du commentaire inutile

        pygame.display.flip()

        # Victoire -> Retour à l'accueil
        if niveau.structure[pc.case_y][pc.case_x] == 'a':
            continuer_jeu = 0

