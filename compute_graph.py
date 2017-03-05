import shelve

word_data = dict()
sense_data = dict()

def word_processing(filename):
    hash1 = shelve.open(filename)
    #print hash1['dog'].Noun_synsets()[0]
    #word_data[''] = list()
    #word_data['defn_word_to_sense'] = dict()
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

def get_words(input_str,size_):
    input_tokens = s.split(' ')
    tokens = list()
    for i in range(0,len(input_tokens)-1):
        tokens.append(input_tokens[i:i+size_])
    print tokens

def sense_to_word_processing(synset_defn,tokens,word_type):
    for tkn in tokens:
        if hash1.has_key(tkn):
            if(word_type == 'definition'):
                sense_data[s]['sense_to_defn_word'].append( \
                (tkn, synset_defn.count(tkn), number_non_noise_words(synset_defn))
            elif word_type == 'example':
                sense_data[s]['sense_to_ex_word'].append(tkn,1)

def sense_processing(filename):
    hash2 = shelve.open(filename)
    for s in hash2.keys():
        #for each synset
        sense_data[s] = dict()
        #sense_data[s]['sense_to_main_word'] =
        synset_defn = s.definition()

        sense_data[s]['sense_to_defn_word'] = list()
        tokens_2 = get_words(synset_defn,2)
        sense_to_word_processing(synset_defn,tokens_2.'definition')
        tokens_1 = get_words(synset_defn,1)
        sense_to_word_processing(synset_defn,tokens_1,'definition')#change this

        sense_data[s]['sense_to_example_word'] = list()
        for example in s.examples():
            tokens_1 = get_words(example,1)
            sense_to_word_processing(synset_defn,tokens_1,'example')

        sense_data[s]['hypernyms'] = list()


if __name__ == "__main__":
    #word_processing(filename='Hash#1.shelve')
    sense_processing(filename='Hash#2.shelve')
