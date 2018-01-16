# coding=utf-8
import pygame, sys
from generer_map import *
from globales import *
from hitbox import *
from save import *
from load import *
from load_x import *
from load_y import *
from load_direction_deposee import *
from load_tab_voitures_deposees import *
from centre import *
from spawn_cars import *
from in_cars import *
from move_npc import *
from spawn_weapon import *
from take_weapon import *
from pygame.locals import *
pygame.init()

display_msg = 0
acceleration_voiture = False
bruit_pas = False
music_menu_played = False
fps_max = pygame.time.Clock()

#entrée boucle de jeu
while inProgress:

	#menu
	if menu_principal == True and display_msg == 0:

		if music_menu_played == False:
			#demarrage du son ambiant
			music_menu.play()
			music_menu_played = True

		#affichage menu
		fenetre.blit(menu_titre, (0, 0))


		#gestion des clics
		for event in pygame.event.get():

			#QUITTER
			if event.type == QUIT:
				inProgress = False
				pygame.mixer.stop()

			#deplacement de la souris
			if event.type == MOUSEMOTION:
				pos_x = event.pos[0]
				pos_y = event.pos[1]

		#souligner new game
		if pos_x in range(116, 390) and pos_y in range(480, 521):
			fenetre.blit(titre_new_game, (0, 0))


		#souliginer continue
		elif pos_x in range(115, 385) and pos_y in range(580, 620):
			fenetre.blit(titre_continue, (0, 0))

		#souligner quit
		elif pos_x in range(115, 221) and pos_y in range(672, 712):
			fenetre.blit(titre_exit, (0, 0))



		#gestion des clics
		for event in pygame.event.get():

			#clics
			if event.type == MOUSEBUTTONUP:
				pos_x = event.pos[0]
				pos_y = event.pos[1]

				#New game
				if pos_x in range(116, 390) and pos_y in range(480, 521):

					#on sort du menu principal
					menu_principal = False

					pygame.mixer.stop()

					#redefinition du spawn
					map_x = 5545
					map_y = 810

					#direction et animation
					direction = 2
					position = 1
					locomotion = 1
					speed = 5
					armed[0] = 0


					#reinitialisation des voitures deposees et affichage de la premier voiture
					for i in range(1, len(tab_voitures_deposees)):
						tab_voitures_deposees.remove(tab_voitures_deposees[i])
						x_deposee.remove(x_deposee[i])
						y_deposee.remove(y_deposee[i])
						direction_deposee.remove(direction_deposee[i])

					tab_voitures_deposees[0] = 3
					x_deposee[0] = 5310
					y_deposee[0] = 755
					direction_deposee[0] = 3


					#reinitialisation des missions
					eta_mission_1 = 0
					eta_mission_2 = 0
					mission_en_cours = 1

					#centre de la fenetre
					afficher_perso(2, 1, 1, 0)

					if eta_mission_1 == 0:
						fenetre.blit(missions_1_1, (1150, 770))
					elif eta_mission_1 == 1:
						fenetre.blit(missions_1_2, (930, 770))


				#Continue
				if pos_x in range(115, 385) and pos_y in range(580, 620):

					#on sort du menu principal
					menu_principal = False

					pygame.mixer.stop()


					#initialisation des variables sauvegardes
					data = load()
					map_x = data[0]
					map_y = data[1]
					locomotion = data[2]
					direction = data[3]
					position = data[4]
					nb_cars_choisi = data[5]
					eta_mission_1 = data[6]
					armed[0] = data[7]

					#vitesse - 20 = voiture, 5 = piéton
					if locomotion == 1:
						speed = 5
					if locomotion == 2:
						speed = 20

					#remise en place avec la sauvegarde
					generation_map(map_x, map_y)


					#spawn des voitures
					spawn_cars(map_x, map_y)


					#centre de la fenetre
					afficher_perso(direction, locomotion, position, voiture_courante)

					if eta_mission_1 == 0:
						fenetre.blit(missions_1_1, (1150, 770))
					elif eta_mission_1 == 1:
						fenetre.blit(missions_1_2, (930, 770))


				#Quitter
				if pos_x in range(115, 221) and pos_y in range(672, 712):
					inProgress = False
					pygame.mixer.stop()


	#game
	if menu_principal == False and display_msg == 0:

		if pygame.mixer.get_busy() == False and title == 0:
			#demarrage du son ambiant
			bruit_ambiant.play()

		#gestion in-game
		for event in pygame.event.get():

			#QUITTER
			if event.type == QUIT:
				inProgress = False


			#gestion selon appui touches
			if event.type == KEYDOWN and title == 0:

				#ebauche bruit dep pas
				if locomotion == 1 and bruit_pas == False:
					bruit_pieton.play()
					bruit_pas = True

				if event.key == K_w or event.key == K_z or event.key == K_UP: #monter
					map_y -= speed
					direction = 1

				if event.key == K_s or event.key == K_DOWN: #descendre
					map_y += speed
					direction = 2

				if event.key == K_a or event.key == K_q or event.key == K_LEFT: #gauche
					map_x -= speed
					direction = 3

				if event.key == K_d or event.key == K_RIGHT: #droite
					map_x += speed
					direction = 4

				#si on appuie sur "e" d'une voiture
				if event.key == K_e:

					#test si on est près d'une voiture
					test_cars = test_in_cars(map_x, map_y, locomotion, direction, voiture_courante)
					locomotion = test_cars[0]
					speed = test_cars[1]


					#si on est près une voiture, on rentre dedans
					if locomotion == 2:
						voiture_courante = test_cars[2]
						direction = test_cars[3]


				#lacher l'arme
				if event.key == K_f and armed[0] == 1:
					armed[0] = 0
					arme_x.append(map_x+20)
					arme_y.append(map_y+20)

				#animation personnage
				position += 1

				#test de la hitbox suite a l'appui sur une touche
				test_hitbox = hitbox(map_x, map_y, direction, locomotion) #derniere valeur correspond au moyen de locomotion (1 ou a pied, 2 pour en voiture)
				map_x = test_hitbox[0]
				map_y = test_hitbox[1]

				# DEBUG, affichage des infos
				if debug:
					cls()
					print("Coordonees relatives du point central : ", map_x, map_y)
					print ("Valeur de la case actuelle dans la matrice : ", matrice[(map_y//75)+5][(map_x//75)+10])
					print("zone de la map", map_x//1500, map_y//825)


			#lancement menu pause
			if event.type == KEYDOWN and event.key == K_ESCAPE:
				touche_echap += 1
				
				#mise en pause des bruits
				pygame.mixer.pause()

				#menu	
				fenetre.blit(menu, (0, 0))

				#blocage des touches de navigation
				title = 1

				#retour en jeu
				if touche_echap == 2:

					pygame.mixer.unpause()

					#reinitialisation
					title = 0
					touche_echap = 0


			#clics selon le menu
			if event.type == MOUSEBUTTONUP and title == 1:
				pos_x = event.pos[0]
				pos_y = event.pos[1]

				#resume
				if pos_x in range(110, 315) and pos_y in range(190, 230):

					pygame.mixer.unpause()


					#reinitialisation
					title = 0


				#quitter
				if pos_x in range(210, 325) and pos_y in range(555, 600):
					inProgress = False


				#sauvegarder
				if pos_x in range(130, 260) and pos_y in range(350, 400):


					#choix des donnes a sauvegarder
					tab_save = [map_x, map_y, locomotion, direction, position, nb_cars_choisi, eta_mission_1, armed[0]]


					save(tab_save)
					fenetre.blit(menu_saved, (0, 0))


				#menu
				if pos_x in range(125, 290) and pos_y in range(260, 320):
					menu_principal = True
					title = 0
					touche_echap = 0
					music_menu_played = False

					#sortir de la voiture
					test_cars = test_in_cars(map_x, map_y, locomotion, direction, voiture_courante)
					locomotion = test_cars[0]
					speed = test_cars[1]

					#choix des donnes a sauvegarder
					tab_save = [map_x, map_y, locomotion, direction, position, nb_cars_choisi, eta_mission_1, armed[0]]

					save(tab_save)

				#settings (son)
				if pos_x in range(110, 320) and pos_y in range(435, 485):
					pass

		#stop bruit de pas
		if event.type == KEYUP and locomotion == 1: bruit_pas = False


		#actualisation
		if title == 0:

			if locomotion == 2 and acceleration_voiture == False:
				bruit_car.play()
				acceleration_voiture = True
			if locomotion == 1:
				bruit_car.stop()
				acceleration_voiture = False

			#actualisation de la map
			generation_map(map_x, map_y)

			#spawn des voitures
			spawn_cars(map_x, map_y)

			#affichage npc
			move_npc(map_x, map_y)

			#affichage des armes
			if mission_en_cours > 2:

				spawn_weapon(map_x, map_y)

				#si tu prends une arme
				if locomotion == 1: take_weapon(map_x, map_y)


			if armed[0]: fenetre.blit(pistol, (1400, 50))

			

			#centre de la fenetre
			afficher_perso(direction, locomotion, position, voiture_courante)
			if position == 12:
				position = 0

			#si mission_1 pas terminé
			if eta_mission_1 != -1 and mission_en_cours == 1:

				#affichage de l'objectif mission 1
				fenetre.blit(zone_mission_1, (5295-(map_x-1500//2), 2520-(map_y-825//2)))

				#changement d'état de la mission
				#si il a prit la voiture
				if locomotion == 2:
					eta_mission_1 = 1

				#si il est retourné a pied
				elif locomotion == 1:
					eta_mission_1 = 0

				#si il a conduit jusqua la destination donc terminé
				if map_x in range(5370, 5400) and map_y in range(2520, 2640) and locomotion == 2:

					#fin mission
					eta_mission_1 = -1
					display_msg = 1


				#affichage du message selon les étapes de la mission
				if eta_mission_1 == 0:
					fenetre.blit(missions_1_1, (1150, 770))
				elif eta_mission_1 == 1:
					fenetre.blit(missions_1_2, (930, 770))

			if mission_en_cours == 2:
				fenetre.blit(missions_2_1, (1150, 770))
				fenetre.blit(pistol, (2930-(map_x-1500//2), 1515-(map_y-825//2)-35))

				if map_x in range(2930, 2990) and map_y in range(1515, 1555) and locomotion == 1:
					display_msg = 1
					armed[0] = 1


	#affichage de la fin de mission
	if display_msg == 1:

		if mission_en_cours == 1: fenetre.blit(mission_1_finished, (0, 0))
		elif mission_en_cours == 2: fenetre.blit(mission_2_finished, (0, 0))

		for event in pygame.event.get():
			if event.type == KEYDOWN and event.key == K_RETURN:

				if mission_en_cours == 1:
					#on le sort de la voiture
					test_cars = test_in_cars(map_x, map_y, locomotion, direction, voiture_courante)
					locomotion = test_cars[0]
					speed = test_cars[1]
				
				#on passe a la mision suivant (ici 2)
				mission_en_cours += 1

				#reinit de la variable
				display_msg = 0

				#actualisation de la map
				generation_map(map_x, map_y)

				#spawn des voitures
				spawn_cars(map_x, map_y)

				afficher_perso(direction, locomotion, position, voiture_courante)

	pygame.display.update()
	fps_max.tick(30)

pygame.quit()
