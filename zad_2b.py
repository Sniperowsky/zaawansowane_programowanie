def mnozenie_liczby(lista_liczb):
    lista_liczb = lista_liczb[:5]
    pomnozone_liczby = [liczba * 2 for liczba in lista_liczb]

    return pomnozone_liczby


lista_liczb = [5, 230, 941, 85, 45, 4, 940, 89412, 50, 24]
print(mnozenie_liczby(lista_liczb))