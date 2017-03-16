from Commons import *
from pattern.en import singularize
from nltk.stem.wordnet import WordNetLemmatizer as WN
import inflect
p = inflect.engine()
lmtr = WN()

hash4 = Shelveopen('Word#.shelve')
synsets = Shelveopen('Hash#2.shelve')

for name in synsets.keys():
	lemmas = wn.synset(name).lemmas()
	for lemma in lemmas:
		name = Unicode(lemma.name())
		lemmatize = Unicode(lmtr.lemmatize(name))
		if lemmatize != name:
			hash4[name] = lemmatize
			hash4[lemmatize] = name
		elif p.plural(name) == name:
			hash4[name] = singularize(name)	#For singulars
			hash4[singularize(name)] = name
		else:
			hash4[name] = p.plural(name)	#For singulars
			hash4[p.plural(name)] = name
		related = Unicode(lemma.derivationally_related_forms())
		for word in related:
			hash4[word] = name

Shelveclose(hash4)
