data = [
{'name': 'Test 1', 'position': 1},
{'name': 'Test 2', 'position': 2},
{'name': 'Test 3', 'position': 3},
]

def add_position(list, position, pos):
    data1 = {'name': f'{pos} {len(list) + 1}', 'position': None}
    list.insert(position - 1, data1)

    for i, j in enumerate(list):
        j['position'] = (i + 1)
    return list

print(add_position(data, 1, 'Test'))



