import random
secret_number=random.randint(1,100)
user_try=0
nb_attempt=0
highscore=0
with open('highscore.txt') as file:
    file.write(f'{highscore}')
print("What number am I thinking of ?")
while user_try!=secret_number:
    user_try=int(input("Try :"))
    if user_try < secret_number:
        print("Too low !")
        nb_attempt+=1
    elif user_try > secret_number:
        print("Too high !")
        nb_attempt+=1   
    else:
        print("Correct !")
        print(f'You did it in {nb_attempt} tries !')
        print(f'Highscore : {highscore} tries')

