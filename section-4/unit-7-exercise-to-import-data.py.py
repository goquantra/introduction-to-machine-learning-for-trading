##### Importing the Libraries#########
from sklearn.svm import SVC
from sklearn.metrics import scorer
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import iexfinance as iex
import datetime

start = datetime.datetime(2017, 1,1)
end = datetime.datetime(2018,1,1)

##### Type your code below ######
Df= iex.get_historical_data('GLD', start, end, output_format = 'pandas')

print Df.tail()