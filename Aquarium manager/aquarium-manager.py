import json

# 
file = open('aquarium.json', encoding='utf8')
data_aquarium = json.load(file)
animals = data_aquarium['data']

def verify_fish(animal):
    if animal['type'] == 'fish':
        return True
    return False

animals_fish = list(filter(verify_fish, animals))

def animal_name(animal):
    return animal['name']

animal_fish_name = str(list(map(animal_name, animals_fish)))
print('Peixes: ' + animal_fish_name + '\n')

def assign_to_tank(animals, names_selected, new_tank_number):
    def change_tank_number(animal):
        if animal['name'] in names_selected:
            animal['tank number'] = new_tank_number
        return animal
    return list(map(change_tank_number, animals))

print('Dados atualizados:\n')
new_aquarium = assign_to_tank(animals, animal_fish_name, 42)
print(new_aquarium)