def liczba_parzysta(liczba):
    czy_parzysta = False
    if (liczba % 2 == 0):
        czy_parzysta = True
    return print(f'Liczba jest {"Parzysta" if czy_parzysta else "Nieparzysta"}')


liczba_parzysta(14)
liczba_parzysta(3)
