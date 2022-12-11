# 🎭 Identity Operators: are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location.


x = ["apple", "banana"]
y = ["apple", "bana"]
z = x

print(x is z)  # return True because z is the same object as x
print(x is not y)  # return True because x is not the same object as y
print(x == y)  # True

# Tip: Two objects with non-overlapping lifetimes may have the same value, but they are not the same object.
