"""Classes du jeu de Labyrinthe Donkey Kong"""
import pygame
from constantes import *
from collections import deque

class Niveau:
    """Classe permettant de créer un niveau"""

    def __init__(self, fichier):
        self.fichier = fichier
        self.structure = 0

    def generer(self):
        """Méthode permettant de générer le niveau en fonction du fichier.
        On crée une liste générale, contenant une liste par ligne à afficher"""
        # On ouvre le fichier
        with open(self.fichier, "r") as fichier:
            structure_niveau = []
            # On parcourt les lignes du fichier
            for ligne in fichier:
                ligne_niveau = []
                # On parcourt les sprites (lettres) contenus dans le fichier
                for sprite in ligne:
                    # On ignore les "\n" de fin de ligne
                    if sprite != '\n':
                        # On ajoute le sprite à la liste de la ligne
                        ligne_niveau.append(sprite)
                # On ajoute la ligne à la liste du niveau
                structure_niveau.append(ligne_niveau)
            # On sauvegarde cette structure
            self.structure = structure_niveau

    def afficher(self, fenetre):
        """Méthode permettant d'afficher le niveau en fonction
        de la liste de structure renvoyée par generer()"""
        # Chargement des images (seule celle d'arrivée contient de la transparence)
        mur = pygame.image.load(image_mur).convert()
        depart = pygame.image.load(image_depart).convert()
        arrivee = pygame.image.load(image_arrivee).convert_alpha()

        # On parcourt la liste du niveau
        num_ligne = 0
        for ligne in self.structure:
            # On parcourt les listes de lignes
            num_case = 0
            for sprite in ligne:
                # On calcule la position réelle en pixels
                x = num_case * taille_sprite
                y = num_ligne * taille_sprite
                if sprite == 'm':  # m = Mur
                    fenetre.blit(mur, (x, y))
                elif sprite == 'd':  # d = Départ
                    fenetre.blit(depart, (x, y))
                elif sprite == 'a':  # a = Arrivée
                    fenetre.blit(arrivee, (x, y))
                num_case += 1
            num_ligne += 1



class Perso:
    """Classe permettant de créer un personnage"""

    def __init__(self, niveau, job_manager):
        # Position du personnage en cases et en pixels
        self.images = [pygame.image.load(img_folder + "pacman.png").convert_alpha()] * 4

        self.case_x = 0
        self.case_y = 0
        self.x = 0
        self.y = 0
        # Niveau dans lequel le personnage se trouve
        self.niveau = niveau
        self.job_manager = job_manager

        self.image = self.images[0]

    def move(self, direction):

        self.image = self.images[direction]  # images = [image_haut, image_bas, ...]

        next_x, next_y = self.next_position(direction)

        if self.can_move_to(next_x, next_y):
            self.case_x = next_x
            self.case_y = next_y
            return True
        return False

    def next_position(self, direction):
        shift_x, shift_y = movement[direction]

        next_x = self.case_x + shift_x
        next_y = self.case_y + shift_y
        return next_x, next_y

    def can_move_to(self, next_x, next_y):
        # si on va en dehors du plateau (on est pas dans le plateau)
        if not (0 <= next_x < nombre_sprite_cote and 0 <= next_y < nombre_sprite_cote):
            return False

        # si on se prend un mur
        if self.niveau.structure[next_y][next_x] == 'm':
            return False

        return True

    def travel(self, direction):
        if not self.move(direction):
            return

        backward_direction = opposite_direction(direction)

        self.job_manager.add_job(lambda: self.progress_into_the_path(backward_direction))

    def progress_into_the_path(self, backward_direction=NOWHERE):

        possible_direction = []

        # on test toutes les directions possibles
        for direction in directions:
            next_x, next_y = self.next_position(direction)

            if not self.can_move_to(next_x, next_y):
                continue

            # si c'est la direction d'ou le perso vient
            if direction is backward_direction:
                continue

            # c'est une direction possible
            possible_direction.append(direction)

        # S'il n'y a qu'une seule direction possible
        if len(possible_direction) == 1:
            direction = possible_direction.pop()

            # on continue le parcours
            self.travel(direction)


def opposite_direction(direction):
    """ Renvoie la direction opposee (UP <-> DOWN) (LEFT <-> RIGHT) """
    if direction in (UP, LEFT) :
        return directions[direction + 1]
    return directions[direction - 1]


class JobManager:
    def __init__(self):
        self.jobs = deque() # Une file

    def add_job(self, job):
        self.jobs.append(job)

    def execute_next_job(self):
        job = self.jobs.popleft() # recup le prochain
        job() # execute le job

    def has_job(self):
        return len(self.jobs) # 0 == False
