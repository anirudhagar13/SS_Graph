import pytest
from Word import *
from nltk.corpus import wordnet as wn
import collections
import shelve

hash1 = shelve.open('Hash#1.shelve')

@pytest.fixture
def word():
    def take_options(wrd='a'):
        return hash1[wrd]

def compare_(l1,l2):
    flag = 0
    for i in l2:
        if str(i.name) not in l1:
            flag = 1
            break
    return flag

def test_word(word):
    word_ = 'dog'
    assert compare_(hash1[word_].Noun_synsets(),wn.synsets(word_,pos='n')) == 1
    assert compare_(hash1[word_].Verb_synsets(),wn.synsets(word_,pos='n')) == 1
    assert compare_(hash1[word_].Adj_synsets(),wn.synsets(word_,pos='n')) == 1
    assert compare_(hash1[word_].Adjsat_synsets(),wn.synsets(word_,pos='n')) == 1
    assert compare_(hash1[word_].Adv_synsets(),wn.synsets(word_,pos='n')) == 1

    word_ = 'good'
    assert compare_(hash1[word_].Noun_synsets(),wn.synsets(word_,pos='n')) == 1
    assert compare_(hash1[word_].Verb_synsets(),wn.synsets(word_,pos='n')) == 1
    assert compare_(hash1[word_].Adj_synsets(),wn.synsets(word_,pos='n')) == 1
    assert compare_(hash1[word_].Adjsat_synsets(),wn.synsets(word_,pos='n')) == 1
    assert compare_(hash1[word_].Adv_synsets(),wn.synsets(word_,pos='n')) == 1
    hash1.close()

'''
if __name__ == "__main__":

    hash1 = shelve.open('Hash#1.shelve')
    print hash1.__sizeof__
    hash1.close()
'''
