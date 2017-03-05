from Commons import *
from Edge import *

#Globals
hash3 = {}
graph = {}
count = 0

def Words(src, data):
    '''
    Create Word Edges
    '''
    #Initializing empty list to store edges
    graph[src] = list()
    for key, value in data.items():
        if key == 'W2S':
            W2S(src, value)
        elif key == 'D2S':
            D2S(src, value)
        else:
            raise Exception('Word Edge not defined')

def Synsets(src, data):
    '''
    Create Word Edges
    '''
    #Initializing Empty lists to store edges
    graph[src] = list()
    for key, value in data.items():
        if key == 'S2W':
            S2W(src, value)
        elif key == 'S2D':
            S2D(src, value)
        elif key == 'S2E':
            S2E(src, value)
        elif key == 'Hyponym':
            Hyponym(src, value)
        elif key == 'Hypernym':
            Hypernym(src, value)
        elif key == 'Meronym':
            Meronym(src, value)
        elif key == 'Holonym':
            Holonym(src, value)
        elif key == 'Similar':
            Similar(src, value)
        elif key == 'Entailment':
            Entailment(src, value)
        else:
            raise Exception('Synset Edge not defined')

#******Synset Functions********
def S2W(src, data):
    '''
    To create sense to word edges
    '''
    for dest in data:
        edge = Edge(src=src, dest=dest, kind='S2W')
        edge.populate()

        #Adding edge created in graph
        graph[src].append(edge)

def S2D(src, data):
    '''
    To create sense to non-noise words in definition
    '''
    #Each edge is a dictionary, data is list of dictionaries
    for item in data:
        dest = item['dest']
        frequency = item['frequency']
        total_freq = item['total_freq']
        edge = Edge(src=src, dest=dest, kind='S2D')
        edge.populate(frequency=frequency, total_freq=total_freq)

        #Adding edge created in graph
        graph[src].append(edge)

def S2E(src, data):
    '''
    To create sense to non-noise words in example
    '''
    #Each edge is a dictionary, data is list of dictionaries
    for item in data:
        dest = item['dest']
        frequency = item['frequency']
        total_freq = item['total_freq']
        edge = Edge(src=src, dest=dest, kind='S2E')
        edge.populate(frequency=frequency, total_freq=total_freq)

        #Adding edge created in graph
        graph[src].append(edge)

def Hypernym(src, data):
    '''
    To create hypernym edges
    '''
    for dest in data:
        edge = Edge(src=src, dest=dest, kind='Hypernym')
        edge.populate()

        #Adding edge created in graph
        graph[src].append(edge)

def Hyponym(src, data):
    '''
    To create hyponym edges
    '''
    for dest in data:
        edge = Edge(src=src, dest=dest, kind='Hyponym')
        edge.populate()

        #Adding edge created in graph
        graph[src].append(edge)

def Holonym(src, data):
    '''
    To create holonym edges
    '''
    for dest in data:
        edge = Edge(src=src, dest=dest, kind='Holonym')
        edge.populate()

        #Adding edge created in graph
        graph[src].append(edge)

def Similar(src, data):
    '''
    To create similar edges
    '''
    for dest in data:
        edge = Edge(src=src, dest=dest, kind='Similar')
        edge.populate()

        #Adding edge created in graph
        graph[src].append(edge)

def Entailment(src, data):
    '''
    To create entailment edges
    '''
    for dest in data:
        edge = Edge(src=src, dest=dest, kind='Entailment')
        edge.populate()

        #Adding edge created in graph
        graph[src].append(edge)

def Meronym(src, data):
    '''
    To create hypernym edges
    '''
    num_mero = len(data)
    for dest in data:
        edge = Edge(src=src, dest=dest, kind='Hypernym')
        edge.populate(num_mero=num_mero)

        #Adding edge created in graph
        graph[src].append(edge)

#******Word Functions********
def W2S(src, data):
    '''
    To create word to sense edges
    '''
    #Each edge is a dictionary, data list of dictionaries
    for item in data:
        dest = item['dest']
        frequency = item['frequency']
        total_freq = item['total_freq']
        edge = Edge(src=src, dest=dest, kind='W2S')
        edge.populate(frequency=frequency, total_freq=total_freq)

        #Adding edge created in graph
        graph[src].append(edge)

def D2S(src, data):
    '''
    To create word to sense backedges in which it occurs
    '''
    total_freq = sum(data.values())
    for dest, frequency in data.items():
        edge = Edge(src=src, dest=dest, kind='D2S')
        edge.populate(frequency=frequency, total_freq=total_freq)

        #Adding edge created in graph
        graph[src].append(edge)

def handle_error(e):
    '''
    To Catch and show exceptions
    '''
    print 'Log - ',e
    print 'Entries Processed - ',count
    Shelveclose(hash3)
    Shelveclose(graph)

if __name__ == '__main__':
    hash3 = Shelveopen('Hash#3.shelve')
    graph = Shelveopen('Graph.shelve')
    try:
        for key in hash3.keys()[:10]:
            if '.' in key:
                #Distinguish between words and Synsets
                Words(key, hash3[key])
            else:
                Synsets(key, hash3[key])
            count += 1
        raise StopIteration('All Entries Processed')
    except Exception as e:
        handle_error(e)