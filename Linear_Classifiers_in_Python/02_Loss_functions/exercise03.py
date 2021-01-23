########################################################
# Implementing logistic regression
# See exercise03.md
#
# Preload
import numpy as np
from scipy.optimize import minimize
from sklearn.linear_model import LogisticRegression
# TODO: add preload for X, y


def log_loss(raw_model_output):
    return np.log(1+np.exp(-raw_model_output))
########################################################


# The logistic loss, summed over training examples
def my_loss(w):
    s = 0
    for i in range(len(X)):
        raw_model_output = w@X[i]
        s = s + log_loss(raw_model_output * y[i])
    return s


# Returns the w that makes my_loss(w) smallest
w_fit = minimize(my_loss, X[0]).x
print(w_fit)

# Compare with scikit-learn's LogisticRegression
lr = LogisticRegression(fit_intercept=False, C=1000000).fit(X, y)
print(lr.coef_)
