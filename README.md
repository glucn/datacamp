# datacamp

Personal notes and resources for datacamp courses.

- NLP
  - [Introduction to Natural Language Processing in Python](/Introduction_to_Natural_Language_Processing_in_Python)
  - [Advanced NLP with spaCy](/Advanced_NLP_with_spaCy)

- Machine Learning
  - [Supervised Learning with scikit-learn](/Supervised_Learning_with_scikit-learn)
  - [Unsupervised Learning in Python](/Unsupervised_Learning_in_Python)
  - [Linear Classifiers in Python](/Linear_Classifiers_in_Python)
  - [Introduction to Deep Learning in Python](/Introduction_to_Deep_Learning_in_Python)

##### Helpers
- Suppress Scientific Notation in Numpy
``` python
import numpy as np

np.set_printoptions(suppress=True)
```

- Dump a NumPy array to stdout
``` python
import numpy as np
import sys

np.savetxt(sys.stdout, predictors, delimiter=',', fmt='%d') # Change fmt as needed
```
