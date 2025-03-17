# Définition des recettes
recettes = {
    "pizza": ["farine", "eau", "sel", "levure", "tomate", "fromage"],
    "salade": ["laitue", "tomate", "concombre", "vinaigre", "huile"],
    "pates_carbonara": ["pates", "creme", "lardons", "fromage", "sel", "poivre"],
    "omelette": ["oeufs", "sel", "poivre", "fromage", "herbes"],
    "sandwich_jambon_beurre": ["pain", "beurre", "jambon", "salade"]
}

# Suggère des recettes en fonction des ingrédients disponibles
def suggere_recette(ingredients):
    suggestions = []
    for recette, recette_ingredients in recettes.items():
        if all(item in ingredients for item in recette_ingredients):
            suggestions.append(recette)
    return suggestions

# Exemple d'utilisation
if __name__ == "__main__":
    ingredients_disponibles = ["farine", "eau", "sel", "tomate", "fromage", "oeufs", "poivre", "herbes"]
    print(suggere_recette(ingredients_disponibles))
