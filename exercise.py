# print("\nHello world")
# x = input("enter value " )
# print(x)



# if else exercise solution by me/////////////////////////////////////////////////////////
# price = 1000000
# good_credit = 200000
# buyer_credit = int(input("the buyers credit is"))
# if buyer_credit > good_credit:
#     down_credit = (10 / 100) * price
#     print("\nBuyer needs to put down the credit of 10% which is: ", down_credit)
# else:
#     down_credit = (20 / 100) * price
#     print("\nBuyer needs too put down the credit of 20% which is: ", down_credit)



# comparison operator exercise sol by me///////////////////////////////////////////////////
# name = input("enter your name: ")
# print("name character length is: ",len(name))

# if len(name) > 50:
#     print("name can be a max of 50 char")
# elif len(name) < 3:
#     print("name can be min of 3 char")
# else:
#     print("name looks fine")


# list exercise remove duplicate using "set" method//////////////////////////////////////////
# lists = [1,1,2,3,4,2,5,4,6,7,7,6]
# lists = set(lists)
# print(lists)



# packedges in python
# from Ahmar_test_python import payment, shipping
# payment.cal_pay()
# shipping.calc_shipping()



# import random
# for i in range(3):
#     print("\n",random.randint(0, 69))


# type converstion

# a = (input("Enter your birth year: "))
# b = int(a)-2024
# print (b)

# 
# aa = 20
# bb = 10
# bb += aa
# print (bb)
# bb -= aa
# print (bb)

# a = True
# b = True

# if a & b:
#     print ("hello")


# name = input("Enter your name: ")
# if len(name) < 3:
#     print ("name too short")
# elif len(name) > 30:
#     print ("name is too long")
# else:
#     print ("your name is:", name, "\nlength of your name is:", len(name))
# ////////////////////////////////////////////////////////////////////////////////////////////
# program to find python version
# import sys
# print("\n""version information")
# print("\n",sys.version)
# print("\n", sys.version_info)

# current date and time 
# import datetime
# now =datetime.datetime.now()
# print(now)


# area of circle
# PI = 3.14
# r = float(input("enter radius of circle: "))
# area = PI * r**2
# print(f"radius of circle is:", r)
# print(f"area of circle is:", area)


# Write a Python program that accepts the user's first and last name and prints them in reverse order with a space between them.

# first_name=input("Your first name: ")
# last_name=input("Your last please: ")

# print(last_name , first_name)

# # Write a Python program that accepts a sequence of comma-separated numbers from the user and generates a list and a tuple of those numbers.
# number= input("Enter Multiple number with , sp: ")
# get_number=number.split(",")
# a=[]
# b=tuple(get_number)
# for i in get_number:
#     a.append(i)

# print(a)
# print(b)

# Write a Python program that accepts a filename from the user and prints the extension of the file.
# user_IP=input("ENTER FILE NAME WITH EXTENSION: ")
# list=user_IP.split(".")
# print(list[-1])

# Write a Python program to display the first and last colors from the following list.
# color_list = ["Red","Green","White" ,"Black"]
# print(color_list[0],color_list[-1])

# Write a Python program to display the examination schedule. (extract the date from exam_st_date).
# exam_st_date = input("enter date: ")
# date =exam_st_date.replace(",", "/")
# print("The examination will start from :", date)

# Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
# n=(input("enter integer value: "))
# n1=int(n+n)
# n2=int(n+n+n)
# result=int(n)+n1+n2

# print("sum: ",result)

# Write a Python program to print the documents (syntax, description etc.) of Python built-in function(s).
# print(tuple.__doc__)

# Write a Python program that prints the calendar for a given month and year.
# import calendar

# m=int(input("enter month: "))
# y=int(input("enter year: "))

# print(calendar.month(y, m))

# Write a Python program to print the following 'here document'.
# n="""a string that you "don't" have to escape
# This
# is a ....... multi-line
# heredoc string --------> example"""
# print(n)

# Write a Python program to calculate the number of days between two dates.
# from datetime import datetime
# user_input = input("Enter a date in YYYY-MM-DD format: ")
# date_object = datetime.strptime(user_input, "%Y-%m-%d")
# date2=datetime.now()

# et=date2-date_object
# print(et)

# Write a Python program that determines whether a given number (accepted from the user) is even or odd, and prints an appropriate message to the user.
# def even_or_odd(value):
#     if value % 2 == 0:
#         print(value, " is even")
#     else:
#         print(value, " is odd")

# number = int(input("enter a value: "))
# even_or_odd(number)


# Write a Python program to count the number 4 in a given list.
# def count_4(num_list):
#     count = 0
#     for i in num_list:
#         if i == 4:
#             count += 1
#     print("number 4 is ", count, " times in the given list")
# count_4([12,23,4,2,65,4,45,4,0,4,70,])
# count_4([1, 4, 6, 4, 7, 4])


# Write a Python program to test whether a passed letter is a vowel or not.

# def identify_vowel(letter):
#     if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
#         print(letter, " is a vowel")
#     else:
#         print(letter, " is not a vowel")

# value = input("enter a character ")
# identify_vowel(value)


# Write a Python program that checks whether a specified value is contained within a group of values.
# def check_value(spec_val, grp_values):
#     if spec_val in grp_values:
#         print("The group of values does contain the specific value")
#     else:
#         print("The group of values does not contain the specific value")

# list_values = [43,23 ,6,69,57,55,684,346,76,4,846,7]
# value = int(input("enter a value to be checked: "))
# check_value(value, list_values)


# Write a Python program that concatenates all elements in a list into a string and returns it.

# def string_formation(elements):
#     result = ""
#     for i in elements:
#         result += str(i)
#     print(result)

# element_list = ["my", " ", "name", " ", "is","........"]
# string_formation(element_list)

# Write a Python program to print all even numbers from a given list of numbers in the same order and stop printing any after 237 in the sequence.
# def print_even(numbers):
#     for i in numbers:
#         if i == 237:
#             print(i)
#             break
#         elif i % 2 == 0:
#             print(i)

# num_list = [    
#     386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 
#     399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 
#     815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 
#     958,743, 527
#     ]
# print_even(num_list)

# Write a Python program to add two objects if both objects are integers.
# x= 5
# y= 4
# if type(x) == int and type(y) == int:
#     add = x+y
#     print("sum of both integers is: ",add )
# else:
#     print("given objects are not integers")
# /////////////////w3 sol//////////////
# def add_numbers(a, b):
#     # Check if both 'a' and 'b' are integers using the 'isinstance' function.
#     if not (isinstance(a, int) and isinstance(b, int)):
#         # If either 'a' or 'b' is not an integer, return an error message.
#         return "Inputs must be integers!"
#     # If both 'a' and 'b' are integers, return their sum.
#     return a + b

# Write a Python program that displays your name, age, and address on three different lines.
# def display(name,age,address):
#     global count
#     data = []
#     data.append(name)
#     data.append(age)
#     data.append(address)
#     print(f"{count} person data is as follows:")
#     for i,d in enumerate(data):
#         if i==0:
#             print("name: " ,d)
#         if i==1:
#             print("age: " ,d)
#         if i==2:
#             print("address: " ,d)
#     count += 1


# count = 1
# display("ahmar","22","cantt")
# display("ali","32","isl")

# Write a Python program to solve (x + y) * (x + y).
# x =int(input("enter first value: "))
# y =int(input("enter second value: "))
# sol = (x+y) ** 2
# print(sol)