from Commons import *
from Synset import *
from Word import *
from wordnet_script import Wordnet

#Global hashes
hash1 = {}
hash2 = {}

def make_words_and_synsets(word):
    new_word = Word(name=word,category='wordnet')
    word = Unicode(word)
    for wn_synset in wn.synsets(word):
        pos = Unicode(wn_synset.pos())
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

def handle_error(error):
    if error == 'Stop':
        print 'Words done, closing Hash !'
    elif error == 'Key':
        print 'Key Interrupt, closing Hash !'
    else:
        print 'Some Other Exception !'

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

    wordnet = Wordnet(make_words_and_synsets)
    wordnet.initiliaze_lemma_list()
    while True:
        try:
            wordnet.get_word()
        except StopIteration as e:
            handle_error('Stop')
        except KeyboardInterrupt:
            handle_error('Key')
            sys.exit(0)
        except Exception:
            handle_error('Other')
