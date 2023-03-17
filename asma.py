import string

def tri_mots(liste_mots):
    if not isinstance(liste_mots, list):
        raise TypeError("liste_mots doit être une liste")
    if len(liste_mots) == 0:
        raise ValueError("liste_mots doit contenir au moins un élément")
    for mot in liste_mots:
        if not isinstance(mot, str):
            raise TypeError("liste_mots doit être une liste de chaînes de caractères")
        #Vérifier que chaque élement est un mot : il ne doit pas contenir d'espace
        if " " in mot:
            raise ValueError("liste_mots doit être une liste de mots, pas de phrases")


    mots_len = []

    #élimination des doublons
    liste_mots = list(set(liste_mots))

    #élimination des caractères spéciaux
    nouveau_liste = []
    for mot in liste_mots:
        mot = mot.lower()
        mot = mot.strip(string.punctuation)
        nouveau_liste.append(mot)

    for mot in nouveau_liste:
        longueur = len(mot)
        item = (mot, longueur)
        mots_len.append(item)

    mots_tries_len = sorted(mots_len, key=lambda x: x[1], reverse=True)

    mots_tries = []

    for x in mots_tries_len:
        item = (x[0], x[1])
        mots_tries.append(item)

    return mots_tries

def construire_chaine(civilite, nom, prenom, age, taille, poids):
    if not isinstance(civilite, str):
        raise TypeError("civilite doit être une chaîne de caractères")
    if not isinstance(nom, str):
        raise TypeError("nom doit être une chaîne de caractères")
    if not isinstance(prenom, str):
        raise TypeError("prenom doit être une chaîne de caractères")
    if not isinstance(age, int):
        raise TypeError("age doit être un entier")
    if age < 0:
        raise ValueError("age doit être positif")
    if not isinstance(taille, float):
        raise TypeError("taille doit être un nombre à virgule flottante")
    if taille < 0:
        raise ValueError("taille doit être positive")
    if not isinstance(poids, float):
        raise TypeError("poids doit être un nombre à virgule flottante")
    if poids < 0:
        raise ValueError("poids doit être positif")

    chaine = ""

    if civilite == "M" or civilite == "Monsieur":
        chaine += "Monsieur "
    elif civilite == "Mme" or civilite == "Madame":
        chaine += "Madame "
    else:
        raise ValueError("civilite doit être M, Mme, Monsieur ou Madame")

    if not prenom.islower():
        prenom = prenom.lower()
    chaine += prenom.capitalize() + " "

    if not nom.isupper():
        nom = nom.upper()
    chaine += nom + ", "

    chaine += str(age) + " ans, "

    if taille - int(taille) > 0:
        taille = round(taille, 1)
    chaine += str(taille) + " m, "

    if poids - int(poids) > 0:
        poids = round(poids, 1)
    chaine += str(poids) + " kg"

    return chaine

#Doivent générer des erreurs
# print(tri_mots(["aaa aa","aaa", "a"]))
# print(tri_mots(["aa",1]))

# Doit éléminer les doublons et les caractères spéciaux
print(tri_mots(["aa","aa","coucou!!!"]))

# Doit générer une erreur
# print(construire_chaine("Truc", "DUPONT", "Jean", 25, 1.75, 75.0))
# print(construire_chaine("M", "DUPONT", "Jean", 25, -1, 75.0))
# Doit transformer M en Monsieur, dupont en DUPONT, jean en Jean et 1.75 en 1.8
print(construire_chaine("M", "dupont", "jean", 25, 1.75, 75.0))