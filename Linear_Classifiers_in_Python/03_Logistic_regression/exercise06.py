########################################################
# Visualizing multi-class logistic regression
# See exercise06.md
#
# Preload
from sklearn.linear_model import LogisticRegression

from exercise05 import lr_mn, lr_ovr

# TODO: add preload for X_train, y_train, plot_classifier()
########################################################


# Print training accuracies
print("Softmax     training accuracy:", lr_mn.score(X_train, y_train))
print("One-vs-rest training accuracy:", lr_ovr.score(X_train, y_train))

# Create the binary classifier (class 1 vs. rest)
lr_class_1 = LogisticRegression(C=100)
lr_class_1.fit(X_train, y_train == 1)

# Plot the binary classifier (class 1 vs. rest)
plot_classifier(X_train, y_train == 1, lr_class_1)
