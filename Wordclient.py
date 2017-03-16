from __future__ import print_function
from Commons import *
from Spider import *
from Edge import *
import pdb

def Printpaths(word, paths):
	'''
	To return web of words around mentioned word
	'''
	print ('TO : ',word)
	for i, path in enumerate(paths):
		print ('PATH',i+1,' :',end='')
		for edge in path:
			print (' |',edge, end='')
		print()

def Score(word, paths):
	'''
	To compute score of word in web
	'''
	print('TO : ',word)
	score = 0
	for i, path in enumerate(paths):
		path_score = 1
		for edge in path:
			path_score *= edge.weight
		score += path_score
	return score

if __name__ == '__main__':
	# pdb.set_trace()
	word = 'wolf'
	sp = Spider('dog')
	web = sp.crawl()
	try:
		Printpaths(word, web[word])
		print (Score(word, web[word]))
	except Exception as e:
		print ('Error - ',e)