def mnozenie_liczby(lista_liczb):
    lista_liczb = lista_liczb[:5]
    pomnozone_liczby = []
    for liczba in lista_liczb:
        pomnozone_liczby.append(liczba*2)
    print(pomnozone_liczby)

lista_liczb = [5,230,941,85,45,4,940,89412,50,24]
mnozenie_liczby(lista_liczb)