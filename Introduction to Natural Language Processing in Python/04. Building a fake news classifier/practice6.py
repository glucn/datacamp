# Improving your model
# Your job in this exercise is to test a few different alpha levels using the Tfidf vectors to determine if there is
# a better performing combination.
#
# The training and test sets have been created, and tfidf_vectorizer, tfidf_train, and tfidf_test have been computed.
# Does the score change along with the alpha? What is the best alpha?

import numpy as np
from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics

from practice1 import y_train, y_test
from practice2 import tfidf_train, tfidf_test

# Create the list of alphas: alphas
alphas = np.arange(0, 1, 0.1)


# Define train_and_predict()
def train_and_predict(alpha):
    # Instantiate the classifier: nb_classifier
    nb_classifier = MultinomialNB(alpha=alpha)
    # Fit to the training data
    nb_classifier.fit(tfidf_train, y_train)
    # Predict the labels: pred
    pred = nb_classifier.predict(tfidf_test)
    # Compute accuracy: score
    score = metrics.accuracy_score(y_test, pred)
    return score


# Iterate over the alphas and print the corresponding score
for alpha in alphas:
    print('Alpha: ', alpha)
    print('Score: ', train_and_predict(alpha))
    print()
