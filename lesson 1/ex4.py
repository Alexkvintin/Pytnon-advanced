def bank(x,y,z):
    for i in range(0,z):
        f = x*(y/100)
        x = x + f
    print(x)

a = int(input('сумма'))
b = int(input('количество лет'))
c = int(input('процент'))
bank(a,c,b)
