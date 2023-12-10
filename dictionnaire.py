from wiktionaryparser import WiktionaryParser

def obtenir_definition_wiktionnaire(mot):
    parser = WiktionaryParser()
    mot_info = parser.fetch(mot, 'french')
    parser.set_default_language('french')
    parser.exclude_part_of_speech('noun')
    parser.include_relation('alternative forms')
    
    # print(mot_info[0]['definitions'][0]['text'][1])
    
    return(mot_info[0]['definitions'][0]['text'][1])

if __name__ == "__main__":
    # Exemple d'utilisation
    mot_a_chercher = "pouvoir"
    definition = obtenir_definition_wiktionnaire(mot_a_chercher)
    print(f"{mot_a_chercher}: {definition}")
