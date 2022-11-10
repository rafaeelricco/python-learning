# 📖 Dictionary: is a collection of key-value pairs. Is a very similar with real dictionaries, on search a word you get the definition of that word.

thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
print(thisdict)  # {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}

# 📓 Dictionary Methods:

thisdict.clear()  # clear the dictionary

thisdict.copy()  # copy the dictionary

thisdict.fromkeys()  # returns a dictionary with the specified keys and values

thisdict.get()  # returns the value of the specified key

thisdict.items()  # returns a list containing a tuple for each key value pair

thisdict.keys()  # returns a list containing the dictionary's keys

thisdict.pop()  # removes the element with the specified key

thisdict.popitem()  # removes the last inserted key-value pair

# returns the value of the specified key. If the key does not exist: insert the key, with the specified value
thisdict.setdefault()

thisdict.update()  # updates the dictionary with the specified key-value pairs

thisdict.values()  # returns a list of all the values in the dictionary
