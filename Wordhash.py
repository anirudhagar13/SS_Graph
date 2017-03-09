from Commons import *
from pattern.en import singularize
import inflect
p = inflect.engine()

hash4 = Shelveopen('Word#.shelve')
synsets = Shelveopen('Hash#2.shelve')

for name in synsets.keys():
	lemmas = wn.synset(name).lemmas()
	for lemma in lemmas:
		name = Unicode(lemma.name())
		if p.plural(name) == name:
			hash4[name] = singularize(name)	#For singulars
		else:
			hash4[name] = p.plural(name)	#For singulars
		related = Unicode(lemma.derivationally_related_forms())
		for word in related:
			hash4[word] = name
			
Shelveclose(hash4)