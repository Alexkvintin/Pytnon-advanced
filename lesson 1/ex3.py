a = list(range(1, 101, 1))
for i in a:
    i+=1
    if i%15==0:
        print('FizzBuzz')
    elif i%5==0:
        print('Buzz')
    elif i%3==0:
        print('Fizz')
    else:
        print(i)
