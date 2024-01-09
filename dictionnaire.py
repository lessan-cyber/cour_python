person = {
    "name": "John",
    "age": 20,
    "sex": "M",
    "address": {
        "pays": "Togo",
        "Ville": "Vogan"
    },
    "notes": [15, 10, 11, 16]
}
person["sex"] = "F"
person["address"]["Ville"] = "Lomé"
person["notes"][1] = 13
person["notes"].append(15)
person["contact"] = "91 66 78 77"
nombreCle = 0
for key in person:
    nombreCle += 1
    if type(person[key]) == dict:
        for subKeys in person[key]:
            nombreCle += 1

print(f"le nombre de est {nombreCle}")
print("nombre de clé", person)
print("longeur", len(person))
print(len("bonjour"))

if "niveau" in person:
    print("le niveau existe deja")
else:
    person["niveau"] = "B2"
    print("le niveau est créer")


def creerVerifierCler(key, value):
    if key in person:
        message = f" {key} est deja dans le dictionary"
    else:
        person[key] = value
        message = f" {key} vient d'etre dans le dictionnaire"
    return message


print(creerVerifierCler("maison", "deux etage"))
print(creerVerifierCler("maison", "deux etage"))
# cle = input("entrer la clé")
# valeur = input("entrer la valeur")
# print(creerVerifierCler(cle, valeur))
print(creerVerifierCler("bank", 1500))
print(person)

for key in person:
    print(key, person[key])


def compterNombreCle(dictonnaire):
    nombre = len(dictonnaire.keys())
    for value in dictonnaire.values():
        if type(value) == dict:
            nombre += compterNombreCle(value)
    return nombre



myDictionnary = {
    "name": "lessan",
    "surname": "aziz",
    "age": 19,
    "address": {
        "pays": "Togo",
        "Résidence": {
            "ville": "Lomé",
            "Quartier": "hédzranawoé"
        }
    },
    "sex": "M",
    }
print(f"le nombre de cle principale et de sous clé dans ce dictionnaire est {compterNombreCle(myDictionnary)}")
