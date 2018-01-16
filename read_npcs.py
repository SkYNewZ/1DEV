# coding=utf-8
from globales import *

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