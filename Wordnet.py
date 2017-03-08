from nltk.corpus import wordnet as wn

class Wordnet:
    def __init__(self):
        # self.callback = callback
        self.all_lemmas = None

    def initiliaze_lemma_list(self):
        self.all_lemmas = wn.all_lemma_names()

    def next_word(self):
        lemma = self.all_lemmas.next()
        return lemma