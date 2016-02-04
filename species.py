# This is just a test script for a Data Structures assignment.
# The goal was to create some sort of structure for dealing with biological data of species
# While my pseudocode implementation would have been better in reality, this was a useful exercise to figure out how to
# proceed.

def insert(species, name):
    species.append(name)
    print(name, "inserted at end")

def search(species, name):
    for x in range(0, len(species)):
        if(species[x] == name):
            print("Found:", name, "at position:", x)

def delete(species, name):
    for x in range(0, len(species)):
        if(species[x] == name):
            species.remove(species[x])
            print(name, "removed from species: ")

def deleteSpecies(species):
    print("Species will be deleted:", species)
    del species[:]
    del species
    print("Deleted.")
    
cat = ['Lion', 'Tiger', 'Snow Leopard', 'Jaguar', 'Leopard']
dog = ['Hyena', 'Wolf', 'Jackal', 'Domestic Doge', 'Fox']
fish = ['Goldfish', 'Koi', 'Trout', 'Salmon', 'Herring']
bird = ['Crow', 'Eagle', 'Hawk', 'Falcon', 'Vulture']

allTypes = [cat, dog, fish, bird]

#search
search(cat, 'Leopard')
#insert
insert(fish, "Tuna")

#delete(fish, "Tuna")
#delete species
#deleteSpecies(fish)

    
