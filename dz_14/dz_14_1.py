# data = [
# {'name': 'Test 1', 'position': 1},
# {'name': 'Test 2', 'position': 2},
# {'name': 'Test 3', 'position': 3},
# ]
#
# for obj in reversed(range(len(data))):
#     if data[obj]["position"] == 2:
#         del data[obj]
#     if data[obj]["position"] == 3:
#         data[obj]["position"] -= 1
# print(data)



# import copy
# data = copy.deepcopy(data)
def delete_item(obj, position):
    for obj in range(5):
        if data[obj][position]:
            del data[obj]
            return data
        if data[obj][position] == 3:
            data[obj][position] -= 1
print(delete_item(2,2))

# for obj in reversed(range(len(data))):
#     if data[obj]["position"] == 2:
#         del data[obj]
#     if data[obj]["position"] == 3:
#         data[obj]["position"] -= 1
# print(data)




# data_item()
#         for obj in data:
#                 if obj[position] == 2:
#                      data1.append(obj)
# print(data1)


# delete_chars = []
#     for i in range(len(a)):
#         value1 = a[i].get('value')
#         for j in range(i+1, len(a)):
#             value2 = a[j].get('value')
#             if value1 < value2:
#                 delete_chars.append(a[i])
#             else:
#                 delete_chars.append(a[j])
#
# a = [i for i in a if i not in delete_chars]


# def add_item(obj: list, position: int) -> list:
#     pass