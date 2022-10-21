import json
A = {'key': 1, 'key1': True}
B = {'key': 'Hello'}

for k, v in B.items():
    if A.get(k):
         A[k] = [A[k], v]
    else:
        A[k] = v
print(A)

json_user = json.dumps(A)
with open('result.json', 'w') as A:
    A.write(json_user)
A.close()





