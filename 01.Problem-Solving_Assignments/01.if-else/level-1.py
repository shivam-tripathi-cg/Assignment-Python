#Question 1

# user=int(input("Enter a number to check: "))
# if user>0:
#     print("Positive")
# elif user==0:
#     print('Zero')
# else:
#     print("Negative")



#Question 2

# user=int(input("Enter number to check: "))
# if user >0 and user%2==0:
#     print("Positive Even")
# elif user>0 and user%2!=0:
#     print("Positive Odd")
# elif user<0 and user%2==0:
#     print("Negative Even")
# elif user<0 and user%2!=0:
#     print("Negative Odd")
# else:
#     print("Zero")



#Question 3

# num1, num2=map(int,input("Enter two numbers with space inbetween.").split())
# if num1>num2:
#     print(f"{num1} is Greater.")
# elif num1==num2:
#     print("Both numbers are equal")
# else:
#     print(f"{num2} is Greater")


#Question 4
# while True:
#     num1,num2,num3=map(int, input("Enter three numbers separating with space").split())
#     if num1<(num2 and num3):
#         print(f"{num1} is Smallest.")
#     elif num2<(num1 and num3):
#         print(f"{num2} is Smallest.")
#     elif num3<(num1 and num2):
#         print(f"{num3} is Smallest.")
#     else:
#         print("All three numbers are equal.")


#Question 5

# while True:
#     num1,num2,num3=map(int, input("Enter three numbers separating with space").split())
#     if num1>(num2 and num3):
#         print(f"{num1} is Largest.")
#     elif num2>(num1 and num3):
#         print(f"{num2} is Largest.")
#     elif num3>(num1 and num2):
#         print(f"{num3} is Largest.")
#     else:
#         print("All three numbers are equal.")



#Question 6
# while True:
#     user=int(input("Enter a number to check divisibilty by 5 and 11: "))
#     if user==0:
#         print("Zero is divisible by all numbers.")
#     elif (user%5==0) and (user%11==0):
#         print(f"The number '{user}' is divisible by both 5 and 11")
#     elif user%5==0 and user%11!=0:
#         print(f"The number '{user}' is divisible by 5 only")
#     elif user%5!=0 and user%11==0:
#         print(f"The number '{user}' is divisible by 11 only")
#     else :
#         print("Divisible by Neither")



#Question 7.
# while True:
#     user=int(input("Enter a number to check divisibilty by 3 and 7: "))
#     if user==0:
#         print("Zero is divisible by all numbers.")
#     elif (user%3==0) and (user%7==0):
#         print(f"The number '{user}' is divisible by both 3 and 7")
#     elif user%3==0 and user%7!=0:
#         print(f"The number '{user}' is divisible by 3 only")
#     elif user%3!=0 and user%7==0:
#         print(f"The number '{user}' is divisible by 7 only")
#     else :
#         print("Divisible by Neither")



#Question 8.

# marks=int(input("Enter marks: "))
# if marks<0 or marks>100:
#     print("Invalid Marks")
# elif marks>=40:
#     print("Pass")
# else:
#     print("Fail")


#Question 9.
# while True:
#     marks=int(input("Enter your marks: "))
#     if marks<0 or marks>100:
#         print("Invalid Marks entered")
#     elif marks>=90:
#         print("Grade A")
#     elif marks<90 and marks>=80:
#         print("Grade B")
#     elif marks<80 and marks>=70:
#         print("Grade C")
#     elif marks<70 and marks>=60:
#         print("Grade D")
#     elif marks <60 and marks>=40:
#         print("Grade E")
#     else :
#         print("Fail")


#Question 10

# age=int(input('Enter your age(in years): '))
# if age<=0:
#     print("Enter valid age.")
# elif age<18:
#     print("Not Eligible for voting.")
# else:
#     print("Eligible for Voting.")



