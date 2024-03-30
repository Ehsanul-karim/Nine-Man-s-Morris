mills = [(0,1,2), (3,4,5), (6,7,8), (9,10,11), (12,13,14), (15,16,17), (18,19,20), (21,22,23),
         (0,9,21), (3,10,18), (6,11,15), (1,4,7), (16,19,22), (8,12,17), (5,13,20), (2,14,23)]

move = 6
temp_available_spaces = []

for position in mills:
    if move in position:
        for element in position:
            print(position.index(element))
            print(position.index(move))
            if abs(element - move) == 1:
                temp_available_spaces.append(element)

print(temp_available_spaces)