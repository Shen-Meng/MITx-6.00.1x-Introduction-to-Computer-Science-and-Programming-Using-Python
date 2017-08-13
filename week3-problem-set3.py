#problem 1
def radiationExposure(start, stop, step):
    '''
    Computes and returns the amount of radiation exposed
    to between the start and stop times. Calls the
    function f (defined for you in the grading script)
    to obtain the value of the function at any point.

    start: integer, the time at which exposure begins
    stop: integer, the time at which exposure ends
    step: float, the width of each rectangle. You can assume that
      the step size will always partition the space evenly.

    returns: float, the amount of radiation exposed to
      between start and stop times.
    '''
    s = 0
    while stop > start:
        s += step * f(start)
        start += step
    return s


#problem 2
def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    for letter in secretWord:
        if letter not in lettersGuessed:
            return False
    return True


#problem 3
def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    output = secretWord
    for i in range(len(secretWord)):
        if secretWord[i] not in lettersGuessed:
            output = output.replace(output[i], '_')
    return str(output)


#problem 4
def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    output = ""
    for letter in string.ascii_lowercase:
        if letter not in lettersGuessed:
            output += letter
    return output


#problem 5
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
    print 'Welcome to the game, Hangman!'
    print 'I am thinking of a word that is %s letters long ' % len(secretWord)
    num = 8
    l = []
    while num > 0:
        print '------------'
        print 'You have %s guesses left ' % num
        print 'Available letters:'+getAvailableLetters(l)
        guesse = raw_input('Please guess a letter: ').lower()
        if guesse not in l:
            l.append(guesse)
            if guesse in secretWord:
                print 'Good guess: ',getGuessedWord(secretWord, l)
            else:
                num -= 1
                print 'Oops! That letter is not in my word: ',getGuessedWord(secretWord, l)
        else:
            print 'Oops! You\'ve already guessed that letter: ',getGuessedWord(secretWord, l)
        if isWordGuessed(secretWord,l):
            break
    print '------------'
    if isWordGuessed(secretWord,l):
        print 'Congratulations, you won!'
    else:
        print 'Sorry, you ran out of guesses. The word was ',secretWord