import numpy as np
import pandas as pd
from pre_process import prepare_data
from keras.models import Sequential
from keras.layers import Dense, Activation


# load data as Pandas dataframe
train_df = pd.read_csv('train.csv', index_col=0)
test_df = pd.read_csv('test.csv', index_col=0)

# categorical and continuous variables
categorical = ['Pclass', 'Sex']
continuous = ['Age', 'SibSp', 'Parch', 'Fare']

# separate inputs from labels
y_train = train_df.iloc[:, :1]
x_train = prepare_data(train_df.iloc[:, 1:], categorical, continuous)
x_test = prepare_data(test_df.iloc[:, :], categorical, continuous)

# create model
model = Sequential()
model.add(Dense(12, input_dim=9, activation='relu'))  # 1st hidden layer
model.add(Dense(7, activation='relu'))  # 2nd hidden layer
model.add(Dense(1, activation='sigmoid'))  # output layer

# compile model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# train model
model.fit(x_train, y_train, epochs=100, batch_size=10)

# evaluate the model
scores = model.evaluate(x_train, y_train)
print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))

# calculate predictions
predictions = model.predict(x_test)
# round predictions
rounded = [round(x[0]) for x in predictions]

# save predictions to csv file
arr = np.array(rounded)
np.savetxt("neural_network.csv",
            np.dstack((np.arange(1, arr.size+1),arr))[0],
            "%d,%d",
            header="PassengerID,Survived")
