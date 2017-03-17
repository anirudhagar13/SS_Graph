from Commons import *
from Edge import *
import time

#Globals
hash3 = {}
hash4 = {}
graph = {}
word_count = 0
synset_count = 0

def Words(src, data):
    '''
    Create Word Edges
    '''
    for key, value in data.items():
        if key == 'W2S':
            if value:
                W2S(src, value)
        elif key == 'D2S':
            if value:
                D2S(src, value)
        else:
            raise Exception('Word Edge not defined - ',key)

def Synsets(src, data):
    '''
    Create Word Edges
    '''
    #Only called when value not empty
    for key, value in data.items():
        if key == 'S2W':
            if value:
                S2W(src, value)
        elif key == 'S2D':
            if value:
                S2D(src, value)
        elif key == 'S2E':
            if value:
                S2E(src, value)
        elif key == 'Hyponym':
            if value:
                Hyponym(src, value)
        elif key == 'Hypernym':
            if value:
                Hypernym(src, value)
        elif key == 'Meronym':
            if value:
                Meronym(src, value)
        elif key == 'Holonym':
            if value:
                Holonym(src, value)
        elif key == 'Similar':
            if value:
                Similar(src, value)
        elif key == 'Entailment':
            if value:
                Entailment(src, value)
        else:
            raise Exception('Synset Edge not defined - ',key)

def Insert(src, edge):
    '''
    Direct appending not working
    '''
    ls = graph[src]
    ls.append(edge)
    graph[src] = ls

#******Synset Functions********
def S2W(src, data):
    '''
    To create sense to word edges
    '''
    for dest in data:
        edge = Edge(src=src, dest=dest, kind='S2W')
        edge.populate()

        #Adding edge created in graph
        Insert(src, edge)

def S2D(src, data):
    '''
    To create sense to non-noise words in definition
    '''
    #Each edge is a dictionary, data is list of dictionaries
    for item in data:
        dest = item[0]
        frequency = item[1]
        total_freq = item[2]
        edge = Edge(src=src, dest=dest, kind='S2D')
        edge.populate(frequency=frequency, total_freq=total_freq)

        #Adding edge created in graph

        Insert(src, edge)

def S2E(src, data):
    '''
    To create sense to non-noise words in example
    '''
    #Each edge is a dictionary, data is list of dictionaries
    for item in data:
        dest = item[0]
        frequency = item[1]
        total_freq = item[2]
        edge = Edge(src=src, dest=dest, kind='S2E')
        edge.populate(frequency=frequency, total_freq=total_freq)

        #Adding edge created in graph
        Insert(src, edge)

def Hypernym(src, data):
    '''
    To create hypernym edges
    '''
    for dest in data:
        edge = Edge(src=src, dest=dest, kind='Hypernym')
        edge.populate()

        #Adding edge created in graph
        Insert(src, edge)

def Hyponym(src, data):
    '''
    To create hyponym edges
    '''
    for dest in data:
        edge = Edge(src=src, dest=dest, kind='Hyponym')
        edge.populate()

        #Adding edge created in graph
        Insert(src, edge)

def Holonym(src, data):
    '''
    To create holonym edges
    '''
    for dest in data:
        edge = Edge(src=src, dest=dest, kind='Holonym')
        edge.populate()

        #Adding edge created in graph
        Insert(src, edge)

def Similar(src, data):
    '''
    To create similar edges
    '''
    for dest in data:
        edge = Edge(src=src, dest=dest, kind='Similar')
        edge.populate()

        #Adding edge created in graph
        Insert(src, edge)

def Entailment(src, data):
    '''
    To create entailment edges
    '''
    for dest in data:
        edge = Edge(src=src, dest=dest, kind='Entailment')
        edge.populate()

        #Adding edge created in graph
        Insert(src, edge)

def Meronym(src, data):
    '''
    To create hypernym edges
    '''
    num_mero = len(data)
    for dest in data:
        edge = Edge(src=src, dest=dest, kind='Meronym')
        edge.populate(num_mero=num_mero)

        #Adding edge created in graph
        Insert(src, edge)

#******Word Functions********
def W2S(src, data):
    '''
    To create word to sense edges
    '''
    #Each edge is a dictionary, data list of dictionaries
    total_freq = sum(data.values())
    for dest, frequency in data.items():
        edge = Edge(src=src, dest=dest, kind='W2S')
        edge.populate(frequency=frequency, total_freq=total_freq)

        #Adding edge created in graph
        Insert(src, edge)

def D2S(src, data):
    '''
    To create word to sense backedges in which it occurs
    '''
    total_freq = sum(data.values())
    for dest, frequency in data.items():
        edge = Edge(src=src, dest=dest, kind='D2S')
        edge.populate(frequency=frequency, total_freq=total_freq)

        #Adding edge created in graph
        Insert(src, edge)

def handle_error(e):
    '''
    To Catch and show exceptions
    '''
    print 'Log - ',e
    print 'Words Processed - ',word_count
    print 'Synsets Processed - ',synset_count
    Shelveclose(hash3)  #For Words
    Shelveclose(hash4)  #For Synsets
    Shelveclose(graph)

def Showgraph(graph, word):
    '''
    To print made graph
    '''
    value = graph[word]
    print word,' :: '
    for edge in value:
        print edge

if __name__ == '__main__':
    hash3 = Shelveopen('Hash#3.shelve')
    hash4 = Shelveopen('Hash#4.shelve')
    graph = Shelveopen('Graph.shelve')
    graph.clear() #Overwrite new graph
    
    # Showgraph(graph, 'tiger.n.01')
    try:
        start_time = time.time()
        for key in hash3.keys():
            #Initialize empty list for each entry
            graph[key] = list()
            Words(key, hash3[key])
            word_count += 1
        for key in hash4.keys():
            #Initialize empty list for each entry
            graph[key] = list()
            Synsets(key, hash4[key])
            synset_count += 1
        end_time = time.time()
        print 'Graph Creation Time : ',end_time - start_time
        raise StopIteration('All Entries Processed')
    except Exception as e:
        handle_error(e)