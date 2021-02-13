########################################################
# Making predictions
# See exercise05.md
#
# Preload
from keras.layers import Dense
from keras.models import Sequential

from preload import titanic_train_df as df, titanic_train_predictors as predictors,\
    titanic_train_target as target, titanic_test_predictors as pred_data

n_cols = len(df.columns) - 1
########################################################


# Specify, compile, and fit the model
model = Sequential()
model.add(Dense(32, activation='relu', input_shape=(n_cols,)))
model.add(Dense(2, activation='softmax'))
model.compile(optimizer='sgd',
              loss='categorical_crossentropy',
              metrics=['accuracy'])
model.fit(predictors, target)

# Calculate predictions: predictions
predictions = model.predict(pred_data)

# Calculate predicted probability of survival: predicted_prob_true
predicted_prob_true = predictions[:, 1]

# print predicted_prob_true
print(predicted_prob_true)
