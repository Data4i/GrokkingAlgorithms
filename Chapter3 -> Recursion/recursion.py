def countdown(n):
    print(n)
    if n <= 1:
        print('GO')
        return
    countdown(n-1)


countdown(5)


def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)


four_factorial = factorial(4)
print(f'The factorial of 4 is: {four_factorial}')