x = {'a': 1, 'b': 2}
# result = [('Статус', 'Количество'), ]
# k = (list(x.items()))
result = [('Статус', 'Количество'), ] + list(x.items()) + [('Total', 'hi')]
# result += list(x.items())
print(result)
a, b = 3, 4
c = (a +
b)

print(c)

