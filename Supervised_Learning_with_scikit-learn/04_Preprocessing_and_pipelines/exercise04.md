### Dropping missing data

The voting dataset from Chapter 1 contained a bunch of missing values that we dealt with for you behind the scenes. Now, it's time for you to take care of these yourself!

The unprocessed dataset has been loaded into a DataFrame `df`. Explore it in the IPython Shell with the `.head()` method. You will see that there are certain data points labeled with a `'?'`. These denote missing values. As you saw in the video, different datasets encode missing values in different ways. Sometimes it may be a `'9999'`, other times a `0` - real-world data can be very messy! If you're lucky, the missing values will already be encoded as `NaN`. We use `NaN` because it is an efficient and simplified way of internally representing missing data, and it lets us take advantage of pandas methods such as `.dropna()` and `.fillna()`, as well as scikit-learn's Imputation transformer `Imputer()`.

In this exercise, your job is to convert the `'?'`s to NaNs, and then drop the rows that contain them from the DataFrame.