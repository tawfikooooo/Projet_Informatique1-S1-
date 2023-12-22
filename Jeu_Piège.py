from fltk import *
import random 

taille_carre = 40
taille_plateau = 7

def créer_matrice(n, Val):
    L = []
    for i in range(n):
        L.append(Val* n)
    return L

def dessine_cercle(x, y, rayon, remplissage, epaisseur):
    cercle(x, y, rayon, remplissage=remplissage, epaisseur= epaisseur)

def dessine_plateau(plateau, cercles, taille_fenetre, Tirette_verticale, Tirette_horizontale):
    global taille_carre

    nb_lignes = len(plateau)
    nb_colonnes = len(plateau)

    depart_x = (taille_fenetre - nb_colonnes * taille_carre) // 2
    depart_y = (taille_fenetre - nb_lignes * taille_carre) // 2

    couleur_des_couches = ''
    couleur_des_billes = ''
    for i, lignes in enumerate(plateau):
        for j, cellule in enumerate(lignes):
            x = depart_x + j * taille_carre
            y = depart_y + i * taille_carre        
            rectangle(x, y, x + taille_carre, y + taille_carre, remplissage='Grey')

            if Tirette_verticale[i][j] == True and Tirette_horizontale[i][j] == False:
                couleur_des_couches = '#306998'
            elif Tirette_verticale[i][j] == True and Tirette_horizontale[i][j] == True:
                couleur_des_couches = '#1F1F1F'
            elif Tirette_verticale[i][j] == False :
                couleur_des_couches = '#FFE873'
            dessine_cercle(x + taille_carre // 2, y + taille_carre // 2, taille_carre // 2, remplissage=couleur_des_couches, epaisseur=1)

            if cercles[i][j] == True:
                if plateau[i][j] == 1:
                    couleur_des_billes = '#77831F'
                if plateau[i][j] == 2:
                    couleur_des_billes = 'fuchsia'
                if plateau[i][j] == 3:
                    couleur_des_billes = 'peru'
                if plateau[i][j] == 4:
                    couleur_des_billes = 'maroon'
                dessine_cercle(x + taille_carre // 2, y + taille_carre // 2, taille_carre // 4, remplissage=couleur_des_billes, epaisseur=1/2 )
             # Dessiner les flèches aux extrémités du plateau
            if i == 0:
                dessine_fleche(x + taille_carre // 2, y, 'Haut')
            elif i == nb_lignes - 1:
                dessine_fleche(x + taille_carre // 2, y + taille_carre, 'Bas')

            if j == 0:
                dessine_fleche(x, y + taille_carre // 2, 'Gauche')
            elif j == nb_colonnes - 1:
                dessine_fleche(x + taille_carre, y + taille_carre // 2, 'Droite')

    mise_a_jour()

def dessine_fleche(x, y, direction):
    # Dessiner une flèche simple en fonction de la direction (Haut, Bas, Gauche, Droite)
    couleur_fleche = 'Black'
    longueur_fleche = 10

    if direction == 'Haut':
        ligne(x, y, x, y - longueur_fleche, couleur_fleche)
        ligne(x, y - longueur_fleche, x + 5, y - longueur_fleche + 5, couleur_fleche)
        ligne(x, y - longueur_fleche, x - 5, y - longueur_fleche + 5, couleur_fleche)
    elif direction == 'Bas':
        ligne(x, y, x, y + longueur_fleche, couleur_fleche)
        ligne(x, y + longueur_fleche, x + 5, y + longueur_fleche - 5, couleur_fleche)
        ligne(x, y + longueur_fleche, x - 5, y + longueur_fleche - 5, couleur_fleche)
    elif direction == 'Gauche':
        ligne(x, y, x - longueur_fleche, y, couleur_fleche)
        ligne(x - longueur_fleche, y, x - longueur_fleche + 5, y + 5, couleur_fleche)
        ligne(x - longueur_fleche, y, x - longueur_fleche + 5, y - 5, couleur_fleche)
    elif direction == 'Droite':
        ligne(x, y, x + longueur_fleche, y, couleur_fleche)
        ligne(x + longueur_fleche, y, x + longueur_fleche - 5, y + 5, couleur_fleche)
        ligne(x + longueur_fleche, y, x + longueur_fleche - 5, y - 5, couleur_fleche)

def demander_nombre_joueurs():
    while True:
        try:
            nombre_joueurs = int(input("Entrez le nombre de joueurs (2 à 4): "))
            if 2 <= nombre_joueurs <= 4:
                return nombre_joueurs
            else:
                print("Veuillez entrer un nombre entre 2 et 4.")
        except ValueError:
            print("Veuillez entrer un nombre valide.")

def demander_taille_fenetre():
    while True:
        try:
            taille = int(input("Entrez la taille de la fenêtre (par exemple, 600): "))
            if taille > 0:
                return taille
            else:
                print("Veuillez entrer une taille valide.")
        except ValueError:
            print("Veuillez entrer une valeur numérique valide.")

def placement_des_trous(matrice):
    for i in matrice:
        nombre_trous = random.randint(1, 6) # Choisissez un nombre aléatoire entre 1 et 6
        indices_trous = random.sample(range(len(i)), nombre_trous)  # Choisissez aléatoirement des indices sans remplacement
        for indice in indices_trous:
            i[indice] = True

def decale_gauche(ma_liste):
    if len(ma_liste) <= 1:
        return ma_liste
    premier_element = ma_liste[0]
    for i in range(1, len(ma_liste)):
        ma_liste[i-1] = ma_liste[i]
    ma_liste[-1] = premier_element

def decale_droite(ma_liste):
    if len(ma_liste) <= 1:
        return ma_liste
    dernier_element = ma_liste[-1]
    for i in range(len(ma_liste)-1, 0, -1):
        ma_liste[i] = ma_liste[i-1]
    ma_liste[0] = dernier_element

def decale_haut(matrice, colonne):
    n = len(matrice)
    element_haut = matrice[0][colonne]

    for ligne in range(1, n):
        matrice[ligne - 1][colonne] = matrice[ligne][colonne]

    matrice[n - 1][colonne] = element_haut

def decale_bas(matrice, colonne):
    n = len(matrice)
    element_bas = matrice[n - 1][colonne]

    for ligne in range(n - 1, 0, -1):
        matrice[ligne][colonne] = matrice[ligne - 1][colonne]

    matrice[0][colonne] = element_bas

def afficher_matrice(matrice):
    '''
    Une fonction qui affiche une matrice ligne par ligne.

    Paramètre :
    matrice -> (list) Une matrice à afficher.
    '''
    for ligne in matrice:
        print(ligne)

nombre_de_joueurs = demander_nombre_joueurs()
taille_fenetre= demander_taille_fenetre()
cree_fenetre(taille_fenetre, taille_fenetre)

plateau = créer_matrice(taille_plateau, Val=[False])
cercles = créer_matrice(taille_plateau, Val=[False])
Tirette_verticale = créer_matrice(taille_plateau, Val=[False])
Tirette_horizontale = créer_matrice(taille_plateau, Val=[False])
placement_des_trous(Tirette_verticale)
placement_des_trous(Tirette_horizontale)
dessine_plateau(plateau, cercles, taille_fenetre, Tirette_verticale, Tirette_horizontale)
afficher_matrice(Tirette_horizontale)
print("------------")
afficher_matrice(Tirette_verticale)
joueur_actuel = 1
billes_placées_joueur1 = 0
billes_placées_joueur2 = 0
billes_placées_joueur3 = 0
billes_placées_joueur4 = 0 
while True:
    ev = donne_ev()
    tev = type_ev(ev)

    if tev == "ClicGauche":
        x = (abscisse(ev) - (taille_fenetre - taille_plateau * taille_carre) // 2) // taille_carre
        y = (ordonnee(ev) - (taille_fenetre - taille_plateau * taille_carre) // 2) // taille_carre

        # Vérifier si la case est un trou blanc
        if Tirette_verticale[y][x] == True and Tirette_horizontale[y][x] == True:
            print("Vous ne pouvez pas placer votre bille sur un trou.")
        else:
            if 0 <= x < taille_plateau and 0 <= y < taille_plateau:
                if joueur_actuel == 1 and billes_placées_joueur1 < 3:
                    cercles[y][x] = True
                    plateau[y][x] = 1
                    billes_placées_joueur1 += 1
                elif joueur_actuel == 2 and billes_placées_joueur2 < 3:
                    cercles[y][x] = True
                    plateau[y][x] = 2
                    billes_placées_joueur2 += 1
                elif joueur_actuel == 3 and billes_placées_joueur3 < 3:
                    cercles[y][x] = True
                    plateau[y][x] = 3
                    billes_placées_joueur3 += 1
                elif joueur_actuel == 4 and billes_placées_joueur4 < 3:
                    cercles[y][x] = True
                    plateau[y][x] = 4
                    billes_placées_joueur4 += 1

                dessine_plateau(plateau, cercles, taille_fenetre, Tirette_verticale, Tirette_horizontale)

                # Passer au joueur suivant et vérifier si tous les joueurs ont placé leurs billes
                if joueur_actuel == 1 and billes_placées_joueur1 == 3:
                    joueur_actuel = 2
                elif joueur_actuel == 2 and billes_placées_joueur2 == 3 and nombre_de_joueurs >= 3:
                    joueur_actuel = 3
                elif joueur_actuel == 3 and billes_placées_joueur3 == 3 and nombre_de_joueurs >= 4:
                    joueur_actuel = 4
                elif joueur_actuel == 4 and billes_placées_joueur4 == 3:
                    joueur_actuel = 0

                if billes_placées_joueur1 == 3 and billes_placées_joueur2 == 3 and billes_placées_joueur3 == 3 and billes_placées_joueur4 == 3:
                    print("Tous les joueurs ont placé leurs billes. Fin du placement initial.")
                    i = 1
                    while i <= 4:
                        # Demander au joueur actuel de tirer sur une tirette
                        choix_tirette = input("Joueur {}, choisissez une tirette (V pour verticale, H pour horizontale): ".format(i))

                        if choix_tirette == 'V':
                            # Demander la ligne et la direction pour la tirette verticale
                            ligne_tirette = int(input("Choisissez la ligne (1 à {}): ".format(taille_plateau)))
                            direction_tirette = input("Choisissez la direction (Haut/Bas): ")

                            # Appliquer le décalage en fonction de la direction choisie
                            if direction_tirette == 'Haut':
                                decale_haut(Tirette_verticale, ligne_tirette - 1)
                            elif direction_tirette == 'Bas':
                                decale_bas(Tirette_verticale, ligne_tirette - 1)

                        elif choix_tirette == 'H':
                            # Demander la colonne et la direction pour la tirette horizontale
                            colonne_tirette = int(input("Choisissez la colonne (1 à {}): ".format(taille_plateau)))
                            direction_tirette = input("Choisissez la direction (Gauche/Droite): ")

                            # Appliquer le décalage en fonction de la direction choisie
                            if direction_tirette == 'Gauche':
                                decale_gauche(Tirette_horizontale[colonne_tirette - 1])
                            elif direction_tirette == 'Droite':
                                decale_droite(Tirette_horizontale[colonne_tirette - 1])

                                # Vérifier si la bille est maintenant sous un trou et la supprimer si nécessaire
                                if Tirette_verticale[y][x] == True and Tirette_horizontale[y][x] == True:
                                    cercles[y][x] = False
                                    plateau[y][x] = False

                        # Dessinez le plateau mis à jour
                        dessine_plateau(plateau, cercles, taille_fenetre, Tirette_verticale, Tirette_horizontale)
                        i += 1

    elif tev == 'Quitte':
        break

    else:
        pass

    mise_a_jour()

# Ferme la fenêtre à la fin du programme
ferme_fenetre()
