#load lib
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import copy
from sklearn.naive_bayes import MultinomialNB
from sklearn import cross_validation
from sklearn import svm
%matplotlib inline

#Loading the prediction/train data as pred/train
pred = pd.read_csv('path/prediction.csv')
train = pd.read_csv('path/train.csv')
