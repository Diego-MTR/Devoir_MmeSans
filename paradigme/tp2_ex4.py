from functools import reduce

notes = [12, 15, 9, 18, 6, 20, 14]

notes100 = list(map(lambda x: x * 5, notes))
notes_sup_50 = list(filter(lambda x: x >= 50, notes100))

if notes_sup_50:
    moyenne = reduce(lambda x, y: x + y, notes_sup_50) / len(notes_sup_50)
else:
    moyenne = 0

print("Notes sur 100 :", notes100)
print("Notes supérieures ou égales à 50 :", notes_sup_50)
print("Moyenne des notes filtrées :", moyenne)

