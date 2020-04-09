import difflib as dl
from nltk.util import ngrams

def get_best_matches(query, corpus):
    corpus_ngrams = ngrams(corpus.split(), len(query.split()))
    ngrams_joined = map(lambda ngram: ' '.join(ngram), corpus_ngrams)

    return dl.get_close_matches(query, ngrams_joined, cutoff = .85)