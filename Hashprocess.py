from Commons import *

#Global hash
hash2 = {}
count = 0

def Hashprocess(synset):
    '''
    To Process each Hashentry one by one
    '''
    #Initialize wordnet object for property access
    wn_synset = wn.synset(synset.name())
    pos = Unicode(synset.pos())
    if pos == 'n':
        Nounhash(wn_synset, synset)
    elif pos == 'v':
        Verbhash(wn_synset, synset)
    elif pos == 'a':
        Adjhash(wn_synset, synset)
    elif pos == 'r':
        Advhash(wn_synset, synset)
    elif pos == 's':
        pass
    else:
        print 'wrong pos here'

def Synsets(data):
    '''
    Returns custom synset objects from hash
    '''
    global hash2
    custom_synsets = list()
    for wn_synset in data:
        name = Unicode(wn_synset.name())

        #Filling only properties which exist in hash
        if name in hash2:
            custom_synsets.append(name)

    return custom_synsets

def Error(error):
    '''
    To handle midway processing stop
    '''
    global count
    print 'Error - ',error
    print 'Hash Updated - ',count
    Shelveclose(hash2)

def Nounhash(wn_synset, synset):
    '''
    Fixed property template for Noun_Synsets
    '''
    if wn_synset.hypernyms():
        #Filling Hypernyms
        custom_synsets = Synsets(wn_synset.hypernyms())
        synset.populate('hypernyms', custom_synsets)

    if wn_synset.hyponyms():
        #Filling Hyponyms
        custom_synsets = Synsets(wn_synset.hyponyms())
        synset.populate('hyponyms', custom_synsets)

    # if wn_synset.meronyms():
    #     #Filling meronyms
    #     custom_synsets = Synsets(wn_synset.meronyms())
    #     synset.populate('meronyms', custom_synsets)

    # if wn_synset.holonyms():
    #     #Filling holonyms
    #     custom_synsets = Synsets(wn_synset.holonyms())
    #     synset.populate('holonyms', custom_synsets)

def Verbhash(wn_synset, synset):
    '''
    Fixed property template for Verb_Synsets
    '''
    if wn_synset.hypernyms():
        #Filling Hypernyms
        custom_synsets = Synsets(wn_synset.hypernyms())
        synset.populate('hypernyms', custom_synsets)

    if wn_synset.hyponyms():
        #Filling Hyponyms
        custom_synsets = Synsets(wn_synset.hyponyms())
        synset.populate('hyponyms', custom_synsets)

    if wn_synset.entailments():
        #Filling Hypernyms
        custom_synsets = Synsets(wn_synset.entailments())
        synset.populate('entailments', custom_synsets)

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

if __name__ == '__main__':
    hash2 = Shelveopen('Hash#2.shelve')
    try:
        for synset in hash2.values():
            Hashprocess(synset)

            #Replace in Hash
            hash2[synset.name()] = synset
            count += 1  #to keep track of updates
        raise StopIteration('Stop Iteration')
    except StopIteration as s:
        Error(s)
    except KeyboardInterrupt as k:
        Error(k)
        sys.exit(0)
    except Exception as e:
        Error(e)
