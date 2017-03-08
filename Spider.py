from Commons import *
from Edge import *

class Spider():
	"""docstring for Spider"""
	def __init__(self, word):
		self.word = word
		self.spread = 5	#to limit recursion depth
		self.depth = 0	#to measure recursion depth
		self.web = dict()
		self.graph = dict()
		self.path = list()	#to store path traversed
		self.visited = list()	#to prevent cycles

	def crawl(self):
		'''
		To get spread of wordnet
		'''
		self.graph = Shelveopen('Graph.shelve')
		self.DFS(self.word)
		return self.web

	def DFS(self, node):
		'''
		To perform DFS using internal stack
		'''
		try:
			if '.' not in node:
				#To distinguish between word and synset
				self.web[node] = self.path

			edges = self.graph[node]
			for edge in edges:
				dest = edge.dest
				if dest in visited:
					pass
				else:
					if self.depth < self.spread:
						#To limit recursion depth
						self.depth += 1
						self.visited.append(dest)
						self.path.append(edge)
						self.DFS(dest)
						self.depth -= 1
						pop = self.path.pop()
		except Exception as e:
			print 'Error - ',e