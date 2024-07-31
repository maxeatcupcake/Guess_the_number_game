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
    with shelve.open('highscore') as highscore:
        best_score = highscore['best_score']
        print(f'The highscore is in {best_score} tries')
        if best_score is None or nb_attempt < best_score:
            highscore['best_score'] = nb_attempt    
            print(f'New highscore: {nb_attempt} tries!')
