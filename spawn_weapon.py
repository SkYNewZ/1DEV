# coding=utf-8
from globales import *

def spawn_weapon(x, y):
	for i in range(len(arme_x)):
		fenetre.blit(pistol, (arme_x[i]-(x-1500//2), arme_y[i]-(y-825//2)-35))