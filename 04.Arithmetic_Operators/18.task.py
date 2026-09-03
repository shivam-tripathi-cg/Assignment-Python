value = None
num = 5

for op in [
    lambda: value + num,
    lambda: value - num,
    lambda: value * num,
    lambda: value / num,
    lambda: value // num,
    lambda: value % num,
    lambda: value ** num,
]:
    try:
        op()
    except TypeError as e:
        print(e)