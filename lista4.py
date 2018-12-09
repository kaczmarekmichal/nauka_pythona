koszyk=['pomidor','ogorek','ser','szynka','pomarancza']
ceny =[100,120,100,150,260]


suma = 0
suma = sum(ceny)
promocja_r1 = False
promocja_r2 = False
promocja_r3 = False

ilosc_produktow_promocja_r1 = 4
cena_produktow_promocja_r2 = 500
cena_produktow_promocja_r3 = 600


if len(koszyk)>ilosc_produktow_promocja_r1:
    promocja_r1=True
    suma_r1= (suma -(suma*5)/100)

if suma>cena_produktow_promocja_r2:
    promocja_r2=True
    suma_r2= (suma -(suma*10)/100)

if suma>cena_produktow_promocja_r3:
    promocja_r3=True
    suma_r3= suma - min(ceny)

if promocja_r3==True:
    print ("przekroczyles wartosc "
    + str(cena_produktow_promocja_r3) + " do zaplaty"
    +  str(suma_r3))
elif promocja_r1 ==True and promocja_r2 == True:
        print ("przekroczyles wartosc "
        + str(cena_produktow_promocja_r2) + " do zaplaty"
        +  str(suma_r2))
elif promocja_r1 ==True and promocja_r2 == False:
    print suma_r1
else:
    print suma
