def sort(a):
    mn = min(a)
    mx = max(a)
    diff = mx - mn
    if not diff:
        return a
    elems = [0 for i in range(diff + 1)]
    for i in a:
        elems[i - mn] += 1
    return [i + mn for i in range(len(elems)) for j in range(elems[i])]


if __name__ == '__main__':
    import time
    import random

    def timeit(func, loop=1):
        t = time.time_ns()
        for i in range(loop):
            func()
        return time.time_ns() - t

    ceil = 1000
    size = 10000
    arr = [random.randint(0, ceil) for i in range(size)]
    res = 0
    for i in range(1000):
        x = timeit(lambda: sorted(arr))
        y = timeit(lambda: sort(arr))
        if x < y:
            res -= 1
        elif x > y:
            res += 1
    if res > 0:
        print("timsort sucks. Mine is faster)")
    elif res == 0:
        print("u would not believe ur eyes - tie")
    else:
        print("better luck for me next time(")
