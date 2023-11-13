#Make several dictionaries, where each dictionary represents a different pet. 
#In each dictionary, include the kind of animal and thevowner’s name. 
#Store these dictionaries in a list called pets. 
#Next, loop through your list and asyou do, print everything you know about each pet. 

pets=[]

pet= {
    "animal type": "cat",
    "name": "Matcha",
    "age": 2,
    "owners name": "Joanna",
    "weight (in pounds)": 35,
    "eats": "salmon"
}

pets.append(pet)

pet= {
    "animal type": "dog",
    "name": "Cutie",
    "age": 2,
    "Owners name": "Micah",
    "weight (in pounds)": 40,
    "eats": "dog treats"
}

pets.append(pet)

pet= {
    "animal type": "Snake",
    "name": "Avalon",
    "age": 4,
    "Owners name": "Gian",
    "weight (in pounds)": 10,
    "eats": "mice"
}

for pet in pets: 
    print("\nThese are the things I know about" + pet["name"].title()+ ": ")
    for key, value in pet.items():
        print("\t" + key + ": " + str(value))





