import random

def hungman():
    word_list = ['mouse', 'bark', 'dark', 'ardvark', 'fork', 'diamond']
    wordVar = random.choice(word_list)
    lives = 5
    display = ['_'] * len(wordVar)
    end_of_game = False

    print(f"Hint: The word is {wordVar}")  # For debugging, can remove this.

    while not end_of_game:
        userLetter = input("Guess a letter: ").lower()

        if userLetter in wordVar:
            for i, letter in enumerate(wordVar):
                if letter == userLetter:
                    display[i] = userLetter
        else:
            lives -= 1
            print(f"Incorrect guess. Lives left: {lives}")
            if lives == 0:
                end_of_game = True
                print("You lose!")
                break

        print(" ".join(display))

        if '_' not in display:
            end_of_game = True
            print("You win!")

if __name__ == "__main__":
    hungman()
