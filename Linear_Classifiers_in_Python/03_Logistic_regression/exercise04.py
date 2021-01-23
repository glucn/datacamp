########################################################
# Visualizing easy and difficult examples
# See exercise04.md
#
# Preload
import numpy as np
from sklearn.linear_model import LogisticRegression

# TODO: add preload for X, y, show_digit()
########################################################


lr = LogisticRegression()
lr.fit(X, y)

# Get predicted probabilities
proba = lr.predict_proba(X)

# Sort the example indices by their maximum probability
proba_inds = np.argsort(np.max(proba, axis=1))

# Show the most confident (least ambiguous) digit
show_digit(proba_inds[-1], lr)

# Show the least confident (most ambiguous) digit
show_digit(proba_inds[0], lr)
