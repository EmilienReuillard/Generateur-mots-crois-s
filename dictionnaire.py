from wiktionaryparser import WiktionaryParser
import random
from translation import *

PATH_DICO = 'database/dico.txt'

def obtenir_definition_wiktionnaire(mot):
    parser = WiktionaryParser()
    mot_info = parser.fetch(mot, 'french')
    parser.set_default_language('french')
    parser.exclude_part_of_speech('noun')    
    # print(mot_info[0]['definitions'][0]['text'][1])
    
    return(mot_info[0]['definitions'][0]['text'][0])

def charger_mots_francais(path):
    with open(path, 'r', encoding='utf-8') as fichier:
        mots = fichier.read().splitlines()
    return mots

def generer_mot_francais_aleatoire(path_dictionnary = PATH_DICO ):
    mots_francais = charger_mots_francais(path_dictionnary)
    mot_aleatoire = random.choice(mots_francais)
    return mot_aleatoire

def find_word(letter, positon, path_dictionnary = PATH_DICO):
    with open(PATH_DICO, 'r') as fichier:
        # content = fichier.read()
        words = fichier.readlines()
        
    for word in words:
        try:
            for l,p in zip(letter, positon):
                if word[p]==l:
                    # print(word)
                    return word.strip()
        except:
            pass
        
    # print("No word founded")
    return False
        
    print(words[positon].strip())

if __name__ == "__main__":
    
    # # Génération d'un mot aléatoire
    # random_word = generer_mot_francais_aleatoire(PATH_DICO)
    # print(f"random_word = {random_word}")
    # print(f"{random_word[4]}")
    
    # # recherche de définition
    # definition = obtenir_definition_wiktionnaire(random_word)
    # print(f"{random_word}: {definition}")
    
    # #traduction
    # definition_trad = traduire_texte(definition)
    # print(f"{random_word}: {definition_trad}")
    
    find_word('e', 1, path_dictionnary = PATH_DICO)
