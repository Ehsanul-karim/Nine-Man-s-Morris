temp_available_spaces = [[481, 399], [582, 387]]
closest_pos = [481, 399]

if any(pos == closest_pos for pos in temp_available_spaces):
    print("closest_pos is in temp_available_spaces")
else:
    print("closest_pos is not in temp_available_spaces")