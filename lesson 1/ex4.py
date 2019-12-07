def bank(x, y, z):
    for i in range(0, z):
        f = x*(y/100)
        x = x + f
    return x


money = int(input('сумма'))
years = int(input('количество лет'))
percent = int(input('процент'))
print(bank(money, percent, years))
