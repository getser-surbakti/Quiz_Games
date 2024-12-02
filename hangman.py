import random

words = [ 'parallel', 'isosceles', 'composite', 'prime', 'vertices', 'edges','perimeter']

# Randomly choose a word from the list
chosen_word=random.choice(words)
word_display=['_' for _ in chosen_word]
attempts=8

print("Welcome to Hangman!")

while attempts > 0 and '_' in word_display:
    print("\n" + ' '.join(word_display))
    print(f"Attempts left: {attempts}")
    guess = input("Guess a letter: ").lower()
    if guess in chosen_word:
        for index, letter in enumerate(chosen_word):
            if letter==guess:
                word_display[index]= guess
    else:
        print("That letter dooesn't appear in the word!")
        attempts -=1
# Game conclusion
if '_' not in word_display:
    print("You guessed the word!")
    print(' '.join(word_display))
    print("You survived")

else:
    print("You ran out of attempts. The word was: " + chosen_word)
    print("You lost")
