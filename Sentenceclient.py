from Wordclient import *
from Hypers import alpha
import operator

class Sentenceclient:
	def __init__(self, sentence1, sentence2):
		wordhash = Shelveopen('Hash#1.shelve')
		self.sent1 = Purify(sentence1, wordhash)	# Sending Hash from here as prevents opening and closing again n again
		self.sent2 = Purify(sentence2, wordhash)
		self.wordset = []
		# Deduplication while preserving order
		for word in self.sent1+self.sent2:
			if word not in self.wordset:
				self.wordset.append(word)
		self.semantic_vectors = [] # To store of both sentences
		self.order_vectors = [] # To store order vectors of both sentences
		self.threshold = 0.001 # To decide if something is not at all similar
		self.pathacc = {} # To accumulate all paths after crawling
		self.wordmap = [[],[]] #  # Words of Sentence1 found in Sentence2 & vice-versa

	def Getsemantics(self):
		'''
		To access semantic vectors
		'''
		if self.semantic_vectors == []:
			# Vectors haven't been created yet
			self.Createvectors()

		else:
			return self.semantic_vectors

	def getPathsacc(self):
		'''
		Getter for accumulation of paths
		'''
		return self.pathacc

	def getWordmap(self):
		'''
		Getter for accumulation of paths
		'''
		return self.wordmap

	def Getorder(self):
		'''
		To access order vectors
		'''
		if self.order_vectors == []:
			# Vectors haven't been created yet
			self.Createvectors()

		else:
			return self.order_vectors

	def Createvectors(self):
		'''
		To create semantic vectors
		'''
		sem1 = []
		sem2 = []
		ord1 = []
		ord2 = []
		ls2 = []

		# For First document
		for i, word in enumerate(self.wordset):
			allpaths = []
			allscores = []
			if word in self.sent1:
				sem1.append(1) # No Semantic Match needed
				ord1.append(i+1)
			else:
				wc = Wordclient(word)
				for key in self.sent1:
					wc.init_client(key)
					score = wc.getmetric()

					if score > 0:
						# Some Semantic Match
						self.Updatepath(word, wc.getpaths())

						# Enter in wordmap, word from sentence2 to sentence1 map
						phrase = word+'->'+key
						if phrase not in self.wordmap[1]:
							self.wordmap[1].append(phrase)

					allscores.append(score)
					allpaths.append(wc.getpaths())
				index, score = max(enumerate(allscores), key=operator.itemgetter(1))
				if score > self.threshold:
					act_index = self.wordset.index(self.sent1[index])
					sem1.append(score)
					ord1.append(act_index+1)
				else:
					sem1.append(0)
					ord1.append(0)

		# For Second document
		for i, word in enumerate(self.wordset):
			allpaths = []
			allscores = []
			if word in self.sent2:
				sem2.append(1) # No Semantic Match needed
				ord2.append(i+1)
			else:
				wc = Wordclient(word)
				for key in self.sent2:
					wc.init_client(key)
					score = wc.getmetric()

					if score > 0:
						# Some Semantic Match
						self.Updatepath(word, wc.getpaths())

						# Enter in wordmap, word from sentence2 to sentence1 map
						phrase = word+'->'+key
						if phrase not in self.wordmap[0]:
							self.wordmap[0].append(phrase)

					allscores.append(score)
					allpaths.append(wc.getpaths())
				index, score = max(enumerate(allscores), key=operator.itemgetter(1))
				if score > self.threshold:
					act_index = self.wordset.index(self.sent2[index])
					sem2.append(score)
					ord2.append(act_index+1)
				else:
					sem2.append(0)
					ord2.append(0)

		self.semantic_vectors.append(sem1)
		self.semantic_vectors.append(sem2)
		self.order_vectors.append(ord1)
		self.order_vectors.append(ord2)

	def Updatepath(self, word, paths):
		# Creating paths to show in UI
		if word not in self.pathacc:
			# Initializing empty list
			self.pathacc[word] = []

		for path in paths:
			packet = []
			for edge in path:
				ls = []
				ls.append(edge.src)
				ls.append(edge.weight)
				ls.append(edge.kind)
				ls.append(edge.dest)
				packet.append(ls)
			if packet not in self.pathacc[word]:
				self.pathacc[word].append(packet)

	def Semantic_calc(self):
		# Calcuating cosine Similarity of semantic vectors
		vector1 = self.semantic_vectors[0]
		vector2 = self.semantic_vectors[1]
		cosine = Cosine_similarity(vector1, vector2)
		return cosine

	def Order_calc(self):
		# Normalizing order vectors to a score
		vector1 = [x - y for x, y in zip(self.order_vectors[0],self.order_vectors[1])]
		vector2 = [x + y for x, y in zip(self.order_vectors[0],self.order_vectors[1])]
		if vector2 == 0:
			# prevent division by zero
			return 1.0
		numerator = Vectormag(vector1)
		denominator = Vectormag(vector2)
		normalize = 1 - (numerator/denominator)
		return round(normalize,3)

	def getmetric(self):

		semantic_score = 0
		order_score = 0

		if self.semantic_vectors == [] and self.sent1 != [] and self.sent2 != []:
			# Vectors haven't been created yet
			self.Createvectors()
			semantic_score = self.Semantic_calc()
			order_score = self.Order_calc()

		score = alpha*semantic_score + (1-alpha)*order_score

		# File logging
		log = '\n************************'
		Filedump('SentenceComparison.log',log)
		log = 'Sentence 1 : '+str(self.sent1)
		Filedump('SentenceComparison.log',log)
		log = 'Sentence 2 : '+str(self.sent2)
		Filedump('SentenceComparison.log',log)
		log = 'WordSet : '+str(self.wordset)
		Filedump('SentenceComparison.log',log)
		log = 'Semantic Vectors : '+str(self.semantic_vectors)
		Filedump('SentenceComparison.log',log)
		log = 'Order Vectors : '+str(self.order_vectors)
		Filedump('SentenceComparison.log',log)
		log = 'All Paths : '+str(self.wordmap)
		Filedump('SentenceComparison.log',log)
		log = '####### Semantic Sentence Score : '+str(score)+' #######'
		Filedump('SentenceComparison.log',log)
		return round(score,4)

if __name__ == '__main__':
	start_time = time.time()
	try:
		ss = Sentenceclient('dog',' frump domestic dog ')
		score = ss.getmetric()
		print ('Execution Time : ',time.time() - start_time)
	except Exception as e:
		print ('Error Sentenceclient- ',e)