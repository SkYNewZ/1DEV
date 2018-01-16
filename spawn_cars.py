# coding=utf-8
import pygame, sys
from globales import *
from pygame.locals import *
from random import *
import random

#mélanger la liste des coordonnes
random.shuffle(liste_x_min)



for i in range(nb_cars_choisi):
	
	#random de la position
	position = liste_x_min[i]

	#stockage des positions - ID
	places_choisies.append(position)

	# #type de voiture+sens
	# voiture.append(liste_voiture[randint(0, len(liste_voiture)-1)])

	#random du modèle
	modele = randint(0, 4)

	#stockage du modele
	modele_voiture.append(modele)

	#random orientation
	orientation = randint(0, 1)

	#stockage
	orientation_voiture.append(orientation)

	#voiture choisie
	voiture.append(tab_voitures[modele][orientation])

	

def spawn_cars(x, y):

	#spawn individuel des voitures
	for i in range(nb_cars_choisi):

		#test si la voiture n'a pas été prise
		if voiture[i] != 0:
			
			#affochage de chaque voiture
			fenetre.blit(voiture[i], (liste_x_min[i]-(x-1500//2), parking_y_min-(y-825//2)))

	#affichage des voitures deposees
	for i in range(len(tab_voitures_deposees)):
		fenetre.blit(tab_voitures[tab_voitures_deposees[i]][direction_deposee[i]], (x_deposee[i]-(x-1500//2), y_deposee[i]-(y-825//2)-35))