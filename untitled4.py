# -*- coding: utf-8 -*-
"""
Created on Thu Apr  5 19:01:41 2018

@author: niles
"""

from textblob.classifiers import NaiveBayesClassifier
from textblob import TextBlob

train = [
    ('environment, water, package, facility, reduce, energy, emission, population, clean, prevention, recycle, tobacco, fuel, climate, carbon', 'pos'),
    
    ('hazardous, waste, agriculture, chemical, deplete', 'neg')
    ]
test = [
    ('environment, water, package, facility, reduce, energy, emission, population, clean, prevention, recycle, tobacco, fuel, climate, carbon', 'pos'),
    
        ('hazardous, waste, agriculture, chemical, deplete', 'neg')
    ]

cl = NaiveBayesClassifier(train)

# Classify some text
print(cl.classify("Their burgers are amazing."))  # "pos"
print(cl.classify("I don't like their pizza."))   # "neg"

# Classify a TextBlob
blob = TextBlob("The beer was amazing. But the hangover was horrible. "
                "My boss was not pleased.", classifier=cl)
print(blob)
print(blob.classify())

for sentence in blob.sentences:
    print(sentence)
    print(sentence.classify())

# Compute accuracy
print("Accuracy: {0}".format(cl.accuracy(test)))

# Show 5 most informative features
cl.show_informative_features(5)