########################################################
# One-vs-rest SVM
# See exercise07.md
#
# Preload
# TODO: add preload for X_train, y_train, plot_classifier()
########################################################


# We'll use SVC instead of LinearSVC from now on
from sklearn.svm import SVC

# Create/plot the binary classifier (class 1 vs. rest)
svm_class_1 = SVC()
svm_class_1.fit(X_train, y_train == 1)
plot_classifier(X_train, y_train == 1, svm_class_1)
