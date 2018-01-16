from globales import *

def load():
	save_txt = open('save', 'r') #lecture du fichier sauvegarder
	save_str = save_txt.read()

	#initilisation
	data = []
	current_str = ""
	current_position = 0


	#parcours la longueur du fichier sauvegarder
	for i in range(len(save_str)):

		#si different de espace alors continue de selectionner les chiffes
		if save_str[i] != " ":
			current_str += save_str[i]

		#sinon, valide en mettant ds le tableau
		else :
			data.append(int(current_str))
			i += 1
			current_str = ""

	

	save_txt.close()

	
	return data