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

def handle_keyboard_interrupt():
    print 'Keyboard interrupt, saving all files, exiting'
    Pickledump(hash1, 'Hash#1.pkl')
    Pickledump(hash2, 'Hash#2.pkl')
    #label_to_word_object.close()

def handle_stop_iteration():
    print 'All words done, saving all files, exiting'
    Pickledump(hash1, 'Hash#1.pkl')
    Pickledump(hash2, 'Hash#2.pkl')

def print_dictionary(filename):
	unserialized_hash = Pickleload(filename)
	print unserialized_hash

if __name__ == '__main__':

	#print_dictionary(filename='Hash#1.pkl')

    #Words loop here
    wordnet = Wordnet(make_words_and_synsets)
    wordnet.initiliaze_lemma_list()
    while True:
        try:
            wordnet.get_word()
        except StopIteration as e:
            handle_stop_iteration()
        except KeyboardInterrupt:
        	handle_keyboard_interrupt()
        	sys.exit(0)
