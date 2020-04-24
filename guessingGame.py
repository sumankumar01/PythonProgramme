# Python Dictionay

# fruit={"orange":"a sweet,orange,citrus fruit",
#        "apple":"good for making cider",
#        "lemon":"a sour, yellow citrus fruit"}
#
# print(fruit)
#
# print(fruit["apple"])
#
# for a in fruit:
#     print(a)
#
# fruit["pearl"]="an odd shaped apple"
# fruit["pearl"]="an odd shaped apple ggg"
# print(fruit)
#
# del fruit["lemon"]
#
# print(fruit)

# del fruit

# fruit.clear()

# print(fruit)

#
# while True:
#     dict=input("Please enter a fruit:")
#     if(dict == "quit"):
#         break
#     description=fruit.get(dict,"we don't have this fruit")
#     print(description)

#
# for i in range(10):
#     for snack in fruit:
#         print(snack + "is" + fruit[snack])
#     print("*" * 20)


# orderd_key=list(fruit.keys())
# orderd_key.sort()
# orderd_key=sorted(list(fruit.keys()))
# for f in orderd_key:
#     print(fruit[f])
#
#
# print(fruit.keys())
# print(fruit.values())
#
# print("*" * 80)
#
# fruit["tomatoes"]="not nice with iceCream"
#
# print(fruit.keys())
#
# print("*" * 80)
# print(fruit.items())
#
# print("*" * 80)
# f_tuples=tuple(fruit.items())
# print(f_tuples)
# print("*" * 80)
#
# for snacks in f_tuples:
#     items,description=snacks
#     print(items +" is " + description)
# print("*" * 80)
#
#
# my_list=["a","b","c","e","f"]
# newString=""
# for c in my_list:
#     newString+=c + ","
#
# print(newString)
#
# print("*" * 80)
# newString="abcdefghijklmnopqrstuvxxuz"
# number="12345678"
# for c in my_list:
#     newString=" suman ".join(number)
#
# print(newString)
# print("*" * 80)


# set

# farm_animals={"cow","gaot","buffalo","lion"}
# print(farm_animals)
#
# for animals in farm_animals:
#     print(animals)
# print("*" * 80)
#
# wild_animls=set(["lions","tiger","elephant"])
# print(wild_animls)
#
# for animals in wild_animls:
#     print(animals)
#
# farm_animals.add("horse")
#
#
#
#
#
# empty_set=set()
# empty_set2={}
# empty_set.add("a")
# #empty_set2.add("a")
#
# even=set(range(0,40,2))
# print(even)
# print(len(even))

file = open("D:\QaClickGit\MobileAutomationAppium\Reports\htmlreport.html", 'r')

for line in file:
    print(line)

file.close();
