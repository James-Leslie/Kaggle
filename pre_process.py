import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, MinMaxScaler


def prepare_data(x, categorical_list, continuous_list):

    '''
    Pre-process data for input to neural network.
    - Drop irrelevant fields.
    - Interpolate null values.
    - Encode categorical variables.
    - Scale continuous variables.

    Keyword Arguments:
    x : Pandas dataframe
        contains all fields to be used as inputs for modelling

    categorical : array
        array containing categorical variable names

    continuous : array
        array containing categorical variable names
    '''

    # replace nan values in Age and Fare
    age_median = x['Age'].median()
    x['Age'].fillna(age_median, inplace=True)

    age_median = x['Fare'].median()
    x['Fare'].fillna(age_median, inplace=True)

    # one hot encode categorical variables
    categorical = x[categorical_list].values

    encoded_vars_temp = []
    for var in categorical.transpose():
        # create label encoder
        label_encoder = LabelEncoder()
        onehot_encoder = OneHotEncoder(sparse=False)

        # perform onehot encoding
        var_encoded = label_encoder.fit_transform(var)
        var_encoded = var_encoded.reshape(len(var_encoded), 1)
        var_onehot = onehot_encoder.fit_transform(var_encoded)

        # store in temp list
        encoded_vars_temp.append(var_onehot)

    # stack all encoded variables together
    encoded_vars = np.hstack(array for array in encoded_vars_temp)

    # scale continuous variables
    continuous = x[continuous_list].values

    scaled_vars_temp = []
    for var in continuous.transpose():
        # create MinMax scaler between -1 and 1
        scaler = MinMaxScaler(feature_range=(-1., 1.))

        # scale variables
        var_scaled = scaler.fit_transform(var.reshape(-1, 1))

        # store in temp list
        scaled_vars_temp.append(var_scaled)

    # stack all scaled variables  together
    scaled_vars = np.hstack(array for array in scaled_vars_temp)

    # stack all variables into training set
    training_set = np.hstack((encoded_vars, scaled_vars))

    return training_set
