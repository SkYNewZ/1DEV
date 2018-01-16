# coding=utf-8
from globales import *
from spawn_cars import *
from deposer_voiture import *


#ne pas oublier, la liste a été mélangé

def test_in_cars(x, y, locomotion, direction, voiture_courante):


	#si t'es a pied, don cque tu veux une voiture
	if locomotion == 1:

		#parcours de toute les voitures placées, placées PARKING
		for i in range(len(places_choisies)):

			#si on a deja pris la voiture
			if places_choisies[i] in parking_empty:
				pass
			
			#si on est sur une voiture
			elif x in range(places_choisies[i], places_choisies[i]+80) and y in range(parking_y_min, parking_y_max):

				#jouer le son entrer dans une voiture
				enter_car.play()				

				#stockage de la voiture chosie
				voiture_courante = modele_voiture[i]


				#on return le mode voiture, le modèle de voiture, la speed
				reponse = [2, speed_max, voiture_courante, orientation_voiture[i]]


				#veroou pour ne pas la réafficher ensuite, la voiture est masquée après avoir été prise
				voiture[i] = 0


				#âjouter la position chosi pour ne pas être repris
				parking_empty.append(places_choisies[i])


				return reponse


		#parcours de n'importe quelle voiture déposée
		for i in range(len(tab_voitures_deposees)):
			if x in range(x_deposee[i], x_deposee[i]+150) and y in range(y_deposee[i], y_deposee[i]+150):

				#jouer le son entrer dans une voiture
				enter_car.play()

				#stockage de la voiture chosie
				voiture_courante = tab_voitures_deposees[i]

				x_deposee.remove(x_deposee[i])
				y_deposee.remove(y_deposee[i])
				tab_voitures_deposees.remove(tab_voitures_deposees[i])
				direction_deposee.remove(direction_deposee[i])


				#on return le mode voiture, le modèle de voiture, la speed
				reponse = [2, speed_max, voiture_courante, direction]


				return reponse




		#sinon, on repasse ou on reste a pied
		reponse = [1, 5]


	#poser la voiture
	if locomotion == 2:

		leave_car.play()

		#deposer la voiture
		deposer_voiture(x, y, voiture_courante, direction)

		#a pied, speed=5
		reponse = [1, 5]



	return reponse