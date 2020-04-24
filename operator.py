a = 12
b = 4
print(a + b)
print(a - b)

print(a * b)
print(a / b)
print(a // b)
print(a % b)

for i in range(1, 4):
    print(i);

age = 24

print("my age is {0} years".format(age))

for i in range(1, 13):
    print("no. {0}  square is {1}  and cube is {2}".format(i, i ** 2, i ** 3))

print("--------------------------")
for i in range(1, 13):
    print("no. {0:2}  square is {1:3}  and cube is {2:4}".format(i, i ** 2, i ** 3))

print("pi is approximately {0:12}".format(22 / 7))
print("pi is approximately {0:12f}".format(22 / 7))
print("pi is approximately {0:12.50f}".format(22 / 7))
print("pi is approximately {0:52.50f}".format(22 / 7))
print("pi is approximately {0:52.50f}".format(22 / 7))
print("pi is approximately {0:62.50f}".format(22 / 7))
print("pi is approximately {0:70.50f}".format(22 / 7))

age = 32
name = 'suman'

print(name + f"is {age} years old")
