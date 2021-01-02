# Inspecting your model
# Now that you have built a "fake news" classifier, you'll investigate what it has learned. You can map the important
# vector weights back to actual words using some simple inspection techniques.
#
# You have your well performing tfidf Naive Bayes classifier available as nb_classifier, and the vectors as
# tfidf_vectorizer.

from practice2 import tfidf_vectorizer
from practice4 import nb_classifier


# Get the class labels: class_labels
class_labels = nb_classifier.classes_

# Extract the features: feature_names
feature_names = tfidf_vectorizer.get_feature_names()

# Zip the feature names together with the coefficient array and sort by weights: feat_with_weights
feat_with_weights = sorted(zip(nb_classifier.coef_[0], feature_names))

# Print the first class label and the top 20 feat_with_weights entries
print(class_labels[0], feat_with_weights[:20])

# Print the second class label and the bottom 20 feat_with_weights entries
print(class_labels[1], feat_with_weights[-20:])
