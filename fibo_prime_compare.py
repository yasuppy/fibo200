# fibo_prime_compare.py
RED = "\033[31m"
RESET = "\033[0m"


def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True


def fibonacci_upto(limit):
    a, b = 0, 1
    while a <= limit:
        if is_prime(a):
            print(f"{RED}{a}{RESET}", end=" ")
        else:
            print(a, end=" ")
        a, b = b, a + b
    print()


if __name__ == "__main__":
    fibonacci_upto(1000)

