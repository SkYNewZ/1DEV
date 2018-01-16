# coding=utf-8
from globales import *


def deposer_voiture(x, y, voiture_courante, direction):

	#referencement dees positons et du type de voiture, et direction
	tab_voitures_deposees.append(voiture_courante)
	x_deposee.append(x)
	y_deposee.append(y)
	direction_deposee.append(direction-1)
	#reinit de la voiture courante, plus utilisée
	voiture_courante = 9