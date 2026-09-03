word = "Hello"
print(word * 3)

try:
    print(word * 2.5)
except TypeError as e:
    print(e)