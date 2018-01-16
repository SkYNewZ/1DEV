# coding=utf-8
from globales import *


def first_spawn_npcs(x, y):
	for i in range(len(npc_x)):
		fenetre.blit(npc_1, (npc_x[i]-(x-1500//2), npc_y[i]-(y-825//2)))