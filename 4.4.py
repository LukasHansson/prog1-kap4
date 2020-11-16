meter = int(input('Släpp bollen från: ')) #Frågar om hur högt bollen ska släppas
centimeter = 100 * meter #Gör så att 1m blir 100cm
studs = 0 #Studsen börjar på noll
while centimeter > 1: #Om cm är större än 1 så tappar den farten med 30%
    centimeter = centimeter * 0.7
    studs += 1 #Lägger till 1 studs varje gång den gångras med 0.7 och är större en 1 cm

print(f'studs: {studs}') #Skriver ut hur många studs det blir