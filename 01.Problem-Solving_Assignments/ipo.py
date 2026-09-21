# Problem 1
# IPO Model:
# INPUT: num1, num2
# PROCESSING: sum = num1 + num2
# OUTPUT: sum
#
# Algorithm:
# 1. Read num1 and num2
# 2. sum = num1 + num2
# 3. Print sum


num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
total_sum = num1 + num2
print("Sum:", total_sum)


# Problem 2
# IPO Model:
# INPUT: num
# PROCESSING: num % 2 == 0
# OUTPUT: "Even" or "Odd"
#
# Algorithm:
# 1. Read num
# 2. If num % 2 == 0 print "Even"
# 3. Else print "Odd"


num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")


# Problem 3
# IPO :
# INPUT: a, b, c
# PROCESSING: Compare a, b, c
# OUTPUT: largest
#
# Algorithm:
# 1. Read a, b, c
# 2. If a >= b and a >= c, largest = a
# 3. Else if b >= c, largest = b
# 4. Else largest = c
# 5. Print largest

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))
if a >= b and a >= c:
    largest = a
elif b >= c:
    largest = b
else:
    largest = c
print("Largest number:", largest)


# Problem 4
# IPO Model:
# INPUT: age
# PROCESSING: age >= 18
# OUTPUT: "Eligible to vote" or "Not eligible to vote"
#
# Algorithm:
# 1. Read age
# 2. If age >= 18 print "Eligible to vote"
# 3. Else print "Not eligible to vote"


age = int(input("Enter your age: "))
if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")


# Problem 5
# IPO Model:
# INPUT: price
# PROCESSING: price >= 2000 ? final_price = price - (price * 0.20) : final_price = price
# OUTPUT: final_price
#
# Algorithm:
# 1. Read price
# 2. If price >= 2000, final_price = price - (price * 0.20)
# 3. Else final_price = price
# 4. Print final_price
#
# Dry Run:
# Case 1: price = 2500 -> 2500 - 500 = 2000
# Case 2: price = 1500 -> 1500

price = float(input("Enter item price: "))
if price >= 2000:
    final_price = price - (price * 0.20)
else:
    final_price = price
print("Final price:", final_price)


# Problem 6
# IPO Model:
# INPUT: m1, m2, m3
# PROCESSING: average = (m1 + m2 + m3) / 3, average >= 40
# OUTPUT: "Pass" or "Fail"
#
# Algorithm:
# 1. Read m1, m2, m3
# 2. average = (m1 + m2 + m3) / 3
# 3. If average >= 40 print "Pass"
# 4. Else print "Fail"
#
# Dry Run:
# Case 1: m1 = 45, m2 = 50, m3 = 55 -> average = 50 -> Pass
# Case 2: m1 = 30, m2 = 35, m3 = 40 -> average = 35 -> Fail

m1 = float(input("Enter marks for Subject 1: "))
m2 = float(input("Enter marks for Subject 2: "))
m3 = float(input("Enter marks for Subject 3: "))
average = (m1 + m2 + m3) / 3
if average >= 40:
    print("Pass")
else:
    print("Fail")