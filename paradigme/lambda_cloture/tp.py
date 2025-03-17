# Exercice 1 : Utilisation d'Expressions Lambda

# Question 1.1
def carre(x):
    return (lambda x: x ** 2)(x)

# Question 1.2
nombres = [1, 2, 3, 4, 5]
carres = list(map(lambda x: x ** 2, nombres))

# Question 1.3
somme = lambda a, b: a + b

# Question 1.4
somme_totale = sum(nombres)

# Exercice 2 : Utilisation de Clôtures

def create_multiplier(n):
    return lambda x: x * n

# Question 2.1
double = create_multiplier(2)

# Question 2.2
triple = create_multiplier(3)

# Question 2.3
result_double = double(4)  # 4 * 2
result_triple = triple(4)  # 4 * 3

# Exercice 3 : Application Pratique

# Question 3.1
mots = ["arbre", "chat", "avion", "bateau", "alligator"]

# Question 3.2
mots_filtrés = list(filter(lambda x: x.startswith("a"), mots))

# Question 3.3
def compter_mots_longs(liste_mots):
    return (lambda mots: len([mot for mot in mots if len(mot) > 5]))(liste_mots)

# Exercice 5 : Fonction composée

def compose(f, g):
    return lambda x: f(g(x))

# Question 5.2
carre_plus_un = compose(lambda x: x + 1, lambda x: x ** 2)

# Exercice 6 : Utilisation Avancée d'Expressions Lambda

def filterMap(filtre, transformation, liste):
    return list(map(transformation, filter(filtre, liste)))

# Question 6.2
strings = ["hello", "", "world", "python", ""]
strings_nettoyes = filterMap(lambda x: x != "", lambda x: x.upper(), strings)

# Exercice 7 : Utilisation Avancée de Clôtures

def memoise(f):
    cache = {}
    def memoized_func(x):
        if x not in cache:
            cache[x] = f(x)
        return cache[x]
    return memoized_func

# Question 7.2
@memoise
def factorielle(n):
    return 1 if n == 0 else n * factorielle(n - 1) 

@memoise
def fibonacci(n):
    return n if n <= 1 else fibonacci(n - 1) + fibonacci(n - 2) 

# Exercice 8 : Application Pratique

def calculateDiscount(prix, reduction):
    return sum(map(reduction, prix))

# Question 8.2

prix_produits = [100, 200, 300] # Prix des produits
reduction_20 = lambda x: x * 0.8 # 20% de réduction
montant_total_apres_reduction = calculateDiscount(prix_produits, reduction_20) 
print(montant_total_apres_reduction) # 480.0
