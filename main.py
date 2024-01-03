"""a = "Bonjour "
b = "les gens"
print(a + b)
a, b = 5, 6
print(a)
print(type(a))
a = 5.5
print(type(a))
a = False
print(type(a))
en python les booléan commence par une letter majuscule
# pour revenir en ligne en python il faut metre \n"""
# nom, prenoms, age = " METCHONOU", "Aziz", "19"
# print(f" je m appelle {nom} {prenoms} et j ai {age} ans")
# note1 = int(input("entrer la premiere note "))
# note2 = int(input("entrer la deuxième note "))
# print(f"la somme est {note1 + note2} la moyenne est {(note1 + note2)/2} et la différence est {note1 - note2}")
#
# number = 10
# if number > 5:
#     print("num est supérieur à 5")
# print("autre instruction")

# LES LISTES
infoPerson = ["John", "Doe", 20, 15.5, False, "B2ITA"]
notes = [15, 12, 13, 10]
somme = 0
for note in notes:
    somme += note
print(f"la moyenne est {somme/len(notes)}")
