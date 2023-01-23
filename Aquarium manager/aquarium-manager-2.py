import json
from functools import reduce

# Import the data from the JSON file
file = open('aquarium.json', encoding='utf8')
data_aquarium = json.load(file)
animals = data_aquarium['data']

# Select the type of animal
def pick_animal_type(animal):
    return animal['type'], 1

# Count the number of animals of each type
def reducer(acc, val):
    if val[0] not in acc.keys():
        acc[val[0]] = 0 + val[1]
    else:
        acc[val[0]] = acc[val[0]] + val[1]
    return acc 

# Show the result to the user
type_animals = list(map(pick_animal_type, animals))
animals_type_count = reduce(reducer, type_animals, {})
print(animals_type_count)