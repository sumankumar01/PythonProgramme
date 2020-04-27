

def topten():
    n=1
    while n < 10:
        sq= n*n
        yield sq
        n +=1




value=topten()

#print(value.__next__())

for i in value:
    print(i)