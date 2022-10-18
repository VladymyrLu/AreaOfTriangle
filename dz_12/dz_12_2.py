import json
A = {'key': [1], 'key1': [True]}
B = {'key': ['Hello']}

for k, v in B.items():
    if k in A:
        A[k].extend(v)
    else:
        A[k] = v
print(A)


json_user = json.dumps(A)
print(json_user)

with open('result.json', 'w') as A:
    A.write(json_user)

