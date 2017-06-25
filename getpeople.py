from nltk.corpus import wordnet
from nltk.tag import pos_tag
from pattern.en import pluralize


def is_person(synset):
    return any(h.name() == 'person.n.01'
               for h in synset.closure(lambda s: s.hypernyms()))

with open('people.txt', 'w') as ofile:
    people = [synset
              for synset in wordnet.all_synsets(wordnet.NOUN)
              if is_person(synset)]
    words = set(lemma.name().replace('_', ' ')
                for synset in people
                for lemma in synset.lemmas())
    for word, tag in pos_tag(sorted(words)):
        plural = pluralize(word)
        if plural.endswith('ss'):
            ofile.write(word)
        else:
            ofile.write(plural)
        ofile.write('\n')
