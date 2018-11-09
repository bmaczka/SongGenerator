import random
from nGramModel import *


# -----------------------------------------------------------------------------
# BigramModel class -----------------------------------------------------------
# Core functions to implement: trainModel, trainingDataHasNGram, and
# getCandidateDictionary

class BigramModel(NGramModel):

    def __init__(self):
        """
        Requires: nothing
        Modifies: self (this instance of the BigramModel object)
        Effects:  this is the BigramModel constructor, which is done
                  for you. It allows BigramModel to access the data
                  from the NGramModel class by calling the NGramModel
                  constructor.
        """
        super(BigramModel, self).__init__()

    def trainModel(self, text):
        """
        Requires: text is a list of lists of strings
        Modifies: self.nGramCounts, a two-dimensional dictionary. For examples
                  and pictures of the BigramModel's version of
                  self.nGramCounts, see the spec.
        Effects:  this function populates the self.nGramCounts dictionary,
                  which has strings as keys and dictionaries of
                  {string: integer} pairs as values.
                  Note: make sure to use the return value of prepData to
                  populate the dictionary, which will allow the special
                  symbols to be included as their own tokens in
                  self.nGramCounts. For more details, see the spec.
        """
        self.nGramCounts = {}
        lyrics = BigramModel.prepData(self, text)
        for words in lyrics:
            for i in range(len(words) - 1):
                self.nGramCounts[words[i]] = {}


        for words in lyrics:
            for i in range(len(words) - 1):
                if self.nGramCounts.get(words[i], False):
                    count = self.nGramCounts[words[i]].get(words[i+1] , 0)
                    self.nGramCounts[words[i]].update({words[i+1] : count + 1 })
                else:
                    self.nGramCounts[words[i]] = {words[i+1] : 1}





































    def trainingDataHasNGram(self, sentence):
        """
        Requires: sentence is a list of strings, and len(sentence) >= 1
        Modifies: nothing
        Effects:  returns True if this n-gram model can be used to choose
                  the next token for the sentence. For explanations of how this
                  is determined for the BigramModel, see the spec.
        """
        if sentence[len(sentence) - 1] in self.nGramCounts:
            return True
        else:
            return False

    def getCandidateDictionary(self, sentence):
        """
        Requires: sentence is a list of strings, and trainingDataHasNGram
                  has returned True for this particular language model
        Modifies: nothing
        Effects:  returns the dictionary of candidate next words to be added
                  to the current sentence. For details on which words the
                  BigramModel sees as candidates, see the spec.
        """
        baseWord = sentence[len(sentence) - 1]
        dict = {}
        dict2 = {}
        dict = self.nGramCounts
        dict2 = dict[baseWord]



        return dict2

# -----------------------------------------------------------------------------
# Testing code ----------------------------------------------------------------

if __name__ == '__main__':
    text = [ ['the', 'quick', 'the', 'quick'], ['the', 'lazy', 'dog'] ]
    text.append(['quick', 'brown'])
    #text = [ ['the', 'quick'], ['the', 'quick']]
    sentence = [ 'the', 'quick' ]
    bigramModel = BigramModel()
    # add your own testing code here if you like
    #print bigramModel.trainModel(text)
    #print bigramModel.trainingDataHasNGram(sentence)
    print bigramModel.getCandidateDictionary(sentence)


