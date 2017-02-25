from Commons import *
from Synset import *
from Word import *

#Global hashes
hash1 = {}
hash2 = {}

def Syn_factory(wn_synset):
    '''
    To create appropriate subclass as per pos()
    '''
    global hash2
    pos = wn_synset.pos()
    if pos == 'n':
        #Create Noun synset
        synset = Noun_Synset(wn_synset)
        hash2[synset.name()] = synset
    elif pos == 'v':
        #Create Noun synset
        synset = Verb_Synset(wn_synset)
        hash2[synset.name()] = synset
    elif pos == 'a':
        #Create Noun synset
        synset = Adjective_Synset(wn_synset)
        hash2[synset.name()] = synset
    elif pos == 'r':
        #Create Noun synset
        synset = Adverb_Synset(wn_synset)
        hash2[synset.name()] = synset
    else:
        print 'Wrong POS tag'

def Word_factory(word, synset):
    '''
    To fill words with synset
    '''
    word.populate(synset)


if __name__ == '__main__':

    #Words loop here
    word = Word('dog', 'wordnet')
    for synset in wn.synsets(word.name()):
        Syn_factory(synset)
        Word_factory(word, synset)

    hash1[word.name()] = word

    Pickledump(hash1, 'Hash#1.pkl')
    Pickledump(hash2, 'Hash#2.pkl')

    unserialized_hash1 = Pickleload('Hash#1.pkl')
    unserialized_hash2 = Pickleload('Hash#2.pkl')
    print unserialized_hash1
    print unserialized_hash2