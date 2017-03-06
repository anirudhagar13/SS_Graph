import shelve
import re
try:
    import cPickle as pickle
except:
    import pickle

HASH1 = 'Hash#1.shelve'
#word_data = dict()
#sense_data = dict()

def word_processing(wd_filename):
    word_data = dict()
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
    pickle.dump( word_data, open( wd_filename, "wb" ) )

def get_words(input_str,size_):
    '''
        strip words from sentence acc to value of 'size_'
        check word existence in wordnet data
    '''
    hash1 = shelve.open(HASH1)
    input_tokens = input_str.split(' ')
    if size_ == 1:
        for tkn in input_tokens:
            if not hash1.has_key(tkn):
                input_tokens.remove(tkn)
        return input_tokens
    if size_ == 2:
        tokens = list()
        for i in range(0,len(input_tokens)-1):
            val = str(input_tokens[i:i+size_][0]) + str(' ') + str(input_tokens[i:i+size_][1])
            if hash1.has_key(val):
                tokens.append(val)
        return tokens

def number_non_noise_words(synset_defn):
    '''
        return the number of non noise words in synset_defn
    '''
    #TODO
    return len(synset_defn.split(' '))

def count_words(word, input_str):
    return sum(1 for _ in re.finditer(r'\b%s\b' % re.escape(word), input_str))

def sense_to_word_processing(sense_data,synset_defn,synset_name,tokens,word_type):
    '''
        sense - definition words
        sense - example words, processing
    '''
    hash1 = shelve.open(HASH1)
    for tkn in tokens:
        if(word_type == 'definition'):
            sense_data[synset_name]['sense_to_defn_word'].append((tkn, count_words(tkn,synset_defn), number_non_noise_words(synset_defn)))
        elif(word_type == 'example'):
            sense_data[synset_name]['sense_to_example_word'].append((tkn,1))
    hash1.close()

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

def defn_word_to_sense_processing(synset_defn,synset,wd_filename,tokens_1,tokens_2):
    hash1 = shelve.open(HASH1)
    word_data = pickle.load( open(wd_filename,'rb'))
    for word in tokens_1+tokens_2:
        if hash1.has_key(word):
            #-1 => total number of occurences of word in all nodes in the graph; compute ONLY THIS after all ops are done
            try:
                word_data[word]['defn_word_to_sense'][synset] = (count_words(word, synset_defn),-1)
            except Exception as e:
                if 'a' not in word_data:
                    print 'Error : Word not found in dict word_data'
                else:
                    print e
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

def sense_processing(sd_filename,wd_filename):
    sense_data = dict()
    hash2 = shelve.open('Hash#2.shelve')
    for s in hash2.keys():
        sense_data[s] = dict()
        synset_ = hash2[s]

        synset_defn = synset_.definition()

        #print 'synset_defn = ' + str(synset_defn)

        #sense_data[s]['sense_to_main_word'] =

        #TODO - remove non noise words in definition of sense before creating the 'sense-defn word' connections
        sense_data[s]['sense_to_defn_word'] = list()
        tokens_2 = get_words(synset_defn,2)
        if tokens_2:
            sense_to_word_processing(sense_data,synset_defn,s,tokens_2,'definition')
        tokens_1 = get_words(synset_defn,1)
        tokens_1 = remove_overlap_words(tokens_1,tokens_2)
        if tokens_1:
            sense_to_word_processing(sense_data,synset_defn,s,tokens_1,'definition')#change this - pass both tokens_1 and tokens_2 together
        #print "\t" + str(s) + str(" : ") + str('***************  sense_to_defn_word done  ************************')

        update_words_frequency(tokens_1,tokens_2)###

        if tokens_1 or tokens_2:
            defn_word_to_sense_processing(synset_defn,s,wd_filename,tokens_1,tokens_2)
        #print "\t" + str(s) + str(" : ") + str('***************  defn_word_to_sense done  ************************')

        sense_data[s]['sense_to_example_word'] = list()
        if synset_.examples():
            for example in synset_.examples():
                tokens_1 = get_words(example,1)
                sense_to_word_processing(sense_data,synset_defn,s,tokens_1,'example')
        #print "\t" + str(s) + str(" : ") + str('***************  sense_to_example_word done  ************************')

        #sense_data[s]['hyponyms'] =

        sense_data[s]['hypernyms'] = synset_.hypernyms()
        sense_data[s]['holonyms'] = synset_.holonyms()
        sense_data[s]['meronyms'] = synset_.meronyms()
        sense_data[s]['entailments'] = synset_.entailments()
        sense_data[s]['similar_tos'] = synset_.similar_tos()
        #print "\t" + str(s) + str(" : ") + str('*************** sense-sense relations done  ************************')

    pickle.dump( sense_data, open( sd_filename, "wb" ) )

if __name__ == "__main__":
    #word_processing(wd_filename='word_data.pkl')
    sense_processing(sd_filename='sense_data.pkl', wd_filename='word_data.pkl')
