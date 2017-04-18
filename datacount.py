from Commons import Shelveopen

def wordno():
	'''
	Count no of words in System
	'''
	hash1 = Shelveopen('Hash#1.shelve')
	return len(hash1.keys())

def synsetno():
	'''
	Count no of synsets
	'''
	hash2 = Shelveopen('Hash#2.shelve')
	return len(hash2.keys())

def graphnodes():
	'''
	Count no of nodes in graph
	'''
	graph = Shelveopen('Graph.shelve')
	return len(graph.keys())

def graphedges():
	'''
	Count no of edges
	'''
	graph = Shelveopen('Graph.shelve')
	edges = 0
	for value in graph.values():
		edges += len(value)
	return edges




if __name__ == '__main__':
	print graphedges()
	