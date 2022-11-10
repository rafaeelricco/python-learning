# More about strings 📖

name = input("What is your name? ")
print(f"Hello {name}")  # Hello John Doe

print("How to work index in string?")
# B E N J A M I N
# 0 1 2 3 4 5 6 7

name = "Benjamin"
print(name[0])  # B
print(name[1])  # E
print(name[2])  # N
print(name[3])  # J
print(name[4])  # A
print(name[5])  # M
print(name[6])  # I
print(name[7])  # N

print("How to work negative index in string?")
# B E N J A M I N
# 0 1 2 3 4 5 6 7
# -8 -7 -6 -5 -4 -3 -2 -1

name = "Benjamin"
print(name[-8])  # B
print(name[-7])  # E
print(name[-6])  # N
print(name[-5])  # J
print(name[-4])  # A
print(name[-3])  # M
print(name[-2])  # I
print(name[-1])  # N

print("How to work slice in string?")
# B E N J A M I N
# 0 1 2 3 4 5 6 7
# -8 -7 -6 -5 -4 -3 -2 -1

name = "Benjamin"
print(name[0:3])  # Ben
print(name[0:4])  # Benj
print(name[0:5])  # Benja
print(name[0:6])  # Benjam
print(name[0:7])  # Benjamin


print("How to use len() function?")

name = "Benjamin"
print(len(name))


print("How to while in string?")

name = "Benjamin"
i = 0
while i < len(name):
    print(name[i])
    i += 1
