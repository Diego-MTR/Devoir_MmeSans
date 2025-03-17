recettes = {
    "pizza": ["farine", "eau", "sel", "levure", "tomate", "fromage"],
    "salade": ["laitue", "tomate", "concombre", "vinaigre", "huile"],
    "pates_carbonara": ["pates", "creme", "lardons", "fromage", "sel", "poivre"],
    "omelette": ["oeufs", "sel", "poivre", "fromage", "herbes"],
    "sandwich_jambon_beurre": ["pain", "beurre", "jambon", "salade"]
}

def suggere_recette(ingredients):
    return list(filter(lambda recette: all(item in ingredients for item in recettes[recette]), recettes))
    
if __name__ == "__main__":
    ingredients_disponibles = ["farine", "eau", "sel", "tomate", "fromage", "oeufs", "poivre", "herbes", "pain" , "beurre", "jambon", "salade", "lardon", "creme", "levure", "vinaigre", "huile", "laitue", "concombre"]
    print(suggere_recette(ingredients_disponibles))
