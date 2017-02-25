class Word:
    def __init__(self, name, category):
        self._category = category
        self._name = name

        #list of synsets
        self._nounsyn = list()
        self._verbsyn = list()
        self._adjsyn = list()
        self._advsyn = list()

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

    def Adv_synsets(self):
        '''
        Getter for adverb synsets attribute
        '''
        return self._advsyn

    def populate(self, synset):
        if synset.pos() == 'n':
            self._nounsyn.append(synset.name())
        elif synset.pos() == 'v':
            self._verbsyn.append(synset.name())
        elif synset.pos() == 'a':
            self._adjsyn.append(synset.name())
        elif synset.pos() == 'r':
            self._advsyn.append(synset.name())
        else:
            print 'Invalid Type, not exists!'

