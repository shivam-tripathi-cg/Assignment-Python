# Q1
i = 0
while i < 5:
    print("Hello")
    i += 1

# Q2
i = 0
while i <= 9:
    print(i, end=" ")
    i += 1
print()

# Q3
i = 1
while i <= 10:
    print(i)
    i += 1

# Q4
i = 10
while i >= 1:
    print(i)
    i -= 1

# Q5
i = 5
while i <= 50:
    print(i)
    i += 5

# Q6
i = 2
while i <= 20:
    print(i)
    i += 2

# Q7
i = 1
while i <= 19:
    print(i)
    i += 2

# Q8
i = 3
while i <= 18:
    print(i, end=" ")
    i += 3
print()

# Q9
i = 20
while i >= 2:
    print(i)
    i -= 2

# Q10
n = int(input("Enter n: "))
i = 1
while i <= n:
    print(i)
    i += 1

# Q11
n = int(input("Enter n: "))
i = 1
while i <= n:
    if i % 2 == 0:
        print(i)
    i += 1

# Q12
n = int(input("Enter n: "))
i = 1
while i <= n:
    if i % 2 != 0:
        print(i)
    i += 1

# Q13
n = int(input("Enter n: "))
i = 1
while i <= n:
    if i % 3 == 0:
        print(i)
    i += 1

# Q14
n = int(input("Enter n: "))
i = 1
while i <= n:
    if i % 2 == 0 and i % 3 == 0:
        print(i)
    i += 1

# Q15
n = int(input("Enter n: "))
i = 1
count = 0
while i <= n:
    if i % 2 == 0:
        count += 1
    i += 1
print(count)

# Q16
n = int(input("Enter n: "))
i = 1
total = 0
while i <= n:
    total += i
    i += 1
print(total)

# Q17
n = int(input("Enter n: "))
i = 1
total = 0
while i <= n:
    if i % 2 == 0:
        total += i
    i += 1
print(total)

# Q18
n = int(input("Enter n: "))
i = 1
total = 0
while i <= n:
    if i % 2 != 0:
        total += i
    i += 1
print(total)

# Q19
num = int(input("Enter number: "))
i = 1
while i <= 10:
    print(f"{num} x {i} = {num * i}")
    i += 1

# Q20
n = int(input("Enter n: "))
i = 1
fact = 1
while i <= n:
    fact *= i
    i += 1
print(fact)

# Q21
text = input("Enter string: ")
i = 0
while i < len(text):
    print(text[i])
    i += 1

# Q22
text = input("Enter string: ")
i = 0
while i < len(text):
    print(text[i], end="")
    i += 1
print()

# Q23
text = input("Enter string: ")
count = 0
i = 0
while i < len(text):
    count += 1
    i += 1
print(count)

# Q24
text = input("Enter string: ")
count = 0
i = 0
while i < len(text):
    if text[i] == 'a':
        count += 1
    i += 1
print(count)

# Q25
text = input("Enter string: ")
count = 0
i = 0
uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
while i < len(text):
    if text[i] in uppercase_letters:
        count += 1
    i += 1
print(count)

# Q26
row = 0
while row < 3:
    col = 0
    while col < 4:
        print("*", end="")
        col += 1
    print()
    row += 1

# Q27
row = 0
while row < 4:
    col = 0
    while col < 5:
        print("*", end="")
        col += 1
    print()
    row += 1

# Q28
row = 1
while row <= 5:
    col = 1
    while col <= row:
        print("*", end="")
        col += 1
    print()
    row += 1

# Q29
row = 1
while row <= 5:
    col = 1
    while col <= row:
        print(col, end="")
        col += 1
    print()
    row += 1

# Q30
row = 1
while row <= 5:
    col = 1
    while col <= 5:
        print(f"{row * col:2d}", end=" ")
        col += 1
    print()
    row += 1