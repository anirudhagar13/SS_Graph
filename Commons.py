from nltk.corpus import wordnet as wn
import pickle
import shelve
import sys

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