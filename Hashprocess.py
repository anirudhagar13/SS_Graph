from Commons import *

#Global hash
hash2 = {}

def Hashprocess():
    '''
    To Process each Hashentry one by one
    '''
    global hash2
    hash2 = Pickleload('Hash#2.pkl')

    for synset in hash2.values():
        #Initialize wordnet object for property access
        wn_synset = wn.synset(synset.name())

        if synset.pos() == 'n':
            Nounhash(wn_synset, synset)
        elif synset.pos() == 'v':
            Verbhash(wn_synset, synset)
        elif synset.pos() == 'a':
            Adjhash(wn_synset, synset)
        elif synset.pos() == 'r':
            Advhash(wn_synset, synset)
        else:
            print 'Wrong POS tag !'

def Synsets(data):
    '''
    Returns custom synset objects from hash
    '''
    custom_synsets = list()
    for wn_synset in data:
        name = wn_synset.name()

        #Filling only properties which exist in hash
        if name in hash2:
            custom_synsets.append(hash2[name])

    return custom_synsets

def Nounhash(wn_synset, synset):
    '''
    Fixed property template for Noun_Synsets
    '''
    #Filling Hypernyms
    custom_synsets = Synsets(wn_synset.hypernyms())
    synset.populate('hypernyms', custom_synsets)

    #Filling Hyponyms
    custom_synsets = Synsets(wn_synset.hyponyms())
    synset.populate('hyponyms', custom_synsets)

def Verbhash(wn_synset, synset):
    '''
    Fixed property template for Verb_Synsets
    '''
    pass

def Adjhash(wn_synset, synset):
    '''
    Fixed property template for Adjective_Synsets
    '''
    pass

def Advhash(wn_synset, synset):
    '''
    Fixed property template for Adverb_Synsets
    '''
    pass

def Hashaccess(data):
    '''
    Return hashed values for W_synsets
    '''
    return [hash2[x] for x in data]

if __name__ == '__main__':
    Hashprocess()

    #Load update Hash
    Pickledump(hash2, 'Hash#2.pkl')