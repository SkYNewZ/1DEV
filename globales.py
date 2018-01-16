# coding=utf-8
import pygame, sys, os
from pygame.locals import *
from random import *
pygame.init()

#effacer console
def cls():
   	os.system('cls' if os.name=='nt' else 'clear')

def read_npc():
	
	str_x = ''
	str_y = ''
	str_v = ''
	str_h = ''

	x_txt = open('npc_x_txt', 'r')
	x = x_txt.read()

	y_txt = open('npc_y_txt', 'r')
	y = y_txt.read()

	v_txt = open('npc_v', 'r')
	v = v_txt.read()

	h_txt = open('npc_h', 'r')
	h = h_txt.read()

	for i in range(len(x)):
		if x[i] != ' ':
			str_x += x[i]
		else:
			npc_x.append(int(str_x))
			str_x = ''
			i += 1

	for i in range(len(y)):
		if y[i] != ' ':
			str_y += y[i]
		else:
			npc_y.append(int(str_y))
			str_y = ''
			i += 1

	for i in range(len(v)):
		if v[i] != ' ':
			str_v += v[i]
		else:
			npc_v.append(int(str_v))
			str_v = ''
			i += 1

	for i in range(len(h)):
		if h[i] != ' ':
			str_h += h[i]
		else:
			npc_h.append(int(str_h))
			str_h = ''
			i += 1

	x_txt.close()
	y_txt.close()
	v_txt.close()
	h_txt.close()

#fenetre
fenetre = pygame.display.set_mode((1500, 825))
pygame.display.set_caption('GTA_v1.0.4')


#initialisation
debug = 0 #affichage des infos
title = 0
locomotion = 1 #voiture = 2, pieton = 1
speed = 5 #vitesse pieton
speed_max = 30 #vitesse en voiture
speed_npc = 4 #vitesse npc pieton
speed_npc_car = 10 #vitesse npc voiture
dim_map = 5
inProgress = True
touche_echap = 0
menu_principal = True
pos_x = 0
pos_y = 0
position = 1
modele_voiture = 0
index_x = 0
index_y = 0
direction = 2
max_voitures = 5 #nombres de voitures maxi
nb_cars_choisi = randint(15,32) #combien de voitures vont spawner

#déclaration et création de la matrice
matrice = [[0] * dim_map*20 for i in range(dim_map*11)]

#gestion du "rester appuyer sur une touche"
pygame.key.set_repeat(150,1)

#blocs impassables
block = [10, 14, 15, 16, 23, 24, 33, 34, 13, 8, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87]


#referencement de chaque voiture
tab_voitures = [[0]*4 for i in range(max_voitures)]
for i in range(max_voitures):
	for j in range(4):
		if j == 0:
			orientation = "up"
		if j == 1:
			orientation = "down"
		if j == 2:
			orientation = "left"
		if j == 3:
			orientation = "right"


		tab_voitures[i][j] = pygame.image.load("cars/car_" + str(i) + "_" + orientation + ".png").convert_alpha()


#spawn aleatoire des voitures
liste_x_min = [175, 335, 550, 860, 1075, 1240, 1380, 1615, 1750, 1900, 2140, 2285, 2435, 2660, 2810, 2965, 3190, 3335, 3490, 3715, 3865, 4010, 4240, 4385, 4535, 4765, 4910, 5060, 5290, 5430, 5595, 5740]
parking_y_min = 2745
parking_y_max = 2900

places_choisies = []
modele_voiture = []
orientation_voiture = []
voiture = []
parking_empty = []

#modele de voiture qu'on est en train de conduire
voiture_courante = 9 #initialiser a 9 car correpond a aucun modele

#liste voitures deposées
tab_voitures_deposees = [3]
x_deposee = [5310]
y_deposee = [755]
direction_deposee = [3]


#etats missions
eta_mission_1 = 0
eta_mission_2 = 0
mission_en_cours = 1

