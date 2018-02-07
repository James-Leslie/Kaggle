import numpy as np
import pandas as pd
from pre_process import prepare_data
from keras.models import Sequential
from keras.layers import Dense, Activation


# load data as Pandas dataframe
train_df = pd.read_csv('../train.csv', index_col=0)
test_df = pd.read_csv('../test.csv', index_col=0)
data_df = train_df.append(test_df)

# categorical and continuous variables
categorical = ['Pclass', 'Sex']
continuous = ['Age', 'Fare']

# separate inputs from labels
y_train = train_df.iloc[:, :1]

# process data
data_processed = prepare_data(data_df, categorical, continuous)
x_train = data_processed[:891, :]
x_test = data_processed[891:, :]

# create model
model = Sequential()
model.add(Dense(5, input_dim=x_train.shape[1], activation='relu'))  # 1st hidden layer
# model.add(Dense(5, activation='relu'))  # 2nd hidden layer
model.add(Dense(1, activation='sigmoid'))  # output layer

# compile model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# train model
model.fit(x_train, y_train, epochs=100, batch_size=32)

# evaluate the model
scores = model.evaluate(x_train, y_train)
print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))

# calculate predictions
predictions = model.predict(x_test)
# round predictions
rounded = [round(x[0]) for x in predictions]

# create output file
solution = np.vstack((test_df.index.astype('int'),
                      np.array(rounded).astype('int')))

solution = np.vstack((['PassengerID', 'Survived'],
                       solution.transpose()))

solution = pd.DataFrame(solution)
solution.to_csv("Neural_Network_Solution.csv", index=False, header=False)
