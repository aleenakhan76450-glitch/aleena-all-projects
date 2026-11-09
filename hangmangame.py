import random
word_list = ["apple", "banana", "cartman", "water", "fish", "boat", "perfume", "notebook", "nintendo", "television"]
index = random.randint(0, len(word_list)-1)
jackpot = word_list[index]


u_guess = ["_"]* len(jackpot)
guessed = []
chances = 5
tries = 0

while chances > 0:

    print("===================================")

    print(" ".join(u_guess))
    

    user = input("enter in a letter to guess: ")
    tries += 1
    if len(user) > 1:
        print("only one letter at a time")
    else:
        if user in jackpot:
            if user in guessed:
                print("already guessed this")
            else:
                for i in range(len(jackpot)):
                    if jackpot[i] == user:
                        u_guess[i] = user
                        guessed.append(user)
        else:
            chances = chances - 1
            print(f"you're wrong, you got {chances} left")

        check = "".join(u_guess)
        if jackpot == check:
            print(f"You win! {tries} tries only!")
            break

if chances == 0:
    print("You lose")