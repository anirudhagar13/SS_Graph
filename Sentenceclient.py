from Wordclient import *

class SentenceClient:
	def __init__(self, sentence1, sentence2):
		wordhash = Shelveopen('Hash#1.shelve')
		self.sent1 = Purify(sentence1, wordhash)
		self.sent2 = Purify(sentence2, wordhash)
		self.wordset = list(set(self.sent1 + self.sent2))	# Exposisng 

if __name__ == '__main__':
	ss = SentenceClient('I loved the united states',' YOurs only habibi');
	print ss.sent1
	print ss.sent2
	print ss.wordset
	hash1 = Shelveopen('Hash#1.shelve')
	print hash1['loved']