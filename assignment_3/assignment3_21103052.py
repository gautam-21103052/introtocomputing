
#que:-1
print("Program1")
input_string = input("Enter your text\n")
if (" " not in input_string):
    word_count = {}

    for i in input_string:
        word_count[i] = input_string.count(i)
    print(word_count)
else:
    print("The input string do not contain space.")


#ques2:-
print("Program2")
date = int(input("Day-"))
month = int(input("Month-"))
year = int(input("Year-"))

if (year%4==0):
    if (year%400==0):
        leap_yr = True
    elif (year%100!=0):
        leap_year = True
else:
    leap_year = False

def last_date(month):
    if (month%2==1):
        if (month<=7):
            last_date = 31
        if (month>7):
            last_date = 30
    if (month%2==0 and month!=2):
        if (month<=7):
            last_date= 30
        if (month>7):
            last_date = 31
    if (month==2):
        if leap_yr==True:
            last_date = 29
        if leap_yr==False:
            last_date = 28
            if dt==29:
                print("Invalid Input. Please try again!")
    return last_date

if (1<=month and month<=12 and 1<=date and date<=31 and 1800<=year and year<=2025):
    if (date<=last_date(month)):
        if (date==last_date(month) and month!=12):
            dt = 1
            month = month+1
        elif (date==31 and month==12):
            dt = 1
            month = 1
            year = year+1
        else:
            date = date+1
        print(f"Next date is: {date}/{month}/{year}")
else:
    print("Error!! Not in Range.")


#ques3:-
print("Program3")
my_list = [3, 9, 10]
sq_list = []
for i in my_list:
    sq_tup = (i, i**2)
    sq_list.append(sq_tup)
print(sq_list)


#Ques4:-
print("Program4")
grd_pt = int(input("Grade:- "))
print("For Grade", grd_pt, "Output is:")
if (grd_pt>=4 and grd_pt<=10):
    if (grd_pt == 4):
        ltr_grd = "D"
        perf = "poor"
    elif (grd_pt == 5):
        ltr_grd = "C"
        perf = "below average"
    elif (grd_pt == 6):
        ltr_grd = "C+"
        perf = "average"
    elif (grd_pt == 7):
        ltr_grd = "B"
        perf = "good"
    elif (grd_pt == 8):
        ltr_grd = "B+"
        perf = "very good"
    elif (grd_pt == 9):
        ltr_grd = "A"
        perf = "excellent"
    elif (grd_pt == 10):
        ltr_grd = "A+"
        perf = "outstanding"
    print(f"Your Grade is '{ltr_grd}' and {perf} performance.")

else:
    print("Error!! Grade is out of range.")

#que5:-
print("Program5")
n = 11

a2z = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for i in range(n):
    if 2*i<n:
        j = a2z[:n-2*i]

        print(" "*i, j)


#ques6:-
print("Program6")
#By default 1st run
repeat="Y"
#Intially empty dictionary
dic={}
dic2={}
list_sid=[]
#List containing Y or N
liste=["Y","y","n","N"]
#Main code
while repeat=="Y" or repeat=="y":
    #Taking input name and sid
    name = str(input("Enter student name:"))
    sid = int(input("Enter student SID:"))
    while sid in list_sid:
        print("\nThis SID is already entered:\nPlease enter unique SID\n")
        sid=int(input("Enter student SID:"))
    list_sid.append(sid)
    while sid<0:
        print("\nError\nSID can't be negative\n")
        sid=int(input("Enter student SID:"))
    else:
        # Updating dic with 'sid':'name'
        dic.update({sid: name})
        # updating dic 2 with 'name':'sid'(will be helpful while sorting)
        dic2.update({name:sid})
        # Asking if want to enter more input or not
        repeat = str(input("Enter Y to continue or N to end:"))
    if repeat=="N" or repeat=="n":
        break
    while (not (repeat in liste)):
        print("\nError\nPlease enter valid input['Y' or 'N']")
        repeat=str(input("\nEnter Y to continue or N to end:"))

# a
#printing the dictionary
print("\nQ.6(a)")
print("The Dictionary containing {'SID':'Name'} is shown below")
print(dic)
# b
#sorting according to name
print("\nQ.6(b)")
list_k=sorted(dic2)
dic3={}
for ele in list_k:
    dic3.update({dic2.get(ele):ele})
print("The Dictionary after sorting according to name:")
print(dic3)

# c
#sorting according to SID
print("\nQ.6(c)")
sort_dic = sorted(dic)
dic4 = {}
for va in sort_dic:
    dic4.update({va: dic.get(va)})
print("The Dictionary after sorting according to SID:")
print(dic4)
# d
print("\nQ.6(d)")
# Taking input SID to be searched
enter_sid = int(input("Enter SID to get name of student:"))
# Searching for sid as key in dic
output_name = str(dic.get(enter_sid))
# printing name with key sid
print(f"Name of student with SID {enter_sid} is {output_name}.")


#ques7:-
print("Program7")
def fibo(n):
    if n==1 or n==2:
        return 1

    return fibo(n-1)+fibo(n-2)

n = int(input("Enter n\n"))

j = 0

for i in range(1, n+1):
    print(f"{fibo(i)}", end = ",")
    j = j+fibo(i)

print(end = "\n")
print(j/n)

#ques8:-
print("Program8")
set1 = {1, 2, 3, 4, 5}
set2 = {2, 4, 6, 8}
set3 = {1, 5, 9, 13, 17}

set_a = (set1 | set2) - (set1 & set2)
print("part a:", set_a)

set_b = (set1 | set2 | set3) - (set1 & set2) - (set2 & set3) - (set3 & set1)
print("part b:", set_b)

set_c  =(set1 & set2) | (set2 & set3) | (set3 & set1) | (set1 & set2 & set3)
print("part :", set_c)

set4 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
# Elements in Range (1, 10) but not in Set1
set_d = set4 - set1
print("part d:", set_d)

# Elements in Range (1, 10) but not in Set1, Set2 and Set3
set_e = set4 - (set1 | set2 | set3)
set_esorted = sorted(set_e)
print("part e:", set_esorted)

