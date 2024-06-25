my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
index = 0
list_length = len(my_list)
while index < list_length:
    current_value = my_list[index]

    if current_value < 0:
        break
    if current_value == 0:
        index += 1
        continue
    print(current_value)
    index += 1