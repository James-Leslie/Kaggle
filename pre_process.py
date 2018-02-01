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

    # extract titles from names
    x['Title'] = x['Name']
    for name in x['Name']:
        x['Title'] = x['Name'].str.extract('([A-Za-z]+)\.', expand=True)

    # replace rare titles with more common ones
    mapping = {'Mlle': 'Miss', 'Major': 'Mr', 'Col': 'Mr', 'Sir': 'Mr',
               'Don': 'Mr', 'Mme': 'Miss', 'Jonkheer': 'Mr', 'Lady': 'Mrs',
               'Capt': 'Mr', 'Countess': 'Mrs', 'Ms': 'Miss', 'Dona': 'Mrs'}
    x.replace({'Title': mapping}, inplace=True)

    # impute missing Age values using median of Title groups
    titles = ['Dr', 'Master', 'Miss', 'Mr', 'Mrs', 'Rev']
    for title in titles:
        age_to_impute = x.groupby('Title')['Age'].median()[titles.index(title)]
        x.loc[(x['Age'].isnull()) & (x['Title'] == title), 'Age'] = age_to_impute

    # impute missing Fare values using median
    age_median = x['Fare'].median()
    x['Fare'].fillna(age_median, inplace=True)

    # create Family_Size column
    x['Family_Size'] = x['Parch'] + x['SibSp']
    continuous_list.append('Family_Size')

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
