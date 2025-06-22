def dump(**kwargs):
    return kwargs

output = dump(**{'x': 1}, y=2, **{'z': 3})

print(output)
# {'x': 1, 'y': 2, 'z': 3}

# later occurrences overwrite! see z
output2 = {'a': 0, **{'x': 1}, 'y': 2, **{'z': 3, 'x': 4}}

print(output2)
# {'a': 0, 'x': 4, 'y': 2, 'z': 3}