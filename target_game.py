from typing import List
import random
import copy

def generate_grid() -> List[List[str]]:
    """
    Generates list of lists of letters - i.e. grid for the game.
    e.g. [['i', 'g', 'e'], ['p', 'i', 's], ['w', 'm', 'g']]
    """
    lst = ["a", "b", "c", "d", "e", "f", "g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z" ]
    output = [[], [], []]
    for i in range(3):
        for _ in range(3):
            output[i].append(random.choice(lst))
    return output

def get_words(f: str, letters: List[str]) -> List[str]:
    """
    Reads the file f. Checks the words with rules and returns a list of words.
    """
    central_letter = letters[4]
    output = []
    counter = 0
    with open(f) as dict:
        lines = dict.readlines()
        for i in range(len(lines)):
            lines[i] = lines[i].replace("\n", "")
            if len(lines[i]) >= 4 and len(lines[i]) <= 9 and lines[i].find(central_letter) != -1:
                lines[i] = lines[i].lower()
                copy = letters.copy()
                for j in range(len(lines[i])):  
                    if lines[i][j] in copy:
                        index = copy.index(lines[i][j])
                        copy[index] = ""
                        counter = counter + 1
                    if counter == len(lines[i]):
                        output.append(lines[i])
                counter = 0
    return output


def get_user_words() -> List[str]:
    """
    Gets words from user input and returns a list with these words.
    Usage: enter a word or press ctrl+d to finish.
    """
    output = []
    while True:
        try:
            answer = input()
            output.append(answer)
        except EOFError:
            break
    return output


def get_pure_user_words(user_words: List[str], letters: List[str], words_from_dict: List[str]) -> List[str]:
    """
    (list, list, list) -> list
 
    Checks user words with the rules and returns list of those words
    that are not in dictionary.
    """
    central_letter = letters[4]
    output = []
    counter = 0
    for k in len(user_words):
        if user_words[k] not in words_from_dict:
            if len(user_words[k]) >= 4 and len(user_words[k]) <= 9 and user_words[k].find(central_letter) != -1:
                user_words[k] = user_words[k].lower()
                copy = letters.copy()
                for j in range(len(user_words[k])):  
                    if user_words[k][j] in copy:
                        index = copy.index(user_words[k][j])
                        copy[index] = ""
                        counter = counter + 1
                    if counter == len(user_words[k]):
                        output.append(user_words[k])
                counter = 0
    return output

def results():
    pass
