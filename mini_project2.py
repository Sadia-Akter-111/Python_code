import random
lucky_num=random.randint(1,50)

while True:
    user_num=int(input("Guess the lucky number: "))

    if lucky_num==user_num:
        print("currect guess,YOU WON!!")
        break
    elif lucky_num<user_num:
        print("Too high")
    else:
        print("Too low")
        

print("----------------GAME HAS ENDED--------------")