from collections import Counter
from Commons import *
import time

# Globals
hash1 = {}
hash2 = {}
hash3 = {}
hash4 = {}
wordsnotinhsah = 0
count_synsets = 0
count_words = 0

def Wordfactory():
	'''
	To create word of fixed format
	'''
	dic = {}
	dic['W2S'] = {}
	dic['D2S'] = {}
	dic['E2S'] = {}
	return dic

def Synfactory(synset):
	'''
	To create synset of fixed formats
	'''
	dic = {}
	dic['S2W'] = synset.lemma_names()
	dic['S2E'] = []
	dic['S2D'] = Process_sentence(synset.definition())
	dic['Hypernym'] = synset.hypernyms()
	dic['Hyponym'] = synset.hyponyms()
	dic['Meronym'] = synset.meronyms()
	dic['Holonym'] = synset.holonyms()
	dic['Entailment'] = synset.similar_tos()
	dic['Similar'] = synset.entailments()
	if synset.examples():	#checking if examples actually exist
		dic['S2E'] = Process_sentence(synset.examples()[0])	#Choosing only first example
	return dic

def Createwords(word, kind, synset, count):
	'''
	To create and store words in hash, or add if words already exist
	'''
	global count_words, wordsnotinhsah

	if word in hash3:
		# Word exists so just add property
		# Updating Shelve, is tedious
		dic = hash3[word]
		dic[kind][synset] = count
		hash3[word] = dic
		# Updated Shelve
	else:
		# Word does not exist so create a new one
		# Just a check for morphological parsing later
		if word not in hash1:
			print 'WordNot in Hash : ',word
			wordsnotinhsah += 1
			# Obtain their morphological form present in wordnet to create same entry for that also
		
		count_words += 1
		dic = Wordfactory()
		dic[kind][synset] = count
		hash3[word] = dic

def Process_words(synset, definition, example):
	'''
	Process all 3 forms of words in a synset
	'''
	# Create Lemma Words
	for i, lemma in enumerate(synset.lemma_names()):
		count = synset.lemma_count()[i]
		Createwords(lemma, 'W2S', synset.name(), count)

	# Creating Definition words
	for word in definition:
		Createwords(word[0], 'D2S', synset.name(), word[1])

	# Creating Example words
	for word in example:
		Createwords(word[0], 'E2S', synset.name(), 1) # Doesn't really matter as how many times word occurs in synset examples, as edge not gonna be traversed for calculation

def Process_sentence(sentence):
	'''
	To process sentences to required tuple 
	'''
	ls = Purify(sentence, hash1)
	total = len(ls)	# Getting total words after stop words removal
	ls = dict(Counter(ls))	# Getting count of words in a list

	# Creating tuples of proper format
	tup = []
	for key, value in ls.items():
		tup.append((key, value, total))
	return tup

def Handle_error(e):
	'''
	Displays error and closes all shelves
	'''
	print 'Error - ',e
	print 'Words Processed - ', count_words
	print 'Synsets Processed - ', count_synsets
	print 'Words More than Hash1 - ', wordsnotinhsah 
	Shelveclose(hash1)
	Shelveclose(hash2)
	Shelveclose(hash3)
	Shelveclose(hash4)
	print 'ComputeGraph Computation took : ',time.time() - start_time

def Showhash(open_hash):
	'''
	To print Some part of hash
	'''
	for key, value in open_hash.items():
		print key, ' :: ', value

if __name__ == '__main__':
	start_time = time.time()
	hash1 = Shelveopen('Hash#1.shelve')
	hash2 = Shelveopen('Hash#2.shelve')
	hash3 = Shelveopen('Hash#3.shelve')
	hash4 = Shelveopen('Hash#4.shelve')
	morpho = Shelveopen('Morpho.shelve')

	# Clearing all previous logs and data
	hash3.clear()
	hash4.clear()
	morpho.clear()
	Filedump('NonMorphed.log','',False)

	# Showhash(hash3)
	try:
		for key, value in hash2.items():
			count_synsets += 1
			synset = Synfactory(value)

			if count_synsets % 10000 == 0:
				log = '******Synsets Computed : '+str(count_synsets)+' ******'
				Filedump('NonMorphed.log',log)
			
			# Enter Into Hash4
			hash4[key] = synset

			# Just process Words now
			Process_words(value, synset['S2D'], synset['S2E'])
		raise StopIteration
	except Exception as e:
		Handle_error(e)