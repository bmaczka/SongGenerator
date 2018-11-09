import random
from nGramModel import *


# -----------------------------------------------------------------------------
# TrigramModel class ----------------------------------------------------------
# Core functions to implement: trainModel, trainingDataHasNGram, and
# getCandidateDictionary

class TrigramModel(NGramModel):

    def __init__(self):
        """
        Requires: nothing
        Modifies: self (this instance of the NGramModel object)
        Effects:  this is the TrigramModel constructor, which is done
                  for you. It allows TrigramModel to access the data
                  from the NGramModel class.
        """
        super(TrigramModel, self).__init__()

    def trainModel(self, text):
        """
        Requires: text is a list of lists of strings
        Modifies: self.nGramCounts, a three-dimensional dictionary. For
                  examples and pictures of the TrigramModel's version of
                  self.nGramCounts, see the spec.
        Effects:  this function populates the self.nGramCounts dictionary,
                  which has strings as keys and dictionaries as values,
                  where those inner dictionaries have strings as keys
                  and dictionaries of {string: integer} pairs as values.
                  Note: make sure to use the return value of prepData to
                  populate the dictionary, which will allow the special
                  symbols to be included as their own tokens in
                  self.nGramCounts. For more details, see the spec.
        """
        self.nGramCounts = {}
        lyrics = TrigramModel.prepData(self, text)
        for words in lyrics:
            for i in range(len(words) - 2):
                self.nGramCounts[words[i]] = {}

        for words in lyrics:
            for i in range(len(words) - 2):
                if self.nGramCounts.get(words[i], False):
                    self.nGramCounts[words[i]].update({words[i +1] : {}})
                else:
                    self.nGramCounts[words[i]] = {words[i + 1] : {}}

        for words in lyrics:
            for i in range(len(words) - 2 ):
                if self.nGramCounts[words[i]].get(words[i +1], False):
                    count = self.nGramCounts[words[i]][words[i+1]].get(words[i + 2], 0)
                    self.nGramCounts[words[i]][words[i+1]].update({words[i+2] : count +1})
                else:
                    self.nGramCounts[words[i]][words[i + 1]] = {words[i+2] : 1}





    def trainingDataHasNGram(self, sentence):
        """
        Requires: sentence is a list of strings, and len(sentence) >= 2
        Modifies: nothing
        Effects:  returns True if this n-gram model can be used to choose
                  the next token for the sentence. For explanations of how this
                  is determined for the TrigramModel, see the spec.
        """
        if sentence[-2] in self.nGramCounts:
            if sentence[-1] in self.nGramCounts[sentence[-2]]:
                return True
            else:
                return False
        else:
            return False

    def getCandidateDictionary(self, sentence):
        """
        Requires: sentence is a list of strings, and trainingDataHasNGram
                  has returned True for this particular language model
        Modifies: nothing
        Effects:  returns the dictionary of candidate next words to be added
                  to the current sentence. For details on which words the
                  TrigramModel sees as candidates, see the spec.
        """
        baseWord = sentence[len(sentence) - 2]
        baseWord2 = sentence[len(sentence) - 1]
        dict = {}
        dict = self.nGramCounts[baseWord][baseWord2]

        return dict


# -----------------------------------------------------------------------------
# Testing code ----------------------------------------------------------------

if __name__ == '__main__':
    text = [ ['the', 'quick', 'brown', 'fox'], ['the', 'lazy', 'dog'] ]
    sentence = [ 'the', 'black', 'brown' ]
    trigramModel = TrigramModel()
    # add your own testing code here if you like
    print trigramModel.trainModel(text)
    print trigramModel.trainingDataHasNGram(sentence)
