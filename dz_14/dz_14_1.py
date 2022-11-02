data = [
{'name': 'Test 1', 'position': 1},
{'name': 'Test 2', 'position': 2},
{'name': 'Test 3', 'position': 3},
]
def remove_item(item, position):
    item.pop(position - 1)
    for i, j in enumerate(item):
        j['position'] = (i + 1)
    return item


print(remove_item(data, 2))
