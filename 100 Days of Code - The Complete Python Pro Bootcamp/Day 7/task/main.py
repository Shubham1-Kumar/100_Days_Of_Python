import random
stages = [
 '''
        _______
     |/      |
     |         
     |         
     |        
     |         
     |
 jgs_|___
 ''',
 '''
        _______
     |/      |
     |      (_)
     |         
     |        
     |         
     |
 jgs_|___
 ''',
 '''
        _______
     |/      |
     |      (_)
     |      \\  
     |        
     |         
     |
 jgs_|___
 ''',
 '''
        _______
     |/      |
     |      (_)
     |      \\| 
     |        
     |         
     |
 jgs_|___
 ''',
 '''
        _______
     |/      |
     |      (_)
     |      \\|/
     |        
     |         
     |
 jgs_|___
 ''',
 '''
        _______
     |/      |
     |      (_)
     |      \\|/
     |       |
     |         
     |
 jgs_|___
 ''',
 '''
        _______
     |/      |
     |      (_)
     |      \\|/
     |       |
     |      /  
     |
 jgs_|___
 ''',
 '''
        _______
     |/      |
     |      (_)
     |      \\|/
     |       |
     |      / \\ 
     |
 jgs_|___
 '''
]

word_list = ["aardvark", "baboon", "camel"]

# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word. Then print it.
chosen_word = random.choice(word_list)
placeholder=""
for position in range(0,len(chosen_word)-1):
    placeholder += "_"
print(chosen_word)
print(placeholder)
# TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
game_over = False
correct_letters = []
used_life = 0
while not game_over:
    guess = str(input("Guess a letter ")).lower()
    # TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word. Print "Right" if it
    #  is, "Wrong" if it's not.

    display = ""
    for letter in chosen_word:
        if letter == guess:
            display += guess
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
    print(display)
    if guess not in chosen_word:
        used_life += 1
        if used_life == 7 or used_life < 0:
            game_over = True
            print("Game Over")
    if "_" not in display:
        game_over = True
        print("You win")
    print(stages[used_life])


