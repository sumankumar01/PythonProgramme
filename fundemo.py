def python_food(food):
    width = 80

    print(food)


def python_food1(*food):
    width = 80
    for i in food:
        print(str(i))


python_food("spam and eggs")

python_food1(80000, "suman", "kumar")
