import random

print("Welcome to HANGMAN..... ")

wordlist=["apple","banana","strawberry","grapes","resberry"]
display_word=[]
num=0
random_word=random.choice(wordlist)

for letter in random_word:
    display_word += "_"
print(display_word)
print("You Got Five chances play carefully....")

game_over=False
while not game_over:
    guess_letter = input("Please Guess a Letter:- ").lower()
    for position in range(len(random_word)):
        letter=random_word[position]
        if letter == guess_letter:
            display_word[position]=letter

    if guess_letter not in random_word:
        num += 1
        if num >=5:
            print("You Lose...... CONTINUE ?")
            game_over=True
    print(display_word)
    if "_" not in display_word:
        print("You won... touch some grass nerd..")
        game_over=True
