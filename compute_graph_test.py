import shelve
try:
    import cPickle as pickle
except:
    import pickle

if __name__ == "__main__":

    '''
    word_data = pickle.load( open( "word_data.pkl", "rb" ) )
    assert word_data['dog']['word_to_sense'][0][0] == 'dog.n.01'
    #print word_data['dog']['defn_word_to_sense']
    '''


    sense_data = pickle.load( open('sense_data.pkl','rb'))
    print sense_data.keys()[3]
    #print sense_data['alum.n.01']['sense_to_defn_word']
    print sense_data[sense_data.keys()[3]]


    '''
    hash2 = shelve.open('Hash#2.shelve')
    #hash2['christian_holy_day.n.01']
    if hash2.has_key('religious_holiday.n.01'):
        print 'in'
        print hash2['christian_holy_day.n.01'].hypernyms()
    hash2.close()
    '''
