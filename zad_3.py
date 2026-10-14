def parzyste_liczby(lista_liczb):
    lista_liczb = lista_liczb[:10]
    for liczba in lista_liczb:
        if (liczba%2 == 0):
            print(liczba)

lista_liczb = [5, 230, 941, 85, 45, 4, 940, 89412, 50, 24]
parzyste_liczby(lista_liczb)