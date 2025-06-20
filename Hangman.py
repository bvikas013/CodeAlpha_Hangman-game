import random

# Predefined word list
word_list = ["python", "apple", "chair", "brain", "light"]
word_to_guess = random.choice(word_list)

# Game state variables
guessed_letters = []
incorrect_guesses = 0
max_attempts = 6

# Create display version of word
display_word = ["_" for _ in word_to_guess]

print("🎮 Welcome to Hangman!")
print("Guess the word, one letter at a time.")
print("You have", max_attempts, "wrong attempts.\n")

while incorrect_guesses < max_attempts and "_" in display_word:
    print("Word:", " ".join(display_word))
    print("Guessed letters:", " ".join(guessed_letters))
    guess = input("Enter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("❌ Please enter a single alphabetic character.\n")
        continue

    if guess in guessed_letters:
        print("🔁 You've already guessed that letter.\n")
        continue

    guessed_letters.append(guess)

    if guess in word_to_guess:
        print("✅ Good guess!\n")
        for i in range(len(word_to_guess)):
            if word_to_guess[i] == guess:
                display_word[i] = guess
    else:
        incorrect_guesses += 1
        print("❌ Incorrect guess. Attempts left:", max_attempts - incorrect_guesses, "\n")

# Endgame messages
if "_" not in display_word:
    print("🎉 Congratulations! You guessed the word:", word_to_guess)
else:
    print("💀 Out of attempts. The word was:", word_to_guess)
