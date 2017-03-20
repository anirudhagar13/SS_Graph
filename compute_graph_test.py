import shelve
try:
    import cPickle as pickle
except:
    import pickle

if __name__ == "__main__":

    '''
    word_data = pickle.load( open( "Hash#3.shelve", "rb" ) )
    #assert word_data['dog']['word_to_sense'][0][0] == 'dog.n.01'
    print word_data['american']['D2S']
    '''

    '''
    #sense_data = pickle.load( open('Hash#4.shelve','rb'))
    sense_data = shelve.open("Hash#4.shelve")
    print sense_data.keys()[3]
    #print sense_data['alum.n.01']['sense_to_defn_word']
    print sense_data[sense_data.keys()[3]]
    sense_data.close()
    '''
    sense_data = shelve.open("Hash#4.shelve")
    for i in sense_data.keys():
        if not sense_data[i]['S2W']:
            print 'S2W : ' + str(i)
        if not sense_data[i]['S2D']:
            print 'S2D : ' + str(i)
    sense_data.close()

    word_data = shelve.open('Hash#3.shelve')
    for i in word_data:
        if not word_data[i].has_key('D2S'):
            print i

    '''
    hash2 = shelve.open('Hash#2.shelve')
    #hash2['christian_holy_day.n.01']
    if hash2.has_key('religious_holiday.n.01'):
        print 'in'
        print hash2['christian_holy_day.n.01'].hypernyms()
    hash2.close()
    '''
