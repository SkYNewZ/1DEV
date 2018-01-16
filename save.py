from globales import *

def save(tab_save):
	fichier = open("save", "w") #ouverture
	for i in range(0, len(tab_save), 1):
		fichier.write(str(tab_save[i]) + " ") #ecrire tout ce qui se trouve + espace
	fichier.close() #fermeture
	
	fichier = open("save_x_deposee", "w")
	for i in range(len(x_deposee)):
		fichier.write(str(x_deposee[i]) + " ")
	fichier.close()

	fichier = open("save_y_deposee", "w")
	for i in range(len(y_deposee)):
		fichier.write(str(y_deposee[i]) + " ")
	fichier.close()

	fichier = open("save_direction_deposee", "w")
	for i in range(len(direction_deposee)):
		fichier.write(str(direction_deposee[i]) + " ")
	fichier.close()

	fichier = open("save_tab_voitures_deposees", "w")
	for i in range(len(tab_voitures_deposees)):
		fichier.write(str(tab_voitures_deposees[i]) + " ")
	fichier.close()