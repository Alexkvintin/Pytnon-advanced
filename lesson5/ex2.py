import threading
import wget

urls = ('https://icons.iconarchive.com/icons/goodstuff-no-nonsense/free-space/1024/rick-icon.png',
        'https://icons.iconarchive.com/icons/goodstuff-no-nonsense/free-space/1024/rick-icon.png',
        'https://icons.iconarchive.com/icons/goodstuff-no-nonsense/free-space/1024/rick-icon.png',
        'https://icons.iconarchive.com/icons/goodstuff-no-nonsense/free-space/1024/rick-icon.png',
        'https://icons.iconarchive.com/icons/goodstuff-no-nonsense/free-space/1024/rick-icon.png',
        'https://icons.iconarchive.com/icons/goodstuff-no-nonsense/free-space/1024/rick-icon.png',
        'https://icons.iconarchive.com/icons/goodstuff-no-nonsense/free-space/1024/rick-icon.png',
        'https://icons.iconarchive.com/icons/goodstuff-no-nonsense/free-space/1024/rick-icon.png',
        'https://icons.iconarchive.com/icons/goodstuff-no-nonsense/free-space/1024/rick-icon.png',
        'https://icons.iconarchive.com/icons/goodstuff-no-nonsense/free-space/1024/rick-icon.png',
        )


def decorator(isdaemon, name):
    def take_func(func):
        def wrapper():
            for url in urls:
                tr = threading.Thread(target=func, name=name, daemon=isdaemon, args=(name, url))
                threads.append(tr)
                tr.start()
            for thread in threads:
                thread.join()

        return wrapper

    return take_func


k = []
for i in range(1, 11):
    k.append(i)


@decorator(True, 'name')
def new_run(name, url):
    number = k.pop(0)
    print(f'Thread {name} {number}: Начал загрузку !')
    wget.download(url, f'Картинка {number}.png')
    print(f'Thread {name} {number}: Завершил загрузку !')


threads = []

new_run()
