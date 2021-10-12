
var1 = 'Hello World!'
var2 = "dap Programming"
print(var1," ",var2)

var1 = 'Hello World!'
var2 = "Python world"

print (var1[0])



print (var2[1:4])



var1 = 'Hello earth!'
print ("Updated String :- ", var1[0:6] + 'cmr')

str1 = input("Please Enter Your Own String : ")

str2 = str1
str3 = str1[:]
str4 = str1[2:6]

print("The Final String : Str2  = ", str2)
print("The Final String : Str3  = = ", str3)
print("The Final String : Str4  = = ", str4)

#Python String capitalize() method returns a copy of the string with only its first character capitalized.
str = "this is string example" 
print ("str.capitalize() : ", str.capitalize())

#count() returns the number of occurrences of substring sub in the range [start, end]. 

#str.count(sub, start= 0,end=len(string))

str = "this is string example.!" 

sub = "i" 
print ("str.count(sub, 4, 40) : ", str.count(sub, 4, 40))
sub = "wow" 
print ("str.count(sub) : ", str.count(sub))

#find() determines if string str occurs in string, or in a substring of string if starting index beg and ending index end are given.

#str.find(str, beg=0, end=len(string))

str1 = "this is string example..!!" 
str2 = "string" 

print (str1.find(str2))
print (str1.find(str2, 10))
print (str1.find(str2, 40))

#index() determines if string str occurs in string or in a substring of string if starting index beg and ending index end are given.

str1 = "this is string example....wow!!!" 
str2 = "examp" 

print (str1.index(str2))
print (str1.index(str2, 10,32))

#isalnum() checks whether the string consists of alphanumeric characters.

str = "this2020"   # No space in this string
print (str.isalnum())

str = "this is string example." 
print (str.isalnum())

str = "CMRuni"   # No space & digit in this string
print (str.isalpha())

str = "this is string example" 
print (str.isalpha())

str = "1236"   # Only digit in this string
print (str.isdigit())

str = "this is string example." 
print (str.isdigit())

str = "THIS is striNG example!"  
print (str.islower())

str = "this is string example....wow!!!" 
print (str.islower())

str = "this2021"   
print (str.isnumeric())

str = "12242183" 
print (str.isnumeric())

str = "  "  
print (str.isspace())

str = "This is string example." 
print (str.isspace())

str = "THIS IS STRING EXAMPLE....WOW!!!"  
print (str.isupper())

str = "THIS is string example....wow!!!" 
print (str.isupper())



#join() returns a string in which the string elements of sequence have been joined by str separator.

s = "  *  *  " 
seq = ("adk", "tttt", "qwerqe")  # This is sequence of strings.
print (s.join( seq ))

str = "this is string example!" 
print ("string length: ", len(str))

#lstrip() returns a copy of the string in which all chars have been stripped from the beginning of the string (default whitespace characters)

str = "     this is string example.     " 
print (str.lstrip())
str = "88888888this is string example....wow!!!999999" 
print (str.lstrip('8'))
print (str.rstrip('9'))

str = "THIS IS STRING EXAMPLE....WOW!!!" 
print (str.lower())

#returns largest character
str = "check" 
print ("Max character: " + max(str))

str = "abdurrrrrrrrr!" 
print ("Max character: " + max(str))

str = "this-is-real-string-example...!!!" 
print ("Min character: " + min(str))

str = "this-is-a-string-example...!!" 
print ("Min character: " + min(str))

#str.replace(old, new[, max])

str = "this is string example... this is really string"
print (str.replace("string", "was"))
print (str.replace("function", "was", 3))

str = "this is string example.." 
print (str.startswith( 'this' ))
print (str.startswith( 'is', 2, 4 ))
print (str.startswith( 'this', 2, 4 ))

str = "this is string example!" 
print ("str.capitalize() : ", str.upper())

str = "this is string example" 
print (str.swapcase())

str = "THIS IS STRING EXAMPLE!" 
print (str.swapcase())

"""***LISTS***"""

list1 = ['physics', 'chemistry', 2001, 2010] 
list2 = [1, 2, 3, 4, 5, 6, 7 ] 
print ("list1[0]: ", list1[2])
print ("list2[1:5]: ", list2[1:3])

list = ['physics', 'chemistry', 1997, 2090] 
print ("Value available at index 2 : ")
print (list[2])
list[2] = 999 
print ("New value available at index 2 : ")
print (list[2])

list1 = ['physics', 'chemistry', 1997, 2000] 
print (list1)
del (list1[2]) 
print ("After deleting value at index 2 :")
print (list1)

list1, list2 = [123, 'xyz', 'HANDM'], [456, 'abc']
print ("First list length : ", len(list1))
print ("Second list length : ", len(list2))

aList = [123, 'xYz', 'BAMBOO', 'abD'] 
aList.append( 2009 ) 
print ("Updated List : ", aList)

