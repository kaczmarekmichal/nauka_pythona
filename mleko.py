produkt ='mleko'
cena_produktu =350

if 100< cena_produktu and cena_produktu <200:
    print ('promocja 30%!')
    cena_produktu = cena_produktu - (cena_produktu*30)/100
elif cena_produktu >= 200 and cena_produktu <300:
    print ('promocja 35%!')
    cena_produktu = cena_produktu - (cena_produktu*35)/100
elif cena_produktu >=300:
    print ('promocja 50%!')
    cena_produktu = cena_produktu - (cena_produktu*50)/100

print('do zaplaty : ' +str(cena_produktu))
