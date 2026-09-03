try:
    print(10 / 0)
except ZeroDivisionError as e:
    print(e)

try:
    print("Hello" - "World")
except TypeError as e:
    print(e)

try:
    print(None + 10)
except TypeError as e:
    print(e)