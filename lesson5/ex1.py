import threading


def decor(isdeamon, name) :
    def wrapper(func, ) :
        tr = threading.Thread(target=func, args=(name,))
        tr.daemon = isdeamon
        tr.setName(name)
        tr.start()
        tr.join()
        return

    return wrapper


@decor(True, 'rtx')
def now_ran(nametr) :
    print(f"Thread {nametr}: starting")
    print(f"Thread {nametr}: finishing")


