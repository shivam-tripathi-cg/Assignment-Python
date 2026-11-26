#Q1
def show(n):
    if n == 0:
        print("Stop")
        return

    print(n)
    show(n - 1)
    print(n)

show(2)



#Q2
def total(n):
    if n == 0:
        return 0

    return n + total(n - 1)



#Q3
def count(n):
    if n == 0:
        return

    count(n + 1)


#Q4
def answer(n):
    if n == 0:
        return 0

    # n + answer(n - 1)







#Q5
def countdown(n):
    if n == 0:
        return "Done!"
    print(n)
    return countdown(n-1)
print(countdown(3))


#Q6
def count_up(n):
    if n == 0:
        return 
    if n == 4:
        return 4
    print(n)
    return count_up(n+1)
print(count_up(1))


#Q7
def sum_to(n):
    if n <= 0:
        return 0
    return n + sum_to(n-1)
print(sum_to(0))

#
#Q8
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)
print(factorial(5))


#Q9
def digit_sum(n):
    if n < 10:
        return n
    return n % 10 + digit_sum(n // 10)
print(digit_sum(583))






#Q11
def count_digits(n):
    if -10 < n < 10:
        return 1

    return 1 + count_digits((n-1) // 10)
print(count_digits(0))


#Q12
def reverse_text(n):
    if n == "":
        return ""
    return reverse_text(n[1:])+n[0]
print(reverse_text("qwe"))




#Q14
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