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

    #All types of synsets have same property
    if wn_synset.hypernyms():
        #Filling Hypernyms
        custom_synsets = Synsets(wn_synset.hypernyms())
        synset.populate('hypernyms', custom_synsets)

    if wn_synset.hyponyms():
        #Filling Hyponyms
        custom_synsets = Synsets(wn_synset.hyponyms())
        synset.populate('hyponyms', custom_synsets)

    if wn_synset.entailments():
        #Filling Entailments
        custom_synsets = Synsets(wn_synset.entailments())
        synset.populate('entailments', custom_synsets)

    if wn_synset.similar_tos():
        #Filling Similar Tos
        custom_synsets = Synsets(wn_synset.similar_tos())
        synset.populate('similar', custom_synsets)

    if wn_synset.part_holonyms():
        #Filling Part Holonyms
        custom_synsets = Synsets(wn_synset.part_holonyms())
        synset.populate('holonyms', custom_synsets)

    if wn_synset.substance_holonyms():
        #Filling Substance Holonyms
        custom_synsets = Synsets(wn_synset.substance_holonyms())
        synset.populate('holonyms', custom_synsets)

    if wn_synset.member_holonyms():
        #Filling Member Holonyms
        custom_synsets = Synsets(wn_synset.member_holonyms())
        synset.populate('holonyms', custom_synsets)

    if wn_synset.part_meronyms():
        #Filling Part Meronyms
        custom_synsets = Synsets(wn_synset.part_meronyms())
        synset.populate('meronyms', custom_synsets)

    if wn_synset.substance_meronyms():
        #Filling Substance Meronyms
        custom_synsets = Synsets(wn_synset.substance_meronyms())
        synset.populate('meronyms', custom_synsets)

    if wn_synset.member_meronyms():
        #Filling Member Meronyms
        custom_synsets = Synsets(wn_synset.member_meronyms())
        synset.populate('meronyms', custom_synsets)

def Synsets(data):
    '''
    Returns custom synset objects names present in hash
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

if __name__ == '__main__':
    hash2 = Shelveopen('Hash#2.shelve')
    try:
        for synset in hash2.values():
            Hashprocess(synset)

            #Replace in Hash
            hash2[synset.name()] = synset
            count += 1  #to keep track of updates
        raise StopIteration
    except StopIteration as s:
        Error(s)
    except KeyboardInterrupt as k:
        Error(k)
        sys.exit(0)
    except Exception as e:
        Error(e)