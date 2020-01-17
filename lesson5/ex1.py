import threading


def decor() :
    def wrapper(func, ) :
        tr = threading.Thread(target=func, args=(1,))
        return tr.start()

    return wrapper


@decor()
def now_ran(nametr) :
    print(f"Thread {nametr}: starting")
    print(f"Thread {nametr}: finishing")
