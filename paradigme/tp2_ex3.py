from functools import reduce

ventes = [120, 50, 30, 20, 90, 100]
somme = reduce(lambda x, y: x + y, ventes)

nombres = [12, 24, 36, 44, 25]
produit = reduce(lambda x, y: x * y, nombres)

print(somme)
print(produit)