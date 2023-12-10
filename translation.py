from googletrans import Translator

def traduire_texte(texte, langue_source='en', langue_cible='fr'):
    try:
        translator = Translator()
        traduction = translator.translate(texte, src=langue_source, dest=langue_cible)
        return traduction.text
    except Exception as e:
        print(f"Erreur lors de la traduction : {str(e)}")
        return texte

if __name__ == "__main__":
    
    texte_a_traduire = "Hello, how are you?"
    texte_traduit = traduire_texte(texte_a_traduire, langue_source='en', langue_cible='fr')

    print(f"Texte original : {texte_a_traduire}")
    print(f"Texte traduit : {texte_traduit}")

