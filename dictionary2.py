koszyk =[
    {'name' : 'pomidor', 'cena' :12.5},
    {'name' : 'ser' , 'cena' :4.5},
    {'name' : 'mleko' , 'cena' :1224.5},
]


print (koszyk[0]['cena'])


suma = (sum(item['cena'] for item in koszyk))

print(suma)

bylo_mleko = False

for poz in koszyk:
    suma = suma +poz['cena']
    nazwa_prod = poz ['name']
    if nazwa_prod =='mleko':
        bylo_mleko==True

if bylo_mleko == True:
    print("znizka")
    suma= suma- (suma*10)/100
    print(suma)
