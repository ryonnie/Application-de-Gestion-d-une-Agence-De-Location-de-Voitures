Voiture ={}
while (True):
    print("\n")
    print("*****Beinvenue dans l'Agence de Location de Voitures*****")
    print("\n")
    i=1
    while (i<=6):
        print(i,"-Afficher les voitures Disponibles")
        i+=1
        print(i,"-Ajouter une nouvelle voiture")
        i+=1
        print(i,"-Louer une voiture ")
        i+=1
        print(i,"-Retourner une voiture")
        i+=1
        print(i,"-Supprimer une voiture ")
        i+=1
        print(i,"-Quitter")
        i+=1
        break

    choix=input("saisir votre choix :")

    if (choix=="1"):
        print(Voiture)
        print("\n")
    elif (choix=="2"):
        id_v=input("Entrer le id de la voiture :")
        marque=input("Entrer la marque de la voiture :")
        modele=input("Entrer le modele de Voiture :")
        annee=input("Entrer Annee :")
        status=input("Disponible ou louee :")

        Voiture[id_v] = {
        "Marque": marque,
        "Modele": modele,
        "Annee": annee,
        "Status_DL":status
        }
        print("\n")
        print("=>La voiture a ete ajouter avec success!\n")
    elif (choix=="3"):
        k = input("Entrer l'ID de la voiture à louer : ")

        if k in Voiture:  
            if Voiture[k]["Status_DL"] == "disponible":
                Voiture[k]["Status_DL"] = "louee"
                print("\n")
                print("=> La voiture a été louée avec succès!\n")
            else:
                print("\n")
                print("=> Cette voiture est déjà louée.\n")
        else:
            print("\n")
            print("=> ID de voiture invalide.\n")

    elif (choix=="4"):

        k = input("Entrer l'ID de la voiture à louer : ")

        if k in Voiture:  
            if Voiture[k]["Status_DL"] == "louee":
                Voiture[k]["Status_DL"] = "disponible"
                print("\n")
                print("=> La voiture a retourneé dans le garage!\n")
            else:
                print("\n")
                print("=>La voiture est deja disponible!\n")
        else:
            print("\n")
            print("=>ID de voiture invalide!\n")

    elif (choix=="5"):
        k= input("Enter the ID of the car to delete: ")

        if k in Voiture:  
            del Voiture[k]
            print("\n")  
            print("=> The car has been deleted successfully!")
        else:
            print("\n")
            print("=> Invalid car ID")

    elif (choix=="6"):
        f=open("hola.txt","w")
        f.write(str(Voiture))
        f.close()
        print("=>Programme Terminer!")
        break
    





