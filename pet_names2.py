pet_names = {"Lukasek": "parrot", "Sofie": "dog", "Micka": "cat", "Plazivec": "had"}

for pet, name in pet_names.items():
    print("{} is {}" .format(pet, name))

new_names = pet_names.copy()
new_names["Karolina"] = "cat"

for pet, name in new_names.items():
    print("{} is {}" .format(pet, name))


del new_names["Karolina"]

for pet, name in new_names.items():
    print("{} is {}" .format(pet, name))
