import random
import ARTpy
import WORDS

chosen_word=random.choice(WORDS.word_list )
print(ART.logo)


display=[]
for letter in chosen_word:
    display+= "_"
print(display)

end_of_game=False
lives=6
while not end_of_game:

    guess=input("Guess a letter").lower()
    if guess in display:
        print(f"You've already guessed{guess}")

    for position in range(len(chosen_word)):
        letter=chosen_word[position]
        if letter==guess:
            display[position]=guess
    if guess  not in chosen_word:
        lives-=1
        if lives==0:
            end_of_game=True
            print("YOU LOOSE")

    print(f"{' '.join(display)}")
    if "_" not in display:
        end_of_game=True
        print("You Win")

    print(ART.stages[lives])

    if end_of_game is True:
        print(f"Answer is {chosen_word}")

