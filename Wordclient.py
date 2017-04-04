from __future__ import print_function
from Commons import *
from Spider import *
from Edge import *
import time

# Needs words in lowercase, and if multiple words, join them using '_'

class Wordclient:
	def __init__(self, word):
		'''
		Constructor to crawl web for a word 
		'''
		self.word = word
		sp = Spider(word)
		self.web = sp.crawl()	# Crawled web

	def printweb(self, word):
		'''
		To Print entire web of mentioned word
		'''
		print ('FROM : ',word)
		for word, paths in self.web.items():
			print ('TO : ',word)
			for i, path in enumerate(paths):
				print ('PATH',i+1,' :',end='')
				score = 1
				for edge in path:
					score *= edge.weight
					print (' |',edge, end='')
				print ()
				print ('PathScore : ',score)

	def printpaths(self, dest):
		'''
		To print paths to a specific word in web
		'''
		if dest in self.web:
			paths = self.web[dest]
			print ('TO : ',dest)
			for i, path in enumerate(paths):
				print ('PATH', i+1,' :',end='')
				score = 1
				for edge in path:
					score *= edge.weight
					print (' |',edge, end='')
				print  ()
				print ('PathScore : ',score)
		else:
			print ('Word',dest,'is not reachable from Source')

	def score(self, dest):
		'''
		To Compute score of word in web
		'''
		if dest in self.web:
			paths = self.web[dest]
			print ('TO : ',dest)
			score = 0
			for i, path in enumerate(paths):
				path_score = 1
				for edge in path:
					path_score *= edge.weight
				score += path_score
			return score
		else:
			print ('Word',dest,'is not reachable from Source')
			return 0

if __name__ == '__main__':
	start_time = time.time()
	word = 'bird'
	client = 'cock'
	try:
		wc = Wordclient(word)
		# wc.printweb(word)
		# wc.printpaths(client)
		print ('Final Score : ',wc.score(client))
		print ('Execution Time : ',time.time() - start_time)
	except Exception as e:
		print ('Error Wordclient- ',e)