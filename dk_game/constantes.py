"""Constantes du jeu de Labyrinthe Donkey Kong"""

#Paramètres de la fenêtre
nombre_sprite_cote = 15
taille_sprite = 30
cote_fenetre = nombre_sprite_cote * taille_sprite

#Personnalisation de la fenêtre
titre_fenetre = "Labyrinthe"

img_folder = "res/img/"
sound_folder = "res/sound/"

image_icone = img_folder + "pacman.png"

#Listes des images du jeu
image_accueil = img_folder + "accueil.png"
image_fond = img_folder + "fond.jpg"
image_mur = img_folder + "mur.png"
image_depart = img_folder + "depart.png"
image_arrivee = img_folder + "arrivee.png"


UP, DOWN, LEFT, RIGHT = range(4)
directions = (UP, DOWN, LEFT, RIGHT)
movement = ((0, -1), (0, 1), (-1, 0), (1, 0))