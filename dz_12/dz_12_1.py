import pickle
users = [
    {
        'name': 'Petr',
        'password': 'petr123',
    },
    {
        'name': 'Vasya',
        'password': '@3RS445'
    }
    ]
f = open('python.txt', 'wb')
pickle.dump(users, f)
f.close()




