########################################################
# Imputing missing data in a ML Pipeline I
# See exercise05.md
########################################################

# Import the Imputer module
# from sklearn.preprocessing import Imputer  # deprecated
from sklearn.impute import SimpleImputer
from sklearn.svm import SVC

# Setup the Imputation transformer: imp
# imp = Imputer(missing_values='NaN', strategy='most_frequent', axis=0)  # deprecated
imp = SimpleImputer(missing_values='NaN', strategy='most_frequent')

# Instantiate the SVC classifier: clf
clf = SVC()

# Setup the pipeline with the required steps: steps
steps = [('imputation', imp),
         ('SVM', clf)]
