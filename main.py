# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import random
from termcolor import colored

def import_words(fileloc, word_len=5):
    with open(fileloc, "r", encoding="utf-8") as f:
        words = f.read().split("\n")
        words = [x for x in words if len(x) == word_len]
        print(len(words), " words imported from ", fileloc)
        return words


def match_check(word, guess):
    result = [None] * len(word)
    for i in range(len(word)):

        if word[i] == guess[i]:
            result[i] = 1

        elif guess[i] in word:
            result[i] = 0

        else:
            result[i] = -1
    return result

# main
if __name__ == '__main__':
    word_len = 5
    termimal_colours = {1:"green",0:"yellow",-1:"red"}
    used_char = set()
    words = import_words("words_tr.txt", word_len=word_len)
    random_w = random.choice(words)
    words = set(words)
    print(random_w)
    guess = ""
    matches = [0]
    print("Start guessing the word:")
    while(sum(matches) != word_len):
        guess = ""
        while(True):
            guess = input()
            if len(guess) != 5:
                print("Your guess does not fit")
            elif(guess not in words):
                print("Not a word")

            else:
                break



        matches = match_check(random_w,guess)
        for i in range(word_len):
            print(colored(guess[i],termimal_colours[matches[i]]),end="")
        print("\n------------")
