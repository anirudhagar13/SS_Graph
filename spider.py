from Commons import *
from Edge import *
try:
    import cPickle as pickle
except:
    import pickle

GRAPH_SHELVE = 'Graph.shelve'
path_info = dict()
score_info = dict()

def populate_dicts(node,parent_node,edge,score_):
    try:
        path_info[node][paths].append(edge)
        path_info[node][paths].extend(path_info[parent_node])
    except KeyError:
        path_info[node][paths] = list()
        path_info[node][paths].append(edge)
        path_info[node][paths].extend(path_info[parent_node])

class Spider():
    '''
    '''
    def __init__(self, word):
        self.word = word
        self.max_spread = 2
        self.max_depth = 2
        self.min_score = 0.003
        self.score = 1
        self.st = list() # stack for dfs
        self.web = dict()
        self.visited = list()

    def crawl(self):

        self.dfs()
        #with open('path_info.pickle', 'wb') as handle:
        #    pickle.dump(a, handle, protocol=pickle.HIGHEST_PROTOCOL)

    def dfs(self):
        self.st.append((self.word,0,1))
        path_info[self.word][paths] = []
        path_info[self.word][score] = 1
        graph_ = Shelveopen(GRAPH_SHELVE)

        self_st_pop = self.st.pop
        self_visited_append = self.visited.append
        self_max_depth = self.max_depth
        self_min_score = self.min_score
        self_st_append = self.st.append

        while( self.st ):
            (node,depth_,score_) = self_st_pop()
            if node not in self.visited: # check if all cases of cycles are handled
                print('node = %s, depth = %s' % (node,depth_))
                self_visited_append(node)
                if graph_[node]:
                    if depth_ < self_max_depth:
                        edges = graph_[node] # implement max_spread here
                        depth_ += 1
                        depth_incr = depth_
                        for edge in edges:
                            score_ *= edge.weight
                            if score_ > self_min_score:
                                dest = edge.dest
                                populate_path_info(dest,node,edge,score_)
                                self_st_append((dest,depth_incr,score_))
            else:
                print('node : %s was already visited' % (node))
        graph_.close()

if __name__ == "__main__":
    s = Spider('dog.n.01')
    s.crawl()
    for key in path_info:
        print 'key = ', key
        for x in path_info[key]:
            print '\t ', x
