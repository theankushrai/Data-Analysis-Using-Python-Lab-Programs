
import numpy as npp
import numpy as np

a = np.array(10)

print("Print A= ", a)

b = np.array([11, 22, 33])

print("Print B= ", b)

addition = np.add(a, b)

print("After Addition =", addition)

sub = np.subtract(b, a)

print("After Subtraction =", sub)

mul = np.multiply(a, b)

print("After Multiplcation =", mul)

div = np.divide(b, a)

print("After Division =", div)

div1 = np.divide(b, 11)

print("After Division =", div1)


a = np.array([0.16, 3.33, 1, 133])

print(a)

rec = np.reciprocal(a)
print(rec)

a = np.array([9, 27, 81])

print(a)

pow = np.power(a, 3)
print("after ^3 = ", pow)


b = np.array([1, 2, 1])

pow1 = np.power(a, b)
print("after b array elements as ^ = ", pow1)

a = np.array([5, 15, 45])
b = np.array([2, 4, 6])

print("A=", a)
print("B=", b)

mm = np.mod(a, b)

rm = np.remainder(a, b)

print("MOD=", mm)
print("REMAINDER=", rm)

a = np.array([-1.6j, 0.3j, 10, 1+1j])
print(a)

print("real=", np.real(a))

print("imaginary=", np.imag(a))

print("Conjugate=", np.conj(a))

a = np.array([12.0, 4.6, 111, 0.56, 20.25, 52])

print(a)

print("after rounding up=", np.around(a))

print("after rounding up to 1st decimal value =", np.around(a, decimals=1))

a = np.array([6.0, -5.3, 100, -0.100, 25.5, 321])

print(a)

print('\n')

print(np.floor(a))

print(np.ceil(a))

np = np.array([1, 2, 3])
print(np)

a = npp.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(a)

a = np.zeros(3)
print(a)


ab = np.empty(2)
print(ab)

a = np.arange(7)
print(a)

a = np.arange(3, 9, 2)
print(a)

y = np.ones(2, dtype=int)
print(y)
y

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
print(arr)

a = np.array([1, 2, 3, 4, 5, 6, 7, 8])
print(a)


a = np.delete(a, 2)
print(a)

a = np.array([21, 42, 49, 1, 85, 67, 7, 81])
print(a)


a = np.sort(a)
print(a)

arr = np.array([[2, 4, 6], [1, 2, 4]])
a = arr.ndim
print(arr)
print("dimensions = ", a)

arr = np.array([[[2, 4, 5], [1, 2, 3]], [[10, 20, 30], [21, 42, 84]]])
a = arr.ndim
b = arr.size
print(arr)
print("dimensions = ", a)
print("size = ", b)

a = np.array(50)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(a)
print("dimension= ", a.ndim)
print(b)
print("dimension= ", b.ndim)
print(c)
print("dimension= ", c.ndim)
print(d)
print("dimension= ", d.ndim)

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

print(arr.shape)

a = np.arange(5)
print(a)

b = a.reshape(1, 5)
print(b)


def hello(str):
    print("in function   " + str)
    print("after printing in function definition")
    return


print("1")
print("2")
hello("AYUSHI")
hello("SINGH")
print("16")


def changeme(mylist):
    mylist.append([1, 2, 3, 4])
    print("Values inside the function: ", mylist)
    return


mylist = [11, 20, 3]
changeme(mylist)
print("Values outside the function: ", mylist)


def changeme(mylist):
    print("Values BEFORE CHANGES: ", mylist)
    mylist = [1, 2, 3, 4]
    print("Values AFTER CHANGES: ", mylist)
    return


mylist1 = [11, 20, 3]
changeme(mylist1)
print("Values outside the function: ", mylist1)


def printme(str):
    print(str)
    return


printme()


def printme(str):
    print(str)
    return


printme(str="MACAOOO")


def printinfo(name, age):
    print("Name: ", name)
    print("Age ", age)
    return


printinfo(age=22, name="NIK")


def printinfo(name, age):
    print("Name: ", name)
    print("Age ", age)
    return


printinfo("nik", 23)


def printinfo(name, age=16):
    print("Name: ", name)
    print("Age ", age)
    return


