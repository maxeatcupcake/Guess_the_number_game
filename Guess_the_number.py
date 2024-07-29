import random
secret_number=random.randint(1,100)
user_try=0
while user_try!=secret_number:
    user_try=int(input("Try :"))
    if user_try < secret_number:
        print("Too low!")
    elif user_try > secret_number:
        print("Too high!")
    else:
        print("Correct!")
