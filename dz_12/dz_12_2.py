import json
A = {'key': 1, 'key1': True}
B = {'key': 'Hello'}

C = {}
for key in set(list(A.keys()) + list(B.keys())):

    try:
        C.setdefault(key,[]).append(A[key])
    except KeyError:
        pass

    try:
        C.setdefault(key,[]).append(B[key])
    except KeyError:
        pass
print(C)

json_user = json.dumps(C)
with open('result.json', 'w') as C:
    C.write(json_user)



