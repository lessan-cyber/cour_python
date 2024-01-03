# nom = str(input("entrer votre nom "))
# prenoms = str(input("entrer votre prenoms "))
# note1 = int(input("entrer la premiere note "))
# note2 = int(input("entrer la deuxième note "))
# moy = (note1 + note2) / 2
# print(f'bonjour {nom} {prenoms} '
#       f' vos notes sont {note1} et {note2} ,'
#       f' leur somme est {note2 + note2} '
#       f'votre moyenne est {moy}')
#
# if moy > 12:
#     print("moyenne est supérieur à 12")
# else:
#    print("votre moyenne est inférieur à 12")

# deux matières, 30 crédits par matière

credit1 = (float(input("entrer la premiere note  ")) * 30) / 20
print(credit1)
credit2 = (float(input("entrer la deuxième note  ")) * 30) / 20
print(credit2)
credit = credit2 + credit1
niveau = str(input("quelle est votre niveau B1 , B2 ou B3  "))

if credit == 60 and niveau == "B2":
    print(f"vous passez en B3 ")
elif credit >= 45 and niveau == "B1":
    print(f"vous redoubler {niveau}")
else:
    print(f"vous passez en classe supérieur")