#sons
bruit_ambiant = pygame.mixer.Sound("son/bruit_ambiant.wav")
bruit_car = pygame.mixer.Sound("son/bruit_car.wav")
bruit_pieton = pygame.mixer.Sound("son/bruit_pieton_pas.wav")
enter_car = pygame.mixer.Sound("son/enter_car.wav")
leave_car = pygame.mixer.Sound("son/leave_car.wav")
music_menu = pygame.mixer.Sound("son/menu.wav")


#perso
armed = [0]
anim = 0
tab_perso = [[0]*24 for i in range(2)]
for i in range(2):
	for k in range(24):
		# if k < 6: orientation = 0 #bas
		# if k == 6 and k < 12: orientation = 1 #haut
		# if k == 12 and k < 18: orientation = 2 #droite
		# if k >= 18: orientation = 3 #gauche

		if i == 0: 
			tab_perso[i][k] = pygame.image.load("perso/perso_" + str(k//6) + "_" + str(anim) + ".png").convert_alpha()
			anim += 1
			if anim == 6: anim = 0
		if i == 1: 
			tab_perso[i][k] = pygame.image.load("perso_arme/perso_" + str(k//6) + "_" + str(anim) + ".png").convert_alpha()
			anim += 1
			if anim == 6: anim = 0

#arme
arme_x = [2278, 5435, 5945, 25, 5920]
arme_y = [3145, 1740, 85, 80, 3155]
pistol = pygame.image.load('perso_arme/pistol.png')


#npcs
tab_npcs = [[0]*4 for i in range(4)]
for i in range(4):
	for k in range(4):
		if i == 0:
			orientation = 'haut'
		if i == 1:
			orientation = 'bas'
		if i == 2:
			orientation = 'gauche'
		if i == 3:
			orientation = 'droite'

		tab_npcs[i][k] = pygame.image.load("perso/pnj_" + str(orientation)+ str(k) + ".png").convert_alpha()

npc_x = []
npc_y = []
npc_h = []
npc_v = []

#remplissage des coordones
read_npc()
sens_npc = [0]*len(npc_x)

if debug:
	print(len(npc_y))
	print(len(npc_x))


car_npc_x = [5700, 4425, 220, 5635, 5700, 3300, 3600, 270, 510]
car_npc_y = [310, 345, 330, 965, 2005, 2065, 2665, 2695, 2095]
car_sens_npc = [0]*len(car_npc_x)
car_type = [0, 1, 2, 3, 2, 4, 1, 1, 3]


npc_up = [0]
npc_down = [0]
npc_left = [0]
npc_right = [0]


#menu pause
menu = pygame.image.load('menu.png') #Menu
menu_saved = pygame.image.load('menu_saved.png') #Menu_saved

#menu d'acceuil
menu_titre = pygame.image.load('title.png') #menu titre
titre_new_game = pygame.image.load('titre_new_game.png') #menu titre_new_game
titre_continue = pygame.image.load('titre_continue.png') #menu titre_continue
titre_exit = pygame.image.load('titre_exit.png') #menu titre_exit

#missions
missions_1_1 = pygame.image.load('missions/1_1.png').convert_alpha()
missions_1_2 = pygame.image.load('missions/1_2.png').convert_alpha()
missions_1_3 = pygame.image.load('missions/1_3.png').convert_alpha()
zone_mission_1 = pygame.image.load('missions/zone_finished.png').convert_alpha()
mission_1_finished = pygame.image.load('missions/ecran_finish_mission_1.png').convert_alpha()

missions_2_1 = pygame.image.load('missions/2_1.png').convert_alpha()
mission_2_finished = pygame.image.load('missions/ecran_finish_mission_2.png').convert_alpha()



#tiles
tile_0 = pygame.image.load('tiles/0.png').convert_alpha() #Par défaut, noir
routenormal = pygame.image.load('tiles/routenormal.png').convert_alpha() #route
routebas = pygame.image.load('tiles/routebas.png').convert_alpha() #route avec bordure en bas
routehaut = pygame.image.load('tiles/routehaut.png').convert_alpha() #route avec bordure en haut
routedroite = pygame.image.load('tiles/routedroite.png').convert_alpha() #route avec bordure a droite
routegauche = pygame.image.load('tiles/routegauche.png').convert_alpha() #route avec bordure a gauche
passage = pygame.image.load('tiles/passagepieton.png').convert_alpha() #passage piéton vers le haut
passage2 = pygame.image.load('tiles/passage2.png').convert_alpha()#passage pieton horizontal
trottoirarbre = pygame.image.load('tiles/trottoirearbre.png').convert_alpha()#trottoir avec un arbre
sapin = pygame.image.load('tiles/sapin.png').convert_alpha()#affiche un sapin fond herbe

eau = pygame.image.load('tiles/eau.png').convert_alpha() #eau
herbe = pygame.image.load('tiles/herbe.png').convert_alpha() #herbe
sable = pygame.image.load('tiles/sable.png').convert_alpha()#Sable
ciel= pygame.image.load('tiles/Ciel.png').convert_alpha()#Ciel
sol= pygame.image.load('tiles/trottoire.png').convert_alpha()#route
terre = pygame.image.load('tiles/pave.png').convert_alpha()#terre
bois = pygame.image.load('tiles/bois.png').convert_alpha()#bois
foret = pygame.image.load('tiles/foret.png').convert_alpha()#affiche une foret


barriere = pygame.image.load('tiles/barriere.png').convert_alpha()#barriere
barrieresable = pygame.image.load('tiles/barrieresable.png').convert_alpha()#barriere avec fond sable
barrieres = pygame.image.load('tiles/barrieres.png').convert_alpha()#double barriere
barriereherbe = pygame.image.load('tiles/barriereherbe.png').convert_alpha()#barriere avec fond herbe
barrieregris = pygame.image.load('tiles/barrieregris.png').convert_alpha()#barriere fond sol
barrieretrottoir = pygame.image.load('tiles/barrieretrottoir.png')#barriere fond sol
barriereroutedroite = pygame.image.load('tiles/barriereroutedroite.png').convert_alpha()#barriere fond route droite
barriereroutegauche = pygame.image.load('tiles/barriereroutegauche.png').convert_alpha()#barriere fond route gauche
barriereroutenormal = pygame.image.load('tiles/barriereroutenormal.png').convert_alpha()#barriere fond route normal


Building1 = pygame.image.load('tiles/Building1.1.png').convert_alpha() #immeuble
Building2 = pygame.image.load('tiles/Building1.2.png').convert_alpha() #immeuble
Building3 = pygame.image.load('tiles/Building1.3.png').convert_alpha() #immeuble
Building4 = pygame.image.load('tiles/Building1.4.png').convert_alpha() #immeuble
Building5 = pygame.image.load('tiles/Building1.5.png').convert_alpha() #immeuble
Building6 = pygame.image.load('tiles/Building1.6.png').convert_alpha() #immeuble
Building7 = pygame.image.load('tiles/Building1.7.png').convert_alpha() #immeuble
Building8 = pygame.image.load('tiles/Building1.8.png').convert_alpha() #immeuble

Building11 = pygame.image.load('tiles/Building3.png').convert_alpha() #immeuble
Building12 = pygame.image.load('tiles/Building4.png').convert_alpha() #immeuble
Building13 = pygame.image.load('tiles/Building5.png').convert_alpha() #immeuble
Building14 = pygame.image.load('tiles/Building6.png').convert_alpha() #immeuble
Building15 = pygame.image.load('tiles/Building7.png').convert_alpha() #immeuble
Building16 = pygame.image.load('tiles/Building8.png').convert_alpha() #immeuble
Building17 = pygame.image.load('tiles/Building9.png').convert_alpha() #immeuble
Building18 = pygame.image.load('tiles/Building10.png').convert_alpha() #immeuble
Building19 = pygame.image.load('tiles/Building11.png').convert_alpha() #immeuble
Building20 = pygame.image.load('tiles/Building12.png').convert_alpha() #immeuble

parking1 = pygame.image.load('tiles/parking1.png').convert_alpha() #parking
parking2 = pygame.image.load('tiles/parking2.png').convert_alpha() #parking
parking3 = pygame.image.load('tiles/parking3.png').convert_alpha() #parking
parking4 = pygame.image.load('tiles/parking4.png').convert_alpha() #parking

maison1 = pygame.image.load('tiles/maison1.png').convert_alpha() #grosse maison
maison2 = pygame.image.load('tiles/maison2.png').convert_alpha() #grosse maison
maison3 = pygame.image.load('tiles/maison3.png').convert_alpha() #grosse maison
maison4 = pygame.image.load('tiles/maison4.png').convert_alpha() #grosse maison
maison5 = pygame.image.load('tiles/maison5.png').convert_alpha() #grosse maison
maison6 = pygame.image.load('tiles/maison6.png').convert_alpha() #grosse maison
maison7 = pygame.image.load('tiles/maison7.png').convert_alpha() #grosse maison
maison8 = pygame.image.load('tiles/maison8.png').convert_alpha() #grosse maison
maison9 = pygame.image.load('tiles/maison9.png').convert_alpha() #grosse maison
maison10 = pygame.image.load('tiles/maison10.png').convert_alpha() #grosse maison
maison11 = pygame.image.load('tiles/maison11.png').convert_alpha() #grosse maison
maison12 = pygame.image.load('tiles/maison12.png').convert_alpha() #grosse maison

maison13 = pygame.image.load('tiles/maison1.1.png').convert_alpha() #petite maison
maison14 = pygame.image.load('tiles/maison1.2.png').convert_alpha() #petite maison
maison15 = pygame.image.load('tiles/maison1.3.png').convert_alpha() #petite maison
maison16 = pygame.image.load('tiles/maison1.4.png').convert_alpha() #petite maison
maison17 = pygame.image.load('tiles/maison1.5.png').convert_alpha() #petite maison
maison18 = pygame.image.load('tiles/maison1.6.png').convert_alpha() #petite maison
maison19 = pygame.image.load('tiles/maison1.7.png').convert_alpha() #petite maison
maison20 = pygame.image.load('tiles/maison1.8.png').convert_alpha() #petite maison
maison21 = pygame.image.load('tiles/maison1.9.png').convert_alpha() #petite maison

police1 = pygame.image.load('tiles/police1.png').convert_alpha() #grosse police
police2 = pygame.image.load('tiles/police2.png').convert_alpha() #grosse police
police3 = pygame.image.load('tiles/police3.png').convert_alpha() #grosse police
police4 = pygame.image.load('tiles/police4.png').convert_alpha() #grosse police
police5 = pygame.image.load('tiles/police5.png').convert_alpha() #grosse police
police6 = pygame.image.load('tiles/police6.png').convert_alpha() #grosse police
police7 = pygame.image.load('tiles/police7.png').convert_alpha() #grosse police
police8 = pygame.image.load('tiles/police8.png').convert_alpha() #grosse police
police9 = pygame.image.load('tiles/police9.png').convert_alpha() #grosse police
police10 = pygame.image.load('tiles/police10.png').convert_alpha() #grosse police
police11 = pygame.image.load('tiles/police11.png').convert_alpha() #grosse police
police12 = pygame.image.load('tiles/police12.png').convert_alpha() #grosse police


hopital1 = pygame.image.load('tiles/hopital1.png').convert_alpha() #grosse hopital
hopital2 = pygame.image.load('tiles/hopital2.png').convert_alpha() #grosse hopital
hopital3 = pygame.image.load('tiles/hopital3.png').convert_alpha() #grosse hopital
hopital4 = pygame.image.load('tiles/hopital4.png').convert_alpha() #grosse hopital
hopital5 = pygame.image.load('tiles/hopital5.png').convert_alpha() #grosse hopital
hopital6 = pygame.image.load('tiles/hopital6.png').convert_alpha() #grosse hopital