from __future__ import division
from Commons import *
from Edge import *
import copy

class Spider():
	"""docstring for Spider"""
	def __init__(self, word):
		self.word = word
		self.spread = 4	# Limit recursion depth
		self.limit = 0.003	# Score limit for paths
		self.depth = 0	# Measure recursion depth
		self.score = 1 # Measure path score
		self.web = dict()
		self.graph = dict()
		self.path = list()	# Store path traversed
		self.visited = list()	# To prevent cycles
		self.closest = list()	# Workaround to speed up spider by stopping dests with paths lenght > 1

	def crawl(self):
		'''
		To get spread of wordnet
		'''
		self.graph = Shelveopen('Graph.shelve')

		# Adding first word into visited
		self.DFS(self.word)
		return {key : value for key, value in self.web.items() if '.' not in key}	# Only returning word targets

	def pathscore(self, dest):
		'''
		Returns true if path length of all paths to a destination is > 1.0
		'''
		if dest in self.web:
			paths = self.web[dest]
			score = 0
			for path in paths:
				path_score = 1
				for edge in path:
					path_score *= edge.weight
				score += path_score
			return True if score > 1.0 else False
		else:
			print 'Spider Web does not have',dest,'yet'
			return False

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
			if node in self.closest:
				# Sum of all paths to node is already > 1.0
				# Done to speed up crawling
				return
			if node in self.visited:
				# Check if path is a cycle of existing path
				paths = self.web[node]
				if self.subset(paths, self.path):
					# It is a cycle
					return
				if self.pathscore(node):
					# Check if sum of paths to node is > 1.0
					self.closest.append(node)
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
						
						# To limit recursion depth and path score
						self.depth += 1
						self.score *= edge.weight
						self.path.append(edge)
						if node not in self.visited:
							# To prevent double entry in visited
							self.visited.append(node)

						if self.score > self.limit:
							# To Limit path score
							self.DFS(dest)

						# After recursion, coming back
						self.depth -= 1
						self.score /= edge.weight
						
						pop = self.path.pop()
			else:
				print 'Sorry ! Spider could not find',node,'in Similarity Graph'
		except Exception as e:
			print 'Error Spider - ',e