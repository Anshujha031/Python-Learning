fruits =["apple","banana","pineapple"]
vegitable = ["celery","carrot","patato"]
meats = ["chicken" , "fish","yurkey"]

groceries = [fruits,vegitable,meats]

for collection in groceries:
    for food in collection:
        print(food,end=" ")
    print()