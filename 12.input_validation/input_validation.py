# Part A — Intermediate Problems

# Problem 1: Valid Marks
marks = int(input("Enter marks (0-100): "))
while marks < 0 or marks > 100:
    print("Invalid marks. Please enter between 0 and 100.")
    marks = int(input("Enter marks (0-100): "))
print("Accepted marks:", marks)


# Problem 2: Positive Integer
num = int(input("Enter a positive integer: "))
while num <= 0:
    print("Must be greater than 0.")
    num = int(input("Enter a positive integer: "))
print("Accepted number:", num)


# Problem 3: Age Validation
age = int(input("Enter your age (0-120): "))
while age < 0 or age > 120:
    print("Invalid age. Enter between 0 and 120.")
    age = int(input("Enter your age (0-120): "))
print("Accepted age:", age)


# Problem 4: Menu Choice
choice = 0
while choice not in [1, 2, 3, 4]:
    print("\n1. View profile")
    print("2. Edit profile")
    print("3. Settings")
    print("4. Exit")
    choice = int(input("Enter choice (1-4): "))
    if choice not in [1, 2, 3, 4]:
        print("Invalid choice, try again.")
print("Selected option:", choice)


# Problem 5: Password Length
password = input("Enter password (at least 8 chars): ")
while len(password.strip()) < 8:
    print("Password too short. Must be at least 8 characters.")
    password = input("Enter password (at least 8 chars): ")
print("Password accepted successfully!")


# Problem 6: Temperature Range
temp = float(input("Enter temperature (-20 to 45): "))
while temp < -20 or temp > 45:
    print("Temperature out of range. Enter between -20 and 45.")
    temp = float(input("Enter temperature (-20 to 45): "))
print("Valid temperature entered:", temp)


# Problem 7: Withdrawal Validation
balance = 5000
amount = float(input("Enter withdrawal amount: "))
while amount <= 0 or amount > balance:
    print("Invalid amount. Must be greater than 0 and up to", balance)
    amount = float(input("Enter withdrawal amount: "))
balance -= amount
print("Withdrawal successful. New balance:", balance)


# Problem 8: Username Validation
username = input("Enter username: ")
while len(username.strip()) < 5 or username == "" or " " in username:
    print("Invalid username. Must be at least 5 chars, non-empty, and contain no spaces.")
    username = input("Enter username: ")
print("Accepted username:", username)


# Problem 9: Divisible Number
n = int(input("Enter a positive integer divisible by 3 and 5: "))
while n <= 0 or n % 3 != 0 or n % 5 != 0:
    print("Invalid. Must be a positive integer divisible by both 3 and 5.")
    n = int(input("Enter a positive integer divisible by 3 and 5: "))
print("Accepted number:", n)


# Problem 10: Limited PIN Attempts
secret_pin = 2468
attempts = 3
success = False
while attempts > 0:
    entered_pin = int(input("Enter 4-digit PIN: "))
    if entered_pin == secret_pin:
        print("Access granted!")
        success = True
        break
    else:
        attempts -= 1
        print(f"Incorrect PIN. Attempts left: {attempts}")
if not success:
    print("Access denied.")


# Problem 11: Number Within a Range
num = int(input("Enter an integer between 10 and 50: "))
while num < 10 or num > 50:
    print("Out of range. Try again.")
    num = int(input("Enter an integer between 10 and 50: "))
if num % 2 == 0:
    print(num, "is even.")
else:
    print(num, "is odd.")


# Problem 12: Deposit Validation
balance = 2000
deposit = float(input("Enter deposit amount: "))
while deposit <= 0:
    print("Deposit must be positive.")
    deposit = float(input("Enter deposit amount: "))
balance += deposit
print("New balance:", balance)



# Part B — Challenging Problems

# Problem 13: Integer Between 1 and 100
num = int(input("Enter integer between 1 and 100: "))
while num < 1 or num > 100:
    print("Invalid range. Try again.")
    num = int(input("Enter integer between 1 and 100: "))
print("Valid number:", num)


# Problem 14: Marks and Result
marks = int(input("Enter marks (0-100): "))
while marks < 0 or marks > 100:
    print("Invalid marks.")
    marks = int(input("Enter marks (0-100): "))
if marks >= 75:
    print("Distinction")
elif marks >= 60:
    print("First Class")
elif marks >= 35:
    print("Pass")
else:
    print("Fail")


# Problem 15: Username and Password Validation
valid_creds = False
while not valid_creds:
    username = input("Enter username: ")
    password = input("Enter password: ")
    
    user_valid = len(username.strip()) >= 5 and " " not in username
    pass_valid = len(password) >= 8 and password.strip() != ""
    
    if user_valid and pass_valid:
        print("Success! Both username and password are valid.")
        valid_creds = True
    else:
        print("Invalid credentials. Check rules and try again.")


