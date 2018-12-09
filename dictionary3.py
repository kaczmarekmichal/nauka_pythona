produkty = {'S122' : 'sukienka trojkat',
            'P123' : 'spodnie krata',
            'x212' : 'konsola' }

igla ='x2x'

if igla in produkty:
    print("znalazlem {0}".format(igla))
else:
    print("Brak w magazynie {0}".format(igla))                
