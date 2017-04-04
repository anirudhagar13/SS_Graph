from nltk.corpus import wordnet as wn
from nltk.stem import WordNetLemmatizer as WL
import difflib
import pickle
import shelve
import sys
import math


StopWords = ['a', 'has', 'such', 'accordance', 'have', 'suitable', 'according', 'having', 'than', 'all', 'herein', 'that', 'also', 'however', 'the', 'an', 'if', 'their', 'and', 'in', 'then', 'another', 'into', 'there', 'are', 'invention', 'thereby', 'as', 'is', 'therefore', 'at', 'it', 'thereof', 'be', 'its', 'thereto', 'because', 'means', 'these', 'been', 'not', 'they', 'being', 'now', 'this', 'by', 'of', 'those', 'claim', 'on', 'thus', 'comprises', 'onto', 'to', 'corresponding', 'or', 'use', 'could', 'other', 'various', 'described', 'particularly', 'was', 'desired', 'preferably', 'were', 'do', 'preferred', 'what', 'does', 'present', 'when', 'each', 'provide', 'where', 'embodiment', 'provided', 'whereby', 'fig', 'provides', 'wherein', 'figs', 'relatively', 'which', 'for', 'respectively', 'while', 'from', 'said', 'who', 'further', 'should', 'will', 'generally', 'since', 'with', 'had', 'some', 'would']

def Unicode(data):
        '''
        To remove Unicode from list of elements
        '''
        #Check if received is string
        if isinstance(data, (str, unicode)):
            return str(data).lower()
        else:
            return [str(x).lower() for x in data]

def Pickledump(data, file):
    '''
    Store data (serialize)
    '''
    with open(file, 'wb') as handle:
        pickle.dump(data, handle)

def Pickleload(file):
    '''
    Load data (deserialize)
    '''
    with open(file, 'rb') as handle:
        unserialized_data = pickle.load(handle)
        return unserialized_data

def Shelveopen(filename):
    '''
    Open shelve dictionary
    '''
    return shelve.open('Shelves/'+filename)

def Shelveclose(shelve):
    '''
    close shelve dictionary
    '''
    shelve.close()

def computeMinMax(minVal,maxVal,ratio):
    if ratio == 1:
        return 1.2*maxVal
    else:
        return minVal + (maxVal - minVal) * (-1/math.log(ratio,2))

def Morphoparse(word):
    # To Give back root word existent in Wordnet
    lemmatizer = WL()
    lemmatized = Unicode(lemmatizer.lemmatize(word))
    if lemmatized != word:
        return lemmatized
    else:
        synsets = wn.synsets(word)
        if synsets:
            lemmas = Unicode(synsets[0].lemma_names())
            similars = difflib.get_close_matches(word,lemmas)
            if similars:
                return similars[0]
            else: 
                return lemmas[0]
        else:
            # Can't Do Anything
            # with open('Shelves/WordDump.txt','a') as file:
            #     file.write(word + "\n")
            return word

if __name__ == '__main__':
    print Morphoparse('adpositions')