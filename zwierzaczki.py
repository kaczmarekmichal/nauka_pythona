zwierzaczki = ['pies' , 'kot']

zwierzaczki.append('chomik')
zwierzaczki.append('papuga')
zwierzaczki.append('kon')


sublist= zwierzaczki[1:4]

print ("")

for z in zwierzaczki:
    print(z)

print ("")

print(", ".join(zwierzaczki))

print ("")

print ("wysietlenie sublist")


for s in sublist:
    print(s)

print ("")

bez_pierwszego = zwierzaczki[1:]

for s in bez_pierwszego:
    print(s)

print ("")

bez_ostatniego = zwierzaczki[:-1]

for s in bez_ostatniego:
    print(s)
