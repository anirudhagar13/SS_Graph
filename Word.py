class Word:
    def __init__(self, name, category):
        self._category = category
        self._name = name

        #list of synsets
        self._nounsyn = list()
        self._verbsyn = list()
        self._adjsyn = list()
        self._advsyn = list()
        self._adjsatsyn = list()

    def __str__(self):
        '''
        Each Object represented by name
        '''
        return self._name

    def category(self):
        '''
        Getter for category attribute
        '''
        return self._category

    def name(self):
        '''
        Getter for name attribute
        '''
        return self._name

    def Noun_synsets(self):
        '''
        Getter for noun synsets attribute
        '''
        return self._nounsyn

    def Verb_synsets(self):
        '''
        Getter for verb synsets attribute
        '''
        return self._verbsyn

    def Adj_synsets(self):
        '''
        Getter for adjective synsets attribute
        '''
        return self._adjsyn

    def Adjsat_synsets(self):
        '''
        Getter for adjective satellite synsets attribute
        '''
        return self._adjsatsyn

    def Adv_synsets(self):
        '''
        Getter for adverb synsets attribute
        '''
        return self._advsyn

    def populate(self, synset):
        pos = synset.pos()
        name = synset.name()

        #Avoid duplicates
        if pos == 'n':
            if name not in self._nounsyn:
                self._nounsyn.append(name)
        elif pos == 'v':
            if name not in self._verbsyn:
                self._verbsyn.append(name)
        elif pos == 'a':
            if name not in self._adjsyn:
                self._adjsyn.append(name)
        elif pos == 'r':
            if name not in self._advsyn:
                self._advsyn.append(name)
        elif pos == 's':
            if name not in self._adjsatsyn:
                self._adjsatsyn.append(name)
        else:
            print 'Invalid POS - ',pos