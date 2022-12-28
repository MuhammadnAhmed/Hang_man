# Created by Muhammad Ahmed
# Checkout my Portfolio https://a03152049334.wixsite.com/muhammadahmed
# Checkout my Fiverr account https://www.fiverr.com/ahmed189
# Checkout my Upwork account https://www.upwork.com/freelancers/~01e248930a029b5290
# Follow me on LinkedIn http://www.linkedin.com/in/muhammad-ahmed189
# Follow me on GitHub https://github.com/MuhammadnAhmed

import random
import string
# imports list of words from other file which I created
from words import words_list


def choose_valid_word(word_list):
    # will choose random word
    word = random.choice(word_list)
    while '_' in word or ' ' in word:
        word = random.choice(word_list)
    return word


def hang_man():
    word = choose_valid_word(words_list)
    word = word.upper()

    # saves the letters of word as a list
    word_letters = set(word)

    # empty list of used letters guessed by user
    used_letters = set()

    alphabet = set(string.ascii_uppercase)

    # input from user
    chance = int(10)
    while len(word_letters) > 0:

        # ' '.join(['a', 'b', 'c']) will give us 'a b c'
        print('\n+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n'
              'You have used the following words: ', ' '.join(used_letters))
        #print(word)
        # current word
        letter_list = [letter if letter in used_letters else '_' for letter in word]
        print('Current Word (' + str(len(word)) + ' characters): ', ' '.join(letter_list))

        user_letter = input('Guess any letter: NUMBER OF CHANCES LEFT = ' + str(chance) + '\n').upper()

        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            chance -= 1
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                chance += 1
        elif user_letter in used_letters:
            print('You have guessed that letter already. TRY AGAIN')
        else:
            print('Invalid Input. TRY AGAIN')
        if chance == 0:
            print('**** YOU LOST !!! ****\nThe correct word was ' + word)
            exit()
    # gets here when word_letters == 0
    print('**** CONGRATS! YOU WON.... ****\nThe correct word is ' + word)


if __name__ == '__main__':
    hang_man()
