i = 0
while i != 101:
    i+=1
    if i%3:
        print('Fizz')
    elif i%5:
        print('Buzz')
    elif i%15:
        print('FizzBuzz')
    else:
        print(i)
