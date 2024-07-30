import random
import shelve
secret_number=random.randint(1,100)
user_try=0
nb_attempt=0
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
        nb_attempt+=1
        print(f'You did it in {nb_attempt} tries !')
data = [f'{nb_attempt}'];      
if nb_attempt > data:
    print("TEST")
else:
    highscore = shelve.open('highscore.txt')
del highscore[f'{nb_attempt}']
highscore[f'{nb_attempt}'] = highscore
highscore.close()
