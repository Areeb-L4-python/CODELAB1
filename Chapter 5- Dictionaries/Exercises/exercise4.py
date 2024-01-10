rivers = {
    'nile' : 'egypt',
    'mississipi' : 'united states',
    'fraser' : 'canada',
    'kuskokwim' : 'alaska',
    'yangtze': 'china',
}

for river, country in rivers.items():
    print(f"The {river.title()} flowes through {country.title()}.")

print("\nThe following rivers are included in this data set:")
for river in rivers.keys():
    print(f"-{river.title()}")    

print("\nThe following rivers are included in this data set:")
for country in rivers.values():
    print(f"-{country.title()}")    
