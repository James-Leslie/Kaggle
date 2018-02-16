# Titanic Challenge
I decided to have a go at the beginner's machine learning challenge on [Kaggle](https://www.kaggle.com/). The aim of the challenge is to train a model to accurately predict the survival of passengers aboard the Titanic. The full challenge description and relevant data sets can be found [here](http://https://www.kaggle.com/c/titanic).

I was interested in learning more about Neural Networks. So I decided to try and tackle this challenge using one. I don't believe this is the best approach for this challenge, but it's a fun exercise in getting some beginner experience with Neural Networks.

## Getting Started
Training and testing data are found in train.csv and test.csv. Code for the different approaches to the challenge are found in subfolders (I'll add more subfolders as I attempt the challenge using different methods).

### Prerequisites
For the Neural Network approach, the following Python packages and modules are required:
```python
import numpy as np
import pandas as pd
from ../pre_process import prepare_data
from keras.models import Sequential
from keras.layers import Dense, Activation
```
## Usage instructions
To use the Neural Network model for classifying the dataset, simply run the main.py module found within the Neural_Network subfolder. The output will be created in the same folder, and this can be submitted for scoring [here](https://www.kaggle.com/c/titanic/submit).
