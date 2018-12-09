samolot = {'name': 'boeing',
            'przebieg' : 10000,
            'type' : 'pasazerski'}

for key, value in samolot.iteritems():
    print("{0} :{1}".format(key, value))

print("")

for key in samolot:
    print("{0} :{1}".format(key, samolot[key]))

print(samolot['nieznany_klucz'])    
