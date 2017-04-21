from Commons import Unicode

class Synset:
    def __init__(self, category, synset=None, props=None):
        '''
        Parent Class Constructor
        '''
        if synset is None:
            # Creating external words
            self._category = category
            self.addsynset(props)
        else:
            # It is wordnet
            self._pos = Unicode(synset.pos())
            self._category = category
            self._name = Unicode(synset.name())
            self._definition = Unicode(synset.definition())
            self._examples = Unicode(synset.examples())
            self._lemma_names = Unicode(synset.lemma_names())
            self._lemma_count = self.Sensecount(synset)
            self._hypernyms = list()
            self._hyponyms = list()
            self._meronyms= list()
            self._holonyms = list()
            self._entailments = list()
            self._similar_tos = list()

    def name(self):
        '''
        Getter for name property
        '''
        return self._name

    def category(self):
        '''
        Getter for category property
        '''
        return self._category

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

    def lemma_count(self):
        '''
        Getter for lemma_count property
        '''
        return self._lemma_count

    def pos(self):
        '''
        Getter for examples property
        '''
        return self._pos

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

    def meronyms(self):
        '''
        Getter for meronyms
        '''
        return self._meronyms

    def holonyms(self):
        '''
        Getter for holonyms
        '''
        return self._holonyms

    def entailments(self):
        '''
        Getter for Entailments
        '''
        return self._entailments

    def similar_tos(self):
        '''
        Getter for Similar Tos
        '''
        return self._similar_tos


    def __str__(self):
        '''
        Each Object represented by name
        '''
        return self._name

    def addsynset(self, props):
        try:
            print 'New Synset Being Added'
            # Add new synsets
            # Necessary least properties
            self._pos = props['pos']
            self._name = props['name']
            self._definition = props['definition'].lower()
            self._lemma_names = props['lemma_names']
            self._lemma_count = props['lemma_count']

            # Non-necessary properties
            self._examples = [[]]   # It is list of lists
            self._hypernyms = list()
            self._hyponyms = list()
            self._meronyms= list()
            self._holonyms = list()
            self._entailments = list()
            self._similar_tos = list()

            if 'example' in props:
                self._examples[0] = props['example'].lower()
            if 'hypernyms' in props:
                self._hypernyms = props['hypernyms']
            if 'hyponyms' in props:
                self._hyponyms = props['hyponyms']
            if 'meronyms' in props:
                self._meronyms = props['meronyms']
            if 'holonyms' in props:
                self._holonyms = props['holonyms']
            if 'entailments' in props:
                self._entailments = props['entailments']
            if 'similar_tos' in props:
                self._similar_tos = props['similar_tos']

        except Exception as e:
            print 'Adding New Synset : ',e


    def Sensecount(self, wn_synset):
        '''
        To fill lemma counts in wordnet
        '''
        data = list()
        for lemma in wn_synset.lemmas():
            count = 1 + lemma.count()   #to avoid zeros
            data.append(count)
        return data

    def populate(self, type, data):
        #Avoid duplicates
        if type == 'hypernyms':
            for synset in data:
                if synset not in self._hypernyms:
                    self._hypernyms.append(synset)
        elif type == 'hyponyms':
            for synset in data:
                if synset not in self._hyponyms:
                    self._hyponyms.append(synset)
        elif type == 'meronyms':
            for synset in data:
                if synset not in self._meronyms:
                    self._meronyms.append(synset)
        elif type == 'holonyms':
            for synset in data:
                if synset not in self._holonyms:
                    self._holonyms.append(synset)
        elif type == 'entailments':
            for synset in data:
                if synset not in self._entailments:
                    self._entailments.append(synset)
        elif type == 'similar':
            for synset in data:
                if synset not in self._similar_tos:
                    self._similar_tos.append(synset)
        else:
            print 'Invalid Property, not exists!'