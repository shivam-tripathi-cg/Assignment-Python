# Question 1
for i in range(5):
    print("Hello")


# Question 2
for i in range(10):
    print(i, end=" ")
print()


# Question 3
for i in range(1, 11):
    print(i)


# Question 4
for i in range(10, 0, -1):
    print(i)


# Question 5
for i in range(5, 51, 5):
    print(i)


# Question 6
for i in range(2, 21, 2):
    print(i)


# Question 7
for i in range(1, 20, 2):
    print(i)


# Question 8
for i in range(3, 19, 3):
    print(i)


# Question 9
for i in range(20, 1, -2):
    print(i)


# Question 10
n = int(input("Enter a positive integer n: "))
for i in range(1, n + 1):
    print(i)


# Question 11
n = int(input("Enter n: "))
for i in range(1, n + 1):
    if i % 2 == 0:
        print(i)


# Question 12
n = int(input("Enter n: "))
for i in range(1, n + 1):
    if i % 2 != 0:
        print(i)


# Question 13
n = int(input("Enter n: "))
for i in range(1, n + 1):
    if i % 3 == 0:
        print(i)


# Question 14
n = int(input("Enter n: "))
for i in range(1, n + 1):
    if i % 2 == 0 and i % 3 == 0:
        print(i)


# Question 15
n = int(input("Enter n: "))
count = 0
for i in range(1, n + 1):
    if i % 2 == 0:
        count += 1
print("Count of even numbers:", count)


# Question 16
n = int(input("Enter n: "))
total_sum = 0
for i in range(1, n + 1):
    total_sum += i
print("Sum:", total_sum)


# Question 17
n = int(input("Enter n: "))
even_sum = 0
for i in range(1, n + 1):
    if i % 2 == 0:
        even_sum += i
print("Sum of even numbers:", even_sum)


# Question 18
n = int(input("Enter n: "))
odd_sum = 0
for i in range(1, n + 1):
    if i % 2 != 0:
        odd_sum += i
print("Sum of odd numbers:", odd_sum)


# Question 19
num = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")


# Question 20
n = int(input("Enter n: "))
factorial = 1
for i in range(1, n + 1):
    factorial *= i
print("Product:", factorial)


# Question 21
text = input("Enter a string: ")
for char in text:
    print(char)


# Question 22
text = input("Enter a string: ")
for char in text:
    print(char, end="")
print()


# Question 23
text = input("Enter a string: ")
length = 0
for char in text:
    length += 1
print("Total characters:", length)


# Question 24
text = input("Enter a string: ")
a_count = 0
for char in text:
    if char == 'a':
        a_count += 1
print("Count of 'a':", a_count)


# Question 25
text = input("Enter a string: ")
uppercase_count = 0
uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for char in text:
    if char in uppercase_letters:
        uppercase_count += 1
print("Count of uppercase letters:", uppercase_count)


# Question 26
for i in range(3):
    for j in range(4):
        print("*", end="")
    print()


# Question 27
for i in range(4):
    for j in range(5):
        print("*", end="")
    print()


# Question 28
for i in range(1, 6):
    for j in range(i):
        print("*", end="")
    print()


# Question 29
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end="")
    print()


# Question 30
for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i * j:2d}", end=" ")
    print()