# Problem 16: Calculator Input Validation
num1 = float(input("Enter first number: "))

op = input("Enter operator (+, -, *, /): ")
while op not in ['+', '-', '*', '/']:
    print("Invalid operator.")
    op = input("Enter operator (+, -, *, /): ")
    
num2 = float(input("Enter second number: "))
while op == '/' and num2 == 0:
    print("Division by zero is not allowed.")
    num2 = float(input("Enter second number: "))

if op == '+':
    result = num1 + num2
elif op == '-':
    result = num1 - num2
elif op == '*':
    result = num1 * num2
else:
    result = num1 / num2
print("Result:", result)


# Problem 17: Banking Menu
balance = 10000
choice = 0
while choice != 4:
    print("\n1. Check balance")
    print("2. Deposit money")
    print("3. Withdraw money")
    print("4. Exit")
    choice = int(input("Choose an option: "))
    
    if choice == 1:
        print("Current balance:", balance)
    elif choice == 2:
        amt = float(input("Enter deposit amount: "))
        while amt <= 0:
            print("Must be greater than zero.")
            amt = float(input("Enter deposit amount: "))
        balance += amt
        print("Updated balance:", balance)
    elif choice == 3:
        amt = float(input("Enter withdrawal amount: "))
        while amt <= 0 or amt > balance:
            print("Invalid withdrawal amount.")
            amt = float(input("Enter withdrawal amount: "))
        balance -= amt
        print("Updated balance:", balance)
    elif choice == 4:
        print("Exiting banking system. Goodbye!")
    else:
        print("Invalid choice.")


# Problem 18: Validate Month and Day
month = int(input("Enter month (1-12): "))
while month < 1 or month > 12:
    print("Invalid month.")
    month = int(input("Enter month (1-12): "))
    
day = int(input("Enter day (1-31): "))
while day < 1 or day > 31:
    print("Invalid day.")
    day = int(input("Enter day (1-31): "))
print(f"Valid date entered: Month {month}, Day {day}")


# Problem 19: Product Quantity and Price
qty = int(input("Enter product quantity: "))
while qty <= 0:
    print("Quantity must be a positive integer.")
    qty = int(input("Enter product quantity: "))
    
price = float(input("Enter unit price: "))
while price <= 0:
    print("Unit price must be greater than zero.")
    price = float(input("Enter unit price: "))
    
total = qty * price
print("Total cost:", total)


# Problem 20: Safe Average Calculator
count = int(input("How many numbers to enter (1-20)? "))
while count < 1 or count > 20:
    print("Count must be between 1 and 20.")
    count = int(input("How many numbers to enter (1-20)? "))
    
total_sum = 0
for i in range(count):
    val = float(input(f"Enter number {i+1}: "))
    total_sum += val
avg = total_sum / count
print("Average:", avg)


# Problem 21: Stronger Password Rules
pwd = ""
while True:
    pwd = input("Enter strong password: ")
    has_upper = any(c.isupper() for c in pwd)
    has_lower = any(c.islower() for c in pwd)
    has_digit = any(c.isdigit() for c in pwd)
    no_space = not any(c.isspace() for c in pwd)
    long_enough = len(pwd) >= 8
    
    if has_upper and has_lower and has_digit and no_space and long_enough:
        print("Strong password accepted!")
        break
    else:
        print("Password does not meet all requirements:")
        if not long_enough: print("- At least 8 characters required")
        if not has_upper: print("- At least one uppercase letter required")
        if not has_lower: print("- At least one lowercase letter required")
        if not has_digit: print("- At least one digit required")
        if not no_space: print("- No whitespace allowed")


# Problem 22: Input Validation Without break
n = 0
while n < 1 or n > 10:
    n = int(input("Enter integer from 1 to 10: "))
    if n < 1 or n > 10:
        print("Invalid value. Try again.")
print("Accepted valid integer:", n)


# Problem 23: Three Valid Scores
scores = []
for i in range(1, 4):
    score = float(input(f"Enter score {i} (0-100): "))
    while score < 0 or score > 100:
        print("Invalid score. Enter between 0 and 100.")
        score = float(input(f"Enter score {i} (0-100): "))
    scores.append(score)
total_score = sum(scores)
avg_score = total_score / 3
print("Total score:", total_score)
print("Average score:", avg_score)


# Problem 24: ATM Withdrawal With Denomination Rules
balance = 10000
amount = float(input("Enter withdrawal amount (multiple of 100): "))
while amount <= 0 or amount > balance or amount % 100 != 0:
    print("Invalid amount. Must be positive, <= balance, and a multiple of 100.")
    amount = float(input("Enter withdrawal amount (multiple of 100): "))
balance -= amount
print("Withdrawn amount:", amount)
print("Remaining balance:", balance)