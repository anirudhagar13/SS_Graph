from Commons import *
from Synset import *
from Word import *
from Wordnet import *

#Global hashes
hash1 = {}
hash2 = {}

def Syn_factory(wn_synset):
    '''
    To create appropriate subclass as per pos()
    '''
    global hash2
    synset = Synset(wn_synset)
    hash2[synset.name()] = synset
    return synset

def Word_factory(name, category):
    '''
    Process all synsets of words before hash insertion
    '''
    word = Word(name=name, category=category)
    synsets = wn.synsets(name)
    for wn_synset in synsets:
        synset = Syn_factory(wn_synset)
        word.populate(synset)
    return word

def handle_error(error):
    print 'Error - ',error

    print 'Words Processed - ',len(hash1.keys())
    print 'Synset Processed - ',len(hash2.keys())
    Shelveclose(hash1)
    Shelveclose(hash2)

def print_hash(filename):
	unserialized_hash = Shelveopen(filename)
	print len(unserialized_hash.keys())

if __name__ == '__main__':
	# print_hash(filename='Hash#2.shelve')

    #Feed Hashes
    hash1 = Shelveopen('Hash#1.shelve')
    hash2 = Shelveopen('Hash#2.shelve')
    hash1.clear()   # Overwriting
    hash2.clear()   # Overwriting

    #Iterator to get all wordnet words
    iterator = Wordnet()
    iterator.initiliaze_lemma_list()

    try:
        #As to how many words to be processed
        for i in range(1000000):
            name = Unicode(iterator.next_word()).lower()
            word = Word_factory(name, 'wordnet')
            hash1[name] = word

        raise StopIteration('Stop Iteration')
    except StopIteration as s:
        handle_error(s)
    except KeyboardInterrupt as k:
        handle_error(k)
        sys.exit(0)
    except Exception as e:
        handle_error(e)