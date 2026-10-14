def porownanie(liczba1,liczba2,liczba_porownawcza):
    if(liczba1+liczba2>liczba_porownawcza):
        return True
    else:
        return False

print(porownanie(3,5,9000))
print(porownanie(3,5,1))