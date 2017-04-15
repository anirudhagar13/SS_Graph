from Wordclient import *
import operator

class SentenceClient:
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
		self.threshold = 0.005 # To decide if something is not at all similar
		self.pathacc = {} # To accumulate all paths after crawling

	def Getsemantics(self):
		'''
		To access semantic vectors
		'''
		if self.semantic_vectors == []:
			# Vectors haven't been created yet
			self.Createvectors()

		else:
			return self.semantic_vectors

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
					allscores.append(score)
					allpaths.append(wc.getpaths())
				index, score = max(enumerate(allscores), key=operator.itemgetter(1))
				if score > self.threshold:
					act_index = self.wordset.index(self.sent1[index])
					sem1.append(score)
					ord1.append(act_index+1)
					self.Updatepath(word, allpaths[index])
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
					allscores.append(score)
					allpaths.append(wc.getpaths())
				index, score = max(enumerate(allscores), key=operator.itemgetter(1))
				if score > self.threshold:
					act_index = self.wordset.index(self.sent2[index])
					sem2.append(score)
					ord2.append(act_index+1)
					self.Updatepath(word, allpaths[index])
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
			ls = []
			for edge in path:
				ls.append(edge.weight)
				ls.append(edge.kind)
				ls.append(edge.dest)
			if ls not in self.pathacc[word]:
				self.pathacc[word].append(ls)

if __name__ == '__main__':
	start_time = time.time()
	try:
		ss = SentenceClient('I love dogs puppy',' I like puppies too ')
		print 'WordSet : ',ss.wordset
		ss.Getsemantics()	
		print ss.pathacc
		print ss.semantic_vectors
		print ss.order_vectors
		print ('Execution Time : ',time.time() - start_time)
	except Exception as e:
		print ('Error Wordclient- ',e)