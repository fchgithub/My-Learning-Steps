capital_country = {"United States" : "Washington", 
                   "US" : "Washington", 
                   "Canada" : "Ottawa",
                   "Germany": "Berlin",
                   "France" : "Paris",
                   "England" : "London",
                   "UK" : "London",
                   "Switzerland" : "Bern",
                   "Austria" : "Vienna",
                   "Netherlands" : "Amsterdam"}
for c in capital_country:
    print("{country:13s} : {capital}".format(country=c, capital=capital_country[c]))
    
    
for c in capital_country:
    print('The %10d' %3434)

    
for c in capital_country:
    print('The {c:10d}'.format(c = 131324) )

for c in capital_country:
    print('The {:10d} and {:3s}'.format(234131324, 'sdsds') )



for i in range(995, 1010):
    # allign from the right
    print('This is a test: %10d' %i)  # print('This is a test: {:>10}'.format(i))
    # allign form the left
    print('This is a test: %-10d' %i) # print('This is a test: {:10}'.format(i)
    # allign in the middle
    print('This is a test: {:^10}'.format(i)
