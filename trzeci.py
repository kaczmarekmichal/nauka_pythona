cena = 9


nazwa_produktu = 'krowa'

if cena>8:
    print("za drogo")
    if nazwa_produktu.startswith('kr'):
        print("czy to krowa z Argentyny?")
    if cena >8 and cena <10:
        print ('chyba kosztuje 9')
        if cena==9:
            print('na pewno 9')

else:
    print("okazja!")

samochody = ['syrenka' , 'polonez']

print(samochody[1])
