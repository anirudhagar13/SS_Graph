from __future__ import print_function
from Wordclient import *
import time

if __name__ == '__main__':
	with open('MilesCharles.txt') as f:
		start_time = time.time()
		for line in f.readlines():
			line = line.replace('\n','')
			ls = line.split('\t')
			w1 = Wordclient(ls[0], ls[1])
			w2 = Wordclient(ls[1], ls[0])
			print (ls[0], ls[1], ls[2], w1.gettotalscore(), w2.gettotalscore(), sep='\t')
		print ('Execution time - ',time.time() - start_time)