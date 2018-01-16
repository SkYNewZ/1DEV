# coding=utf-8
import pygame, sys
from pygame.locals import *
from matrice import *
from globales import *
pygame.init()

def generation_map(posX, posY):

	coord_x = 0
	coord_y = 0


	#effacer map
	pygame.draw.rect(fenetre, (0,0,0), (0,0,1500,825))


	for i in range(0, dim_map*11, 1): #lignes
		for j in range(0, dim_map*20, 1): #colonnes


			#Sol

			#afficher une route 
			if matrice[i][j] == 1:
				fenetre.blit(routenormal, (coord_x-posX, coord_y - posY))

			#affiche une route (bordure en bas)
			elif matrice[i][j] == 2:
				fenetre.blit(routebas, (coord_x-posX, coord_y - posY))

			#affiche une route (bordure en haut)
			elif matrice[i][j] == 3:
				fenetre.blit(routehaut, (coord_x-posX, coord_y - posY))

			#affiche trottoir
			elif matrice[i][j] == 4:
				fenetre.blit(sol, (coord_x-posX, coord_y - posY))

			#affiche une route (bordure a gauche )
			elif matrice[i][j] == 5:
				fenetre.blit(routegauche, (coord_x-posX, coord_y - posY))

			#affiche une route (bordure a droite )
			elif matrice[i][j] == 6:
				fenetre.blit(routedroite, (coord_x-posX, coord_y - posY))

			#affiche un passage pieton vers le haut
			elif matrice[i][j] == 7:
				fenetre.blit(passage, (coord_x-posX, coord_y - posY))

			#affiche un passage pieton horizontal
			elif matrice[i][j] == 56:
				fenetre.blit(passage2, (coord_x-posX, coord_y - posY))

			#affiche trottoire avec un arbre dessu
			elif matrice[i][j] == 51:
				fenetre.blit(trottoirarbre, (coord_x-posX, coord_y - posY))

			#affiche un sapin avec un fond d'herbe
			elif matrice[i][j] == 66:
				fenetre.blit(sapin, (coord_x-posX, coord_y - posY))

			#affiche terre
			elif matrice[i][j] == 67:
				fenetre.blit(terre, (coord_x-posX, coord_y - posY))

			#affiche bois
			elif matrice[i][j] == 68:
				fenetre.blit(bois, (coord_x-posX, coord_y - posY))

			#foret
			elif matrice[i][j] == 90:
					fenetre.blit(foret, (coord_x-posX, coord_y - posY))


			#barrière

			#affiche barriere fond trottoir 
			elif matrice[i][j] == 52:
				fenetre.blit(barrieretrottoir, (coord_x-posX, coord_y - posY))

			#affiche barriere fond sable
			elif matrice[i][j] == 8:
				fenetre.blit(barrieregris, (coord_x-posX, coord_y - posY))

			#affiche barriere
			elif matrice[i][j] == 13:
				fenetre.blit(barriere, (coord_x-posX, coord_y - posY))					

			#affiche barriere fond de sable
			elif matrice[i][j] == 14:
				fenetre.blit(barrieresable, (coord_x-posX, coord_y - posY))	

			#affiche barriere croisement
			elif matrice[i][j] == 15:
				fenetre.blit(barrieres, (coord_x-posX, coord_y - posY))	

			#affiche barriere fond d'herbe vers le haut
			elif matrice[i][j] == 16:
				fenetre.blit(barriereherbe, (coord_x-posX, coord_y - posY))	

			#affiche barriere fond route droite
			elif matrice[i][j] == 55:
				fenetre.blit(barriereroutedroite, (coord_x-posX, coord_y - posY))	

			#affiche barriere fond route gauche
			elif matrice[i][j] == 53:
				fenetre.blit(barriereroutegauche, (coord_x-posX, coord_y - posY))	

			#affiche barriere fond route normal
			elif matrice[i][j] == 54:
				fenetre.blit(barriereroutenormal, (coord_x-posX, coord_y - posY))	


			#nature

			#affiche Ciel
			elif matrice[i][j] == 9:
				fenetre.blit(ciel, (coord_x-posX, coord_y - posY))	

			#affiche eau
			elif matrice[i][j] == 10:
				fenetre.blit(eau, (coord_x-posX, coord_y - posY))

			#affiche herbe
			elif matrice[i][j] == 11:
				fenetre.blit(herbe, (coord_x-posX, coord_y - posY))

			#affiche sable
			elif matrice[i][j] == 12:
				fenetre.blit(sable, (coord_x-posX, coord_y - posY))	



			#Immeuble/batiment

			#affiche immeuble
			elif matrice[i][j] == 17:
				fenetre.blit(Building1, (coord_x-posX, coord_y - posY))	

			#affiche immeuble
			elif matrice[i][j] == 18:
				fenetre.blit(Building2, (coord_x-posX, coord_y - posY))	

			#affiche immeuble
			elif matrice[i][j] == 19:
				fenetre.blit(Building3, (coord_x-posX, coord_y - posY))	

			#affiche immeuble
			elif matrice[i][j] == 20:
				fenetre.blit(Building4, (coord_x-posX, coord_y - posY))	

			#affiche immeuble
			elif matrice[i][j] == 21:
				fenetre.blit(Building5, (coord_x-posX, coord_y - posY))	

			#affiche immeuble
			elif matrice[i][j] == 22:
				fenetre.blit(Building6, (coord_x-posX, coord_y - posY))					

			#affiche immeuble
			elif matrice[i][j] == 23:
				fenetre.blit(Building7, (coord_x-posX, coord_y - posY))	

			#affiche immeuble
			elif matrice[i][j] == 24:
				fenetre.blit(Building8, (coord_x-posX, coord_y - posY))	

			#affiche immeuble
			elif matrice[i][j] == 25:
				fenetre.blit(Building11, (coord_x-posX, coord_y - posY))	

			#affiche immeuble
			elif matrice[i][j] == 26:
				fenetre.blit(Building12, (coord_x-posX, coord_y - posY))	

			#affiche immeuble
			elif matrice[i][j] == 27:
				fenetre.blit(Building13, (coord_x-posX, coord_y - posY))	

			#affiche immeuble
			elif matrice[i][j] == 28:
				fenetre.blit(Building14, (coord_x-posX, coord_y - posY))	

			#affiche immeuble
			elif matrice[i][j] == 29:
				fenetre.blit(Building15, (coord_x-posX, coord_y - posY))	

			#affiche immeuble
			elif matrice[i][j] == 30:
				fenetre.blit(Building16, (coord_x-posX, coord_y - posY))	

			#affiche immeuble
			elif matrice[i][j] == 31:
				fenetre.blit(Building17, (coord_x-posX, coord_y - posY))	

			#affiche immeuble
			elif matrice[i][j] == 32:
				fenetre.blit(Building18, (coord_x-posX, coord_y - posY))	

			#affiche immeuble
			elif matrice[i][j] == 33:
				fenetre.blit(Building19, (coord_x-posX, coord_y - posY))	

			#affiche immeuble
			elif matrice[i][j] == 34:
				fenetre.blit(Building20, (coord_x-posX, coord_y - posY))

			#affiche parking
			elif matrice[i][j] == 35:
				fenetre.blit(parking1, (coord_x-posX, coord_y - posY))

			#affiche parking
			elif matrice[i][j] == 36:
				fenetre.blit(parking2, (coord_x-posX, coord_y - posY))

			#affiche parking
			elif matrice[i][j] == 37:
				fenetre.blit(parking3, (coord_x-posX, coord_y - posY))

			#affiche parking
			elif matrice[i][j] == 38:
				fenetre.blit(parking4, (coord_x-posX, coord_y - posY))

			#affiche grosse maison
			elif matrice[i][j] == 39:
				fenetre.blit(maison1, (coord_x-posX, coord_y - posY))

			#affiche grosse maison
			elif matrice[i][j] == 40:
				fenetre.blit(maison2, (coord_x-posX, coord_y - posY))

			#affiche grosse maison
			elif matrice[i][j] == 41:
				fenetre.blit(maison3, (coord_x-posX, coord_y - posY))

			#affiche grosse maison
			elif matrice[i][j] == 42:
				fenetre.blit(maison4, (coord_x-posX, coord_y - posY))

			#affiche grosse maison
			elif matrice[i][j] == 43:
				fenetre.blit(maison5, (coord_x-posX, coord_y - posY))

			#affiche grosse maison
			elif matrice[i][j] == 44:
				fenetre.blit(maison6, (coord_x-posX, coord_y - posY))

			#affiche grosse maison
			elif matrice[i][j] == 45:
				fenetre.blit(maison7, (coord_x-posX, coord_y - posY))

			#affiche grosse maison
			elif matrice[i][j] == 46:
				fenetre.blit(maison8, (coord_x-posX, coord_y - posY))

			elif matrice[i][j] == 47:
				fenetre.blit(maison9, (coord_x-posX, coord_y - posY))

			#affiche grosse maison
			elif matrice[i][j] == 48:
				fenetre.blit(maison10, (coord_x-posX, coord_y - posY))

			#affiche grosse maison
			elif matrice[i][j] == 49:
				fenetre.blit(maison11, (coord_x-posX, coord_y - posY))

			#affiche grosse maison
			elif matrice[i][j] == 50:
				fenetre.blit(maison12, (coord_x-posX, coord_y - posY))

			#affiche petite maison
			elif matrice[i][j] == 57:
				fenetre.blit(maison13, (coord_x-posX, coord_y - posY))

			#affiche petite maison
			elif matrice[i][j] == 58:
				fenetre.blit(maison14, (coord_x-posX, coord_y - posY))

			#affiche petite maison
			elif matrice[i][j] == 59:
				fenetre.blit(maison15, (coord_x-posX, coord_y - posY))

			#affiche petite maison
			elif matrice[i][j] == 60:
				fenetre.blit(maison16, (coord_x-posX, coord_y - posY))

			#affiche petite maison
			elif matrice[i][j] == 61:
				fenetre.blit(maison17, (coord_x-posX, coord_y - posY))

			#affiche petite maison
			elif matrice[i][j] == 62:
				fenetre.blit(maison18, (coord_x-posX, coord_y - posY))

			#affiche petite maison
			elif matrice[i][j] == 63:
				fenetre.blit(maison19, (coord_x-posX, coord_y - posY))

			#affiche petite maison
			elif matrice[i][j] == 64:
				fenetre.blit(maison20, (coord_x-posX, coord_y - posY))

			#affiche petite maison
			elif matrice[i][j] == 65:
				fenetre.blit(maison21, (coord_x-posX, coord_y - posY))


			#affiche POSTE police
			elif matrice[i][j] == 70:
				fenetre.blit(police1, (coord_x-posX, coord_y - posY))

			#affiche POSTE police
			elif matrice[i][j] == 71:
				fenetre.blit(police2, (coord_x-posX, coord_y - posY))

			#affiche POSTE police
			elif matrice[i][j] == 72:
				fenetre.blit(police3, (coord_x-posX, coord_y - posY))

			#affiche POSTE police
			elif matrice[i][j] == 73:
				fenetre.blit(police4, (coord_x-posX, coord_y - posY))

			#affiche POSTE police
			elif matrice[i][j] == 74:
				fenetre.blit(police5, (coord_x-posX, coord_y - posY))

			#affiche POSTE police
			elif matrice[i][j] == 75:
				fenetre.blit(police6, (coord_x-posX, coord_y - posY))

			#affiche POSTE police
			elif matrice[i][j] == 76:
				fenetre.blit(police7, (coord_x-posX, coord_y - posY))

			#affiche POSTE police
			elif matrice[i][j] == 77:
				fenetre.blit(police8, (coord_x-posX, coord_y - posY))

			#affiche POSTE police
			elif matrice[i][j] == 78:
				fenetre.blit(police9, (coord_x-posX, coord_y - posY))

			#affiche POSTE police
			elif matrice[i][j] == 79:
				fenetre.blit(police10, (coord_x-posX, coord_y - posY))

			#affiche POSTE police
			elif matrice[i][j] == 80:
				fenetre.blit(police11, (coord_x-posX, coord_y - posY))

			#affiche POSTE police
			elif matrice[i][j] == 81:
				fenetre.blit(police12, (coord_x-posX, coord_y - posY))

			#affiche hopital
			elif matrice[i][j] == 82:
				fenetre.blit(hopital1, (coord_x-posX, coord_y - posY))

			#affiche hopital
			elif matrice[i][j] == 83:
				fenetre.blit(hopital2, (coord_x-posX, coord_y - posY))

			#affiche hopital
			elif matrice[i][j] == 84:
				fenetre.blit(hopital3, (coord_x-posX, coord_y - posY))

			#affiche hopital
			elif matrice[i][j] == 85:
				fenetre.blit(hopital4, (coord_x-posX, coord_y - posY))

			#affiche hopital
			elif matrice[i][j] == 86:
				fenetre.blit(hopital5, (coord_x-posX, coord_y - posY))

			#affiche hopital
			elif matrice[i][j] == 87:
				fenetre.blit(hopital6, (coord_x-posX, coord_y - posY))



			#sinon affiche rien
			else :
				fenetre.blit(tile_0, (coord_x-posX, coord_y - posY))


			#retour chariot
			coord_x += 75
			if coord_x == dim_map*1500:
				coord_x = 0
				coord_y += 75
			
			#66