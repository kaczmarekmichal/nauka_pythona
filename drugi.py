marka ='Peugeot'
marka2 = 'Audi'
ilosc_drzwi = 5
pojemnosc =1.3

marka_up = marka.upper()

marka_low = marka.lower()

print ("Samochod " + marka + " ma " + str(ilosc_drzwi) + " drzwi")
print (marka_low)
print("pojemnosc po zmianach " + str(pojemnosc*2))

marka_swap=marka.swapcase()

print(marka_swap)

if ilosc_drzwi >3:
    print('duzy')
else:
    print('maly')

if marka.startswith('Pe'):
    print('uwaga peugeot')
else:
    print("na szczescie to nie francuz!")
