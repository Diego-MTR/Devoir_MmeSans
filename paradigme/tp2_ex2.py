âges = [12, 25, 17, 18, 40, 15, 22]
âges_senior = [2, 15, 28, 36, 43, 22, 60, 70, 80, 90]

majeur = list(filter(lambda x: x >= 18, âges))
senior = list(filter(lambda x: x >= 60, âges_senior))

print(majeur)
print(senior)
