Hyper1 = 0.5    #For non-noise words in sense definition
Hyper2 = 0.2    #For non-noise words in sense examples
Hyper3 = 0.7    #For words present in other synsets
Hyper4 = 1  #Sense to its wordforms
Hyper5 = 0.8    #For Hyponyms, needs to be multiplied with BNC ratio
Hyper6 = 0.8    #For Hypernyms
Hyper7 = 0.5    #For Meronyms
Hyper8 = 0.5    #For Holonyms
Hyper9 = 1  #For Similar adjectives
Hyper10 = 0.6   #For Verb Entailments
DMax = 0.9	#Definition to example MaXval in ComputeMinMax
EMax = 0.3	#Sense to example MaXval in ComputeMinMax
alpha = 0.6 #Metric to get final Sentence semantic score, decides weightage between order and semantics
tuners = [1,100,100,150]	#Tune dimenational vectors of Wordclient