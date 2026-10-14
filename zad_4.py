def co_druga_liczba(lista_liczb):
    lista_liczb = lista_liczb[:10]
    for i in range(10):
        if (i % 2 == 0):
            print(lista_liczb[i])


lista_liczb = [5, 230, 941, 85, 45, 4, 940, 89412, 50, 24]
co_druga_liczba(lista_liczb)