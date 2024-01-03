notes = [10, 11, 12, 15, 12, 13]
for i in range(len(notes)):
    notes[i] += 2
print(notes)

# faire la meme chose avec map
marks = [10, 11, 12, 15, 12, 13]
marksTwo = map(lambda x: x + 2, marks)
print(list(marksTwo))


