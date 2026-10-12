# section - a

# Q4
for limit in [10, 5, 7]:
    for i in range(1, limit + 1):
        if i == 7:
            break
        print(i, end=" ")
    print()

# Q5
for text, target in [("computer", "p"), ("banana", "x"), ("level", "l")]:
    for ch in text:
        print(ch, end=" ")
        if ch == target:
            break
    print()

# Q6
for seq in [[4, 8, 2, -3, 9], [4, 8, 2, -1, 5, 6], [-2, 4, 6]]:
    printed = False
    for num in seq:
        if num < 0:
            break
        print(num, end=" ")
        printed = True
    if not printed:
        print("No numbers printed", end="")
    print()

# Q8
for sentence, target_word in [("python makes coding fun", "coding"), ("loops are useful", "java"), ("learn python python python", "python")]:
    found = False
    for word in sentence.split():
        if word == target_word:
            print("Found")
            found = True
            break
    if not found:
        print("Not found")


# section - b

# Q12
for n in [8, 3, 2]:
    for i in range(1, n + 1):
        if i % 3 == 0:
            continue
        print(i, end=" ")
    print()

# Q13
for text, char in [("mississippi", "s"), ("banana", "a"), ("hello", "x")]:
    for ch in text:
        if ch == char:
            continue
        print(ch, end="")
    print()

# Q14
for marks in [[25, 40, 75, 32, 90], [10, 20, 30], [40, 40, 40]]:
    printed = False
    for mark in marks:
        if mark < 40:
            continue
        print(mark, end=" ")
        printed = True
    if not printed:
        print("No marks printed", end="")
    print()

# Q16
n = 0
while n < 5:
    n += 1
    if n == 3:
        continue
    print(n)

# Q17
for word in ["education", "rhythm", "apple"]:
    count = 0
    for ch in word:
        if ch in "aeiou":
            continue
        count += 1
    print(count)


# section - c

# Q22
for lst, target in [([4, 8, 12, 16], 12), ([3, 6, 9], 5), ([7, 7, 7, 7], 7)]:
    for num in lst:
        if num == target:
            print("Found")
            break
    else:
        print("Not found")

# Q23
for text, target in [("programming", "g"), ("computer", "z"), ("a", "a")]:
    for ch in text:
        if ch == target:
            print("Character exists")
            break
    else:
        print("Character missing")

# Q24
for n in [7, 12, 2]:
    for i in range(2, n):
        if n % i == 0:
            print("Not prime")
            break
    else:
        print("Prime")

# Q27
for s in ["lamp", "level", "abcded"]:
    for i in range(len(s)):
        if s.count(s[i]) >= 2:
            print(s[i])
            break
    else:
        print("No repeated character")


# section - d

# Q31
for i in range(1, 6):
    if i % 2 == 0:
        pass
    print(i)

# Q32
choice = "1"
if choice == "1":
    print("Option 1 executed")
elif choice == "2":
    pass
elif choice == "9":
    print("Unknown option")
print("Program closed")


# section - e

# Q36
for lst, target in [[[-2, 4, 7, 9], 7], [[-5, -1, 3, 6, 8], 3], [[2, 4, 6], 2]]:
    for num in lst:
        if num < 0:
            continue
        if num == target:
            print("Target found")
            break
    else:
        print("Target not found")

# Q37
for seq in [[2, 0, 4, -1, 8], [2, 4, 0, 3, 5], [-1, 2, 3]]:
    printed = False
    for num in seq:
        if num == 0:
            continue
        if num == -1:
            break
        print(num, end=" ")
        printed = True
    else:
        if printed:
            print("All values processed")
        else:
            print("No numbers printed and no completion message")
    print()

# Q39
for lst in [[-3, 8, 12, 24], [5, 7, 10, 14], [-12, 6, 18]]:
    for num in lst:
        if num < 0:
            continue
        if num % 4 == 0 and num % 6 == 0:
            print(f"Found: {num}")
            break
    else:
        print("No matching number")