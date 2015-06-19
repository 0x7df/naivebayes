"""Main routine for the naive Bayes classifier.

Required argument: filename of YAML input deck.
"""

import nbutil
from sh import find
import yaml
import sys
import math
import imp


try:
    filename = sys.argv[1]
except IndexError:
    sys.exit("Name of file to categorise required as argument to nb.py")

# read input
stream = file(filename, 'r')
uinput = yaml.load(stream)


# load the categorise function from the user-supplied module
trainingmodfilename = uinput['categorisemodule']
imp.load_source('trainingmod', trainingmodfilename)
from trainingmod import categorise

# setup some structures to store our data
vocab = {}
word_counts = {}
priors = {}
log_prob = {}
for icat in uinput['categories']:
    word_counts[icat] = {}
    priors[icat] = 0.
    log_prob[icat] = 0.

docs = []
for f in find(uinput['trainingdata']):
    f = f.strip()
    if not f.endswith(".txt"):
        # skip non .txt files
        continue
    category = categorise(f)
    docs.append((category, f))
    # ok time to start counting stuff...
    priors[category] += 1
    text = open(f).read()
    words = nbutil.tokenize(text)
    counts = nbutil.count_words(words)
    for word, count in list(counts.items()):
        # if we haven't seen a word yet, let's add it to our dictionaries with
        # a count of 0
        if word not in vocab:
            vocab[word] = 0.0  # use 0.0 here so Python does "correct" math
        if word not in word_counts[category]:
            word_counts[category][word] = 0.0
        vocab[word] += count
        word_counts[category][word] += count

priors_sum = sum(priors.values())
for icat in uinput['categories']:
    priors[icat] = priors[icat] / priors_sum

for testfile in uinput['testfile']:
    new_doc = open(testfile).read()
    words = nbutil.tokenize(new_doc)
    counts = nbutil.count_words(words)
    for icat in uinput['categories']:
        log_prob[icat] = 0.

    for w, cnt in list(counts.items()):
        # skip words that we haven't seen before, or words less than 3
        # letters long
        if w not in vocab or len(w) <= 3:
            continue

        p_word = vocab[w] / sum(vocab.values())
        p_w_given = {}
        for icat in uinput['categories']:
            p_w_given[icat] = (word_counts[icat].get(w, 0.0) /
                               sum(word_counts[icat].values()))

        for icat in uinput['categories']:
            if p_w_given[icat] > 0.:
                log_prob[icat] += math.log(cnt * p_w_given[icat] / p_word)

    for icat in uinput['categories']:
        print("Score("+icat+"):", math.exp(log_prob[icat] +
                                  math.log(priors[icat])))
