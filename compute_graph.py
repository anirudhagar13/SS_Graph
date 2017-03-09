import shelve
import pdb
import re
try:
    import cPickle as pickle
except:
    import pickle
from nltk.corpus import stopwords
from Commons import *

HASH1 = 'Hash#1.shelve'

#word_data = dict()
#sense_data = dict()

def word_processing(wd_filename):
    #word_data = dict()
    word_data = shelve.open(wd_filename, writeback=True)
    hash1 = shelve.open(HASH1)
    hash2 = shelve.open('Hash#2.shelve')
    count = 0
    #try:
    for w in hash1.keys():
        print w
        word_data[w] = dict()
        word_data[w]['W2S'] = list()

        #word_data[w]['D2S'] = dict()
        if w in hash1:
            word_ = hash1[w]
        else:
            print 'word_processing : ' + str(w) + ' not found in hash1'

        for i in word_.Noun_synsets() + word_.Verb_synsets() \
            + word_.Adj_synsets() + word_.Adv_synsets():
            if i in hash2:
                if w[-1:] == 's':
                    #simple_w = word_hash[w]
                    if w in hash2[i].lemma_names():
                        freq = hash2[i].lemma_count()[hash2[i].lemma_names().index(w)]
                    else:
                        print '&&&&&&&&&&&&&&&&word not found in lemma_names&&&&&&&&&&&&&&'
                        try:
                            word_hash = shelve.open('Word#.shelve')
                        except:
                            print 'cannot open word_hash'
                        w_mod = word_hash[w]
                        print w_mod
                        print '**************************************************'
                        word_hash.close()
                        try:
                            freq = hash2[i].lemma_count()[hash2[i].lemma_names().index(w_mod)]
                        except:
                            pass
                    total_freq = 10
                    word_data[w]['W2S'].append((i,freq,total_freq))
                else:
                    pass
            else:
                print 'word_processing : ' + str(i) + ' not found in hash2'

        count += 1
    '''
    except TypeError as e:
        print 'TypeError : ' + str(e)
    except KeyError as e:
        print 'KeyError : ' + str(e)
    except Exception as e:
        print e
    '''
    hash1.close()
    hash2.close()
    print 'word_processing() - Words processed : ' + str(count)
    #pickle.dump( word_data, open( wd_filename, "wb" ) )
    word_data.close()

def get_words(input_str,size_):
    '''
        strip words from sentence acc to value of 'size_'
        check word existence in wordnet data
    '''
    hash1 = shelve.open(HASH1)
    input_tokens = [x.lower() for x in input_str.split()]
    if size_ == 1:
        for tkn in input_tokens:
            if not hash1.has_key(tkn):
                input_tokens.remove(tkn)
        return input_tokens
    if size_ == 2:
        tokens = list()
        for i in range(0,len(input_tokens)-1):
            val = str(input_tokens[i:i+size_][0]) + str('_') + str(input_tokens[i:i+size_][1])
            if hash1.has_key(val):
                tokens.append(val)
        return tokens

def number_non_noise_words(synset_defn):
    '''
        return the number of non noise words in synset_defn
    '''
    '''
    cnt = 0
    for word in synset_defn.split():
        if word not in stopwords.words('english'):
            cnt += 1
    return cnt
    '''
    return len(synset_defn.split())

def count_words(word, input_str):
    if '_' in word:
        new_word = word.replace('_', ' ')
        return sum(1 for _ in re.finditer(r'\b%s\b' % re.escape(new_word), input_str))
    else:
        return sum(1 for _ in re.finditer(r'\b%s\b' % re.escape(word), input_str))

