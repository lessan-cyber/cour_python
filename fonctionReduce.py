
# import reduce
from functools import reduce

my_liste = [1, 2, 3, 4, 5, 6, 7, 8, 9]
resultMultiplication = reduce(lambda x, y: x * y, my_liste)  # affiche la multiplication de tous les éléments de la liste
resultatAddition = reduce(lambda x, y: x + y, my_liste)  # affiche la somme de tous les éléments de la liste
print(resultMultiplication)

my_liste2 = [1 , "lessan",  2, 3, 4, "jean", "afi", 5, "christian", 6, 7, 8, 9]
resultatEntier = filter(lambda x: type(x) == int, my_liste2)  # affiche la liste des entiers
resutatPaire = filter(lambda x: x % 2 == 0, my_liste)  # affiche la liste des entiers pairs
print(list(resutatPaire))
print(list(resultatEntier))
