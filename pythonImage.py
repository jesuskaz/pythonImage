from  PIL import Image
def set_image1(image):
	i = 0
	nouveau_tabl = []
	counting = len(image) - 1
	for ima in range(counting):
		while(i <= counting):
			stock_ima = image[i]
			print("stock_ima\n",stock_ima)
			try :
				im = Image.open("%s.JPG" % (stock_ima))
				#Charge l'image dans le fichier
				sauve = (im.format,im.size,im.mode) 
				#donne les informations de du fichier charge
				sauve = list(sauve)
				#convertit le fichier charge en liste
				for j in range(len(sauve)):
					#parcours les informations de la liste 
					if(j == 1):
						#convertir le tuple en liste de l'element situe a l'indice 1.le pixel
						conver = list(sauve[j])
						counting_conver = len(conver) - 1
						#remet le nouveau tableau a dans l'ancien tableau a l'indice 1
						sauve[1] = conver
						print(sauve)
						l = 0
						while(l<counting_conver):
							for calc in range(counting_conver+1):
								if(calc == l):
									pass #on passe si la condition verifie
								elif(calc != l):
									conver[l]*=conver[calc]
									print(conver)	
								else:
									break
							l+=1
				#ajout du produit de pixel au nouveau tableau : nouveau_tabl
				nouveau_tabl.append(conver[0])
			except FileNotFoundError:
				#affiche le message lorsqu'on trouve l'erreur du type FileNotFoundError
				print("You image is not exist,so sorry")
			i+=1
    #retourne tous les elements du tableau
	return nouveau_tabl
def get_image(image):
	superieur = 0
	k = 0
	call_set = set_image1(image)
	print(call_set)
	count = len(call_set) - 1
	for i in range(count):
		sup = call_set[i]
		imag = image[i]
		for j in range(count):
			if(sup > call_set[j]):
				#permutation de la capacite
				call_set[i] = call_set[j]
				#permutation de l'image
				image[i] = image[j]
				call_set[j] = sup
				image[j] = imag
				sup = call_set[i]
				imag = image[i] 
	#affichage du tableau image et du tableau call_set pour les capacites
	print(image,"\n",call_set)
	while(k < 1):
		print("The best picture : ",image[k]," ",call_set[k]," pixel")
		img = image[k]
		imag = Image.open("%s.JPG" % img)
		imag.show()
		k+=1

def called(image):
	called1 = get_image(image)
	print(called1)
called(['picture1','picture2','picture3','picture4','picture5']) 