# -*- coding: utf-8 -*-
"""Microsoft Stock Forecasting with LSTMs.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Bk4zPQwAfzoSHZokKUefKL1s6lqmam6S
"""

# dataset @ https://finance.yahoo.com/quote/MSFT/history/

# If you want the exact same dataset as the YouTube video,
# use this link: https://drive.google.com/file/d/1WLm1AEYgU28Nk4lY4zNkGPSctdImbhJI/view?usp=sharing

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import datetime

from tensorflow.keras.models import Sequential
from tensorflow.keras.optimizers import Adam
from tensorflow.keras import layers
from copy import deepcopy


class BasicStockPredictor():

  def __init__(self):
    self.df = pd.DataFrame()
    self.dates_train = None
    self.dates_val = None
    self.dates_test = None
    self.y_train = None
    self.y_val = None
    self.y_test = None
    self.X_train = None
    self.X_val = None
    self.X_test = None
    self.model = None
    self.train_predictions = None
    self.val_predictions = None
    self.test_predictions = None

# Converts date of type string to datetime object. 
  def str_to_datetime(self, s):
    split = s.split('-')
    year, month, day = int(split[0]), int(split[1]), int(split[2])
    return datetime.datetime(year=year, month=month, day=day)

  # This function creates n+2 columns. Each row contains:
  # Target Date: Date of data we are looking at
  # Target - 3: Closing price 3 days before target date
  # Target - 2: Closing price 2 days before target date
  # Target - 1: Closing price 1 day before target date
  # Target: Closing price on the target date
  # The rows correspond to all the data between the entered date range. 

  def df_to_windowed_df(self, dataframe, first_date_str, last_date_str, n=3):
    # Set the range of the dates we want
    first_date = self.str_to_datetime(first_date_str)
    last_date  = self.str_to_datetime(last_date_str)

    target_date = first_date

    dates = []
    X, Y = [], []


    last_time = False
    while True:
      df_subset = dataframe.loc[:target_date].tail(n+1) # (n,2)

      if len(df_subset) != n+1:
        print(f'Error: Window of size {n} is too large for date {target_date}')
        return

      values = df_subset['Close'].to_numpy()
      x, y = values[:-1], values[-1] 

      dates.append(target_date)
      X.append(x)
      Y.append(y)

      # The dataset skips some days because there is no public trading on weekdays, holidays, etc. 
      # This means we can't directly move on to the next date, we must do some data manipulation to 
      # get the next row.
      next_week = dataframe.loc[target_date:target_date+datetime.timedelta(days=7)]
      next_datetime_str = str(next_week.head(2).tail(1).index.values[0])
      next_date_str = next_datetime_str.split('T')[0]
      year_month_day = next_date_str.split('-')
      year, month, day = year_month_day
      next_date = datetime.datetime(day=int(day), month=int(month), year=int(year))

      if last_time:
        break

      target_date = next_date

      if target_date == last_date:
        last_time = True

    ret_df = pd.DataFrame({})
    ret_df['Target Date'] = dates

    X = np.array(X)
    for i in range(0, n):
      X[:, i]
      ret_df[f'Target-{n-i}'] = X[:, i] # Add all of the rows for that column

    ret_df['Target'] = Y

    return ret_df

  # This function separates the df into 3 separate numpy array.
  # dates: all of the dates in the inputted data frame
  # X: The middle n rows, which are essentially the inputs in the LSTM. 
  #    These are the closing prices of the n days before the target date. 
  # Y: This is the actual closing price of the target date. 
  def windowed_df_to_date_X_y(self, windowed_dataframe):
    df_as_np = windowed_dataframe.to_numpy()

    dates = df_as_np[:, 0]

    middle_matrix = df_as_np[:, 1:-1]
    X = middle_matrix.reshape((len(dates), middle_matrix.shape[1], 1))

    Y = df_as_np[:, -1]

    return dates, X.astype(np.float32), Y.astype(np.float32)

  # Reads and stores the data from the csv file
  def setup(self):

    self.df = pd.read_csv('MSFT.csv')
    self.df = self.df[['Date', 'Close']]

    datetime_object = self.str_to_datetime('1986-03-19')

    self.df['Date'] = self.df['Date'].apply(self.str_to_datetime)
    self.df.index = self.df.pop('Date')

    # plt.plot(self.df.index, self.df['Close']) #Optional: Plot for visual understanding, Date vs Closing Price
    # plt.show()

    # plt.clf()
    # Start day second time around: '2021-03-25'
    windowed_df = self.df_to_windowed_df(self.df,
                                    '2021-03-25',
                                    '2022-03-23',
                                    n=3)

    dates, X, y = self.windowed_df_to_date_X_y(windowed_df)

    q_80 = int(len(dates) * .8)
    q_90 = int(len(dates) * .9)

    self.dates_train, self.X_train, self.y_train = dates[:q_80], X[:q_80], y[:q_80]

    self.dates_val, self.X_val, self.y_val = dates[q_80:q_90], X[q_80:q_90], y[q_80:q_90]
    self.dates_test, self.X_test, self.y_test = dates[q_90:], X[q_90:], y[q_90:]

    plt.plot(self.dates_train, self.y_train)
    plt.plot(self.dates_val, self.y_val)
    plt.plot(self.dates_test, self.y_test)

    plt.legend(['Train', 'Validation', 'Test'])

    plt.show()

    plt.clf()

  # Initiliaze and run the model on the data set. 
  def forward(self):
    self.setup()

    self.model = Sequential([layers.Input((3, 1)),
                        layers.LSTM(64),
                        layers.Dense(32, activation='relu'),
                        layers.Dense(32, activation='relu'),
                        layers.Dense(1)])

    self.model.compile(loss='mse',
                  optimizer=Adam(learning_rate=0.001),
                  metrics=['mean_absolute_error'])

    self.model.fit(self.X_train, self.y_train, validation_data=(self.X_val, self.y_val), epochs=100)

    self.train_predictions = self.model.predict(self.X_train).flatten()

    plt.plot(self.dates_train, self.train_predictions)
    plt.plot(self.dates_train, self.y_train)
    plt.legend(['Training Predictions', 'Training Observations'])

    plt.show()
    plt.clf()

    self.val_predictions = self.model.predict(self.X_val).flatten()

    plt.plot(self.dates_val, self.val_predictions)
    plt.plot(self.dates_val, self.y_val)
    plt.legend(['Validation Predictions', 'Validation Observations'])

    plt.show()

    plt.clf()

    self.test_predictions = self.model.predict(self.X_test).flatten()
    
    plt.plot(self.dates_test, self.test_predictions)
    plt.plot(self.dates_test, self.y_test)
    plt.legend(['Testing Predictions', 'Testing Observations'])

    plt.plot(self.dates_train, self.train_predictions)
    plt.plot(self.dates_train, self.y_train)
    plt.plot(self.dates_val, self.val_predictions)
    plt.plot(self.dates_val, self.y_val)
    plt.plot(self.dates_test, self.test_predictions)
    plt.plot(self.dates_test, self.y_test)
    plt.legend(['Training Predictions',
                'Training Observations',
                'Validation Predictions',
                'Validation Observations',
                'Testing Predictions',
                'Testing Observations'])
    plt.show()

    plt.clf()


  # This will recursively predict the testing data and instead of using the observation data to predict 
  # results, it will use its own predictions. 
  def recur_predictions(self):


    recursive_predictions = []
    recursive_dates = np.concatenate([self.dates_val, self.dates_test])
    last_window = deepcopy(self.X_train[-1])
    for target_date in recursive_dates:
      next_prediction = self.model.predict(np.array([last_window])).flatten()
      recursive_predictions.append(next_prediction)
      last_window[-1] = next_prediction

    plt.plot(self.dates_train, self.train_predictions)
    plt.plot(self.dates_train, self.y_train)
    plt.plot(self.dates_val, self.val_predictions)
    plt.plot(self.dates_val, self.y_val)
    plt.plot(self.dates_test, self.test_predictions)
    plt.plot(self.dates_test, self.y_test)
    plt.plot(recursive_dates, recursive_predictions)
    plt.legend(['Training Predictions',
                'Training Observations',
                'Validation Predictions',
                'Validation Observations',
                'Testing Predictions',
                'Testing Observations',
                'Recursive Predictions'])
    plt.show()

    plt.clf()


#Main
lstm = BasicStockPredictor()
lstm.forward()
lstm.recur_predictions()
