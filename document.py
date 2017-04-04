import string
from collections import Counter
from Wordclient import Wordclient
from compute_graph import get_words, remove_overlap_words
from Computegraph import Removestopwords

class Document:

    '''
    '''
    def __init__(self,text_,type_, edge_weight_):
        self.intialize_tokens(text_)
        self.type = type_
        self.edge_weight = edge_weight_

    def intialize_tokens(self, text):
        text = text.translate(None, string.punctuation)
        text = ' '.join(Removestopwords(text.strip().split()))
        tokens_2 = get_words(input_str=text, size_=2)
        tokens_1 = get_words(input_str=text, size_=1)
        tokens_1 = remove_overlap_words(tokens_1, tokens_2)
        all_tokens = tokens_1+tokens_2
        counts = Counter(all_tokens)
        list_len = len(all_tokens)
        self.tokens = dict()
        for tkn in all_tokens:
            self.tokens[tkn] = (Wordclient(tkn), round(float(counts[tkn])/list_len,3))

    def get_tokens(self):
        return self.tokens


if __name__ == "__main__":
    d = Document(text_='united states is a country.', type_='doc1.heading', edge_weight_=0.6)
    #print d.edge_weight
    print d.tokens
    #print d.type
