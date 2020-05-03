text="what have the romens ever done for us"

capitals=[char.upper() for char in text]

print(capitals)

map_capitals=list(map(str.upper,text))

print(map_capitals)
words=[word.upper() for word in text.split(' ')]
print(words)

map_words=list(map(str.upper,text.split(' ')))
print(map_words)
