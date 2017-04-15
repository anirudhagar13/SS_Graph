from __future__ import print_function
from Wordclient import *
import time

if __name__ == '__main__':
	with open('MilesCharles.txt') as f:
		start_time = time.time()
		Filedump('WordComparison.log','',False)	# Clear log
		for line in f.readlines():
			line = line.replace('\n','')
			ls = line.split('\t')
			w1 = Wordclient(ls[0])
			w1.init_client(ls[1])
			w1.getmetric()
			w2 = Wordclient(ls[1])
			w2.init_client(ls[0])
			w2.getmetric()
		print ('Execution time - ',time.time() - start_time)