from __future__ import division
from Hypers import *
from Commons import computeMinMax

class Edge(object):
    """docstring for Edge"""
    def __init__(self, kind='', src='', dest=''):
        self.kind = kind
        self.src = src
        self.dest = dest
        self.weight = 0

    def __str__(self):
        '''
        Making edge printable
        '''
        data = self.src + ' ~>>{0}({1})>>> '.format(self.kind, self.weight) + self.dest
        return data

    #******Word Functions*******
    def W2S(self, **kwargs):
        '''
        Word to Sense Edge
        '''
        freq = kwargs['frequency']
        tot_freq = kwargs['total_freq']
        self.weight = round(freq/tot_freq, 5)

    def D2S(self, **kwargs):
        '''
        Words to senses defn in which they are present
        '''
        freq = kwargs['frequency']
        tot_freq = kwargs['total_freq']
        prod = Hyper3*computeMinMax(0, DMax, freq/tot_freq)
        self.weight = round(prod, 5)

    def E2S(self, **kwargs):
        '''
        Words to senses defn in which they are present
        '''
        freq = kwargs['frequency']
        tot_freq = kwargs['total_freq']
        prod = Hyper3*computeMinMax(0, EMax, freq/tot_freq)
        self.weight = round(prod, 5)

     #******Synset Functions*******
    def S2W(self, **kwargs):
        '''
        Sense to its own wordforms
        '''
        self.weight = Hyper4

    def S2D(self, **kwargs):
        '''
        Sense to non-noise definition words
        '''
        freq = kwargs['frequency']
        tot_freq = kwargs['total_freq']
        prod = Hyper1*(freq/tot_freq)
        self.weight = round(prod, 5)

    def S2E(self, **kwargs):
        '''
        Sense to non-noise example words
        '''
        freq = kwargs['frequency']
        tot_freq = kwargs['total_freq']
        prod = Hyper2*(freq/tot_freq)
        self.weight = round(prod, 5)

    def Hyponym(self, **kwargs):
        '''
        For subsenses i.e. hyponyms
        '''
        self.weight = Hyper5

    def Hypernym(self, **kwargs):
        '''
        For hypernyms i.e. supersenses
        '''
        self.weight = Hyper6

    def Meronym(self, **kwargs):
        '''
        For Meronyms
        '''
        #1/total no of meronyms
        ratio = 1/kwargs['num_mero']
        self.weight =  round(Hyper7*ratio, 5)

    def Holonym(self, **kwargs):
        '''
        For Holonyms
        '''
        self.weight = Hyper8

    def Similar(self, **kwargs):
        '''
        For Similar to adjective senses
        '''
        self.weight = Hyper9

    def Entailment(self, **kwargs):
        '''
        For verb entailments
        '''
        self.weight = Hyper10

    def populate(self, **kwargs):
        '''
        To calcualte weight
        '''
        try:
            if self.kind == 'W2S':
                self.W2S(**kwargs)
            elif self.kind == 'D2S':
                self.D2S(**kwargs)
            elif self.kind == 'E2S':
                self.E2S(**kwargs)
            elif self.kind == 'S2W':
                self.S2W(**kwargs)
            elif self.kind == 'S2D':
                self.S2D(**kwargs)
            elif self.kind == 'S2E':
                self.S2E(**kwargs)
            elif self.kind == 'Hyponym':
                self.Hyponym(**kwargs)
            elif self.kind == 'Hypernym':
                self.Hypernym(**kwargs)
            elif self.kind == 'Meronym':
                self.Meronym(**kwargs)
            elif self.kind == 'Holonym':
                self.Holonym(**kwargs)
            elif self.kind == 'Entailment':
                self.Entailment(**kwargs)
            elif self.kind == 'Similar':
                self.Similar(**kwargs)
            else:
                raise Exception('Kind not defined')
        except Exception as e:
            print 'Error Edge - ',e