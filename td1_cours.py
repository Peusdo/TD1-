import string
import random


def generer_mot_de_passe(taille=12, caracteres_speciaux=True):
    """
    Génère un mot de passe aléatoire.

    Args:
    taille (int): La longueur du mot de passe généré (default: 12).
    caracteres_speciaux (bool): Si True, inclut des caractères spéciaux dans le mot de passe (default: True).

    Returns:
    str: Le mot de passe généré.
    """
    caracteres = string.ascii_letters + string.digits

    if caracteres_speciaux:
        caracteres += string.punctuation

    mot_de_passe = ""

    # Utiliser randrange pour choisir un caractère aléatoire et l'ajouter au mot de passe
    for _ in range(taille):
        index_aleatoire = random.randrange(len(caracteres))
        mot_de_passe += caracteres[index_aleatoire]

    return mot_de_passe


def texte_vers_morse(texte):
    """
    Convertit une chaîne de caractères en code Morse.

    Args:
    texte (str): La chaîne de caractères à convertir.

    Returns:
    str: Le texte converti en code Morse.
    """
    code_morse = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
        'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
        'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
        'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
        '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----', ' ': '/'
    }

    texte = texte.upper()
    texte_morse = ""

    for caractere in texte:
        if caractere in code_morse:
            texte_morse += code_morse[caractere] + " "
        else:
            texte_morse += '? '

    return texte_morse.strip()


if __name__ == "__main__":
    # Exemple d'utilisation
    taille_du_mot_de_passe = 14
    inclure_caracteres_speciaux = True

    mot_de_passe_genere = generer_mot_de_passe(taille_du_mot_de_passe, inclure_caracteres_speciaux)
    print(f"Mot de passe généré: {mot_de_passe_genere}")

    # Exemple d'utilisation
    texte_en_morse = texte_vers_morse(mot_de_passe_genere)

    print(f"Texte original: {mot_de_passe_genere}")
    print(f"Texte en Morse: {texte_en_morse}")
