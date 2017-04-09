from __future__ import print_function
from Commons import *
from Spider import *
from Edge import *
import time
import copy

# Needs words in lowercase, and if multiple words, join them using '_'

class Wordclient:
	def __init__(self, word, client):
		'''
		Constructor to crawl web for a word 
		'''
		self.word = word
		self.client = client
		sp = Spider(word, spread=2, limit=0.008)
		self.web = sp.crawl('Graph.shelve')	# Crawled web
		self.paths = []	# To store all paths
		self.scores = []	# To store corresponding pathscores
		self.calcmetric() # To calculate all paths and scores

	def calcmetric(self):
		if self.paths:
			# Calculations already done
			return

		graph = Shelveopen('Graph.shelve')
		clientedges = graph[self.client]
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
			edges = graph[node]
			for edge in edges:
				if edge.dest == self.client:
					extrapath[node] = edge
					break

		for node in common_points:
			paths = self.web[node]
			for path in paths:
				extraedge = extrapath[node]
				if extraedge:	# If path exists
					ls = copy.deepcopy(path)
					ls.append(extraedge)
					self.paths.append(ls)

		# Score calculation
		for path in self.paths:
			score = 1
			for edge in path:
				score *= edge.weight
			self.scores.append(score)

	def getscores(self, dest):
		'''
		To Compute score of word in web
		'''
		return self.scores

	def getpaths(self, dest):
		'''
		To Compute score of word in web
		'''
		return self.paths

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

	def printpaths(self):
		'''
		To print paths to a sclient
		'''
		if self.paths:
			for i, path in enumerate(self.paths):
				print ('PATH', i+1,' :',end='')
				for edge in path:
					print (' |',edge, end='')
				print  ()
				print ('PathScore : ',self.scores[i])
		else:
			print ('Word',dest,'is not reachable from Source')

if __name__ == '__main__':
	start_time = time.time()
	word = 'cock'
	client = 'bird'
	try:
		wc = Wordclient(word, client)
		# wc.printweb()
		wc.printpaths()
		print ('Execution Time : ',time.time() - start_time)
	except Exception as e:
		print ('Error Wordclient- ',e)