from fltk import *
import time
import random

taille_carre = 40
taille_plateau = 7

def créer_matrice(n, Val):
    """
    Crée une matrice de taille n x n avec des valeurs initiales Val.

    Args:
    - n (int): La taille de la matrice.
    - Val (list): La valeur initiale pour chaque élément de la matrice.

    Returns:
    - list: Une matrice de taille n x n avec des valeurs initiales Val.
    """
    L = []
    for i in range(n):
        L.append(Val * n)
    return L

def dessine_cercle(x, y, rayon, remplissage, epaisseur):
    """
    Dessine un cercle avec les paramètres spécifiés.

    Args:
    - x (int): Coordonnée x du centre du cercle.
    - y (int): Coordonnée y du centre du cercle.
    - rayon (int): Rayon du cercle.
    - remplissage (str): Couleur de remplissage du cercle.
    - epaisseur (float): Épaisseur du trait du cercle.
    """
    cercle(x, y, rayon, remplissage=remplissage, epaisseur=epaisseur)

def dessine_plateau(plateau, cercles, taille_fenetre, Tirette_verticale, Tirette_horizontale):
    """
    Dessine le plateau de jeu avec les billes, les tirettes et les trous.

    Args:
    - plateau (list): Matrice représentant l'état du plateau de jeu.
    - cercles (list): Matrice représentant l'emplacement des billes sur le plateau.
    - taille_fenetre (int): Taille de la fenêtre de jeu.
    - Tirette_verticale (list): Matrice représentant l'état des tirettes verticales.
    - Tirette_horizontale (list): Matrice représentant l'état des tirettes horizontales.
    """
    global taille_carre

    nb_lignes = len(plateau)
    nb_colonnes = len(plateau[0])

    depart_x = (taille_fenetre - nb_colonnes * taille_carre) // 2
    depart_y = (taille_fenetre - nb_lignes * taille_carre) // 2

    for i, lignes in enumerate(plateau):
        for j, cellule in enumerate(lignes):
            x = depart_x + j * taille_carre
            y = depart_y + i * taille_carre
            rectangle(x, y, x + taille_carre, y + taille_carre, remplissage='Grey')

            if Tirette_verticale[i][j] == True and Tirette_horizontale[i][j] == False:
                couleur_des_couches = '#306998'
            elif Tirette_verticale[i][j] == True and Tirette_horizontale[i][j] == True:
                couleur_des_couches = '#1F1F1F'
            elif Tirette_verticale[i][j] == False:
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
                dessine_cercle(x + taille_carre // 2, y + taille_carre // 2, taille_carre // 4, remplissage=couleur_des_billes, epaisseur=1/2)
    mise_a_jour()

def placement_des_trous(matrice):
    """
    Place aléatoirement des trous (True) dans la matrice représentant les tirettes.

    Args:
    - matrice (list): La matrice représentant les tirettes du plateau de jeu.

    Returns:
    - None
    """
    for i in matrice:
        nombre_trous = random.randint(1, 6)
        indices_trous = random.sample(range(len(i)), nombre_trous)
        for indice in indices_trous:
            i[indice] = True

def decale_gauche(ma_liste):
    """
    Décale les éléments d'une liste vers la gauche.

    Args:
    - ma_liste (list): La liste à décaler.

    Returns:
    - list: La liste décalée vers la gauche.
    """
    if len(ma_liste) <= 1:
        return ma_liste
    premier_element = ma_liste[0]
    for i in range(1, len(ma_liste)):
        ma_liste[i-1] = ma_liste[i]
    ma_liste[-1] = premier_element

def decale_droite(ma_liste):
    """
    Décale les éléments d'une liste vers la droite.

    Args:
    - ma_liste (list): La liste à décaler.

    Returns:
    - list: La liste décalée vers la droite.
    """
    if len(ma_liste) <= 1:
        return ma_liste
    dernier_element = ma_liste[-1]
    for i in range(len(ma_liste)-1, 0, -1):
        ma_liste[i] = ma_liste[i-1]
    ma_liste[0] = dernier_element

def decale_haut(matrice, colonne):
    """
    Décale les éléments d'une colonne d'une matrice vers le haut.

    Args:
    - matrice (list): La matrice à modifier.
    - colonne (int): L'indice de la colonne à décaler.

    Returns:
    - None
    """
    n = len(matrice)
    element_haut = matrice[0][colonne]

    for ligne in range(1, n):
        matrice[ligne - 1][colonne] = matrice[ligne][colonne]

    matrice[n - 1][colonne] = element_haut

def decale_bas(matrice, colonne):
    """
    Décale les éléments d'une colonne d'une matrice vers le bas.

    Args:
    - matrice (list): La matrice à modifier.
    - colonne (int): L'indice de la colonne à décaler.

    Returns:
    - None
    """
    n = len(matrice)
    element_bas = matrice[n - 1][colonne]

    for ligne in range(n - 1, 0, -1):
        matrice[ligne][colonne] = matrice[ligne - 1][colonne]

    matrice[0][colonne] = element_bas

def afficher_matrice(matrice):
    """
    Affiche la matrice dans la console. (Utile pour tester la suppression des billes lorsqu'elles tombent sur un trou)

    Args:
    - matrice (list): La matrice à afficher.

    Returns:
    - None
    """
    for ligne in matrice:
        print(ligne)

def verifier_bille_et_supprimer(matrice):
    """
    Vérifie si une bille est positionnée sur une intersection des tirettes.
    Si c'est le cas, la bille est supprimée du plateau.

    Args:
    - matrice (list): Matrice représentant l'état du plateau de jeu.

    Returns:
    - None
    """
    for i in range(len(matrice)):
        for j in range(len(matrice)):
            if Tirette_horizontale[i][j] == True and Tirette_verticale[i][j] == True:
                plateau[i][j] = False
                cercles[i][j] = False

def a_perdu(matrice, numero_joueur):
    """
    Vérifie si un joueur a perdu en ne trouvant plus aucune de ses billes sur le plateau.

    Args:
    - matrice (list): Matrice représentant l'état du plateau de jeu.
    - numero_joueur (int): Le numéro du joueur à vérifier.

    Returns:
    - bool: True si le joueur a perdu, False sinon.
    """
    for i in range(len(matrice)):
        for j in range(len(matrice)):
            if plateau[i][j] == numero_joueur:
                return False
    return True

def tous_identiques(liste, element_a_comparer):
    """
    Vérifie si tous les éléments d'une liste sont identiques à une valeur spécifiée.

    Args:
    - liste (list): La liste à vérifier.
    - element_a_comparer: L'élément avec lequel comparer.

    Returns:
    - bool: True si tous les éléments sont identiques, False sinon.
    """
    ensembles_uniques = set(liste)
    return len(ensembles_uniques) == 1 and ensembles_uniques.pop() == element_a_comparer

def a_gagne(matrice, numero_joueur):
    """
    Vérifie si un joueur a gagné en ayant toutes ses billes alignées.

    Args:
    - matrice (list): Matrice représentant l'état du plateau de jeu.
    - numero_joueur (int): Le numéro du joueur à vérifier.

    Returns:
    - bool: True si le joueur a gagné, False sinon.
    """
    L1 = []
    for i in range(len(matrice)):
        for j in range(len(matrice)):
            if plateau[i][j] != False:
                L1.append(plateau[i][j])
    return tous_identiques(L1, numero_joueur)

def afficher_instruction(instruction, tag_ins, alert=False):
    """
    Affiche une instruction à l'utilisateur dans la fenêtre du jeu.

    Args:
    - instruction (str): L'instruction à afficher.
    - tag_ins (str): Le tag associé à l'instruction.
    - alert (bool): Indique s'il s'agit d'une alerte (texte en rouge).

    Returns:
    - None
    """
    if alert:
        y_position = taille_fenetre // 6
        texte(taille_fenetre // 2 - len(instruction) * 4, y_position, instruction, taille=14, police='Helvetica', tag=tag_ins, couleur='red')
    else:
        y_position = taille_fenetre // 8
        texte(taille_fenetre // 2 - len(instruction) * 4, y_position, instruction, taille=14, police='Helvetica', tag=tag_ins, couleur='navy')
    mise_a_jour()

def bille_tombee(matrice, numero_joueur, x, y):
    """
    Vérifie si une bille est tombée sur un trou.
    Si c'est le cas, affiche une instruction.

    Args:
    - matrice (list): Matrice représentant l'état du plateau de jeu.
    - numero_joueur (int): Le numéro du joueur à vérifier.
    - x (int): Coordonnée x de la bille.
    - y (int): Coordonnée y de la bille.

    Returns:
    - None
    """
    if Tirette_horizontale[y][x] and Tirette_verticale[y][x]:
        afficher_instruction("Une bille du joueur {} est tombée !".format(numero_joueur), tag_ins='Info', alert=True)

def demander_saisie_numerique(message, plage_valide):
    """
    Demande à l'utilisateur une saisie numérique dans une plage valide.

    Args:
    - message (str): Le message à afficher pour la saisie.
    - plage_valide (range): La plage valide pour la saisie.

    Returns:
    - int: La valeur saisie par l'utilisateur.
    """
    while True:
        try:
            valeur = int(input(message))
            if valeur in plage_valide:
                return valeur
            else:
                print("Veuillez entrer une valeur dans la plage spécifiée.")
        except ValueError:
            print("Veuillez entrer une valeur numérique valide.")

def demander_saisie_texte(message, options_valides):
    """
    Demande à l'utilisateur une saisie de texte parmi les options valides.

    Args:
    - message (str): Le message à afficher pour la saisie.
    - options_valides (list): Les options valides pour la saisie.

    Returns:
    - str: L'option saisie par l'utilisateur.
    """
    while True:
        valeur = input(message)
        if valeur in options_valides:
            return valeur
        else:
            print("Veuillez entrer une option valide parmi : {}".format(", ".join(options_valides)))

 
# Demande le nombre de joueurs et la taille de la fenêtre
nombre_de_joueurs = demander_saisie_numerique('Choisissez le nombre de joueurs (2 à 4) : ', range(2, 5))
taille_fenetre = demander_saisie_numerique('Choissez la taille de la fenêtre (Par exemple : 600) : ', range(200, 3000))

# Crée la fenêtre du jeu
cree_fenetre(taille_fenetre, taille_fenetre)

# Initialise les matrices pour le plateau, les cercles et les tirettes
plateau = créer_matrice(taille_plateau, Val=[False])
cercles = créer_matrice(taille_plateau, Val=[False])
Tirette_verticale = créer_matrice(taille_plateau, Val=[False])
Tirette_horizontale = créer_matrice(taille_plateau, Val=[False])

# Place les trous sur les tirettes
placement_des_trous(Tirette_verticale)
placement_des_trous(Tirette_horizontale)
afficher_matrice(Tirette_horizontale)
print("------------------")
afficher_matrice(Tirette_verticale)
# Dessine le plateau initial avec les trous
dessine_plateau(plateau, cercles, taille_fenetre, Tirette_verticale, Tirette_horizontale)

# Initialise les compteurs de billes placées pour chaque joueur
joueur_actuel = 1
billes_placées_joueur1 = 0
billes_placées_joueur2 = 0
billes_placées_joueur3 = 0
billes_placées_joueur4 = 0

# Affiche l'instruction pour le premier joueur
afficher_instruction("Joueur {}, placez vos trois billes sur le plateau.".format(joueur_actuel), tag_ins='Ins1')

# Boucle principale du jeu
while True:
    ev = donne_ev()
    tev = type_ev(ev)

    if tev == "ClicGauche":
        # Récupère les coordonnées du clic
        x = (abscisse(ev) - (taille_fenetre - taille_plateau * taille_carre) // 2) // taille_carre
        y = (ordonnee(ev) - (taille_fenetre - taille_plateau * taille_carre) // 2) // taille_carre

        
        if not (0 <= x < taille_plateau and 0 <= y < taille_plateau):
            afficher_instruction("Vous ne pouvez pas placez votre bille en dehors du plateau !", tag_ins='Alerte0', alert=True)
            time.sleep(1)
            efface('Alerte0')
        else :
            # Vérifie si la bille peut être placée
            if Tirette_verticale[y][x] == True and Tirette_horizontale[y][x] == True:
                afficher_instruction("Vous ne pouvez pas placez votre bille sur un trou !", tag_ins='Alerte1', alert=True)
                time.sleep(1)
                efface('Alerte1')
            else:
                if plateau[y][x] == False:
                    # Vérifie les limites du plateau
                    if 0 <= x < taille_plateau and 0 <= y < taille_plateau:
                        # Place la bille en fonction du joueur actuel
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

                        # Dessine le plateau mis à jour
                        dessine_plateau(plateau, cercles, taille_fenetre, Tirette_verticale, Tirette_horizontale)


                        # Change de joueur une fois que toutes les billes ont été placées
                        if joueur_actuel == 1 and billes_placées_joueur1 == 3: 
                            joueur_actuel = 2
                            efface('Ins1')
                            afficher_instruction("Joueur {}, placez vos trois billes sur le plateau.".format(joueur_actuel), tag_ins='Ins2')
                        if joueur_actuel == 2 and billes_placées_joueur2 == 3 and nombre_de_joueurs >= 3:
                            joueur_actuel = 3
                            efface('Ins2')
                            afficher_instruction("Joueur {}, placez vos trois billes sur le plateau.".format(joueur_actuel), tag_ins='Ins3')
                        if joueur_actuel == 3 and billes_placées_joueur3 == 3 and nombre_de_joueurs >= 4:
                            joueur_actuel = 4
                            efface('Ins3')
                            afficher_instruction("Joueur {}, placez vos trois billes sur le plateau.".format(joueur_actuel), tag_ins='Ins4')
                        if joueur_actuel == 4 and billes_placées_joueur4 == 3:
                            efface('Ins4')
                            joueur_actuel = 0

                    else:
                        # Avertissement si la case est déjà prise
                        afficher_instruction("Cette case est déjà prise !", tag_ins='Alerte2', alert=True)
                        time.sleep(1)
                        efface('Alerte2')

                else:
                    # Avertissement si la bille ne peut pas être placée sur un trou
                    afficher_instruction("Cette case est déjà prise !", tag_ins='Alerte2', alert=True)
                    time.sleep(1)
                    efface('Alerte2')

            # Vérifie si toutes les billes ont été placées par tous les joueurs
            if billes_placées_joueur1 == 3 and billes_placées_joueur2 == 3 and nombre_de_joueurs==2 or billes_placées_joueur1 == 3 and billes_placées_joueur2 == 3 and billes_placées_joueur3 == 3 and nombre_de_joueurs==3 or  billes_placées_joueur1 == 3 and billes_placées_joueur2 == 3 and billes_placées_joueur3 == 3 and billes_placées_joueur4 == 3 and nombre_de_joueurs == 4:
                efface('Ins2')
                efface('Ins3')
                efface('Ins4')
                afficher_instruction("Tous les joueurs ont placé leurs billes, fin du placement !", tag_ins='Alerte3', alert=True)
                time.sleep(2)
                efface('Alerte3')
                i = 1
                
                # Boucle pour chaque joueur
                while i <= nombre_de_joueurs:
                    afficher_instruction("Joueur {}, choisissez une tirette (V/H) : ".format(i), tag_ins='tag1')
                    choix_tirette = demander_saisie_texte("Choisissez une tirette (V/H): ", ['V', 'H'])
                    if choix_tirette == 'V':
                        efface('tag1')
                        afficher_instruction("Choisissez la ligne (1 à {}): ".format(taille_plateau), tag_ins='tag2')
                        ligne_tirette = demander_saisie_numerique("Choisissez la ligne (1 à {}): ".format(taille_plateau), range(1,taille_plateau+1))
                        if type(ligne_tirette) == int :
                            efface('tag2')
                        afficher_instruction("Choisissez la direction (Haut/Bas): ", tag_ins= 'tag3')
                        direction_tirette = demander_saisie_texte("Choisissez la direction (Haut/Bas): ", ['Haut','Bas'])
                        if type(direction_tirette) == str:
                            efface('tag3')
                        if direction_tirette == 'Haut':
                            decale_haut(Tirette_verticale, ligne_tirette - 1)
                        elif direction_tirette == 'Bas':
                            decale_bas(Tirette_verticale, ligne_tirette - 1)
                        verifier_bille_et_supprimer(plateau)

                    elif choix_tirette == 'H':
                        efface('tag1')
                        afficher_instruction("Choisissez la colonne (1 à {}): ".format(taille_plateau), tag_ins='tag2')
                        colonne_tirette = demander_saisie_numerique("Choisissez la colonne (1 à {}): ".format(taille_plateau), range(1,taille_plateau+1))
                        if type(colonne_tirette) == int :
                            efface('tag2')
                        afficher_instruction("Choisissez la direction (Gauche/Droite): ", tag_ins= 'tag3')
                        direction_tirette = demander_saisie_texte("Choisissez la direction (Gauche/Droite): ", ['Gauche','Droite'])
                        if type(direction_tirette) == str:
                            efface('tag3')
                        if direction_tirette == 'Gauche':
                            decale_gauche(Tirette_horizontale[colonne_tirette - 1])
                        elif direction_tirette == 'Droite':
                            decale_droite(Tirette_horizontale[colonne_tirette - 1])
                        verifier_bille_et_supprimer(plateau)
                        
                    afficher_matrice(Tirette_horizontale)
                    print("------------------")
                    afficher_matrice(Tirette_verticale)
                    dessine_plateau(plateau, cercles, taille_fenetre, Tirette_verticale, Tirette_horizontale)
                    i += 1

                    # Réinitialise le compteur pour boucler à nouveau si nécessaire
                    if not a_gagne(plateau, 1) and not a_gagne(plateau, 2) and not a_gagne(plateau, 3) and not a_gagne(plateau, 4) and i > nombre_de_joueurs:
                        i = 1
                    elif a_gagne(plateau, 1) == True :
                        numero_joueur = 1
                        afficher_instruction("Félicitations ! Joueur {}, a gagné la partie !.".format(numero_joueur), tag_ins='Win1')
                        time.sleep(3)
                        break
                    elif a_gagne(plateau,2) == True :
                        numero_joueur = 2
                        afficher_instruction("Félicitations ! Joueur {}, a gagné la partie !.".format(numero_joueur), tag_ins='Win2')
                        time.sleep(3)
                        break
                    elif a_gagne(plateau,3) == True :
                        numero_joueur = 3
                        afficher_instruction("Félicitations ! Joueur {}, a gagné la partie !.".format(numero_joueur), tag_ins='Win3')
                        time.sleep(3)
                        break
                    elif a_gagne(plateau,4) == True :
                        numero_joueur = 4
                        afficher_instruction("Félicitations ! Joueur {}, a gagné la partie !.".format(numero_joueur), tag_ins='Win4')
                        time.sleep(3)
                        break
                break

    elif tev == 'Quitte':
        break

    else:
        pass
    mise_a_jour()

attend_ev()
ferme_fenetre()

