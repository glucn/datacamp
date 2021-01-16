### Centering and scaling in a pipeline

With regard to whether or not scaling is effective, the proof is in the pudding! See for yourself whether or not scaling the features of the White Wine Quality dataset has any impact on its performance. You will use a k-NN classifier as part of a pipeline that includes scaling, and for the purposes of comparison, a k-NN classifier trained on the unscaled data has been provided.

The feature array and target variable array have been pre-loaded as `X` and `y`. Additionally, `KNeighborsClassifier` and `train_test_split` have been imported from `sklearn.neighbors` and `sklearn.model_selection`, respectively.