def sense_to_word_processing(sd_filename,synset_defn,synset_name,tokens,word_type):
    '''
        sense - definition words
        sense - example words, processing
    '''
    sense_data = shelve.open(sd_filename,writeback=True)
    hash1 = shelve.open(HASH1)
    for tkn in tokens:
        if(word_type == 'definition'):
            sense_data[synset_name]['S2D'].append((tkn, count_words(tkn,synset_defn), number_non_noise_words(synset_defn)))
        elif(word_type == 'example'):
            sense_data[synset_name]['S2E'].append((tkn,1))
    hash1.close()
    sense_data.close()

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
    #word_data = pickle.load( open(wd_filename,'rb'))
    word_data = shelve.open(wd_filename,writeback=True)
    for word in tokens_1+tokens_2:
        if hash1.has_key(word):
            #-1 => total number of occurences of word in all nodes in the graph; compute ONLY THIS after all ops are done
            try:
                if word_data[word]:
                    word_data[word]['D2S'] = dict()
                    word_data[word]['D2S'][synset] = count_words(word, synset_defn)
                    if count_words(word, synset_defn) == 0:
                        print word + str(" : ") + synset_defn
                        print 'zero'
                else:
                    word_data[word] = dict()
                    word_data[word]['D2S'] = dict()
                    word_data[word]['D2S'][synset] = count_words(word, synset_defn)
                    if count_words(word, synset_defn) == 0:
                        print word + str(" : ") + synset_defn
                        print 'zero'
            except KeyError as e:
                print 'Defn_word_to_sense - KeyError - Word: ' + word + ' : not found in dict word_data'
            except Exception as e:
                if word not in word_data:
                    print 'Defn_word_to_sense -  Word - ' + word + ' : not found in dict word_data'
                else:
                    print 'defn_word_to_sense_processing : ' + str(e)
        else:
            #put to logs
            pass
    #pickle.dump( word_data, open( wd_filename, "wb" ) )
    word_data.close()
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

def handle_error(sense_data,sd_filename):
    print 'something seriously f*cked up'
    #pickle.dump( sense_data, open( 'sense_data.pkl', "wb" ) )
    #pickle.dump( sense_data, open( sd_filename, "wb" ) )
    sense_data.close()

def sense_processing(sd_filename,wd_filename):
    #sense_data = dict()
    #sense_data = shelve.open(sd_filename,writeback=True)
    hash2 = shelve.open('Hash#2.shelve')
    #try:
    for s in hash2.keys()[:200]:
        sense_data = shelve.open(sd_filename,writeback=True)
        print s
        sense_data[s] = dict()
        synset_ = hash2[s]

        synset_defn = synset_.definition()

        #print 'synset_defn = ' + str(synset_defn)

        sense_data[s]['S2W'] = list()
        for i in synset_.lemma_names():
            sense_data[s]['S2W'].append((i,1))


        #TODO - remove non noise words in definition of sense before creating the 'sense-defn word' connections
        sense_data[s]['S2D'] = list()
        sense_data.close()
        tokens_2 = get_words(synset_defn,2)
        if tokens_2:
            sense_to_word_processing(sd_filename,synset_defn,s,tokens_2,'definition')

        tokens_1 = get_words(synset_defn,1)
        tokens_1 = remove_overlap_words(tokens_1,tokens_2)
        if tokens_1:
            sense_to_word_processing(sd_filename,synset_defn,s,tokens_1,'definition')#change this - pass both tokens_1 and tokens_2 together
        #print "\t" + str(s) + str(" : ") + str('***************  sense_to_defn_word done  ************************')

        #update_words_frequency(tokens_1,tokens_2)###
        if tokens_1 or tokens_2:
            #print '1'
            defn_word_to_sense_processing(synset_defn,s,wd_filename,tokens_1,tokens_2)
        #print "\t" + str(s) + str(" : ") + str('***************  defn_word_to_sense done  ************************')
        #print '2'
        sense_data = shelve.open(sd_filename,writeback=True)
        sense_data[s]['S2E'] = list()
        sense_data.close()
        if synset_.examples():
            #print 'inside examples'
            for example in synset_.examples():
                tokens_1 = get_words(example,1)
                sense_to_word_processing(sd_filename,synset_defn,s,tokens_1,'example')

        #print "\t" + str(s) + str(" : ") + str('***************  sense_to_example_word done  ************************')
        sense_data = shelve.open(sd_filename,writeback=True)
        sense_data[s]['Hyponym'] = synset_.hyponyms()
        sense_data[s]['Hypernym'] = synset_.hypernyms()
        sense_data[s]['Holonym'] = synset_.holonyms()
        sense_data[s]['Meronym'] = synset_.meronyms()
        sense_data[s]['Entailment'] = synset_.entailments()
        sense_data[s]['Similar'] = synset_.similar_tos()
        sense_data.close()
        #print "\t" + str(s) + str(" : ") + str('*************** sense-sense relations done  ************************')
    #except Exception as e:
    #    print "Exception : " + str(e)
    #    handle_error(sense_data,sd_filename)
    #pickle.dump( sense_data, open( sd_filename, "wb" ) )
    hash2.close()
    #sense_data.close()

if __name__ == "__main__":

    #pdb.set_trace()
    #word_processing(wd_filename='Hash#3.shelve')
    sense_processing(sd_filename='Hash#4.shelve', wd_filename='Hash#3.shelve')
