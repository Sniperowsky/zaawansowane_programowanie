def sprawdzenie(lista_liczb: list, liczba_porownawcza: int):
    czy_zawiera = False
    for liczba in lista_liczb:
        if(liczba == liczba_porownawcza):
           czy_zawiera = True
           break
    return czy_zawiera

lista = [5,2,1,6,8,9]
liczba1 = 8
liczba2 = 9503146

print(sprawdzenie(lista, liczba1))
print(sprawdzenie(lista, liczba2))