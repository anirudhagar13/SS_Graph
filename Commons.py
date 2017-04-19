from nltk.corpus import wordnet as wn
from nltk.stem import WordNetLemmatizer as WL
from nltk.corpus import stopwords
from nltk import ngrams
import difflib
import pickle
import shelve
import sys
import math
import os


uipath = os.getcwd()
if 'ssgraph' in uipath: # Running from UI
    uipath = '/'.join(uipath.split("\\")[:-1])
else:
    uipath = '/'.join(uipath.split("\\"))
    
StopWords = ['a', 'has', 'such', 'accordance', 'have', 'suitable', 'according', 'having', 'than', 'all', 'herein', 'that', 'also', 'however', 'the', 'an', 'if', 'their', 'and', 'in', 'then', 'another', 'into', 'there', 'are', 'invention', 'thereby', 'as', 'is', 'therefore', 'at', 'it', 'thereof', 'be', 'its', 'thereto', 'because', 'means', 'these', 'been', 'not', 'they', 'being', 'now', 'this', 'by', 'of', 'those', 'claim', 'on', 'thus', 'comprises', 'onto', 'to', 'corresponding', 'or', 'use', 'could', 'other', 'various', 'described', 'particularly', 'was', 'desired', 'preferably', 'were', 'do', 'preferred', 'what', 'does', 'present', 'when', 'each', 'provide', 'where', 'embodiment', 'provided', 'whereby', 'fig', 'provides', 'wherein', 'figs', 'relatively', 'which', 'for', 'respectively', 'while', 'from', 'said', 'who', 'further', 'should', 'will', 'generally', 'since', 'with', 'had', 'some', 'would']

def Unicode(data):
        '''
        To remove Unicode from list of elements
        '''
        #Check if received is string
        if isinstance(data, (str, unicode)):
            return data.encode('utf-8').lower()
        else:
            return [x.encode('utf-8').lower() for x in data]

def Cosine_similarity(v1, v2):
    # compute cosine similarity of v1 to v2: (v1 dot v2)/{||v1||*||v2||)
    # Prevent division by zero condition
    if not any(v1):
        return 0.0
    if not any(v2):
        return 0.0
    sumxx, sumxy, sumyy = 0, 0, 0
    for i in range(len(v1)):
        x = v1[i]; y = v2[i]
        sumxx += x*x
        sumyy += y*y
        sumxy += x*y
    return round(sumxy/math.sqrt(sumxx*sumyy),4)

def Vectormag(v1):
    # Returns magnitude of vector received
    if not any(v1):
        return 0.0
    sumd = 0
    for dimension in v1:
        sumd += dimension*dimension
    return sumd ** 0.5


def Filedump(filename, content, appendflag=True):
    # Appends/Overwrites data to files
    if appendflag:
        with open(uipath+'/ssgraph/helloapp/Logs/'+filename,'a') as file:
            file.write(content+'\n')
    else:
        # File Overwritten
        with open(uipath+'/ssgraph/helloapp/Logs/'+filename,'w') as file:
            file.write(content+'\n')

def Pickledump(data, file):
    '''
    Store data (serialize)
    '''
    with open(file, 'wb') as handle:
        pickle.dump(data, handle)

def Pickleload(file):
    '''
    Load data (deserialize)
    '''
    with open(file, 'rb') as handle:
        unserialized_data = pickle.load(handle)
        return unserialized_data

def Shelveopen(filename):
    '''
    Open shelve dictionary
    '''
    return shelve.open(uipath+'/Shelves/'+filename)

def Shelveclose(shelve):
    '''
    close shelve dictionary
    '''
    shelve.close()

def computeMinMax(minVal,maxVal,ratio):
    if ratio == 1:
        return 1.2*maxVal
    else:
        return minVal + (maxVal - minVal) * (-1/math.log(ratio,2))

def Ngrams(ls, wordhash):
    # For now Bigram but can handle any Ngram
    sentence = ' '.join(ls)
    bigrams = ngrams(ls,2)
    for i in bigrams:
        st = i[0]+'_'+i[1] 
        if st in wordhash:
            # Double words Exists
            # Replace its occurences in sentence with double word
            spaced = i[0]+' '+i[1]
            sentence = sentence.replace(spaced,st)
    return sentence.split()

def Removestopwords(sent):
    '''
    Removes a list of stop words and gives back rest of the sentence
    '''
    ls = [x for x in sent if x not in StopWords]    #US PTO stopwordlist
    ls = [x for x in ls if x not in Unicode(stopwords.words('english'))]    #NLTK stopwordlist
    return ls

# System specific function, removes special characters, creates wordnet present bigrams and removes stopwords
def Purify(sentence, wordhash):
    morphohash = Shelveopen('Morpho.shelve')
    sentence = sentence.strip().lower();
    sentence = sentence.replace("'s","")
    sentence = sentence.replace("n't"," not")    #Bad Hardcode to replace all apostrophies
    ls = ''.join(e for e in sentence if e.isalpha() or e == ' ')    #To remove special characters/numbers from words
    ls = ls.split() #list of words
    ls = Removestopwords(ls)
    ls = Ngrams(ls, wordhash)  #Get pair of words together
    parsed_list = []
    for key in ls:
        if key not in wordhash:    # Not present in wordnet
            if key not in morphohash:
                # Morphological parsing
                newkey = Morphoparse(key)
                if newkey == key:
                    # Word does not exist in WOrdnet & Our hash
                    Filedump('NonMorphed.log',key, True)
                    continue
                else:
                    morphohash[key] = newkey
                    parsed_list.append(newkey)
            else:
                parsed_list.append(morphohash[key])
        else:
            parsed_list.append(key)
    return parsed_list

def Morphoparse(word):
    # To Give back root word existent in Wordnet
    lemmatizer = WL()
    lemmatized = Unicode(lemmatizer.lemmatize(word))
    if lemmatized != word:
        return lemmatized
    else:
        synsets = wn.synsets(word)
        if synsets:
            lemmas = Unicode(synsets[0].lemma_names())
            similars = difflib.get_close_matches(word,lemmas)
            if similars:
                return similars[0]
            else: 
                return lemmas[0]
        else:
            # Can't Do Anything, word not found anywhere
            return word

if __name__ == '__main__':
    print Morphoparse('happening')