data = input()
row = int(ord(data[0])) - int(ord('a')) + 1
col = int(data[1])

move_types = [
    (2, -1), (2, 1),
    (1, -2), (1, 2),
    (-1, -2), (-1, 2),
    (-2, -1), (-2, 1)
]

count = 0

for move in move_types:
    nrow = row + move[0]
    ncol = col + move[1]

    if nrow < 1 or ncol < 1 or nrow > 8 or ncol > 8:
        continue

    count += 1

print(count)
