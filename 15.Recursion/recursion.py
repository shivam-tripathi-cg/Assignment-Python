# task 1
def show(n):
    if n == 0:
        print("Stop")
        return

    print(n)
    show(n - 1)
    print(n)

show(2)
# 2
# 1
# Stop
# 1
# 2

# task 2
def total(n):
    if n == 0:
        return 0

    return n + total(n - 1)
# First of All ,The Function isn't call anywhere and when function is called with an argument ,it doesn't make error if the argument is greater than 0.

# task 3
def count(n):
    if n == 0:
        return

    count(n + 1)
# count(2)
# That's because the count function starts with 2 and its base case occurs when n is 0 ,means to the base case ,we must need to decrement the value of n,but here in the code ,the count(n) is increased and that's why its output becomes RecursionError and write [Previous line repeated 996 more times].

# task 4
def answer(n):
    if n == 0:
        return 0

    # n + answer(n - 1)

# print(answer(3))
# The Output of the given code is as follows:- 
# TypeError .Because at the num1 of the recursion to get the base case, it gives none as no any return statement is given like the 0 is returned to whom , so it shows none and at the num1 we got n ,which is an integer and none's sum which raise TypeError

# task 5
def countdown(n):
    if n == 0:
        return "Done!"
    print(n)
    return countdown(n-1)
print(countdown(3))

# task 6
def count_up(n):
    if n == 0:
        return 
    if n == 4:
        return 4
    print(n)
    return count_up(n+1)
print(count_up(1))

# task 7
def sum_to(n):
    if n <= 0:
        return 0
    return n + sum_to(n-1)
print(sum_to(0))

# task 8
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)
print(factorial(5))

# # task 9
def digit_sum(n):
    if n < 10:
        return n
    return n % 10 + digit_sum(n // 10)
print(digit_sum(583))

# task 10
def  power(base, exponent):
    if exponent == 0:
        return 1
    return base * power(base, exponent-1)
print(power(2,3))

# task 11
def count_digits(n):
    if -10 < n < 10:
        return 1

    return 1 + count_digits((n-1) // 10)
print(count_digits(0))

# task 12
def reverse_text(n):
    if n == "":
        return ""
    return reverse_text(n[1:])+n[0]
print(reverse_text("qwe"))

# task 13
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(6))

# task 14
def max_digit(n):
    if n == 0:
        return 0
    num1 = n % 10
    num2 = max_digit(n // 10)

    if num1 > num2:
        return num1
    else:
        return num2


print(max_digit(4729))  # 9
print(max_digit(555))   # 5
print(max_digit(0))     # 0

# task 15
def mystery(n):
    if n <= 1:
        return n

    return mystery(n - 1) + mystery(n - 2)
print(mystery(4))
print(mystery(0))
print(mystery(1))
print(mystery(2))

# task 16
def factorial(n):
    if n == 0:
        return 1# return 0 
    
    return n * factorial(n - 1)
print(factorial(5))

# task 17
def stop_at_zero(n):
    if n == 0:
        return
    print(n)
    return stop_at_zero(n-1)
stop_at_zero(7)

# task 18
# If a recursive function makes too many nested calls then  Python may have reached its recursion limit and after that it will give a Recursive Error.

def func(n):
    if n==0:
        return 0
    func(n-1)
    print(n)
print(func(5))