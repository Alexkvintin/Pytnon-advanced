class Stack :
    def __init__(self) :
        self.items = []

    def empty(self) :
        return self.items == []

    def push(self, item) :
        self.items.append(item)

    def pop(self) :
        return self.items.pop()

    def peek(self) :
        return self.items[len(self.items) - 1]

    def size(self) :
        return len(self.items)


a = Stack()
a.push('smth')
a.push('x')
a.push('y')
print(a.pop())
a.push('z')
print(a.peek())


class Queue :
    def __init__(self) :
        self.items = []

    def empty(self) :
        return self.items == []

    def enqueue(self, item) :
        self.items.insert(0, item)

    def pop(self) :
        return self.items.pop()

    def size(self) :
        return len(self.items)


q = Queue()
q.enqueue('hello')
q.enqueue('dog')
q.enqueue(3)
print(q.pop())


class Cmplex:
    def __init__(self, x, y) :
        self.x = x
        self.y = y

    def __add__(self, obj) :
        self.sumax = self.x + obj.x
        self.sumay = self.y + obj.y

    def __mul__(self, obj) :
        self.multx = self.x * obj.x - self.y * obj.y
        self.multy = self.y * obj.x + self.x * obj.y

    def __sub__(self, obj):
        self.submax = self.x - obj.x
        self.submay = self.y - obj.y







x = float(input())
y = float(input())
a = Cmplex(x, y)
x = float(input())
y = float(input())
b = Cmplex(x, y)
a + b
a * b
a - b
print('Сумма:   %.2f+%.2fj' % (a.sumax, a.sumay))
print('Произв.: %.2f+%.2fj' % (a.multx, a.multy))
print('Вычитание.: %.2f+%.2fj' % (a.submax, a.submay))
