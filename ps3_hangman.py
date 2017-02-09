# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
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

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # Defines counter
    counter = 0
    
    #If a letters in lettersGuessed matches a letter in secretWord then counter +1
    for guessLetter in lettersGuessed:
        if guessLetter in secretWord:
            counter += 1
    
    #If counter matches the lenght of secretWord returns True else return False
    if counter == len(secretWord):
        return True
    else:
        return False



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # If a letter in secretWord is not in lettersGuessed then replaces it with '_ '
    for secretLetter in secretWord:
        if secretLetter not in lettersGuessed:
            secretWord = secretWord.replace(secretLetter, '_ ')

    # Removes the space at the end of the string and returns secretWord  
    if secretWord[-1] == ' ':
       secretWord = secretWord.strip()
    return secretWord



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    
    # Goes through lettersGuessed and if guessLetter is in alphabet then removes that letter
    for guessLetter in lettersGuessed:
        if guessLetter in alphabet:
            alphabet = alphabet.replace(guessLetter, '')
    return alphabet
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    guesses = -1
    lettersGuessed = []
    
    if guesses < 0:
	    print('Welcome to the game Hangman!')
	    print('I am thinking of a word that is', len(secretWord), 'letters long.')
	    print('-----------')
	    guesses = 8
	
    while guesses <= 8 and guesses > 0:
        print('You have', guesses, 'guesses left')
        print('Available Letters:', getAvailableLetters(lettersGuessed))
        guessLetter = input('Please guess a letter: ')
        guessInLowerCase = guessLetter.lower()
        if guessInLowerCase in lettersGuessed:
            print("Oops! You've already guessed that letter:", getGuessedWord(secretWord, lettersGuessed))
            print('-----------')
        elif guessInLowerCase not in lettersGuessed: 
            lettersGuessed.append(guessInLowerCase)
            
            
            if lettersGuessed[-1] in secretWord:
                print('Good guess:',getGuessedWord(secretWord, lettersGuessed))
                print('-----------')
                if lettersGuessed[-1] in secretWord and getGuessedWord(secretWord, lettersGuessed) == secretWord:
                    print('Congratulations, you won!')
                    break
            
            elif lettersGuessed[-1] not in secretWord:
                print('Oops! That letter is not in my word:',getGuessedWord(secretWord, lettersGuessed))
                print('-----------')
                guesses -= 1
            
            
    if guesses == 0:
        print('Sorry, you ran out of guesses. The word was', secretWord+'.')
        


# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
#secretWord = 'star'
secretWord = secretWord.lower()
hangman(secretWord)

