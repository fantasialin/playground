
# iteration version of fibonacci
import time

def fib(nums: int):
    # Fib(0) = 0, Fib(1) = 1, nums should positive integer or equal to 0
    if nums <= 1: return nums
    nums_prev = [0, 1]
    result = 1
    for _ in range (nums-1):
        result = nums_prev[0] + nums_prev[1]
        nums_prev[0] = nums_prev[1]
        nums_prev[1] = result
    return result


# local test code

def main():
    print(f' fib(10) == {fib(10)}')

    start = time.time()
    fib30 = fib(30)
    end = time.time()
    print(f' fib(30) = {fib30:10d} time {((end-start)*1000):5.3f} ms')

    for i in range(20, 35, 2):
        start = time.time()
        result = fib(i)
        end = time.time()
        print(f' fib({i}) = {result:10d} time {((end-start)*1000):5.3f} ms')


if __name__ == '__main__':
    main()

