# 🔖 List Comprehension: create a new(copy) list with the results of a for loop or a function.

# Sintax: [expression for item in iterable if condition == True]

fruits = ["apple", "banana", "cherry", "kiwi", "mEngo"]
newlist = []

for x in fruits:
    if "a" in x:
        newlist.append(x)

print(newlist)
