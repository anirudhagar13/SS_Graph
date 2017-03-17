from __future__ import print_function
from Commons import *
from Spider import *
from Edge import *

def Printpaths(word, paths):
	'''
	To print paths to a specific word in web
	'''
	print ('TO : ',word)
	for i, path in enumerate(paths):
		print ('PATH', i+1,' :',end='')
		score = 1
		for edge in path:
			score *= edge.weight
			print (' |',edge, end='')
		print  ()
		print ('PathScore : ',score)

def Score(word, paths):
	'''
	To Compute score of word in web
	'''
	print ('TO : ',word)
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
			score = 1
			for edge in path:
				score *= edge.weight
				print (' |',edge, end='')
			print ()
			print ('PathScore : ',score)

if __name__ == '__main__':
	word = 'tiger'
	client = 'lion'
	try:
		sp = Spider(word)
		web = sp.crawl()	# Web obtained back around mentioned word
		# Printweb(word, web)
		Printpaths(client, web[client])
		# print (Score(client, web[client]))
	except Exception as e:
		print ('Error Wordclient- ',e)