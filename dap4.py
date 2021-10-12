

dict = {'name': 'Ankush', 'designation': 'student',
        'unqual': 'btech', 'univ': 'cmr'}
print(dict['name'])


print(dict['unqual'])

dict = {'name': '', 'designation': 'student',
        'unqual': 'btech', 'univ': 'cmr'}
dict['name'] = 'singh'

print(dict['name'])

dict['class'] = 'cse7semA'

print(dict['class'])

dict = {'name': 'Ankush', 'designation': 'student',
        'unqual': 'btech', 'univ': 'cmr'}
del dict['designation']
dict.clear()
del dict

dict = {'name': 'Ankush', 'designation': 'student',
        'unqual': 'btech', 'univ': 'cmr'}
print(dict['name'])

print(len(dict))

dict = {'name': 'Ankush', 'designation': 'student',
        'unqual': 'btech', 'univ': 'cmr', 'name': 'aayu'}

print(dict.values())

print(dict.items())

print(dict.keys())

dict = {'name': 'Ankush', 'designation': 'student',
        'unqual': 'btech', 'univ': 'cmr', 'name': 'aayu'}
print(dict['name'])

print(dict.get('abc', "YOYOYO"))

dict = {'name': 'Ankush', 'designation': 'student',
        'unqual': 'btech', 'univ': 'cmr', 'name': 'aayu'}
dict2 = dict.copy()

print(dict2['name'])

print(len(dict2))

dict = {'name': 'Ankush', 'designation': 'student',
        'unqual': 'btech', 'univ': 'cmr', 'name': 'aayu'}
dict2 = {'edu': 'btech-mtech', 'students': '7sem'}

print(dict)
print(dict2)

dict.update(dict2)

print(dict)

"""***TUPLES***

"""

tup = ('cse', 'EC', 'mech')
print(tup)
tup1 = (1, 2, 4, 3, 5, 6, 9, 10)
print(tup1)
tup2 = "xyz", "fgh"
print(tup2)

tup1 = (633)
print(tup1)

tup = ('cse', 'EC', 'civil', 'electrical')
print(tup[1])
print(tup[3])
print(tup[2:5])

tup1 = ()
print(tup1)

tup1 = ('cse', 'it', 'civil', 'ece', 'electrical')
print(tup1)
tup2 = ('Ankush', 'aayu', 'aay')
print(tup2)


tup3 = tup1+tup2
print(tup3)

tup1 = ('cse', 'it', 'civil', 'ece', 'electrical')
print(tup1)
tup2 = ('Ankush', 'singh', 'aay')
print(tup2)
a = len(tup1)
b = len(tup2)
print(a)
print(b)

print(len(tup1))
print(len(tup2))

tup1 = ('cse', 'it', 'civil', 'ece', 'electrical')
print(tup1)
tup2 = ('Ankush', 'singh', 'aayu')
print(tup2)


print(max(tup1))

"""***FILES***

"""

print("Python is A USER FRIENDLY language,", "isn't it?")

str = input("Enter your input: ")
print("Received input is : ", str)

# Open a file
fo = open("cseA7.txt", "ab")
print("Name of the file: ", fo.name)

# Close opend file
fo.close()

f = open("cse7sem7.txt", "a")
f.write("aayu")
f.close()

# open and read the file after the appending:
f = open("cse7sem7.txt", "r")
print(f.read())

# Open a file
fo = open("cse7sem7.txt", "r+")
str = fo.read(20)
print("Read String is : ", str)
# Close opend file
fo.close()

fo = open("cse7sem7.txt", "wb")
print("Name of the file: ", fo.name)
print("Closed or not : ", fo.closed)
print("Opening mode : ", fo.mode)

# Open a file
fo = open("cseA7.txt", "r+")

str = fo.read(20)
print("Read String is : ", str)

# Check current position
position = fo.tell()
print("Current file position : ", position)

# Reposition pointer at the beginning once again
position = fo.seek(1, 0)
str = fo.read(7)
print("Again read String is : ", str)

ptr = fo.seek(0, 1)
str1 = fo.read(3)
print("my new string= ", str1)

# Close opened file
fo.close()

f = open("cse7sem1.txt", "a")
f.write("Ankush")
f.close()

# open and read the file after the appending:
f = open("cse7sem1.txt", "r")
print(f.read())

# Open a file
fo = open("cse7sem1.txt", "r+")
str = fo.read(20)
print("Read String is : ", str)
# Close opend file
fo.close()

# Open a file
fo = open("cse7sem1.txt", "r+")

str = fo.read(10)
print("Read String is : ", str)

# Check current position
position = fo.tell()
print("Current file position : ", position)

# Reposition pointer at the beginning once again
position = fo.seek(1, 0)
str = fo.read(7)
print("Again read String is : ", str)

ptr = fo.seek(0, 1)
str1 = fo.read(3)
print("my new string= ", str1)

# Close opened file
fo.close()
