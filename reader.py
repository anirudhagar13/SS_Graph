from document import Document
from Wordclient import Wordclient
from benchmark import manager
from Commons import computeMinMax
import math

matching_doc1 = dict()
matching_doc2 = dict()

def doc_score(doc1, doc2):
    '''
        doc1/2 - instance of class Document corresponding to document1/2
    '''
    global matching_doc1
    global matching_doc2
    total_score = 0.0
    doc1_tokens = doc1.get_tokens()
    doc2_tokens = doc2.get_tokens()
    doc1_edge_wt = doc1.edge_weight
    doc2_edge_wt = doc2.edge_weight

    for i in doc1_tokens:
        i_wc_inst = doc1_tokens[i][0]
        i_freq = doc1_tokens[i][1]
        for j in doc2_tokens:
            score_fwd = i_wc_inst.score(j)
            score_bkwd = doc2_tokens[j][0].score(i)
            if score_fwd != 0:
                try:
                    matching_doc1[i].append(j)
                except KeyError:
                    matching_doc1[i] = [j]
            if score_bkwd != 0:
                try:
                    matching_doc2[j].append(i)
                except KeyError:
                    matching_doc2[j] = [i]
            total_score += ( computeMinMax(0,doc1_edge_wt,i_freq) * manager(score_fwd,score_bkwd) *
                            computeMinMax(0,doc2_edge_wt,doc2_tokens[j][1]) )
    return total_score

if __name__ == '__main__':
    doc1 = Document(text_='united states is a car car.', type_='doc1.heading', edge_weight_ = 0.6)
    doc2 = Document(text_='this is a sample engine!', type_='doc2.heading', edge_weight_ = 0.6)
    print doc_score(doc1,doc2)
    print matching_doc1
    print matching_doc2
