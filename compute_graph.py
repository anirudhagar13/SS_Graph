import shelve
try:
    import cPickle as pickle
except:
    import pickle

HASH1 = 'Hash#1.shelve'
word_data = dict()
sense_data = dict()

def word_processing():
    hash1 = shelve.open(HASH1)
    #word_data = shelve.open('word_data.shelve')
    for w in hash1.keys():
        word_data[w] = dict()
        word_data[w]['word_to_sense'] = list()
        word_data[w]['defn_word_to_sense'] = dict()
        word_ = hash1[w]
        for i in word_.Noun_synsets():
            word_data[w]['word_to_sense'].append((i,-1,-1))
        for i in word_.Verb_synsets():
            word_data[w]['word_to_sense'].append((i,-1,-1))
        for i in word_.Adj_synsets():
            word_data[w]['word_to_sense'].append((i,-1,-1))
        for i in word_.Adv_synsets():
            word_data[w]['word_to_sense'].append((i,-1,-1))
    #word_data.close()
    hash1.close()
    pickle.dump( word_data, open( "word_data.pkl", "wb" ) )

def get_words(input_str,size_):
    '''
        strip words from sentence acc to value of 'size_'
    '''
    input_tokens = input_str.split(' ')
    if size_ == 1:
        return input_tokens
    if size_ == 2:
        tokens = list()
        for i in range(0,len(input_tokens)-1):
            val = str(input_tokens[i:i+size_][0]) + str(' ') + str(input_tokens[i:i+size_][1])
            tokens.append(val)
        return tokens

def number_non_noise_words(synset_defn):
    '''
        return the number of non noise words in synset_defn
    '''
    #TODO
    return len(synset_defn.split(' '))

def sense_to_word_processing(synset_defn,synset_name,tokens,word_type):
    '''
        sense - definition words
        sense - example words, processing
        checks that words must exist in wordnet
        returns list of words existing in wordnet(vocab_words)
    '''
    hash1 = shelve.open(HASH1)
    vocab_words = list()
    for tkn in tokens:
        #print '*******************************************************************'
        #print type(tkn)
        if hash1.has_key(tkn): #word node exists in wordnet
            print 'tkn = ' + str(":") + tkn
            vocab_words.append(tkn)
            if(word_type == 'definition'):
                #print '*******************************************************************'
                count = sum(1 for _ in re.finditer(r'\b%s\b' % re.escape(tkn), synset_defn))
                sense_data[synset_name]['sense_to_defn_word'].append((tkn, count, number_non_noise_words(synset_defn)))
            elif(word_type == 'example'):
                sense_data[synset_name]['sense_to_ex_word'].append((tkn,1))
    hash1.close()
    return vocab_words

def remove_overlap_words(tokens_1, tokens_2):
    final = list()
    flag = 0
    for tkn in tokens_1:
        for tkn2 in tokens_2:
            if tkn in tkn2.split(' '):
                flag = 1
                break
        if flag == 0:
            final.append(tkn)
        flag = 0
    return final

def defn_word_to_sense_processing(synset_defn,synset,tokens_1,tokens_2):
    hash1 = shelve.open(HASH1)
    for word in tokens_1+tokens_2:
        if hash1.has_key(word):
            #-1 => total number of occurences of word in all nodes in the graph; compute this after all ops
            count = sum(1 for _ in re.finditer(r'\b%s\b' % re.escape(word), synset_defn))
            word_data[word]['defn_word_to_sense'][synset] = (count,-1)
        else:
            #put to logs
            pass
    hash1.close()

def update_words_frequency(tokens_1,tokens_2):
    '''
        word_freq - shelve dict
    '''
    word_freq = shelve.open('word_freq.shelve')
    for word in tokens_1+tokens_2:
        if word in word_freq:
            v = word_freq[word] #Do not change; necessary to assign values to shelve variables
            v += 1
            word_freq[word] = v
        else:
            word_freq[word] = 1
    word_freq.close()

def sense_processing(filename):
    hash2 = shelve.open(filename)
    for s in hash2.keys()[:1]:
        #print hash2[s]

        sense_data[s] = dict()
        synset_ = hash2[s]

        synset_defn = synset_.definition()
        print synset_defn

        #sense_data[s]['sense_to_main_word'] =

        #TODO - remove non noise words in definition of sense before creating the 'sense-defn word' connections
        sense_data[s]['sense_to_defn_word'] = list()
        tokens_2 = get_words(synset_defn,2)
        tokens_2 = sense_to_word_processing(synset_defn,s,tokens_2,'definition')
        tokens_1 = get_words(synset_defn,1)
        tokens_1 = remove_overlap_words(tokens_1,tokens_2)
        sense_to_word_processing(synset_defn,s,tokens_1,'definition')#change this - pass both tokens_1 and tokens_2 together
        print sense_data[s]['sense_to_defn_word']
        update_words_frequency(tokens_1,tokens_2)###

        defn_word_to_sense_processing(synset_defn,s,tokens_1,tokens_2)

        sense_data[s]['sense_to_example_word'] = list()
        for example in synset_.examples():
            tokens_1 = get_words(example,1)
            sense_to_word_processing(synset_defn,s,tokens_1,'example')


        #sense_data[s]['hyponyms'] =

        sense_data[s]['hypernyms'] = synset_.hypernyms()
        sense_data[s]['holonyms'] = synset_.holonyms()
        sense_data[s]['meronyms'] = synset_.meronyms()
        sense_data[s]['entailments'] = synset_.entailments()
        sense_data[s]['similar_tos'] = synset_.similar_tos()

    pickle.dump( sense_data, open( "sense_data.pkl", "wb" ) )

if __name__ == "__main__":
    #word_processing()
    sense_processing(filename='Hash#2.shelve')
