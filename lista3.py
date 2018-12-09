
samoloty = ['boing' , 'bombardier', 'junkers']
ilosc = [3,5,6]
#pasazerowie = [100,10,140]


for idx in range(len (samoloty)):
        print("idx: " + str(idx) + " " + samoloty[idx])
        print(samoloty[idx] + " ma ilosc bomb " +str(ilosc[idx]))

if len(samoloty) >2:
    print (samoloty[2])

if sum(ilosc)>5:
    print sum(ilosc)
