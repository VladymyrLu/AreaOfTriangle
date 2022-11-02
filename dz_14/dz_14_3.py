data = [
{'name': 'Test 1', 'position': 1},
{'name': 'Test 2', 'position': 2},
{'name': 'Test 3', 'position': 3},
]


def change_position(list, position1, position2):
    list.insert(position1 - 1, list[position2 - 1])
    list.pop(position2)
    list.insert(position2, list[position1])
    list.pop(position1)

    for i, j in enumerate(list):
        j['position'] = (i + 1)
    return list


print(change_position(data, 1, 3))

