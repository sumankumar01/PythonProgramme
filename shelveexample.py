with shelveexample.open('shelfTest') as fruit:
    fruit['orange'] = "a sweet, orange, apple"
    fruit['apple'] = "good for making cider"
    fruit['lemon'] = "a sour, yellow in color"

print(fruit['orange'])
print(fruit['apple'])
