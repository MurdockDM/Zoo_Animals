zoo = ("lion", "tiger", "elephant", "giraffe", "alligator", "hippo", "cheetah", "llama", "parrot", "lemur")

print(zoo.index("giraffe"))

animal_to_find = "lemur"
if animal_to_find in zoo:
    print(f"{animal_to_find} is in zoo")   

(firstAnimal, secondAnimal, thirdAnimal, fourthAnimal, fifthAnimal, sixthAnimal, seventhANimal, eighthAnimal, ninthAnimal, tenthAnimal) = zoo

for animal in zoo:
    print(f"{animal}")

zooList = list(zoo)

threeMoreAnimals = ["meerkat", "bobcat", "zebra"]

zooList.extend(threeMoreAnimals)   

zooListTuple = tuple(zooList)

print(zooListTuple)