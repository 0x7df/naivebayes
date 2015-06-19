"""Utility functions for naive Bayes classifier."""
import re
import string

def remove_punctuation(s):
    """See: http://stackoverflow.com/a/266162."""
    exclude = set(string.punctuation)
    return ''.join(ch for ch in s if ch not in exclude)

def tokenize(text):
    """Process text into lower-case tokens."""
    text = remove_punctuation(text)
    text = text.lower()
    return re.split(r"\W+", text)

def count_words(words):
    """Count number of occurrences of each word."""
    wc = {}
    for word in words:
        wc[word] = wc.get(word, 0.0) + 1.0
    return wc
