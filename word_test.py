import pytest
from Word import *
from nltk.corpus import wordnet as wn
import collections
import shelve

#hash1 = shelve.open('Hash#1.shelve')

@pytest.fixture
def word():
    return hash1['dog']

def compare_(l1,l2):
    flag = 0
    for i in l2:
        if str(i.name) not in l1:
            flag = 1
            break
    return flag

def test_word(word):
    assert compare_(word.Noun_synsets(),wn.synsets('dog',pos='n')) == 1
    hash1.close()

if __name__ == "__main__":

    hash1 = shelve.open('Hash#1.shelve')
    print hash1.__sizeof__
    hash1.close()
