import random

# Projet 1 
# Les fonctions utiles pour la suite du projet.

# 1. La foncion affichage 
def affiche(elems):
    '''
    Une fonction qui reçoit un itérable 
    elems (de type list, tuple, str et range)
    et affiche ses élements ligne par ligne.

    Paramètre : 
    1/ elems -> (list, tuple, str et range)

    '''
    for i in elems :
        print(i)


# Test 

elems1 = [1,5,7]
elems2 = (1,2,3,4)
elems3 = "1234"
elems4 = list(range(1, 5))

# 2. La fonction appartenance 

def appartient(elems, x):
    '''
    Une fonction qui reçoit un itérable elems
    (de type list, tuple, str et range) et 
    une valeur x et renvoie True si x est un 
    élément de elems et False sinon.

    Paramètres : 
    1/ elems -> (list, tuple, str et range)
    2/ x -> (int)
    '''
    for i in elems :
        if x == i :
            return True
        return False
    
if __name__ == "__main__" :
    import doctest
    doctest.testmod()

# 3. (1) La fonction recherche

def premier_indice(elems, x):
    '''
    Une fonction qui renvoie la première
    position de x dans la liste elems, 
    (ou None si x n’est pas dans elems) en
    utilisant une boucle for et la fonction range.

    '''
    for i in range(len(elems)):
        if elems[i] == x :
            return i 
    return None 

# Test :

#print(premier_indice(elems1, 7))

# 3. (2) La fonction dernier indice 

def dernier_indice(elems, x):
    '''
    Une fonction dernier_indice(elems, x) qui renvoie la dernière
    position de x dans la liste elems,
    (ou None si x n’est pas dans elems) en
    utilisant une boucle for et la fonction range.

    Paramètres : 
    1/ elems -> (list)
    2/ x -> (int)

    '''
    L = []
    for i in range(len(elems)):
        if elems[i]==x :
            L.append(i)
    if len(L) > 0 :
        return L[-1]
    return None 

# Test :

#print(dernier_indice(elems1, 3))


# 3. (3) Les mêmes fonctions en utilisant enumerate :

def premier_indice_enumerate(elems, x):
    '''
    Une fonction en utilisant enumerate
    qui renvoie la première
    position de x dans la liste elems, 
    (ou None si x n’est pas dans elems) en
    utilisant une boucle for et la fonction range.

    Paramètres : 
    1/ elems -> (list)

    '''
    for i, elements in enumerate(elems):
        if elements == x :
            return i 
    return None 

# La deuxième fonction en utilisant enumerate :

def dernier_indice_enumerate(elems, x):
    '''
    Une fonction  en utilisant enumerate 
    dernier_indice(elems, x) qui renvoie la dernière
    position de x dans la liste elems,
    (ou None si x n’est pas dans elems) en
    utilisant une boucle for et la fonction range.

    Paramètres : 
    1/ elems -> (list)
    2/ x -> (int)
    '''
    L = []
    for i, elements in enumerate(elems):
        if elements ==x :
            L.append(i)
    if len(L) > 0 :
        return L[-1]
    return None 

# 4. La fonction renversement de liste 

# 4. (1) Une fonction recevant une liste et renvoyant la liste inversée sans modifier la liste initiale

def renversement_de_liste(liste) :
    '''
    Une fonction recevant une liste et renvoyant la liste inversée sans
    modifier la liste initiale

    Paramètres : 
    1/ liste -> (list)
    2/ x -> (int)
    '''
    L = []
    for i in range(len(liste)-1,-1, -1) :
        L.append(liste[i])
    return L 

#Test 
#print(renversement_de_liste(elems1))

def renversement_de_lordre_liste(liste):
    '''
    Une fonction recevant une liste et inversant 
    l’ordre de ses éléments sur place

    Paramètre : 
    1/ liste -> (list)
    '''
    debut = 0
    fin = len(liste) - 1
    while debut < fin:
        liste[debut], liste[fin] = liste[fin], liste[debut]
        debut += 1
        fin -= 1

# Test 

#renversement_de_lordre_liste(elems1)
#print(elems1)

# 5. (1) Decalage de liste vers la gauche :

