#playing with python lists

places = ["Lisbon", "Porto", "Aveiro", "Braga", "Coimbra"]
print(places)
print(sorted(places))
print(places)
print(sorted(places, reverse=True))
print(places)
places.sort(reverse=True)
print(places)
places.sort()
print(places)
places.sort(reverse=True)
print(places)
print(len(places))


#for loop

pizzas = ["cheese", "meat", "fish"]

for pizza in pizzas:
    print(pizza)


for pizza in pizzas:
    print(f"I like {pizza} pizza")
print("I really like pizza")

#for value in range (1,21):
 #   print(value)

numbers = list(range(1, 1000001))

print(min(numbers))
print(max(numbers))
print(sum(numbers))

for value in range (1,21,2):
    print(value)


for multiples_of_three in list(range(3, 31, 3)):
    print(multiples_of_three)
    
for cubes in range(1,11):
    print(cubes**3)

cubes = [cube**3 for cube in range (1,11)]
print(cubes)