
nombreTerme = int(input("entrer le nombre de terme que vous voulez: "))
def fibonaci(nombre: int):
    terme = [0, 1]
    essai = 1
    while nombre < 3 and essai <= 3:
        print("invalide")
        nombreTerme = int(input("entrer le nombre de terme que vous voulez: "))
        essai += 1
        break

    i = 2
    while i < nombre:
        new = terme[i - 1] + terme[i - 2]
        terme.append(new)
        i += 1
    return terme

print(fibonaci(nombreTerme))