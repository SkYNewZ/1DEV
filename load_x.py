from globales import *

def load_x():
	save_txt = open('save_x_deposee', 'r') #lecture du fichier sauvegarder
	save_str = save_txt.read()

	#initilisation
	data_x = []
	current_str = ""
	x_deposee = []


	#parcours la longueur du fichier sauvegarder
	for i in range(len(save_str)):

		#si different de espace alors continue de selectionner les chiffes
		if save_str[i] != " ":
			current_str += save_str[i]

		#sinon, valide en mettant ds le tableau
		else :
			x_deposee.append(int(current_str))
			i += 1
			current_str = ""	

	save_txt.close()