# coding=utf-8
from globales import *

def generer_matrice():
	map_txt = open('map', 'r') #lecture du fichier
	map_str = map_txt.read()

	str_courante = ""
	tile_courante = 0


	#remplissage de la matrice
	for i in range(0, dim_map*11, 1): #lignes
		for j in range(0, dim_map*20, 1): #colonnes


			#saisie de la valeur jusq'a l'espace
			while map_str[tile_courante] != " " and tile_courante < len(map_str)-1:
				str_courante += map_str[tile_courante]
				tile_courante += 1


			#remplissage de la matrice
			if tile_courante < len(map_str)-1 :
				matrice[i][j] = int(str_courante)
				str_courante = ""
				tile_courante += 1

	map_txt.close()

	
	return matrice


#reçoit la matrice de la map
matrice = generer_matrice()