try:
    import cPickle as pickle
except:
    import pickle

if __name__ == "__main__":
    word_data = pickle.load( open( "word_data.pkl", "rb" ) )
    assert word_data['dog']['word_to_sense'][0][0] == 'dog.n.01'
    print word_data['dog']['defn_word_to_sense']