aList = [123, 'xyz', 'xyz', 'abc', 123] 
print ("Count for xyz : ", aList.count('xyz'))
print ("Count for NIKE : ", aList.count('NIKE'))

aList = [123, 'xyyzz', 'nike', 'abcd', 123] 
bList = [2010, 'cmr'] 
aList.extend(bList)
print ("Extended List : ", aList)

aList = [123, 'xyz', 'nike', 'abc', 'nike'] 
print ("Index for xyz : ", aList.index( 'xyz' ) )
print ("Index for nike : ", aList.index( 'nike' ) )

aList = [123, 'xyz', 'zara', 'abc']
aList.insert( 3, 2009)
print ("Final List : ", aList)

aList = [123, 'abc', 'nike', 'abc'] 

print(aList)

print ("List after popping last element : ", aList.pop())

print(aList)

print ("List after popping element from mentioned index: ", aList.pop(2))

print(aList)

aList.insert(3, 2009)

print(aList)

aList = [123, 'xyz', 'zara', 'abc', 'xyz']
aList.remove('xyz')
print ("List : ", aList)
aList.remove('abc')
print ("List : ", aList)

aList = ['cmruni', 'xyz', 'hackurr', 'abc', 'hiive']
aList.reverse()
print ("List : ", aList)

aList = ['cmr', 'reva', 'so', 'all', 'five']
aList.sort()
print ("List : ", aList)

"""***LOOPS_BREAK_CONTINUE_PASS***"""

str = "computer"  
for i in str:  
        print(i)

list = [1,2,3,4,5,6,7,8,9,10]  
n = 3 
for i in list:  
        c = n*i  
        print(n," *",i, " =", c)

list = [110,320,232,433,653,12]  
sum = 0  
for i in list:  
        sum = sum+i  
print("The sum is:",sum)

for i in range(14):  
        print(i,end=' ')

n = int(input("Enter the number "))  
for i in range(1,11):  
        c = n*i  
        print(n,"*",i,"=",c)

n = int(input("Enter the number "))  
for i in range(2,n,2):  
        print(i)

list = ['Peter','pan','vicky','bhavansh']  
for i in range(len(list)):  
        print("bye",list[i])

for i in range(0,4):    
        print(i)    
else:  
        print("the loop completely exhausted, since there is no break.")

for i in range(0,3):    
        print(i)    
        print("bye")
        continue     
        print("hello")
else:print("for loop is exhausted")     
print("The loop is broken due to break statement")

# prints all letters except 'a' and 't'   
i = 0  
str1 = 'tittat'  
print(str1)
while i < len(str1):
        print('entered while loop before if statement')
        if str1[i] == 'a' or str1[i] == 't':   
            print('entered if statement')
            i += 1  
            print('i incremented')
            continue  
            print('after continue')
        print('Current Letter :', str1[i])   
        i += 1 
        print('going back to starting of while loop')

i = 0  
str1 = 'cmruni'  
  
while i < len(str1):   
    if str1[i] == 'n':   
        i += 1  
        break  
    print('Current Letter :', str1[i])   
    i += 1

#The pass statement is used to declare the empty loop. 
#It is also used to define empty class, function, and control statement.

str1 = 'hellomotoo!'  
i = 0  
  
while i < len(str1):   
    i += 1  
    pass  
print('Value of i :', i)

i=1  
    #The while loop will iterate until condition becomes false.  
while(i<=6):    
        print(i)   
        i=i+1

i=1    
number = int(input("Enter the number:"))    
while i<=10:    
        print("%d X %d = %d \n"%(number,i,number*i))    
        i = i+1

while (1):    
    print("Hi! we are inside the infinite while loop")

i=1   
while(i<=5):    
    print(i)    
    i=i+1    
else:  
    print("The while loop exhausted")

i=1    
while(i<=3):    
    print(i)    
    i=i+1    
    if(i==3):    
        break   
else:  
    print("The while loop exhausted")
print("bye bye")

list =[1,2,3,4]  
i=1
count = 1   
for i in list:  
        if i == 4:  
            print("item matched")  
            count = count + 1   
            break  
print("found at",count,"location") 

str = "cmruni"  
for i in str:  
        if i == 'o':  
            break  
        print(i)

n=2  
while 1:  
        i=1   
        while i<=10:  
            print("%d X %d = %d\n"%(n,i,n*i))   
            i = i+1   
        choice = int(input("Do you want to continue printing the table, press 0 for no?"))  
        if choice == 0:  
            break       
        n=n+1

i = 0                     
while(i < 5):                
       i = i+1  
       if(i == 5):  
          continue  
       print(i)

list = [1,2,3]    
flag = 0    
for i in list:    
        print("Current element:",i,end=" ")     
        if i==3:    
            pass    
            print("\nWe are inside pass block\n")     
            flag = 1    
        if flag==1:    
            print("\nCame out of pass\n")     
            flag=0

for i in [1,2,3,4,5]:   
        if(i==4):  
            pass  
            print("This is pass block",i)  
        print(i)