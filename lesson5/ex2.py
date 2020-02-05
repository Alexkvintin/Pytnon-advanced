import threading
import wget
import os

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
            for i, url in enumerate(urls, start=1):
                tr = threading.Thread(target=func, name=name, daemon=isdaemon, args=(name, i, url))
                threads.append(tr)
                tr.start()
            for i in threads:
                i.join()

        return wrapper

    return take_func


@decorator(True, 'name')
def new_run(name, i, url):
    print(f'Thread {name} {i}: Начал загрузку !')
    wget.download(url, f'Картинка {i}.png')
    print(f'Thread {name} {i}: Завершил загрузку !')


threads = []

new_run()
