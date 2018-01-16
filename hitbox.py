# coding=utf-8
from globales import *

def hitbox(x, y, direction, locomotion):


	#decalage de px selon la direction et le moyen de locomotion pour rester dans le bloc autorisé et donner l'impression du "rafler le mur"
	#decalage de 2px, a pied
	if locomotion == 1:
		decalage = 2

	#decalage de 10px, voiture
	if locomotion == 2:
		decalage = 30
	
	#on recupere l'emplacement du bloc suivant
	idx_x = (x//75)+10
	idx_y = (y//75)+5

	#valeur du bloc suivant
	direction_bloc = matrice[idx_y][idx_x]

	#if direction_bloc in block:
	if direction_bloc in block:
		
		#monter
		if direction == 1:
			y = (idx_y+1)*75-(375-decalage)

		#descendre
		if direction == 2:
			y = (idx_y)*75-(375+decalage)

		#gauche
		if direction == 3:
			x = (idx_x+1)*75-(750-decalage)

		#droite
		if direction == 4:
			x = idx_x*75-(750+decalage)

		reponse = [x, y]

	else:
		reponse = [x, y]


	return reponse
