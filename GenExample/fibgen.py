
def fibseries():
    current,previous  = 0, 1
    while True:
        current, previous = current + previous, current
        yield current

fib=fibseries()

print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))

print("*" * 80)

for f in range(10):
    print(next(fib))

