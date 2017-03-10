from __future__ import print_function
from Commons import *
from Spider import *
from Edge import *
import pdb

def Printpaths(dic):
	for key, value in dic.items():
		print ('TO : ',key)
		for i, path in enumerate(value):
			print ('PATH',i+1,' :',end='')
			for edge in path:
				print (' |',edge, end='')
			print()

if __name__ == '__main__':
	# pdb.set_trace()
	word = 'dog'
	sp = Spider(word)
	Printpaths(sp.crawl())