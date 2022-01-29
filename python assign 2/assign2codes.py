print("Prog.1")
"""
1. For a given input string “Python is a case sensitive language”. Write python
code for the following:
a. Find the length of the input string.
"""
str1 = "Python is a case sensitive language"
print(len(str1))

# b. Reverse the order of the string in one line code.
str1 = "Python is a case sensitive language"
print(str1[::-1])

# c. Using Slice function store “a case sensitive” in new string.
str1 = "Python is a case sensitive language"
str2 = str1[10:26]
print(str2)

# d. Replace “a case sensitive” with “object oriented”.
str1 = "Python is a case sensitive language"
print(str1.replace("a case sensitive", "object oriented"))

# e. Find index of substring “a” in the given input string.
str1 = "Python is a case sensitive language"
print(str1.find("a"))

# f. Remove the white spaces from the given input string.
str1 = "Python is a case sensitive language"
#to replace white spaces we can replace spaces with blank
print(str1.replace(" ", ""))

print("Prog.2")
"""
2. Store your name, SID, department name and CGPA into different variables.
With the help of String formatting print the following output:
Hey, ABC Here!
My SID is 2110XXXX
I am from XYZ department and my CGPA is 9.9
"""
#input name,sid,course and cgpa from the user
inp_name = input("Hi Pecian, Please enter your name\n")
inp_SID = input("Please enter you SID[eg.2110XXXX]\n")
inp_course = input("Please enter your department[eg.CSE,ECE,ELE,etc.]\n")
inp_CGPA = input("Please enter your CGPA[eg.5.5,9.0,10.0]\n")

print("Hey,",inp_name, "Here!")
print("My SID is", inp_SID)
print("I am from", inp_course, "department and my CGPA is", inp_CGPA)

print("Prog.3")
"""
3. For a=56 and b=10 with the help of bitwise operators calculate the following:
a. a&b
b. a|b
c. a^b
d. Left shift both a and b with 2 bits.
e. Right shift a with 2 bits and b with 4 bits.
"""
a=56
b=10
#3a
print(a&b)
#3b
print(a|b)
#3c
print(a^b)
#3d left shift both by 2
print(a<<2)
print(b<<2)
#3e right shift a by 2 and b by 4
print(a>>2)
print(b>>4)


print("Prog.4")
"""
4. Write a python program to find the greatest of three numbers entered by the
user.
"""
#input 3 numbers
n1 = int(input("Enter the first number\n"))
n2 = int(input("Enter the second number\n"))
n3 = int(input("Enter the third number\n"))

#check if n1 is greater than n2 and similarly ahead for the same
if n1>n2:
    if n1>n3:
        print("The greatest of three numbers is", n1)
    else:
        print("The greatest of three numbers is", n3)
elif n1<n2:
    if n2>n3:
        print("The greatest of three numbers is", n2)
    else:
        print("The greatest of three numbers is", n3)


print("Prog.5")
"""
5. Write a python program to check if the word “name” is present in the string
entered by the user (Print : “Yes” or “No”).
"""
#firstly take the input string
inp_str = input("Enter your string\n")
#now find the string using 'in' function
if "name" in inp_str:
#print yes or no
    print("Yes")
else:
    print("NO")


print("Prog.5")
"""
6. For any three lengths, there is a simple test to see if it is possible to form a
triangle. If any of the three lengths is greater than the sum of the other two,
then you cannot form a triangle. Otherwise, Enter three sides of a triangle,
converts them to integers, and to check whether the given input lengths can
form a triangle or not (Print : “Yes” or “No”).
"""
#firstly input three numbers
a = int(input("Enter first length\n"))
b = int(input("Enter second length\n"))
c = int(input("Enter third length\n"))
#now check one by one that any of the three lengths is greater than the sum of the other two or not
if a+b<=c or a+c<=b or c+b<=a:
    print("No")
else:
    print("Yes")