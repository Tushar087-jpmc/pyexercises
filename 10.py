letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]

for index,position in enumerate(letters):
    if index % 2 == 0:
        print(index, position)

# letters = [position for index, position in enumerate(letters) if index % 2 == 0]
# print(letters)

print(letters[::2])