import time


def main():
    num = 10

    start = time.perf_counter()
    result1 = iterative_fibonacci(num)
    end = time.perf_counter()

    print("[Iterative Fibonacci]")
    print("Num {0} : Fibonacci Number {1}".format(num, result1))
    print("Elapsed Time: {0:08f}s".format((end - start)))
    print()

    start = time.perf_counter()
    result2 = recursive_fibonacci(num)
    end = time.perf_counter()

    print("[Recursive Fibonacci]")
    print("Num {0} : Fibonacci Number {1}".format(num, result2))
    print("Elapsed Time: {0:08f}s".format((end - start)))
    print()


def iterative_fibonacci(num):
    if num <= 1:
        return num
    a, b = 0, 1
    for _ in range(2, num + 1): #2부터 num까지 반복
        a, b = b, a + b
    return b

def recursive_fibonacci(num):
    if num <= 1:
        return num
    return recursive_fibonacci(num - 1) + recursive_fibonacci(num - 2)


if __name__ == "__main__":
    main()
