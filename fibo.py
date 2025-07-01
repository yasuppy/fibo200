# fibo.py
def fibonacci_upto(limit):
    a, b = 0, 1
    while a <= limit:
        print(a, end=' ')
        a, b = b, a + b
    print()

if __name__ == "__main__":
    fibonacci_upto(500)
