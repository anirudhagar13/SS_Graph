try:
    import cPickle as pickle
except:
    import pickle

if __name__ == "__main__":

    '''
    word_data = pickle.load( open( "word_data.pkl", "rb" ) )
    assert word_data['dog']['word_to_sense'][0][0] == 'dog.n.01'
    print word_data['dog']['defn_word_to_sense']
    '''
    sense_data = pickle.load( open('sense_data.pkl','rb'))
    #print sense_data.keys()
    print sense_data['alum.n.01']['sense_to_defn_word']
