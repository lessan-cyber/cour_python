def average(liste):
    # verifier si l element est un entier d abord
    listeInt = list(filter(lambda x: type(x) == int, liste))
    moyenne = liste.reduce(lambda x, y: x + y, listeInt) / len(listeInt)
    # on peut aussi utiliser la fonction sum en verifiant que tu les element sont
    return moyenne
def nombrePaire(liste):
    listePaire = liste.filter(lambda x: x % 2 == 0, liste)
    return listePaire

def multipy(liste):
    listeMultiplication = liste.reduce(lambda x, y: x * y, liste)
    return listeMultiplication