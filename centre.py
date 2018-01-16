# coding=utf-8
import pygame, sys
from globales import *
from pygame.locals import *


def afficher_perso(direction, locomotion, position, modele_voiture):

	coord_centre_perso_horizontal = [1500//2-20, 825//2-65]
	coord_centre_perso_vertical = [1500//2-30, 825//2-55]

	#coordonnées du (centre de la map)-x/2; (centre de la map)-y/2 
	
	#voiture
	if locomotion == 2:
		#monter
		if direction == 1:
			fenetre.blit(tab_voitures[modele_voiture][0], ((1500//2)-35, (825//2-35)-67))
		#descendre
		if direction == 2:
			fenetre.blit(tab_voitures[modele_voiture][1], ((1500//2)-35, (825//2-35)-67))
		#gauche
		if direction == 3:
			fenetre.blit(tab_voitures[modele_voiture][2], ((1500//2)-67, (825//2-35)-35))
		#droite
		if direction == 4:
			fenetre.blit(tab_voitures[modele_voiture][3], ((1500//2)-67, (825//2-35)-35))	





	##a pied
	if locomotion == 1:

		#gauche
		if direction == 3:
			if position == 1 or position == 2:
				fenetre.blit(tab_perso[armed[0]][18], (coord_centre_perso_horizontal[0], coord_centre_perso_horizontal[1]))
			if position == 3 or position == 4:
				fenetre.blit(tab_perso[armed[0]][19], (coord_centre_perso_horizontal[0], coord_centre_perso_horizontal[1]))
			if position == 5 or position == 6:
				fenetre.blit(tab_perso[armed[0]][20], (coord_centre_perso_horizontal[0], coord_centre_perso_horizontal[1]))
			if position == 7 or position == 8:
				fenetre.blit(tab_perso[armed[0]][21], (coord_centre_perso_horizontal[0], coord_centre_perso_horizontal[1]))
			if position == 9 or position == 10:
				fenetre.blit(tab_perso[armed[0]][22], (coord_centre_perso_horizontal[0], coord_centre_perso_horizontal[1]))
			if position == 11 or position == 12:
				fenetre.blit(tab_perso[armed[0]][23], (coord_centre_perso_horizontal[0], coord_centre_perso_horizontal[1]))

		#droite
		if direction == 4:
			if position == 1 or position == 2:
				fenetre.blit(tab_perso[armed[0]][12], (coord_centre_perso_horizontal[0], coord_centre_perso_horizontal[1]))
			if position == 3 or position == 4:
				fenetre.blit(tab_perso[armed[0]][13], (coord_centre_perso_horizontal[0], coord_centre_perso_horizontal[1]))
			if position == 5 or position == 6:
				fenetre.blit(tab_perso[armed[0]][14], (coord_centre_perso_horizontal[0], coord_centre_perso_horizontal[1]))
			if position == 7 or position == 8:
				fenetre.blit(tab_perso[armed[0]][15], (coord_centre_perso_horizontal[0], coord_centre_perso_horizontal[1]))
			if position == 9 or position == 10:
				fenetre.blit(tab_perso[armed[0]][16], (coord_centre_perso_horizontal[0], coord_centre_perso_horizontal[1]))
			if position == 11 or position == 12:
				fenetre.blit(tab_perso[armed[0]][17], (coord_centre_perso_horizontal[0], coord_centre_perso_horizontal[1]))

		#haut
		if direction == 1:
			if position == 1 or position == 2:
				fenetre.blit(tab_perso[armed[0]][6], (coord_centre_perso_vertical[0], coord_centre_perso_vertical[1]))
			if position == 3 or position == 4:
				fenetre.blit(tab_perso[armed[0]][7], (coord_centre_perso_vertical[0], coord_centre_perso_vertical[1]))
			if position == 5 or position == 6:
				fenetre.blit(tab_perso[armed[0]][8], (coord_centre_perso_vertical[0], coord_centre_perso_vertical[1]))
			if position == 7 or position == 8:
				fenetre.blit(tab_perso[armed[0]][9], (coord_centre_perso_vertical[0], coord_centre_perso_vertical[1]))
			if position == 9 or position == 10:
				fenetre.blit(tab_perso[armed[0]][10], (coord_centre_perso_vertical[0], coord_centre_perso_vertical[1]))
			if position == 11 or position == 12:
				fenetre.blit(tab_perso[armed[0]][11], (coord_centre_perso_vertical[0], coord_centre_perso_vertical[1]))

		#bas
		if direction == 2:
			if position == 1 or position == 2:
				fenetre.blit(tab_perso[armed[0]][0], (coord_centre_perso_vertical[0], coord_centre_perso_vertical[1]))
			if position == 3 or position == 4:
				fenetre.blit(tab_perso[armed[0]][1], (coord_centre_perso_vertical[0], coord_centre_perso_vertical[1]))
			if position == 5 or position == 6:
				fenetre.blit(tab_perso[armed[0]][2], (coord_centre_perso_vertical[0], coord_centre_perso_vertical[1]))
			if position == 7 or position == 8:
				fenetre.blit(tab_perso[armed[0]][3], (coord_centre_perso_vertical[0], coord_centre_perso_vertical[1]))
			if position == 9 or position == 10:
				fenetre.blit(tab_perso[armed[0]][4], (coord_centre_perso_vertical[0], coord_centre_perso_vertical[1]))
			if position == 11 or position == 12:
				fenetre.blit(tab_perso[armed[0]][5], (coord_centre_perso_vertical[0], coord_centre_perso_vertical[1]))



		#DEBUG
		# pygame.draw.circle(fenetre, (255, 0,0), (1500//2, 825//2-35), 5)