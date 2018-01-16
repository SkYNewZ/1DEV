# coding=utf-8
from globales import *
from pygame.locals import *

def move_npc(map_x, map_y):

	decalage_img_y = 35//2
	temp_down = 0
	temp_up = 0
	temp_left = 0
	temp_right = 0
	bloc_passed_npc = [4, 67, 56]
	bloc_passed_cars = [1, 2, 3, 5, 6, 7, 56]

	#npc
	for i in range(len(npc_x)):

		#vertical
		if i in npc_v:

			#recupération des coordonnes de l'étape d'avant
			x = npc_x[i]
			y = npc_y[i]

			#down
			if sens_npc[i] == 0:

				#calcul de la positon de l'animation
				temp_down = npc_down[0]//4
				y += speed_npc
				npc_y[i] = y
				valeur_matrice = matrice[(y//75)+5][(x//75)+10]

				#test si le npc peut se déplacer
				if valeur_matrice in bloc_passed_npc:
					fenetre.blit(tab_npcs[1][temp_down], (x-(map_x-1500//2), y-(map_y-825//2)-35-decalage_img_y))
					npc_down[0] += 1
					if npc_down[0] == 16 : npc_down[0] = 0
				#sinon, retour a la positon d'avant
				else:
					sens_npc[i] = 1
					npc_y[i] -= speed_npc


			#up
			if sens_npc[i] == 1:
				temp_up = npc_up[0]//4
				y -= speed_npc
				npc_y[i] = y
				valeur_matrice = matrice[(y//75)+5][(x//75)+10]
				if valeur_matrice in bloc_passed_npc:
					fenetre.blit(tab_npcs[0][temp_up], (x-(map_x-1500//2), y-(map_y-825//2)-35-decalage_img_y))
					npc_up[0] += 1
					if npc_up[0] == 16 : npc_up[0] = 0
				else:
					sens_npc[i] = 0
					npc_y[i] += speed_npc


		#horizontal
		if i in npc_h:
			x = npc_x[i]
			y = npc_y[i]

			
			#right
			if sens_npc[i] == 0:
				temp_right = npc_right[0]//4
				x += speed_npc
				npc_x[i] = x
				valeur_matrice = matrice[(y//75)+5][(x//75)+10]
				if valeur_matrice in bloc_passed_npc:
					fenetre.blit(tab_npcs[3][temp_right], (x-(map_x-1500//2), y-(map_y-825//2)-35-decalage_img_y))
					npc_right[0] += 1
					if npc_right[0] == 16 : npc_right[0] = 0
				else:
					sens_npc[i] = 1
					npc_x[i] -= speed_npc


			#left
			if sens_npc[i] == 1:
				x -= speed_npc
				temp_left = npc_left[0]//4
				npc_x[i] = x
				valeur_matrice = matrice[(y//75)+5][(x//75)+10]
				if valeur_matrice in bloc_passed_npc:
					fenetre.blit(tab_npcs[2][temp_left], (x-(map_x-1500//2), y-(map_y-825//2)-35))
					npc_left[0] += 1
					if npc_left[0] == 16 : npc_left[0] = 0
				else:
					sens_npc[i] = 0
					npc_x[i] += speed_npc

	#npc_car
	for i in range(len(car_npc_x)):
		#vertical
		if i == 1 or i == 2 or i == 5 or i == 6:

			#recupération des coordonnes de l'étape d'avant
			x = car_npc_x[i]
			y = car_npc_y[i]

			#down
			if car_sens_npc[i] == 0:

				y += speed_npc_car
				car_npc_y[i] = y
				valeur_matrice = matrice[(y//75)+5][(x//75)+10]

				#test si le npc peut se déplacer
				if valeur_matrice in bloc_passed_cars:
					fenetre.blit(tab_voitures[car_type[i]][1], (x-(map_x-1500//2), y-(map_y-825//2)-35-140))
				#sinon, retour a la positon d'avant
				else:
					car_sens_npc[i] = 1
					car_npc_y[i] -= speed_npc_car


			#up
			if car_sens_npc[i] == 1:
				y -= speed_npc_car
				car_npc_y[i] = y
				valeur_matrice = matrice[(y//75)+5][(x//75)+10]
				if valeur_matrice in bloc_passed_cars:
					fenetre.blit(tab_voitures[car_type[i]][0], (x-(map_x-1500//2), y-(map_y-825//2)-35-140))
				else:
					car_sens_npc[i] = 0
					car_npc_y[i] += speed_npc_car

		#horizontal
		if i ==0 or i == 3 or i == 4 or i == 7 or i == 8:

			#recupération des coordonnes de l'étape d'avant
			x = car_npc_x[i]
			y = car_npc_y[i]

			#left
			if car_sens_npc[i] == 1:
				x -= speed_npc_car
				car_npc_x[i] = x
				valeur_matrice = matrice[(y//75)+5][(x//75)+10]
				if valeur_matrice in bloc_passed_cars:
					fenetre.blit(tab_voitures[car_type[i]][2], (x-(map_x-1500//2), y-(map_y-825//2)-35))
				else:
					car_sens_npc[i] = 0
					car_npc_x[i] += speed_npc_car

			#right
			if car_sens_npc[i] == 0:
				x += speed_npc_car
				car_npc_x[i] = x
				valeur_matrice = matrice[(y//75)+5][(x//75)+10]
				if valeur_matrice in bloc_passed_cars:
					fenetre.blit(tab_voitures[car_type[i]][3], (x-(map_x-1500//2)-14, y-(map_y-825//2)-35))
				else:
					car_sens_npc[i] = 1
					car_npc_x[i] -= speed_npc_car
