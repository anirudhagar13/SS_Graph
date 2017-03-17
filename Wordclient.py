from __future__ import print_function
from Commons import *
from Spider import *
from Edge import *
import pdb

def Printpaths(word, paths):
	'''
	To Return web of words around mentioned word
	'''
	print ('TO : ',word)
	for i, path in enumerate(paths):
		print ('PATH',i+1,' :',end='')
		for edge in path:
			print (' |',edge, end='')
		print()

def Score(word, paths):
	'''
	To Compute score of word in web
	'''
	print('TO : ',word)
	score = 0
	for i, path in enumerate(paths):
		path_score = 1
		for edge in path:
			path_score *= edge.weight
		score += path_score
	return score

def Printweb(word, web):
	'''
	To Print entire web of mentioned word
	'''
	print ('FROM : ',word)
	for word, paths in web.items():
		print ('TO : ',word)
		for i, path in enumerate(paths):
			print ('PATH',i+1,' :',end='')
			for edge in path:
				print (' |',edge, end='')
			print()

if __name__ == '__main__':
	# pdb.set_trace()
	word = 'wolf'
	sp = Spider('tiger')
	web = sp.crawl()
	try:
		Printweb('tiger', web)
		# Printpaths(word, web[word])
		# print (Score(word, web[word]))
	except Exception as e:
		print ('Error - ',e)