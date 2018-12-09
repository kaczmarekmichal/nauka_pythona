print("Hello world!")


nazwa_samochodu = "Toyota"
v_max = 180
spalanie = 7.8
cena_paliwa =4.52

print ("Wybrany samochod to: " +nazwa_samochodu
        + " jego predkosc max to : " +str(v_max)
        + ", srednie spalanie = " +str(spalanie))
cena_za_100_km = round(spalanie*cena_paliwa,2)

print ("koszt przejechania 100 km to srednio: " +str(cena_za_100_km) +"pln")
