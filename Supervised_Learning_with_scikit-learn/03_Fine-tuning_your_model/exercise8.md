### Hold-out set in practice II: Regression

Remember lasso and ridge regression from the previous chapter? Lasso used the L1 penalty to regularize, while ridge used the L2 penalty. There is another type of regularized regression known as the elastic net. In elastic net regularization, the penalty term is a linear combination of the L1 and L2 penalties:
```
a∗L1+b∗L2
```
In scikit-learn, this term is represented by the `'l1_ratio'` parameter: An `'l1_ratio'` of `1` corresponds to an L1 penalty, and anything lower is a combination of L1 and L2.

In this exercise, you will `GridSearchCV` to tune the `'l1_ratio'` of an elastic net model trained on the Gapminder data. As in the previous exercise, use a hold-out set to evaluate your model's performance.
