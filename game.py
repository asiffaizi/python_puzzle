import random

# List of words for the game
word_list = ["father", "baker", "country", "green", "aeroplane", "python", "puzzle", "game", "program", "random"]

def shuffle_word(word):
    # Shuffle letters of the word to create a puzzle
    word = list(word)
    random.shuffle(word)
    return ''.join(word)

def play_game():
    # Select 5 random words from the list
    words_to_guess = random.sample(word_list, 5)
    score = 0

    for word in words_to_guess:
        # Shuffle the word for the puzzle
        shuffled_word = shuffle_word(word)
        print("Arrange the letters to form a valid word:")
        print(shuffled_word)

        # Get the user's answer
        user_answer = input("Your answer: ").strip().lower()

        # Check if the answer is correct
        if user_answer == word:
            print("Correct")
            score += 1
        else:
            print("Wrong")
            score -= 1

    # Print the final score
    print("Net Score is", score)

# Start the game
play_game()
