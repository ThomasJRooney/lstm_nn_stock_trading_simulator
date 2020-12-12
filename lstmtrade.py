import math
import pandas_datareader as web
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import Dense, LSTM
from datetime import datetime, timedelta, date
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')
pd.options.mode.chained_assignment = None

training_data_len = 0

def prepare_data(symbol):
    df = web.DataReader(symbol, data_source='yahoo', start='2012-01-01', end='2020-01-01')

    #capture and split dataset
    data = df.filter(['Close'])
    dataset = data.values
    training_data_len = math.ceil(len(dataset) * .8)

    #normalize all the data to be between 0 and 1 to account for price differences
    scaler = MinMaxScaler(feature_range=(0,1))
    scaled_data = scaler.fit_transform(dataset)

    #create scaled training dataset
    train_data = scaled_data[0:training_data_len, :]
    #split into x and y using past 60 days
    x_train = []
    y_train = []
    for i in range(60, len(train_data)):
        x_train.append(train_data[i-60:i,0])
        y_train.append(train_data[i,0])

    #convert to numpy arrays
    x_train, y_train = np.array(x_train), np.array(y_train)

    #reshape data so it is 3 dimensional
    x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))

    #create scaled testing dataset
    test_data = scaled_data[training_data_len - 60:, :]

    x_test = []
    y_test = dataset[training_data_len:, :]
    for i in range(60, len(test_data)):
        x_test.append(test_data[i-60:i, 0])
    x_test = np.array(x_test)
    x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 1))
    return(x_train, y_train, x_test, scaler, data)


def train(x_train, y_train):
    #build LSTM model
    model = Sequential()
    model.add(LSTM(50, return_sequences=True, input_shape=(x_train.shape[1], 1)))
    model.add(LSTM(50, return_sequences=False))
    model.add(Dense(25))
    model.add(Dense(1))
    model.compile(optimizer='adam', loss='mean_squared_error')
    model.fit(x_train, y_train, batch_size=1, epochs=1)
    return(model)

def predict(x_test, model, scaler, data):
    # get models predicted price values
    predictions = model.predict(x_test)
    predictions = scaler.inverse_transform(predictions)
    train = data[:training_data_len]
    valid = data[training_data_len:]
    #valid['Predictions'] = predictions
    return(scaler, model)

def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)

def trade(scaler, model, data):
    shares = 0
    money = 10000
    data = data[-366:]
    data = data.values.tolist()

    in_trade = False
    down = False
    up = False

    start_date = date(2018, 7, 20)
    end_date = date(2019, 1, 1)
    i = 0
    for single_date in daterange(start_date, end_date):
        #get date
        todays_date = single_date.strftime("%Y-%m-%d")
        #predict tommorrows price
        df = web.DataReader('AAPL', data_source='yahoo', start='2012-01-01', end=todays_date)
        df2 = df.filter(['Close'])
        df2 = df2[-60:]
        last_60_days = df2.values
        last_60_scaled = scaler.transform(last_60_days)
        X_test = []
        X_test.append(last_60_scaled)
        X_test = np.array(X_test)
        X_test = np.reshape(X_test, (X_test.shape[0], X_test.shape[1], 1))
        pred_price = model.predict(X_test)
        pred_price = scaler.inverse_transform(pred_price)
        #tommorrows predicted price
        pred = pred_price[0][0]
        print("prediction")
        print(pred)
        #todays price
        today = data[i][0]
        print("today")
        print(today)
        print("")
        if(today > pred):
            down = True
        else:
            up = True

        if(in_trade):
            if(down):
                #sell
                print("sell")
                money = shares * today
                print("money")
                print(money)
                print("")
                shares = 0
                in_trade = False
        else:
            if(up):
                #buy
                print("buy")
                shares = money / today
                print("shares")
                print(shares)
                print("")
                money = 0
                in_trade = True

        down = False
        up = False
        i += 1

    #cash out
    if(in_trade):
        #sell
        money = shares * today
        shares = 0
        in_trade = False

    print(money)




def visualize():
    plt.figure(figsize=(16,8))
    #plt.title('Model')
    #plt.xlabel('Date', fontsize=18)
    #plt.ylabel('Close Price USD', fontsize=18)
    #plt.plot(train['Close'])
    #plt.plot(valid[['Close', 'Predictions']])
    #plt.legend(['Train', 'Val', 'Predictions'], loc='lower right')
    plt.show()

def main():
    res = prepare_data('AAPL')
    model = train(res[0], res[1])
    pred = predict(res[2], model, res[3], res[4])
    trade(pred[0], pred[1], res[4])

if __name__ == "__main__":
    main()
