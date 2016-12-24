#This would help me to:
#Catch exceptions
#Use available tools with "Imports" like the 'Random Library'.



import random #must use the "import" keyword and then the name of the library


def game():
    #generate a random number from 1 -10
    secret_num = random.randint(1, 10)
    guesses = []
    
    while len(guesses) < 5:#when guess are 5 or greater; game will end
                           #Limit the number of guesses
        try:
            #get a number guess from player
            guess = int(input("Guess a number between 1 and 10: "))
        except ValueError:  #Catch when someone submits a non integer
            print("{} isn't a number!".format(guess))

        else:#this is the actual guessing game
            #compare guess to secret number
            if guess == secret_num:
                print("You got it! My number was {}".format(secret_num))
                break

            #Print too low or too high messages for bad guesses
            elif guess < secret_num:
                print("My number is higher than {}".format(guess))
            else:
                print("My number is lower than {}".format(guess))
            guesses.append(guess)
    else:
        print("You didn;t get it! My number was {}".format(secret_num))

#Outside of the 'While Loop; but inside of the function...
        #Let people play again
    play_again = input("Do you want to play again? Y/n ")#Cap Y means the yes is default
    if play_again.lower() != 'n':
        game()
    else:
        print("Bye!") 

game()#this will run the function       

   
    
    
            

    #if guess > secret_num:
        #print ("Too High")

    #if guess < secret_num:
        #print ("Too Low")
