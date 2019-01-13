def add(a, b):
    return a + b


add(1, 23)

# 函数即对象
add2 = add


def add_wrapper():
    return add


# print(add_wrapper()(10, 20))


def calculate(func, a, b):
    return func(a, b)


# print(calculate(add2, 2, 3))

from time import time


def timeit(func, *args, **kwargs):
    start = time()
    func(*args, **kwargs)
    end = time()
    print(end - start)


def test1(n):
    s = 0
    for i in range(n):
        s += i * i
    return s


def timeit2(func):  # 闭包
    def wrapper(*args, **kwargs):
        start = time()
        func(*args, **kwargs)
        end = time()
        print(end - start)

    return wrapper


test1 = timeit2(test1)


# print(test1)
# test1(1000000)


@timeit2
def test2(n):
    s = 0
    for i in range(n):
        s += i * i
    return s


# test2(1000000)

handlers = set()


def on_message(func):
    handlers.add(func)
    return func


@on_message
def handler(ctx):
    pass


@on_message
def handler2(ctx):
    pass


print(handlers)
