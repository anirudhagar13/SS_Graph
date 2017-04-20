from Sentenceclient import *
from nltk.tokenize import sent_tokenize
import numpy
import sys  

reload(sys)  
sys.setdefaultencoding('utf8')

class Documentclient:
	def __init__(self, weight_1=1, weight_2=1, doc_1='', doc_2=''):
		self.weight_1 = weight_1
		self.weight_2 = weight_2

		tokenized_1 = sent_tokenize(doc_1)
		tokenized_2 = sent_tokenize(doc_2)
		self.doc_1 = tokenized_1 if len(tokenized_1) <= len(tokenized_2) else tokenized_2	# Smaller doc
		self.doc_2 = tokenized_1 if self.doc_1 == tokenized_2 else tokenized_2	# Bigger doc

		# Initializing smaller document as rows
		self.sem_matrix = [[0 for col in range(len(self.doc_2))] for row in range(len(self.doc_1))] # Fill matrix with zeros
		self.allpaths = {}
		self.wordmap = [{},{}] # Words of Doc1 found in Doc2 & vice-versa
		self.score = 0	# Final document score

	def getWordMap(self):
		'''
		Getter for wordmap
		'''
		return self.wordmap

	def getPaths(self):
		'''
		Getter for allpaths
		'''
		return self.allpaths

	def getScore(self):
		'''
		Getter for score
		'''
		return self.score

	def wordmapacc(self, wordmap):
		'''
		Create Mapping of words found in other Document
		'''
		for phrase in wordmap[0]:
			key, dest = phrase.split('->')
			if key not in self.wordmap[0]:
				self.wordmap[0][key] = []
			if dest not in self.wordmap[0][key]:
				self.wordmap[0][key].append(dest)

		for phrase in wordmap[1]:
			key, dest = phrase.split('->')
			if key not in self.wordmap[1]:
				self.wordmap[1][key] = []
			if dest not in self.wordmap[1][key]:
				self.wordmap[1][key].append(dest)

	def pathaccumulation(self, pathacc):
		'''
		Accumulate paths obtained in sentence Match into document paths
		'''
		for key, paths in pathacc.items():
			# Paths is list of paths from key to other destinations
			if key not in self.allpaths:
				# Directly put all paths
				self.allpaths[key] = paths
			else:
				for path in paths:
					# If key already exists, check if path exists among various paths from key
					if path not in self.allpaths[key]:
						self.allpaths[key].append(path)

	def clearlogs(self):
		'''
		Just to clear all logs
		'''
		Filedump('NonMorphed.log','', False)
		Filedump('WordComparison.log','', False)
		Filedump('SentenceComparison.log','', False)
		Filedump('DocumentComparison.log','', False)

	def makemaps(self):
		'''
		Initialize semantic Matrix
		'''		
		# Clear Logs
		self.clearlogs()

		for i, sent1 in enumerate(self.doc_1):
			for j, sent2 in enumerate(self.doc_2):
				ss = Sentenceclient(sent1, sent2)
				score = ss.getmetric()
				self.sem_matrix[i][j] = score

				paths = ss.getPathsacc()
				wordmap = ss.getWordmap()
				self.pathaccumulation(paths)
				self.wordmapacc(wordmap)

				if score == 1:
					# Has Found match, no point is searching for more
					break
					
	def calcmetric(self):
		'''
		To give similarity matrix score between documents
		'''
		score = 0
		for row in self.sem_matrix:
			score += max(row) # Get Highest score from each row

		return round(score/len(self.sem_matrix),4)

	def getmetric(self):
		'''
		Obtain final Document Similarity Score
		'''
		# Initialize Similarity Matrix
		self.makemaps()

		# Calculate score from Matrix here, sum of all matrix elements
		self.score = self.calcmetric()
		
		# File Logging
		log = '\n************************'
		Filedump('DocumentComparison.log',log)
		log = 'Document 1 : '+str(self.doc_1)
		Filedump('DocumentComparison.log',log)
		log = 'Document 2 : '+str(self.doc_2)
		Filedump('DocumentComparison.log',log)
		log = 'Semantic Matrix : '+str(self.sem_matrix)
		Filedump('DocumentComparison.log',log)
		log = 'Words Semantically Mapped Doc 1 to Doc 2 : '+str(self.wordmap[0])
		Filedump('DocumentComparison.log',log)
		log = 'Words Semantically Mapped Doc 2 to Doc 1 : '+str(self.wordmap[1])
		Filedump('DocumentComparison.log',log)
		log = '####### Document Similarity Score : '+str(self.score)+' #######'
		Filedump('DocumentComparison.log',log)

		return self.score

if __name__ == '__main__':
	try:
		start_time = time.time()
		dd = Documentclient(doc_1='I Like Dogs. I Hate you. I love puppies too ? I hate balloons',doc_2="I hate you. i like dogs. I adore dalmatians!")
		dd.getmetric()
		print 'Execution Time : ',time.time() - start_time
	except Exception as e:
		print 'Document Client Exception : ',e
	