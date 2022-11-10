# ⛓ Chained conditionals: Python provides an alternative way to write nested selection such as the one shown in the previous section.

x = 10
y = 20

result1 = x == y
result2 = x > y
result3 = x < y

result4 = result1 and result2
result5 = result1 or result2
result6 = not result1

print(result1)  # False
print(result2)  # False
print(result3)  # True
print(result4)  # False
print(result5)  # False
print(result6)  # True
