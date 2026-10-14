def zlaczenie(lista1: list, lista2: list):
    nowa_lista = []
    for liczba in lista2:
        lista1.append(liczba)
    lista1 = list(dict.fromkeys(lista1))
    lista1.sort()
    for liczba in lista1:
        liczba = liczba**3
        nowa_lista.append(liczba)
    return nowa_lista

lista1 = [5,20,15,95,93,14]
lista2 = [2,3,9,5,50,22,14]

print(zlaczenie(lista1,lista2))