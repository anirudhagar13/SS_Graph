from __future__ import division
from Commons import *
from Edge import *
import copy

class Spider():
	"""docstring for Spider"""
	def __init__(self, word, spread=3, limit=0.008):
		self.word = word
		self.spread = spread	# Limit recursion depth
		self.limit = limit	# Score limit for paths
		self.depth = 0	# Measure recursion depth
		self.score = 1 # Measure path score
		self.web = dict()
		self.graph = dict()
		self.path = list()	# Store path traversed
		self.visited = list()	# To prevent cycles

	def crawl(self, filename):
		'''
		To get spread of wordnet
		'''
		self.graph = Shelveopen(filename)

		# Adding first word into visited
		edges = self.graph[self.word]
		for edge in edges:
			if edge.weight != 0: # Prevents division by zero error
				self.score *= edge.weight
				self.depth += 1

				if self.depth <= self.spread and self.score >= self.limit:
					self.path.append(edge)
					self.DFS(edge.dest)
					pop = self.path.pop()

				self.depth -= 1
				self.score /= edge.weight
			else:
				pass

		return self.web # Only for fast processing
		return {key : value for key, value in self.web.items() if '.' not in key}	# Only returning word targets

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
					if edge.weight != 0: # Prevent division by zero error
						self.score *= edge.weight
						self.depth += 1

						if self.depth <= self.spread and self.score >= self.limit:
							self.path.append(edge)
							if node not in self.visited:
								# To prevent double entry in visited
								self.visited.append(node)

							self.DFS(edge.dest)							
							pop = self.path.pop()
													
						# After recursion, coming back
						self.depth -= 1
						self.score /= edge.weight

					else:
						return
			else:
				print 'Sorry ! Spider could not find',node,'in Similarity Graph'
		except Exception as e:
			print 'Error Spider - ',e