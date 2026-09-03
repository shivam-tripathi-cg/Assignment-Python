str1 = "Hello"
str2 = "World"

try:
    print(str1 + str2)
except TypeError as e:
    print(e)

try:
    print(str1 - str2)
except TypeError as e:
    print(e)

try:
    print(str1 * 3)
except TypeError as e:
    print(e)

try:
    print(str1 / str2)
except TypeError as e:
    print(e)