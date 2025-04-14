import random
randno= random.randint(0,3)
random_words=['hello','commit','lion','cello']
random_word=random_words[randno]
len_random=len(random_word)
space_printing =len_random*("_")
print(space_printing)
under_score="_"
print(random_word)
new_guess=[]*len_random
for j in range(len_random):
    new_guess.append("_")
print(new_guess)
life=6
for i in range(life):
    letter=input("Enter a guess to start the game: ")

    gues_letter=letter.lower()
    guess_letter=list(gues_letter)
    
    correct=False

    for idx, letter in enumerate(random_word):
        
        if letter==gues_letter:
            new_guess[idx]=letter
            print(new_guess)
            correct=True
    if correct:
        if("_" not in new_guess):
            print("You won")
        else:
            print("good guess")
            
            


    else:
        print("Worong guess")
        life-=1
        print(f"your life remmaing {life}")
        if(life==0):
            print("Game Over\nYou Loose")



        
    

            
            
        
    # print(new_guess)