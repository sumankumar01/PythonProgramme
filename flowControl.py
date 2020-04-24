# name=input('Enter your name')
# age=int(input("how old are you, {0} ?".format(name)))
# print(age)


##if 0:
##("true")
###else:
## print("false")

number = input("please enter the series of number, using any seperator you like")
seperator = ""

for char in number:
    if not char.isnumeric():
        seperator = seperator + char

print(seperator)
