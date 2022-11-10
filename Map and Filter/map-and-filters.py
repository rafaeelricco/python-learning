# 🗺 Map and Filters: Map and Filters are two of the most useful functions in Python. They are used to transform data in a list. Sintax: map(function, list) and filter(function, list)

x = [1, 2, 3, 4, 5]

mp = map(lambda x: x * 2, x)
print(list(mp))  # Output: [2, 4, 6, 8, 10]

fl = filter(lambda x: x % 2 == 0, x)
print(list(fl))  # Output: [2, 4]
