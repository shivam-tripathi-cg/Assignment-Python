#practice problems

#======================================= Question=1 =====================================
name = input("Enter your name:- ")
print(name)

#======================================= Question=2 =====================================
city = input("Enter your city name:- ")
print("your city is ",city)

#======================================= Question=3 =====================================
name = input("Enter your name:- ")
age = input("Enter your age:- ")
print(name)
print(age)

#======================================= Question=4 =====================================

#  "string type value return input()"

#======================================= Question=5 =====================================
num = input("Enter any number:- ")
print(num,type(num))

#======================================= Question=6 =====================================
first_name = input("Enter your first name:- ")
last_name = input("Enter your last name:- ")

print(first_name,last_name)

#======================================= Question=7 =====================================
name = input("Enter your name:- ")
city = input("enter your city:- ")
college = input("Enter you college:- ")

print(name)
print(city)
print(college)

#======================================= Question=8 =====================================
name1,name2 = input("Enter your name1 and name2 :- ").split()
print(name1)
print(name2)

#======================================= Question=9 =====================================
# If we take input of two variable in same line with split function
# like user enters Python Programming then veriable1 receive "Python" and variable2 receive "Programming"

#======================================= Question=10 =====================================
a,b,c = input("Enter any three words:- ").split()

print(a)
print(b)
print(c)

#======================================= Question=11 =====================================
a = "25"
print(int(a))

#======================================= Question=12 =====================================
print(float("25.5"))

#======================================= Question=13 =====================================
print(str(100))

#======================================= Question=14 =====================================
num = int(input("Enter ant integer value:- "))

print(num,type(num))

#======================================= Question=15 =====================================
dec = float(input("Enter ant float value:- "))

print(dec,type(dec))

#======================================= Question=16 =====================================
''' a = input()
    b = input()

    print(a + b)
This produce string concatenation because of by default input fuction take input from user in string dataType'''

#======================================= Question=17 =====================================
'''a = input("Enter first number: ")
   b = input("Enter second number: ")

   print(a + b)
   
   Here we do some modify in this program so that it performs numeric addition'''

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print(a + b) 

#======================================= Question=18 =====================================
name = "Rahul"
age = 20

print(f"My name is {name} and I am {age} years old.")

#======================================= Question=19 =====================================
a = 10
b = 20

print(f"Sum of a and b is equal to:- {a+b}")

#======================================= Question=20 =====================================
name,age = input("Enter your name and age:- " ).split()

print(f"Your name is {name} and you're {age} years old.")

#======================================= Question=21 =====================================
product_price = float(input("Enter product's price:- "))

print(f"{product_price:.2f}")

#======================================= Question=22 =====================================
#The purpose of :.2f inside an f-string is f means floating-point formatting and 2 means show two digit after the decimal point.

#======================================= Question=23 =====================================
product_name = input("Enter product's name:- ")
price = float(input("Enter the price of product:- "))
quantity = int(input("Enter quatity of product:- "))

print(f"product is {product_name} and price of one product is {price} and total quatity of product are {quantity}")

#======================================= Question=24 =====================================
#print("A", "B", "C")
#This will display A B C

#======================================= Question=25 =====================================
print("2026", "08", "19", sep="-")

#======================================= Question=26 =====================================
print("Hello",end=" ")
print("World")

#======================================= Question=27 =====================================
x = int(input("First number: "))
y = int(input("Second number: "))

print(f"Sum: {x + y}")

#======================================= Question=28 =====================================
price = float(input("price: "))
Quantity = int(input("Quantity: "))

print(f"Total: {price*Quantity}")

#======================================= Question=29 =====================================
name = input("enter Student's name:- ")
age = int(input("Enter Student's age:- "))
marks = float(input("Enter Student's marks:- "))

print(f"Nmae of student is {name} and he is {age} years old and got {marks} marks.")

#======================================= Question=30 =====================================
student_name = input("Enter student's name: ")
student_age = int(input("Enter student's age: "))
student_height = float(input("Enter student's height: "))
city_name = input("Enter city's name: ")

print(f"Student's name is {student_name} and he is {student_age} year old and his height is equal to {student_height:.2f} and he is lived in {city_name} ")