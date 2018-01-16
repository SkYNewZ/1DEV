# coding=utf-8
from globales import *

def take_weapon(x, y):
	for i in range(len(arme_x) - 1, -1, -1):
		if x in range(arme_x[i], arme_x[i]+60) and y in range(arme_y[i], arme_y[i]+45):
			#alors tu prends l'arme
			armed[0] = 1
			arme_x.remove(arme_x[i])
			arme_y.remove(arme_y[i])