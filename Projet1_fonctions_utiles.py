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
        L.append([0]*n)
    return L
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

#Test : 
ma_matrice = créer_matrice(5)
affecte_case(2,2, ma_matrice, 5)
print(ma_matrice)
    

