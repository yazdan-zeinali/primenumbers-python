number = int(input('please input your number: '))
if number > 1 and number != 4:
    for i in range(2 , number//2):
        if number % i == 0:
            print('your number is not prime')
            break
    else:
        print('your number is prime')  
else:
    print('your number is not prime')
        