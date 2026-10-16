def check_prime(num):
    if num<=1:
        print(num,"is not prime")
        return
    for i in range(2,num):
        if num%i==0:
            print(num,"is not prime")
            return

    print(num,"is prime")
check_prime(7)
check_prime(10)