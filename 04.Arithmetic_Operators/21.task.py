a = 10
b = -3
c = 2.5

expressions = [
    ("a + b", a + b),
    ("a - b", a - b),
    ("a * c", a * c),
    ("a / c", a / c),
    ("a // b", a // b),
    ("a % b", a % b),
    ("b ** 2", b ** 2),
    ("a + b * c", a + b * c),
    ("(a + b) * c", (a + b) * c),
    ("a - b / c ** 2", a - b / c ** 2),
]

for expr_str, actual in expressions:
    print(f"{expr_str} = {actual}")