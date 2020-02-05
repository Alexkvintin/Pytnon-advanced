import threading


def decor(isdaemon, name):
    def take_func(func):
        def wrapper():
            tr = threading.Thread(target=func, name=name, daemon=isdaemon, args=(name,))
            tr.start()

        return wrapper

    return take_func


@decor(True, 'name')
def now_ran(name):
    print(f"Thread {name}: starting")
    print(f"Thread {name}: finishing")


now_ran()
