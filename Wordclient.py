from __future__ import print_function
from Commons import *
from Spider import *
from Edge import *
import pdb

def Printpaths(web):
	'''
	To return web of words around mentioned word
	'''
	for key, value in web.items():
		print ('TO : ',key)
		for i, path in enumerate(value):
			print ('PATH',i+1,' :',end='')
			for edge in path:
				print (' |',edge, end='')
			print()

def Score(web, word):
	'''
	To compute score of word in web
	'''
	paths = web[word]
	score = 0
	for i, path in enumerate(paths):
		path_score = 1
		for edge in path:
			path_score *= edge.weight
		score += path_score
	return score

if __name__ == '__main__':
	# pdb.set_trace()
	word = 'dog'
	sp = Spider(word)
	answer = sp.crawl()
	Printpaths(answer)
	print (Score(answer,'man'))