# 📂 List: lists are mutable. They can be changed.

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # List

print(x[5])  # 6

# 📂 List Methods:

x.append(11)  # append method: adds an element at the end of the list
print(x)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

x.clear()  # clear method: removes all the elements from the list
print(x)  # []

x.copy()  # copy method: returns a copy of the list
print(x)  # []

x.count(1)  # count method: returns the number of elements with the specified value
print(x)  # []

# extend method: add the elements of a list (or any iterable), to the end of the current list
x.extend([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(x)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# index method: returns the index of the first element with the specified value
x.index(5)
print(x)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

x.insert(0, 0)  # insert method: adds an element at the specified position
print(x)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

x.pop()  # pop method: removes the element at the specified position
print(x)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

x.remove(0)  # remove method: removes the first item with the specified value
print(x)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

x.reverse()  # reverse method: reverses the order of the list
print(x)  # [9, 8, 7, 6, 5, 4, 3, 2, 1]

x.sort()  # sort method: sorts the list
print(x)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
