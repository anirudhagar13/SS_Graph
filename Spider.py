from Commons import *
from Edge import *
import copy

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

		# Adding first word into visited
		self.DFS(self.word)
		return self.web

	def subset(self, paths, path):
		'''
		Check if path of visited is same or different
		'''
		for i in paths:
			# If list not empty and It is a subset of existing path
			if set(i).issubset(set(path)):
				return True
		return False

	def DFS(self, node):
		'''
		To perform DFS using internal stack
		'''
		try:
			if node in self.visited:
				# Check if path is a cycle of existing path
				paths = self.web[node]
				if self.subset(paths, self.path):
					# It is a cycle
					return

			# Check if word entry for first time in web
			if node not in self.web:
				self.web[node] = list()

			# To prevent from object getting copied
			ls = copy.deepcopy(self.path)
			self.web[node].append(ls)

			if node in self.graph:
				edges = self.graph[node]
				for edge in edges:
					dest = edge.dest
					if self.depth < self.spread:
						#To limit recursion depth
						self.depth += 1
						self.path.append(edge)
						if node not in self.visited:
							#to prevent double entry in visited
							self.visited.append(node)
						self.DFS(dest)
						self.depth -= 1
						pop = self.path.pop()
		except Exception as e:
			print 'Error - ',e