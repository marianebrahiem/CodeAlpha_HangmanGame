import random
word_list =["hashing","encryption","symmetric","asymmetric"]
word = random.choice(word_list).lower()
guessed = ["_"] * len(word)
guessed_letters = []
tries =6
print ("Welcome to Hangman!")
print("Guess The Word, One Letter at a time. \n")

while tries > 0 and "_" in guessed:
    print("word:", " ".join(guessed))
    print(f"Tries left:{tries}")
    print("Guessed letters:", " ".join(guessed_letters))
    guess = input("Enter a letter: ").lower()

    if not guess.isalpha() or len(guess) !=1:
        print("Invalid input. Enter a single alphabet letter.\n")
        continue

    if guess in guessed_letters:
        print("you have already guessed that letter. \n")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("Correct! \n")
        for idx, char in enumerate(word):
            if char == guess:
                guessed[idx] =guess
    else:
        print("Wrong guess!\n")
    tries -=1
    if "_" not in guessed:
        print(" Conguratulations! You guessed the word:", word)
    else:
        print("Game Over. The word was:",word)

