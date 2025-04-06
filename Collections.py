# collection = single "variable" used to store multiple values
# List = [] ordered and changeable, Duplicates OK
# Set = {} unordered and immutable, but Add/Remove Ok. No duplicates
# Tuple = () ordered and unchangeable. Duplicates Ok. Faster



# ---------------list[]----------------------------

# fruits = ["apple","banana","pineapple"]
# print(dir(fruits))

# print(len(fruits))
# print("apple" in fruits)
# print("orange" in fruits)

# fruits[0] = "orange"

# fruits.append("orange") //to add element
# fruits.remove("apple")
# fruits.insert(0,"orange")
# fruits.sort()
# fruits.reverse()
# fruits.clear()
# print(fruits.index("apple"))
# print(fruits.count("banana"))

# for fruit in fruits:
#     print(fruit)


#-------------------------set{}----------------------------

# fruits = {"apple","orange","banana","pineapple","apple"}

# print(len(fruits))
# print("pineapple" in fruits)
# fruits.add("oragne")
# fruits.remove("orange")
# fruits.pop()
# fruits.clear()

# for fruit in fruits:
#     print(fruit)

#------------------tuple--------------------------
# fruits = ("apple","orange","banana","pineapple","apple")
# print(fruits)


#-----------------------------dictionary-------------------------

# dictionary = a collection of {key:value} pairs
#              ordered and changeable. No duplicates

capitals = {"USA":"Washington D.C",
            "India":"New Delhi",
            "China":"Beijing",
            "Russia":"Moscow"}

# print(dir(capitals))

# print(capitals.get("USA"))

# if capitals.get("Japan"):
#     print("That capital exists")
# else:
#     print("That capital doesnt exists")

# capitals.update({"Germany":"Berline"})
# capitals.pop("China")
# capitals.popitem()
# capitals.clear()

# keys = capitals.keys()

# for key in keys:
#     print(key)

# values = capitals.values()

# for value in values:
#     print(value)


#  items = capitals.items()

for key,value in capitals.items():
    print(f"{key}:{value}")