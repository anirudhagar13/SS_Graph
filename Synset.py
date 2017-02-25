from Commons import Unicode
class Synset:
    def __init__(self, synset):
        '''
        Parent Class Constructor
        '''
        self._pos = Unicode(synset.pos())
        self._name = Unicode(synset.name())
        self._definition = Unicode(synset.definition())
        self._examples = Unicode(synset.examples())
        self._lemma_names = Unicode(synset.lemma_names())

    def name(self):
        '''
        Getter for name property
        '''
        return self._name

    def definition(self):
        '''
        Getter for definition property
        '''
        return self._definition

    def examples(self):
        '''
        Getter for examples property
        '''
        return self._examples

    def lemma_names(self):
        '''
        Getter for lemma_names property
        '''
        return self._lemma_names

    def pos(self):
        '''
        Getter for examples property
        '''
        return self._pos

    def __str__(self):
        '''
        Each Object represented by Label
        '''
        return self._name

class Noun_Synset(Synset):
    def __init__(self, synset):
        '''
        Subclass Constructor
        '''
        Synset.__init__(self, synset)
        self._hypernyms = list()
        self._hyponyms = list()

    def hypernyms(self):
        '''
        Getter for hypernyms
        '''
        return self._hypernyms

    def hyponyms(self):
        '''
        Getter for hyponyms
        '''
        return self._hyponyms

    def populate(self, type, data):
        if type == 'hypernyms':
            self._hypernyms.extend(data)
        elif type == 'hyponyms':
            self._hyponyms.extend(data)
        else:
            print 'Invalid Property, not exists!'

class Verb_Synset(Synset):
    def __init__(self, synset):
        '''
        Subclass ctor
        '''
        Synset.__init__(self, synset)

class Adjective_Synset(Synset):
    def __init__(self, synset):
        '''
        Subclass  ctor
        '''
        Synset.__init__(self, synset)

class Adverb_Synset(Synset):
    def __init__(self, synset):
        '''
        Subclass ctor
        '''
        Synset.__init__(self, synset)