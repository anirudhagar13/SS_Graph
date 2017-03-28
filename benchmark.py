from __future__ import print_function
from Wordclient import *
import time

def manager(score1, score2):
	if score1 == 0 or score2 == 0:
		#just return non zero score
		return score1 if score1 != 0 else score2

	else:
		#See if adding them makes any diff
		score_tot = score1 + score2
		bigger = score1 if score1 > score2 else score2
		bigger = bigger if bigger > 0.07 else bigger*10
		if score_tot > 1.7*bigger:
			#If total is 1.5times bigger the bigger score, return average
			return score_tot/2
		else:
			#Just return the bigger
			return bigger

if __name__ == '__main__':
	with open('Radinsky.txt') as f:
		start_time = time.time()
		for line in f.readlines():
			line = line.replace('\n','')
			ls = line.split('\t')
			word1 = Wordclient(ls[0])
			word2 = Wordclient(ls[1])
			score1 = word1.score(ls[1])
			score2 = word2.score(ls[0])
			print (ls[0],ls[1], ls[2], manager(score1, score2), sep='\t')
		print ('Execution time - ',time.time() - start_time)