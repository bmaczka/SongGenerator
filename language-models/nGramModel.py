import random
import sys
sys.path.append('../data')
from data.musicData import *

# -----------------------------------------------------------------------------
# NGramModel class ------------------------------------------------------------
# Core functions to implement: prepData, weightedChoice, and getNextToken
# Reach functions to implement: getNextNote

class NGramModel(object):

    def __init__(self):
        """
        Requires: nothing
        Modifies: self (this instance of the NGramModel object)
        Effects:  This is the NGramModel constructor. It sets up an empty
                  dictionary as a member variable. It is called from the
                  constructors of the NGramModel child classes. This
                  function is done for you.
        """
        self.nGramCounts = {}

    def __str__(self):
        """
        Requires: nothing
        Modifies: nothing
        Effects:  returns the string to print when you call print on an
                  NGramModel object. This function is done for you.
        """
        return 'This is an NGramModel object'

    def prepData(self, text):
        # type: (object) -> object
        """
        Requires: text is a list of lists of strings
        Modifies: nothing
        Effects:  returns a copy of text where each inner list starts with
                  the symbols '^::^' and '^:::^', and ends with the symbol
                  '$:::$'. For example, if an inner list in text were
                  ['hello', 'goodbye'], that list would become
                  ['^::^', '^:::^', 'hello', 'goodbye', '$:::$'] in the
                  returned copy.
                  Make sure you are not modifying the original text
                  parameter in this function.
        """
        textCopy = []
        textCopy = text[:]
        for row in textCopy:
                row.insert(0,'^:::^')
                row.insert(0,'^::^')
        for row in textCopy:
                row.append('$:::$')



        # add the rest of your prepData implementation here

        return textCopy

    def trainModel(self, text):
        """
        Requires: text is a list of lists of strings
        Modifies: self.nGramCounts
        Effects:  this function populates the self.nGramCounts dictionary.
                  It does not need to be modified here because you will
                  override it in the NGramModel child classes according
                  to the spec.
        """
        return

    def trainingDataHasNGram(self, sentence):
        """
        Requires: sentence is a list of strings, and trainingDataHasNGram
                  has returned True for this particular language model
        Modifies: nothing
        Effects:  returns a bool indicating whether or not this n-gram model
                  can be used to choose the next token for the current
                  sentence. This function does not need to be modified because
                  you will override it in NGramModel child classes according
                  to the spec.
        """
        return False

    def getCandidateDictionary(self, sentence):
        """
        Requires: sentence is a list of strings
        Modifies: nothing
        Effects:  returns the dictionary of candidate next words to be added
                  to the current sentence. This function does not need to be
                  modified because you will override it in the NGramModel child
                  classes according to the spec.
        """
        return {}

    def weightedChoice(self, candidates):
        """
        Requires: candidates is a dictionary; the keys of candidates are items
                  you want to choose from and the values are integers
        Modifies: nothing
        Effects:  returns a candidate item (a key in the candidates dictionary)
                  based on the algorithm described in the spec.
        """
        token = candidates.keys()
        values = candidates.values()
        total = 0
        culm = []
        for i in values:
            total += i
            culm.append(total)
        randomize = random.randrange(0, max(culm))
        for x in culm:
            if x > randomize:
                index = culm.index(x)
                return token[index]




    def getNextToken(self, sentence):
        """
        Requires: sentence is a list of strings, and this model can be used to
                  choose the next token for the current sentence
        Modifies: nothing
        Effects:  returns the next token to be added to sentence by calling
                  the getCandidateDictionary and weightedChoice functions.
                  For more information on how to put all these functions
                  together, see the spec.
        """
        value1 = self.getCandidateDictionary(sentence)
        value2 = self.weightedChoice(value1)
        return value2

    def getNextNote(self, musicalSentence, possiblePitches):
        """
        Requires: musicalSentence is a list of PySynth tuples,
                  possiblePitches is a list of possible pitches for this
                  line of music (in other words, a key signature), and this
                  model can be used to choose the next note for the current
                  musical sentence
        Modifies: nothing
        Effects:  returns the next note to be added to the "musical sentence".
                  For details on how to do this and how this will differ
                  from the getNextToken function from the core, see the spec.
                  Please note that this function is for the reach only.
        """
        alldict = {}
        listofkeys = []
        justnote = 'string'
        secondList = {}
        alldict = self.getCandidateDictionary(musicalSentence)
        listofkeys = alldict.keys()
        for note in listofkeys:
            if note == '$:::$':
                secondList[note] = alldict[note]
            else:
                justnote = note[0]
                list1 = justnote.split(justnote[-1])
                if list1[0] in possiblePitches:
                    secondList[note] = alldict[note]

        if bool(secondList):
            return self.weightedChoice(secondList)
        else:
            pitch = str(random.choice(possiblePitches)) + '4'
            duration = random.choice(NOTE_DURATIONS)
            return (pitch, duration)


# -----------------------------------------------------------------------------
# Testing code ----------------------------------------------------------------

if __name__ == '__main__':
    text = [ ['the', 'quick', 'brown', 'fox'], ['the', 'lazy', 'dog'] ]
    choices = { 'the': 2, 'quick': 1, 'brown': 1 }
    nGramModel = NGramModel()
    # add your own testing code here if you like


