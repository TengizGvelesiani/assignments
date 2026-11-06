subjects = {
    'math': {'George': 85, 'Salome': 78, 'David': 92},
    'physics': {'George': 90, 'David': 75, 'Salome': 88},
    'chemistry': {'David': 82, 'George': 80, 'Salome': 91}
    }
ans = {}

for key, value in subjects.items():
    for k, v in value.items():
        if k not in ans:
            ans[k] = {key: v}
        else:
            ans[k][key] = v

for k, v in ans.items():
    print(k, v)
