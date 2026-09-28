# Question 21
a = float(input("Enter side 1: "))
b = float(input("Enter side 2: "))
c = float(input("Enter side 3: "))

if (a + b > c) and (a + c > b) and (b + c > a):
    if a == b == c:
        print("Equilateral")
    elif a == b or b == c or a == c:
        print("Isosceles")
    else:
        print("Scalene")
else:
    print("Invalid triangle")


# Question 22
balance = float(input("Enter account balance: "))
withdrawal = float(input("Enter withdrawal amount: "))

if withdrawal <= 0:
    print("Withdrawal amount must be greater than 0")
elif withdrawal % 100 != 0:
    print("Withdrawal amount must be divisible by 100")
elif withdrawal > balance:
    print("Insufficient funds")
elif balance - withdrawal < 500:
    print("Minimum balance of ₹500 must remain")
else:
    remaining = balance - withdrawal
    print("Withdrawal successful")
    print("Remaining balance:", remaining)


# Question 23
username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin":
    if password == "python123":
        print("Login successful")
    else:
        print("Wrong password")
else:
    print("User not found")


# Question 24
amount = float(input("Enter purchase amount: "))

if amount < 500:
    discount_pct = 0
elif amount <= 999:
    discount_pct = 5
elif amount <= 1999:
    discount_pct = 10
elif amount <= 4999:
    discount_pct = 15
else:
    discount_pct = 20

discount_amount = amount * (discount_pct / 100)
final_amount = amount - discount_amount

print("Original amount:", amount)
print("Discount:", str(discount_pct) + "%")
print("Discount amount:", discount_amount)
print("Final amount:", final_amount)


# Question 25
m1 = float(input("Enter marks for Subject 1: "))
m2 = float(input("Enter marks for Subject 2: "))
m3 = float(input("Enter marks for Subject 3: "))

if m1 < 0 or m1 > 100 or m2 < 0 or m2 > 100 or m3 < 0 or m3 > 100:
    print("Invalid marks entered")
elif m1 < 35 or m2 < 35 or m3 < 35:
    print("Fail")
else:
    avg = (m1 + m2 + m3) / 3
    if avg >= 75:
        print("Distinction")
    elif avg >= 60:
        print("First Class")
    elif avg >= 50:
        print("Second Class")
    else:
        print("Pass")


# Question 26
day = int(input("Enter day: "))
month = int(input("Enter month: "))
year = int(input("Enter year: "))

if month < 1 or month > 12 or day < 1 or year < 1:
    print("Invalid")
else:
    is_leap = (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)
    
    if month in (1, 3, 5, 7, 8, 10, 12):
        max_days = 31
    elif month in (4, 6, 9, 11):
        max_days = 30
    elif month == 2:
        max_days = 29 if is_leap else 28

    if day <= max_days:
        print("Valid")
    else:
        print("Invalid")


# Question 27
hours = int(input("Enter hours: "))
minutes = int(input("Enter minutes: "))
seconds = int(input("Enter seconds: "))

if 0 <= hours <= 23 and 0 <= minutes <= 59 and 0 <= seconds <= 59:
    print("Valid time")
else:
    print("Invalid time")


# Question 28
name1 = input("Enter name of person 1: ")
age1 = int(input("Enter age of person 1: "))
name2 = input("Enter name of person 2: ")
age2 = int(input("Enter age of person 2: "))
name3 = input("Enter name of person 3: ")
age3 = int(input("Enter age of person 3: "))

if age1 < age2 and age1 < age3:
    print(name1, "is the youngest")
elif age2 < age1 and age2 < age3:
    print(name2, "is the youngest")
elif age3 < age1 and age3 < age2:
    print(name3, "is the youngest")
elif age1 == age2 == age3:
    print("All three have the same age")
elif age1 == age2 and age1 < age3:
    print(name1, "and", name2, "are the youngest")
elif age1 == age3 and age1 < age2:
    print(name1, "and", name3, "are the youngest")
else:
    print(name2, "and", name3, "are the youngest")


# Question 29
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

if (num1 > num2 and num1 < num3) or (num1 < num2 and num1 > num3):
    print(num1)
elif (num2 > num1 and num2 < num3) or (num2 < num1 and num2 > num3):
    print(num2)
else:
    print(num3)


# Question 30
age = int(input("Enter age: "))
marks = float(input("Enter marks: "))
income = float(input("Enter family income: "))
attendance = float(input("Enter attendance percentage: "))

cond_age = 18 <= age <= 25
cond_marks = marks >= 85
cond_income = income <= 300000
cond_attendance = attendance >= 75

if cond_age and cond_marks and cond_income and cond_attendance:
    print("Scholarship Approved")
else:
    print("Scholarship Rejected")
    if not cond_age:
        print("Reason: Age must be between 18 and 25")
    if not cond_marks:
        print("Reason: Marks below 85")
    if not cond_income:
        print("Reason: Family income above ₹300000")
    if not cond_attendance:
        print("Reason: Attendance below 75%")