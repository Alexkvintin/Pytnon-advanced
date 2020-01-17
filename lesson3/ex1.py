import timeit


def decor(*args) :
    def decor_start(func) :
        for i in range(10) :
            def wrapper() :
                print(args)
                a = timeit.default_timer()
                res = func()
                print('func time: ', a)
                print('func name: ', func.__name__)
                return res

            return wrapper

    return decor_start


@decor('123', 123)
def hi_world() :
    print('hi')


for i in range(10):
    hi_world()
