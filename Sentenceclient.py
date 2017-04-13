from Wordclient import *
import operator

class SentenceClient:
	def __init__(self, sentence1, sentence2):
		wordhash = Shelveopen('Hash#1.shelve')
		self.sent1 = Purify(sentence1, wordhash)	# Sending Hash from here as prevents opening and closing again n again
		self.sent2 = Purify(sentence2, wordhash)
		self.wordset = list(set(self.sent1 + self.sent2))	# Exposisng
		self.semantic_vectors = [] # To store of both sentences
		self.order_vectors = [] # To store order vectors of both sentences
		self.threshold = 0.005 # To decide if something is not at all similar
		self.pathacc = {} # To accumulate all paths after crawling

	def Getsemantics(self):
		'''
		To access semantic vectors
		'''
		if semantic_vectors == []:
			# Vectors haven't been created yet
			self.Createvectors()

		else:
			return self.semantic_vectors

	def Getorder(self):
		'''
		To access order vectors
		'''
		if order_vectors == []:
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
		allpaths = []
		allscores = []
		ls2 = []

		# For First document
		for i, word in enumerate(self.wordset):
			if word in self.sent1:
				sem1.append(1) # No Semantic Match needed
				ord1.append(i+1)
			else:
				wc = Wordclient(word)
				for key in self.sent1:
					wc.init_client(key)
					allscores.append(wc.getmetric())
					allpaths.append(wc.getpaths())
				index, score = max(enumerate(allscores), key=operator.itemgetter(1))
				if score > self.threshold:
					sem1.append(score)
					ord1.append(index+1)
					self.Updatepath(word, allpaths[index])
				else:
					sem1.append(0)
					ord1.append(0)

	def Updatepath(word, paths):
		# Creating paths to show in UI
		if word not in self.pathacc:
			# Initializing empty list
			self.pathacc[word] = []

		for path in paths:
			ls = []
			for edge in path:
				ls.append(edge.weight)
				ls.append(edge.destination)
			if ls not in self.pathacc[word]:
				self.pathacc[word].append(ls)


if __name__ == '__main__':
	start_time = time.time()
	try:
		ss = SentenceClient('I loved the united states',' I like flowers ')
		wc = Wordclient('dog')
		wc.init_client('puppy')
		wc.printpaths();	
		print ('Execution Time : ',time.time() - start_time)
	except Exception as e:
		print ('Error Wordclient- ',e)