def decale_gauche(ma_liste):
    """
    Cette fonction décale la liste d'un cran vers la gauche.
    
    Parametre :
    ma_liste (list): La liste à décaler.
    """
    if len(ma_liste) <= 1:
        return ma_liste
    premier_element = ma_liste[0]
    for i in range(1, len(ma_liste)):
        ma_liste[i-1] = ma_liste[i]
    ma_liste[-1] = premier_element

# Test :

#decale_gauche(elems1)
#print(elems1)

# 5 (2) Decalage de liste vers la droite :

def decale_droite(ma_liste):
    """
    Cette fonction décale la liste d'un cran vers la droite.
    
    Parametres:
    ma_liste (list): La liste à décaler.
    """
    if len(ma_liste) <= 1:
        return ma_liste
    dernier_element = ma_liste[-1]
    for i in range(len(ma_liste)-1, 0, -1):
        ma_liste[i] = ma_liste[i-1]
    ma_liste[0] = dernier_element

def decale_haut(matrice, colonne):
    '''
    Une fonction qui décale les éléments d'une colonne vers le haut.

    Paramètres :
    matrice -> (list) Une matrice à traiter.
    colonne -> (int) Le numéro de la colonne à décaler.
    '''
    n = len(matrice)

    element_haut = matrice[0][colonne]

    for ligne in range(1, n):
        matrice[ligne - 1][colonne] = matrice[ligne][colonne]

    matrice[n - 1][colonne] = element_haut

def decale_bas(matrice, colonne):
    '''
    Une fonction qui décale les éléments d'une colonne vers le bas.

    Paramètres :
    matrice -> (list) Une matrice à traiter.
    colonne -> (int) Le numéro de la colonne à décaler.
    '''
    n = len(matrice)

    element_bas = matrice[n - 1][colonne]

    for ligne in range(n - 1, 0, -1):
        matrice[ligne][colonne] = matrice[ligne - 1][colonne]

    matrice[0][colonne] = element_bas

# Test :

#decale_droite(elems1)
#print(elems1)

# 6. Affecter une Case Matrice 

# Creer une matrice 
def créer_matrice(n):
    '''
    Une fonction qui crée une matrice de n*n.

    Paramètre :
    n -> (int)
    '''
    L=[]
    for i in range(n):
        L.append([False]*n)
    return L

def créer_plateau_de_balle(n):
    '''
    Une fonction qui crée une matrice de n*n.

    Paramètre :
    n -> (int)
    '''
    L=[]
    for i in range(n):
        L.append(['.']*n)
    return L

def afficher_matrice(matrice):
    '''
    Une fonction qui affiche une matrice ligne par ligne.

    Paramètre :
    matrice -> (list) Une matrice à afficher.
    '''
    for ligne in matrice:
        print(ligne)

#Test 
#print(créer_matrice(5))

def affecte_case(i,j,matrice,valeur):
    '''
    Une fonction qui prend en argument deux entiers i et j, 
    une liste de listes matrice et une valeur
    valeur et qui affecte la case de coordonnées (i, j) 
    de la matrice à la valeur donnée. 
    La fonction ne renvoie rien.

    Paramètres : 
    i -> (int)
    j -> (int)
    matrice -> (list (Une liste de liste pour être plus précis))
    valeur -> (int)

    '''
    matrice[i][j] = valeur

def recupere_valeur(i,j,matrice) :
    valeur = matrice[i][j]
    return valeur

def a_gagne(matrice):
    '''
    Vérifie si toutes les listes dans la matrice sont entièrement composées de valeurs False.

    Paramètre :
    matrice -> (list) Une matrice à vérifier.

    Retourne :
    (bool) True si toutes les listes sont entièrement False, False sinon.
    '''
    for ligne in matrice:
        for element in ligne :
            if element != '.' :
                return False
    return True


def affecte_liste(L,i, valeur):
    L[i]= valeur

def placement_des_trous(matrice):
    for i in matrice:
        nombre_trous = random.randint(1, 6) # Choisissez un nombre aléatoire entre 1 et 6
        indices_trous = random.sample(range(len(i)), nombre_trous)  # Choisissez aléatoirement des indices sans remplacement
        for indice in indices_trous:
            affecte_liste(i, indice, True)