printinfo(age=22, name="nik")
printinfo(name="Nik")


def printinfo(arg1, *vartuple):
    print("Output: ")
    print("arg1==", arg1)
    for var in vartuple:
        print(var)
    return


printinfo(1, 2)
printinfo(70, 60, 50, 90)


def sum(arg1, arg2): return arg1 + arg2


print("Value of total : ", sum(1, 2))
print("Value of total : ", sum(2, 2))


def sum(arg1, arg2):
    total = arg1 + arg2
    print("Inside the function : ", total)
    return total


total1 = sum(10, 20)
print("Outside the function : ", total1)

total = 99


def sum(arg1, arg2):
    total = arg1 + arg2
    print("Inside the function local total : ", total)
    return total


sum(10, 20)
print("Outside the function global total : ", total)

dict = {'name': ' Ankush', 'designation': 'student',
        'qual': 'Btech', 'univ': 'cmr'}
print(dict['name'])


print(dict['qual'])

dict = {'name': 'Ankush', 'designation': 'student',
        'qual': 'Btech', 'univ': 'cmr'}

dict['name'] = 'singh'

print(dict['name'])

dict['class'] = 'cseA'

print(dict['class'])

dict = {'name': ' Ankush', 'designation': 'Student',
        'qual': 'Btech', 'univ': 'cmr'}


del dict['designation']

# print(dict['designation'])

dict.clear()

# print(dict['name'])

del dict

dict = {'name': '', 'designation': 'Student',
        'qual': 'Btech', 'univ': 'cmr', 'name': 'ABCD'}


print(dict['name'])

print(len(dict))

dict = {'name': 'Ankush', 'designation': 'Student',
        'qual': 'Btech', 'univ': 'cmr', 'name': 'ABCD'}


print(dict.values())

print(dict.items())

print(dict.keys())

dict = {'name': 'Ankush', 'designation': 'Student',
        'qual': 'Btech', 'univ': 'cmr', 'name': 'ABCD'}


print(dict['name'])

print(dict.get('edu', "nothing"))

dict = {'name': 'Ankush', 'designation': 'student',
        'qual': 'Btech', 'univ': 'cmr', 'name': 'ABCD'}


dict2 = dict.copy()

print(dict2['name'])

print(len(dict2))

dict = {'name': 'Ankush', 'designation': 'student',
        'qual': 'Btech', 'univ': 'cmr', 'name': 'ABCD'}


dict2 = {'edu': 'btech-mtech', 'students': '7sem'}

print(dict)
print(dict2)

dict.update(dict2)

print(dict)

tup = ('cse', 'it', 'mech')
print(tup)
tup1 = (1, 23, 4, 5, 5, 6)
print(tup1)
tup2 = "abc", "def"
print(tup2)

tup = ('cse', 'it', 'mech')
print(tup)
tup1 = (1, 23, 4, 5, 5, 6)
print(tup1)
tup2 = "abc", "def"
print(tup2)

tup1 = ()
print(tup1)

tup1 = (16)
print(tup1)

tup = ('cse', 'it', 'mech', 'ece', 'electrical')
print(tup[1])
print(tup[0])
print(tup[1:3])

tup1 = ('cse', 'it', 'mech', 'ece', 'electrical')
print(tup1)
tup2 = (' Ankush', 'siri', 'alexa')
print(tup2)


tup3 = tup1+tup2
print(tup3)

tup1 = ('cse', 'it', 'mech', 'ece', 'electrical')
print(tup1)
tup2 = ('Ankush', 'alexa', 'siri')
print(tup2)
a = len(tup1)
b = len(tup2)
print(a)
print(b)

print(len(tup1))

tup1 = ('cse', 'it', 'mech', 'ece', 'electrical')
print(tup1)
tup2 = ('Ankush', 'siri', 'alexa')
print(tup2)


print(max(tup1))

f = open("cse7sem1.txt", "a")
f.write("singh")
f.close()

# open and read the file after the appending:
f = open("cse7sem1.txt", "r")
print(f.read())

# Open a file
fo = open("cse7sem1.txt", "r+")

str = fo.read(10)
print("Read String is : ", str)  # Ankush---output

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
