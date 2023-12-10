from wiktionaryparser import WiktionaryParser
import random

def obtenir_definition_wiktionnaire(mot):
    parser = WiktionaryParser()
    mot_info = parser.fetch(mot, 'french')
    parser.set_default_language('french')
    parser.exclude_part_of_speech('noun')
    parser.include_relation('alternative forms')
    
    # print(mot_info[0]['definitions'][0]['text'][1])
    
    return(mot_info[0]['definitions'][0]['text'][1])

def charger_mots_francais(path):
    with open(path, 'r', encoding='utf-8') as fichier:
        mots = fichier.read().splitlines()
    return mots

def generer_mot_francais_aleatoire(path_dictionnary):
    mots_francais = charger_mots_francais(path_dictionnary)
    mot_aleatoire = random.choice(mots_francais)
    return mot_aleatoire

if __name__ == "__main__":
    
    # Génération d'un mot aléatoire
    random_word = generer_mot_francais_aleatoire('database/dico.txt')
    print(random_word)
    
    # recherche de définition
    definition = obtenir_definition_wiktionnaire(random_word)
    print(f"{random_word}: {definition}")
