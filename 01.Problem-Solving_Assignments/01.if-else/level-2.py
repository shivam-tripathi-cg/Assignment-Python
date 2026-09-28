#Question 11.
# year=int(input('Enter Year: '))
# if year%4==0 and year%100!=0:
#     print('Leap Year')
# else:
#     print("Not a leap year")


#Question 12.
# char=input("Enter a character: ")
# char=ord(char[0])
# if char>=65 and char<=90:
#     print("Uppercase Character")
# elif char>=97 and char <=122:
#     print("Lowercase Character")
# elif char>= 48 and char <= 57:
#     print('Digit')
# elif (char>=32 and char<=47) or (char>=58 and char <= 64) or (char>=91 and char<=96) or (char>=123 and char<=126):
#     print('Special Character')


# Question 13

# char=input('Enter a character: ')
# char=ord(char[0])
# if char>=97 and char<=122:
#     if char==97 or char==101 or char==105 or char==111 or char==117:
#         print("Lowercase Vowels")
#     else:
#         print("Lowercase Consonants")
# elif char>=65 and char<=90:
#     if char==65 or char==69 or char==73 or char==79 or char==85:
#         print("Uppercase Vowels")
#     else:
#         print("Uppercase Consonants")
# else:
#     print("Enter only Alphabatical Characters.")

# Question 14
# cp=int(input("Enter Cost Price: "))
# sp=int(input("Enter Selling Price: "))
# if cp>sp:
#     print(f"Loss: {cp-sp}")
# elif sp>cp:
#     print(f"Profit: {sp-cp}") 
# else:
#     print("No Profit no loss")



#Question 15

# cp=int(input("Enter Cost Price: "))
# sp=int(input("Enter Selling Price: "))
# if cp>sp:
#     loss=cp-sp
#     print(f"Loss: {(loss/cp)*100}%")
# elif sp>cp:
#     profit=sp-cp
#     print(f"Profit: {(profit/cp)*100}%") 
# elif cp<=0 or sp<=0:
#     print("Enter vaild prices.")
# else:
#     print("No profit no loss.")


#Question 16

# units=int(input("Enter units: ").strip())
# bill=0
# if units>=0 and units<=100:
#     bill+=units*5
# elif units>100 and units<=200:
#     units-=100
#     bill+= units*7 + 500
# elif units>200:
#     units-=200
#     bill+=units*10 +1200
# print(bill)


#Question 17

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operator = input("Enter operator (+, -, *, /): ")

if operator == '+':
    print(num1 + num2)
elif operator == '-':
    print(num1 - num2)
elif operator == '*':
    print(num1 * num2)
elif operator == '/':
    if num2 == 0:
        print("Division by zero is not allowed.")
    else:
        print(num1 / num2)
else:
    print("Invalid operator")


#question 18

temp = float(input("Enter temperature in Celsius: "))

if temp < 0:
    print("Freezing")
elif temp <= 15:
    print("Very Cold")
elif temp <= 25:
    print("Cold")
elif temp <= 35:
    print("Normal")
else:
    print("Hot")




#question 19

num = float(input("Enter a number: "))

if num < 0:
    print("Negative")
elif num <= 10:
    print("Number is between 0 and 10")
elif num <= 50:
    print("Number is between 11 and 50")
elif num <= 100:
    print("Number is between 51 and 100")
else:
    print("Above 100")


#question20

a = float(input("Enter first side: "))
b = float(input("Enter second side: "))
c = float(input("Enter third side: "))

if (a + b > c) and (a + c > b) and (b + c > a):
    print("Valid triangle")
else:
    print("Invalid triangle")