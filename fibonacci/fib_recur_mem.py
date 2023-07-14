
# recursive with memory version of fibonacci
import time

def fib(nums: int):
    record = {0:0, 1:1}
    def lookup(nums):
        if nums not in record:
            record[nums] = lookup(nums-1) + lookup(nums-2)
        return record[nums]
    return lookup(nums)

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

