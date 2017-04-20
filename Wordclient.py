from __future__ import print_function, division
from Hypers import tuners
from Spider import *
from Edge import *
import time
import copy
import math


# Needs words in lowercase, and if multiple words, join them using '_'

class Wordclient:
	def __init__(self, word):
		'''
		Constructor to crawl web for a word 
		'''
		self.word = word
		sp = Spider(word, spread=2, limit=0.01)
		self.web = sp.crawl('Graph.shelve')	# Crawled web
		self.graph = Shelveopen('Graph.shelve')

		self.paths = []	# To store all paths
		self.scores = []	# To store corresponding pathscores

		self.clientfeatures = []	# Feature vector for client
		self.standardfeatures = []	# To compare against

	# Reusable function for another client
	def init_client(self, client=None):
		'''
		To initialize diff. parameters related to client
		'''
		if client is None:
			client = self.client 	#Takes previous client
		else:
			self.client = client

		self.paths, self.scores = self.calcmetric(client)

		#Initializing client features
		i = self.getpathnum()
		j = self.gethighestscore()
		k = self.getmeanscore()
		l = self.gettotalscore()
		self.clientfeatures = [i, j, k, l]

	def init_standard(self):
		'''
		To initialize diff. parameters to oneself
		'''
		paths, scores = self.calcmetric(self.word)

		#Initializing client features
		i = self.getpathnum(paths)
		j = self.gethighestscore(scores)
		k = self.getmeanscore(scores)
		l = self.gettotalscore(scores)
		self.standardfeatures = [i, j, k, l]

	#Generic function for reuse
	def calcmetric(self, client):
		clientpaths = []
		clientscores = []
		total = []

		clientedges = self.graph[client]
		clientdests = []
		for edge in clientedges:
			clientdests.append(edge.dest)

		common_points = []
		for node in self.web:
			if node in clientdests:
				common_points.append(node)

		# Handles case when no common points exist
		extrapath = {}
		for node in common_points:
			edges = self.graph[node]
			for edge in edges:
				if edge.dest == client:
					extrapath[node] = edge
					break

		for node in common_points:
			paths = self.web[node]
			for path in paths:
				extraedge = extrapath[node]
				if extraedge:	# If path exists
					ls = copy.deepcopy(path)
					ls.append(extraedge)
					clientpaths.append(ls)

		# Score calculation
		for path in clientpaths:
			score = 1
			for edge in path:
				score *= edge.weight
			clientscores.append(score)

		total.append(clientpaths)
		total.append(clientscores)
		return total

	# Functions strictly for access only, no reuse
	def getscores(self):
		'''
		To access client scores
		'''
		return self.scores

	def getpaths(self):
		'''
		To access client paths
		'''
		return self.paths

	def getfeatures(self):
		'''
		To access client features
		'''
		return self.clientfeatures

	def getstandard(self):
		'''
		To access standard features to oneself
		'''
		if self.standardfeatures:
			return self.standardfeatures
		else:
			self.init_standard()	# Initialize Standard
			return self.standardfeatures

	def getmetric(self):
		'''
		To get semantic score between client and word
		'''
		if self.standardfeatures == []:
			self.init_standard()

		#Scaling dimensions to get nearest results
		standfeat = []
		clientfeat = []
		for i in range(len(self.clientfeatures)):
			standfeat.append(self.standardfeatures[i] * tuners[i])
			clientfeat.append(self.clientfeatures[i] * tuners[i])

		score = Cosine_similarity(standfeat, clientfeat)

		# File Logging
		log = '\n*******FROM : '+self.word+' TO : '+self.client+' *******'
		Filedump('WordComparison.log',log)
		log = 'Client Feature : '+str(self.clientfeatures)
		Filedump('WordComparison.log',log)
		log = 'Standard Feature : '+str(self.standardfeatures)
		Filedump('WordComparison.log',log)
		log = '#######Semantic Word Score : '+str(score)+' #######'
		Filedump('WordComparison.log',log)
		return score

	def printweb(self):
		'''
		To Print entire web
		'''
		print ('FROM : ',self.word)
		for dest, paths in self.web.items():
			print ('TO : ',dest)
			for i, path in enumerate(paths):
				print ('PATH',i+1,' :',end='')
				for edge in path:
					print (' |',edge, end='')
				print ()

	def printpaths(self, paths=None, scores=None):
		'''
		To print paths to a client by default, else can print any paths and scores to them
		'''
		if paths is None:
			paths = self.paths
		if scores is None:
			scores = self.scores
		if paths:
			for i, path in enumerate(paths):
				print ('PATH', i+1,' :',end='')
				for edge in path:
					print (' |',edge, end='')
				print  ()
				print ('PathScore : ',scores[i])
		else:
			print ('Word',dest,'is not reachable from Source')

	# Functions reused to create features for standard and client, also can be accessed directly for client
	def gettotalscore(self, scores=None):
		'''
		To compute total score
		'''
		if scores is None:
			scores = self.scores
		return sum(scores)

	def getmeanscore(self, scores=None):
		'''
		Get Mean of all scores
		'''
		if scores is None:
			scores = self.scores
		if len(scores) == 0:
			return 0	# To prevent division by zero
		else:
			return round(sum(scores)/len(scores),3)

	def gethighestscore(self, scores=None):
		'''
		To return highest score
		'''
		if scores is None:
			scores = self.scores
		if len(scores) == 0:
			return 0	# To prevent no arg. error
		else:
			return max(scores)

	def getpathnum(self, paths=None):
		'''
		To return no of paths obtained
		'''
		if paths is None:
			paths = self.paths
		return len(paths)

if __name__ == '__main__':
	start_time = time.time()
	word = 'dog'
	client = 'labrador'
	try:
		wc = Wordclient(word)
		wc.init_client(client)
		# wc.printweb()
		# wc.printpaths()
		score = wc.getmetric()
		print ('Execution Time : ',time.time() - start_time)
	except Exception as e:
		print ('Error Wordclient- ',e)