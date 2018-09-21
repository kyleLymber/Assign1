import sys


def fibItHelper(n, a, b):
    if n == 0:
        return a
    elif n == 1:
        return b
    else:
        return fibItHelper(n-1, b, a+b)


def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n-1)+fib(n-2)


def fibIt(n):
    return fibItHelper(n, 0, 1)


def main():
    print(fibIt(int(sys.argv[1])))


if __name__ == "__main__":
    main()


