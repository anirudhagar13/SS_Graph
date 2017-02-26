from Commons import *
from Synset import *
from Word import *
from wordnet_script import Wordnet
import sys

#Global hashes
hash1 = {}
hash2 = {}

def make_words_and_synsets(word):
	new_word = Word(name=word,category='wordnet')
	word = str(word)
	global hash2
	for wn_synset in wn.synsets(word):
		pos = str(wn_synset.pos())
		if pos == 'n':
			#Create Noun synset
			synset = Noun_Synset(wn_synset)
			hash2[synset.name()] = synset
		elif pos == 'v':
			#Create Verb synset
			synset = Verb_Synset(wn_synset)
			hash2[synset.name()] = synset
		elif pos == 'a':
			#Create Adjective synset
			synset = Adjective_Synset(wn_synset)
			hash2[synset.name()] = synset
		elif pos == 'r':
			#Create Adverb synset
			synset = Adverb_Synset(wn_synset)
			hash2[synset.name()] = synset
		elif pos == 's':
			#print 'Not yet decided!'
			pass
		else:
			print 'Wrong POS tag'

	hash1[word] = new_word

if __debug__:
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
else:
	print 'Syn_factory not executing'

def Word_factory(word, synset):
    '''
    To fill words with synset
    '''
    word.populate(synset)

def handle_error():
    print 'Words done, closing dictionary'
    Shelveclose(hash2)
    Shelveclose(hash1)

def print_dictionary(filename):
	unserialized_hash = Pickleload(filename)
	print unserialized_hash

if __name__ == '__main__':
    '''
	print_dictionary(filename='Hash#1.pkl')
	'''
    #Words loop here
    hash1 = Shelveopen('Hash#1.shelve')
    hash2 = Shelveopen('Hash#2.shelve')
    wordnet = Wordnet(make_words_and_synsets)
    wordnet.initiliaze_lemma_list()
    while True:
        try:
            wordnet.get_word()
        except StopIteration as e:
            handle_error()
        except KeyboardInterrupt:
        	handle_error()
        	sys.exit(0)