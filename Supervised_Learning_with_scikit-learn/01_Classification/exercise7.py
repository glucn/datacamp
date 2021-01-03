# Overfitting and underfitting
# Remember the model complexity curve that Hugo showed in the video? You will now construct such a curve for the
# digits dataset! In this exercise, you will compute and plot the training and testing accuracy scores for a variety
# of different neighbor values. By observing how the accuracy scores differ for the training and testing sets with
# different values of k, you will develop your intuition for overfitting and underfitting.
#
# The training and testing sets are available to you in the workspace as X_train, X_test, y_train, y_test. In
# addition, KNeighborsClassifier has been imported from sklearn.neighbors.

import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

digits = datasets.load_digits()
X_train, X_test, y_train, y_test = train_test_split(digits.data, digits.target,
                                                    test_size=0.4, random_state=42, stratify=digits.target)

print(X_train.shape)

# Setup arrays to store train and test accuracies
neighbors = np.arange(1, 9)
train_accuracy = np.empty(len(neighbors))
test_accuracy = np.empty(len(neighbors))

# Loop over different values of k
for i, k in enumerate(neighbors):
    # Setup a k-NN Classifier with k neighbors: knn
    knn = KNeighborsClassifier(n_neighbors=k)

    # Fit the classifier to the training data
    knn.fit(X_train, y_train)

    # Compute accuracy on the training set
    train_accuracy[i] = knn.score(X_train, y_train)

    # Compute accuracy on the testing set
    test_accuracy[i] = knn.score(X_test, y_test)

# Generate plot
plt.title('k-NN: Varying Number of Neighbors')
plt.plot(neighbors, test_accuracy, label='Testing Accuracy')
plt.plot(neighbors, train_accuracy, label='Training Accuracy')
plt.legend()
plt.xlabel('Number of Neighbors')
plt.ylabel('Accuracy')
plt.show()
