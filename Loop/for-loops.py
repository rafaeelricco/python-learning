# 🔂 For Loops: for loops are used to iterate over a sequence (list, tuple, string) or other iterable objects.

for i in range(1, 11):
    print(i)

# Output:
# 1
# 2
# 3
# 4
# 5
# ...


# range(start, stop, step)
# start: start of the range
# stop: end of the range
# step: step size

for iterator in range(1, 11, 2):
    print(iterator)


# How to loop functions?
yourFunction = 0
[yourFunction() for _ in range(50)]  # repeat 50 times
