from Commons import *
from Synset import *
from Word import *
from wordnet import Wordnet

#Global hashes
hash1 = {}
hash2 = {}


def make_word_and_synset(name, category):
    word = Word(name=name, category=category)
    for i in wn.synsets(name):
        synset = Synset(i)
        hash2[synset.name()] = synset
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

    #Iterator to get all wordnet words
    iterator = Wordnet()
    iterator.initiliaze_lemma_list()

    try:
        #As to how many words to be processed
        for i in range(1000000):
            name = Unicode(iterator.next_word())
            #word = Word_factory(name, 'wordnet')
            word = make_word_and_synset(name, 'wordnet')
            hash1[name] = word

        raise StopIteration('Stop Iteration')
    except StopIteration as s:
        handle_error(s)
    except KeyboardInterrupt as k:
        handle_error(k)
        sys.exit(0)
    #except Exception as e:
    #    handle_error(e)
