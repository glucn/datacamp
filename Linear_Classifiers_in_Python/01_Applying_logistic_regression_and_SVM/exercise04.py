########################################################
# Sentiment analysis for movie reviews
# See exercise03.md
#
# Preload
import matplotlib.pyplot as plt

from preload import plot_4_classifiers
# TODO: add preload for X, y
########################################################


from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC, LinearSVC
from sklearn.neighbors import KNeighborsClassifier

# Define the classifiers
classifiers = [LogisticRegression(), LinearSVC(), SVC(), KNeighborsClassifier()]

# Fit the classifiers
for c in classifiers:
    c.fit(X, y)

# Plot the classifiers
plot_4_classifiers(X, y, classifiers)
plt.show()
