from Commons import *

def Create():
    hash3 = Shelveopen('Hash#3.shelve')
    hash4 = Shelveopen('Hash#4.shelve')
    dic = {}
    dic2 = {}
    dic1 = {}
    dic['W2S'] = {'dog.n.01': 43,
                    'frump.n.01': 1,
                    'dog.n.03': 1,
                    'cad.n.01': 1,
                    'frank.n.02': 1,
                    'pawl.n.01': 1,
                    'andiron.n': 1,
                    'chase.v.01': 3}

    dic['D2S'] = {'dog.n.01':3, 'dog.n.03':2, 'cad.n.01':7}
    dic1['W2S'] = {'dog.n.01': 33}
    dic1['D2S'] = {'dog.n.03':4 }

    syn = {}
    dic2['S2W'] = ['dog','man']
    syn['S2W'] = ['dog', 'domestic_dog', 'Canis_familiaris']

    dic2['S2D'] = [('man', 1,6)]
    syn['S2D'] = [('member', 1, 6),
                    ('genus', 1, 6),
                    ('canis', 1, 6),
                    ('wolf', 1, 6),
                    ('domesticated', 1, 6),
                    ('man', 1, 6)]

    dic2['S2E'] = [('man', 1, 4)]
    syn['S2E'] = [('dog', 1, 3),
                    ('barked', 1, 3),
                    ('night', 1, 3)]

    dic2['Hypernym'] = ['dog.n.01']
    dic2['Hyponym'] = []
    dic2['Meronym'] = []
    dic2['Holonym'] = []
    dic2['Entailment'] = []
    dic2['Similar'] = []
    syn['Hypernym'] = ['canine.n.02','domestic_animal.n.01']
    syn['Hyponym'] = ['basenji.n.01', 'corgi.n.01', 'cur.n.01', 'dalmatian.n.02',
                     'great_pyrenees.n.01', 'griffon.n.02', 'hunting_dog.n.01',
                      'lapdog.n.01','leonberg.n.01', 'mexican_hairless.n.01',
                       'newfoundland.n.01', 'pooch.n.01','poodle.n.01', 'pug.n.01',
                        'puppy.n.01', 'spitz.n.01', 'toy_dog.n.01','working_dog.n.01']
    syn['Meronym'] = ['flag.n.07']
    syn['Holonym'] = ['canine.n.01','pack.n.06']
    syn['Entailment'] = []
    syn['Similar'] = []
    hash3['dog'] = dic
    hash3['man'] = dic1
    hash4['dog.n.01'] = syn
    hash4['dog.n.03'] = dic2
    Shelveclose(hash3)
    Shelveclose(hash4)

if __name__ == '__main__':
    Create()