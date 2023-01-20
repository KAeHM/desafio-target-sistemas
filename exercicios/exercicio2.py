


def calc_fibonacci(number: int):
    a, b = 0, 1
    while a <= number:
        a, b = b, a + b
        if number == a or number == 0:
            return True
    return False

print(calc_fibonacci(3)) # True
print(calc_fibonacci(34)) # True
print(calc_fibonacci(987)) # True
print(calc_fibonacci(4)) # False
print(calc_fibonacci(35)) # False
print(calc_fibonacci(988)) # False