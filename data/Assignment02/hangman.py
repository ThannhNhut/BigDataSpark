# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string
import enum 

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    return set(letters_guessed).issuperset(set(secret_word))



def get_guessed_word(secret_word, letters_guessed):
    words_show = set(secret_word).intersection(set(letters_guessed))
    result = ""
    temp = []
    for i in list(secret_word):
        if(set(i).issubset(words_show)):
            temp.append(i)
        else:
            temp.append(" _ ")
    return result.join(temp)


def get_available_letters(letters_guessed):
    words_show = set(string.ascii_lowercase).intersection(set(letters_guessed))
    temp = []
    result = ""
    for i in list(string.ascii_lowercase):
        if(not set(i).issubset(words_show)):
            temp.append(i)
    return result.join(temp)
    
class ErrorCode(enum.Enum):
    Early_Hints = 103 #gợi ý sớm
    Ok = 200 #ok
    Forbidden = 403 #bị cấm
    Not_Acceptable = 406 #Không thể chấp nhận
    Conflict = 409 #Xung đột
    Gone = 410 #đã qua
    Length_Required = 411 #Độ dài Yêu cầu
    

def check_input(input_string, secret_word, letters_guessed):
    if str.isalpha(str(input_string)):
        input_string_lower = str.lower(input_string)
        vowels = {"a","e","i","o","u"}
        if set(input_string_lower).issubset(set(letters_guessed)):
            return ErrorCode.Gone.value #410 -1
        else:
            if set(input_string_lower).issubset(set(secret_word)):
                return ErrorCode.Ok.value # 200 0
            else:
                if set(input_string_lower).issubset(vowels):
                    return ErrorCode.Conflict.value #409 -2
                else:
                    return ErrorCode.Not_Acceptable.value #406 -1
    else:
        if str(input_string) == "*":
            return ErrorCode.Early_Hints.value #103
        return ErrorCode.Forbidden.value #403 -1
    
    

def hangman(secret_word):
    guesses_remaining = 6
    letters_guessed = []
    warnings_remaining = 3
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is " + str(len(secret_word)) + " letters long.")
    print("You have " + str(warnings_remaining) + " warnings left.")

    while guesses_remaining != 0 and not is_word_guessed(secret_word,letters_guessed):
        print("-------------")
        print("You have " + str(guesses_remaining) + " guesses left")
        print("Available letters: "+ get_available_letters(letters_guessed))
        word_guessed = input("Please guess a letter: ")
        if check_input(word_guessed, secret_word, letters_guessed) == 103:
            print("Possible word matches are: ")
            show_possible_matches(get_guessed_word(secret_word, letters_guessed))
        elif check_input(word_guessed, secret_word, letters_guessed) == 200:
            letters_guessed.append(str.lower(word_guessed))
            print("Good guess: " + get_guessed_word(secret_word, letters_guessed))
        elif check_input(word_guessed, secret_word, letters_guessed) == 409:
            letters_guessed.append(str.lower(word_guessed))
            guesses_remaining -= 2
            print("Oops! That letter is not in my word: " + get_guessed_word(secret_word, letters_guessed))
        elif check_input(word_guessed, secret_word, letters_guessed) == 406:
            letters_guessed.append(str.lower(word_guessed))
            guesses_remaining -= 1
            print("Oops! That letter is not in my word: " + get_guessed_word(secret_word, letters_guessed))
        elif warnings_remaining > 0:
            if check_input(word_guessed, secret_word, letters_guessed) == 410:
                warnings_remaining -= 1
                print("Oops! You've already guessed that letter. You have " + str(warnings_remaining) + " warnings left: " + get_guessed_word(secret_word, letters_guessed))
            if check_input(word_guessed, secret_word, letters_guessed) == 403:
                warnings_remaining -= 1
                print("Oops! That is not a valid letter. You have " + str(warnings_remaining) + " warnings left: " + get_guessed_word(secret_word, letters_guessed))
        else:
            guesses_remaining -= 1
            print("Oops! You've already guessed that letter. You have no warnings left so you lose one guess: " + get_guessed_word(secret_word, letters_guessed))
    if not is_word_guessed(secret_word,letters_guessed):
         print("-----------")
         print("Sorry, you ran out of guesses. The word was else.")
    else:
        print("-----------")
        print("Congratulations, you won!")
        print("Your total score for this game is: "+str(guesses_remaining *  len(secret_word)))
        

# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    my_word_not_space = my_word.replace(" ","")
    my_word_not_underscore_space = my_word_not_space.replace("_","")
    if len(my_word_not_space) == len(other_word) and not set(other_word).difference(set(my_word_not_underscore_space)) == set() and set(my_word_not_underscore_space).difference(set(other_word)) == set():
        for i in range(0,len(my_word_not_space)):
            if my_word_not_space[i] == other_word[i]:
                continue
            elif my_word_not_space[i] == "_" and other_word[i] not in set(my_word_not_underscore_space):
                continue
            else:
                return False
        return True
    return False



def show_possible_matches(my_word):
    no_match = True
    for i in wordlist:
        if match_with_gaps(my_word, i):
            no_match = False
            print(i, end=' ')
    if no_match:
        print('No matches found')



def hangman_with_hints(secret_word):
    hangman(secret_word)



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
