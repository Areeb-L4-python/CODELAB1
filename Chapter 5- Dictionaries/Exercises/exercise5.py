pets.append(pet)

pet = {
    'animal type' : 'dog',
    'name' : 'Ash',
    'owner' : 'Niall',
    'weight' : 37,
}

pets.append(pet)
# Display information about each pet.
for pet in pets:
    print(f"\nhere is what i know about {pet['name'].title()}:")
    for key, value in pet.items():
        print(f"\t{key}: {value}")
