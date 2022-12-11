#  Logic Operators: are used to combine conditional statements.

# Principle logic operators:
#  and: returns True if both statements are true
#  or: returns True if one of the statements is true
#  not: reverses the result, returns False if the result is true

# Principle comparison operators:
#  ==: equal to
#  !=: not equal to
#  >: greater than
#  <: less than
#  >=: greater than or equal to
#  <=: less than or equal to

# Tip: empty values, such as (), [], {}, "", the value None, and the number 0, evaluate to False. Other values are True.

x = 5
y = 3

#  and
print(x > 3 and x < 10)  # True

#  or
print(x > 3 or x < 4)  # True

#  not
print(not (x > 3 and x < 10))  # False

#  in
print(x in [1, 2, 3])  # False

#  not in
print(x not in [1, 2, 3])  # True

#  is
print(x is y)  # False

#  is not
print(x is not y)  # True

# E Operator: is used to check if a value is equal to another value.

#  ==: equal to
print(x == y)  # False

#  !=: not equal to
print(x != y)  # True

#  >: greater than
print(x > y)  # True

#  <: less than
print(x < y)  # False

#  >=: greater than or equal to
print(x >= y)  # True

#  <=: less than or equal to
print(x <= y)  # False
