

numbers=[1,2,3,4,5,6,7,8,9,10]

even=[]

for i in numbers:
    if i%2==0:
        even.append(i)

print(even)

evens=[i for i in numbers if i%2 == 0]

print(evens)

print("*" * 40)

square_num= [i*i for i in numbers]

print(square_num)


s=set([1,2,3,4,5,2,3])

print(s)

even={i for i in numbers if i%2 == 0}

print(even)