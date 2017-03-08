import sys
import shelve
from wordnet import Wordnet
from Commons import Unicode
from nltk.corpus import wordnet as wn
try:
    import cPickle as pickle
except:
    import pickle

all_lemmas = list()

def handle_1():
    output = open('all_lemmas.pkl','wb')
    pickle.dump(all_lemmas,output,-1)
    output.close()

if __name__ == "__main__":
    #print sys.argv[1]
    if sys.argv[1] == 'create_lemmas_list':
        iterator = Wordnet()
        iterator.initiliaze_lemma_list()
        try:
            for i in range(1000000):
                name = Unicode(iterator.next_word())
                all_lemmas.append(name)
            raise StopIteration('Exited for loop')
        except StopIteration:
            handle_1()
    else:
        print 'here'

    if sys.argv[1] == '2':
        hash1 = shelve.open('Hash#1.shelve') #open without 'writeback=True'; faster
        all_lemmas = pickle.load(open('all_lemmas.pkl','rb'))
        for lemma_name in all_lemmas:
            hash1 = shelve.open('Hash#1.shelve')
            assert hash1.has_key(lemma_name)
            word = hash1[lemma_name]

            wn.synsets(lemma_name)
