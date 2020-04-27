def oddnumber():
    n=1
    while True:
        yield n
        n +=2

def piseries():
    odd=oddnumber()
    approximation=0
    while True:
        approximation +=(4/next(odd))
        yield  approximation
        approximation -= (4/next(odd))
        yield approximation

approx_pi=piseries()
for x in range(3):
    print(next(approx_pi))