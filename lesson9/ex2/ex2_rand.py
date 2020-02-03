import random
import string


class RandStud:

    def fullname(self):
        y = ''.join(random.choice(string.ascii_letters) for i in range(random.randint(4, 60)))
        return y

    def grupe(self):
        return random.randint(101, 509)

    def fakult(self):
        return ''.join(random.choice(string.ascii_letters) for i in range(1, 8))

    def mark(self):
        a = []
        for i in range(5):
            a.append(random.randint(60, 100))
        return a

    def cure(self):
        return ''.join(random.choice(string.ascii_letters) for i in range(random.randint(3, 60)))
