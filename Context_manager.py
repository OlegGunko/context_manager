# Задача №1


import time

class Timer:

    def __init__(self, path=None, encoding='utf-8'):
        self.path = path

    def __enter__(self):
        self.start = time.time()
        print(f'Время запуска кода: {self.start}')

    def __exit__(self, exc_type, exc_value, exc_tb):
        self.end = time.time()
        print(f'Время окончания кода: {self.end}')

    def duration(self):
        return self.end - self.start


timer = Timer()

if __name__ == '__main__':
    with timer:
        time.sleep(1)

print(f'Потрачено времени на выполнение кода: {timer.duration()}')

# Задача №2

class Feed(Timer):

    def __init__(self, path=None, encoding='utf-8'):
        super().__init__(path=None, encoding='utf-8')

    def meow(self):
        return print('\nЭй, погромист, покорми кота!')


cat = Feed()
cat.meow()