def recupere_liste_dans_matrice(matrice, i):
    return matrice[i]

# Début de l'objectif intermediaire 

Plateau_de_balle = créer_plateau_de_balle(7)
tirage_verticale = créer_matrice(7)
tirage_horizontal = créer_matrice(7)
placement_des_trous(tirage_horizontal)
placement_des_trous(tirage_verticale)
print("------Plateau de balle-------")
afficher_matrice(Plateau_de_balle)
print("------Les tirettes horizontales-------")
afficher_matrice(tirage_horizontal)
print("------Les tirettes verticales-------")
afficher_matrice(tirage_verticale)

# Placement des billes par le joueur
i = 0
while i < 2:
    Placement_des_billes1 = int(input("Placez votre bille dans le plateau (ligne) : ")) -1
    Placement_des_billes2 = int(input("Placez votre bille dans le plateau (colonne) : ")) -1
    
    # Vérifie si la case est déjà occupée
    if recupere_valeur(Placement_des_billes1,Placement_des_billes1,Plateau_de_balle)=='O':
        print("La case est dejà occupé. Choisissez une autre case.")
        i-=1
    elif recupere_valeur(Placement_des_billes1, Placement_des_billes2, tirage_verticale)==True and recupere_valeur(Placement_des_billes1, Placement_des_billes2, tirage_horizontal)==True:
        print("La case est un trou. Vous avez perdu votre bille.")
    else:
        affecte_case(Placement_des_billes1, Placement_des_billes2, Plateau_de_balle, 'O')
        i += 1

# Affichage du plateau après le placement des billes
afficher_matrice(Plateau_de_balle)

# Phase de tirage sur les tirettes
arret = ""
cpt =3
while not a_gagne(Plateau_de_balle) and arret != 'fin':
    Utiliser_tirette1 = input("Quelle tirette vous voulez utiliser (Verticale/Horizontale) : ")
    Utiliser_tirette2 = int(input("Choisissez la ligne ou la colonne à tirer : ")) -1
    Utiliser_tirette3 = input("De quelle côté vous voulez tirer (Droite/Gauche), (Haut/Bas) : ")

    if Utiliser_tirette1 == "Verticale":
        if Utiliser_tirette3 == "Haut":
            decale_haut(tirage_verticale, Utiliser_tirette2)
        elif Utiliser_tirette3 == "Bas":
            decale_bas(tirage_verticale, Utiliser_tirette2)
        
    if Utiliser_tirette1 == "Horizontale":
        L = recupere_liste_dans_matrice(tirage_horizontal, Utiliser_tirette2)
        if Utiliser_tirette3 == "Droite":
            decale_droite(L)
        elif Utiliser_tirette3 == "Gauche":
            decale_gauche(L)

    print("------Les tirettes horizontales(Modifier)-------")
    afficher_matrice(tirage_horizontal)
    print("------Les tirettes verticales(Modifier)-------")
    afficher_matrice(tirage_verticale)

    # Change la bille en False si elle est au-dessus d'un trou
    bille_tombee = False
    for ligne in range(len(Plateau_de_balle)):
        for colonne in range(len(Plateau_de_balle[ligne])):
            if recupere_valeur(ligne, colonne, Plateau_de_balle)=='O'  and recupere_valeur(ligne, colonne, tirage_horizontal) == True and recupere_valeur(ligne, colonne, tirage_verticale)== True:
                affecte_case(ligne, colonne, Plateau_de_balle, '.')
                bille_tombee = True

    if bille_tombee == True :
        print("Une bille est tombée ! Voici le plateau de billes mis à jour :")
        afficher_matrice(Plateau_de_balle)
        
    # Vérifie si le joueur a gagné
    if a_gagne(Plateau_de_balle):
        print("Il ne reste plus de billes sur le plateau ! Bien joué, vous avez gagné !")
        break
    
    cpt-=1
    if cpt == 0 :
        print("Il ne vous reste plus de chances, vous avez perdu.")
        break

    print("Il vous reste ", cpt, "chances restantes.")
    arret = input("Vous voulez continuer('Oui') ? Si non, tapez 'fin' :  ")
