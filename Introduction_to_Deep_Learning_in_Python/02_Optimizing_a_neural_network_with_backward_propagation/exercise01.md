Coding how weight changes affect accuracy
=========================================

Now you'll get to change weights in a real network and see how they affect model accuracy!

Have a look at the following neural network: ![Ch2Ex4](https://s3.amazonaws.com/assets.datacamp.com/production/course_3524/datasets/ch2ex4.png)

Its weights have been pre-loaded as `weights_0`. Your task in this exercise is to update a single weight in `weights_0` to create `weights_1`, which gives a perfect prediction (in which the predicted value is equal to `target_actual`: 3).

Use a pen and paper if necessary to experiment with different combinations. You'll use the `predict_with_network()` function, which takes an array of data as the first argument, and weights as the second argument.
