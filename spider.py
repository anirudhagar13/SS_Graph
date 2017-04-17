from Commons import *
from Edge import *
try:
    import cPickle as pickle
except:
    import pickle

GRAPH_SHELVE = 'Graph.shelve'
path_info = dict()
score_info = dict()
'''
def populate_dicts(node,parent_node,edge,score_):
    try:
        path_info[node]['path'].append(edge)
        path_info[node]['path'].extend(path_info[parent_node])
    except KeyError:
        path_info[node] = dict()
        path_info[node]['path'] = list()
        path_info[node]['path'].append(edge)
        path_info[node]['path'].extend(path_info[parent_node])
'''

def populate_path_info(node,parent_node,edge,score_):
    try:
        path_info[node].append(edge)
        path_info[node].extend(path_info[parent_node])
    except KeyError:
        path_info[node] = list()
        path_info[node].append(edge)
        path_info[node].extend(path_info[parent_node])
        path_info[node].append('END')

class Spider():
    '''
    '''
    def __init__(self, word):
        self.word = word
        self.max_spread = 2
        self.max_depth = 3
        self.min_score = 0.003
        self.score = 1
        self.st = list() # stack for dfs
        self.web = dict()
        self.visited = list()

    def crawl(self):

        self.dfs()
        #with open('path_info.pickle', 'wb') as handle:
        #    pickle.dump(a, handle, protocol=pickle.HIGHEST_PROTOCOL)

    def is_cycle(node,parent_node):
        print path_info['asdf']

    def dfs(self):
        self.st.append((self.word,0,1))
        path_info[self.word] = []
        # path_info[self.word] = dict()
        # path_info[self.word]['path'] = []
        # path_info[self.word]['score'] = 1
        graph_ = Shelveopen(GRAPH_SHELVE)

        self_st_pop = self.st.pop
        self_visited_append = self.visited.append
        self_max_depth = self.max_depth
        self_min_score = self.min_score
        self_st_append = self.st.append

        while( self.st ):
            (node,parent_node,depth_,score_) = self_st_pop()
            #if not is_cycle(node,parent_node): # checking for cycles
            if node not in self.visited: # check if all cases of cycles are handled
                print('node = %s, depth = %s, score = %s' % (node,depth_,score_))
                self_visited_append(node)
                if graph_[node]:
                    if depth_ < self_max_depth:
                        edges = graph_[node][:3] # implement max_spread here, something like graph_[node][:max_spread] - check this
                        depth_ += 1
                        depth_incr = depth_
                        for edge in edges:
                            #score_ *= edge.weight
                            print '\t edge : ', edge
                            new_score = round((score_ * edge.weight),3)
                            if new_score > self_min_score:
                                dest = edge.dest
                                print '\t dest : ', dest
                                populate_path_info(dest,node,edge,new_score)
                                print '\t path_info[dest] : ', path_info[dest]
                                self_st_append((dest,node,depth_incr,new_score))
            else:
                print('node : %s was already visited' % (node))
            print self.st
        graph_.close()


if __name__ == "__main__":
    s = Spider('dog.n.01')
    s.dfs()

    for key in path_info:
        print 'key = ', key
        for x in path_info[key]:
            print '\t : ', x
