import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import datasets, layers, models
import csv
import numpy as np








def get_weekday_enc(d):
	1+1 #use datetime package and mod 7 to get a weekday uncoding
	#let's do this if we have time

def flatten(arr):
	flat_arr = []
	for i in arr:
		if type(i) is not list:
			flat_arr.append(float(i))
		else:
			for j in flatten(i):
				flat_arr.append(j)
	return flat_arr
def normalize(arr):
	arr = flatten(arr)
	return [i/sum(arr) for i in arr]


def process_data(data): #process into percentages
	p_data = []

	for d in range(1,len(data)):
		datapoint_open_close = normalize([data[d][1],data[d][4]])
		datapoint_open_close_past = normalize([data[d-1][1],data[d-1][4]]) #might end up being redundant
		datapoint_open_open = normalize([data[d][1], data[d-1][1]])
		datapoint_close_close = normalize([data[d][4], data[d-1][4]])
		datapoint_day = normalize([data[d][1:5]])
		datapoint_days = normalize([data[d][1:5], data[d-1][1:5]])

		p_data.append(flatten([datapoint_open_close, datapoint_open_close_past, datapoint_open_open,
			datapoint_close_close, datapoint_day, datapoint_days]))
	return p_data



def make_dataset(data):
	data = process_data(data)
	x, y = [], []

	for d in range(30,len(data)-1):
		x.append(flatten(data[d-30:d])) #30 days of history
		y.append(data[d+1][6]) #next day's closing

	return np.array(x), np.array(y), len(x[0]), 1

def make_model(shape_in, shape_out, loss = 'mse'):
	inpt = keras.layers.Input(shape=shape_in)
	o1 = keras.layers.Dense(128,activation='elu')(inpt)
	o2 = keras.layers.Dense(128,activation='elu')(o1)
	o3 = keras.layers.Dense(128,activation='elu')(o2)
	o4 = keras.layers.Dense(128,activation='elu')(o3)
	c = keras.layers.Concatenate()([o2, o3, o4])
	out = keras.layers.Dense(shape_out, activation='softmax')(c)

	model = keras.Model(inputs=inpt, outputs=out)
	model.compile(optimizer='adam', loss=loss, metrics=['accuracy'])

	return model







dataset = []
with open('data/SPY93-20.csv', newline='') as f:
	datareader = csv.reader(f)
	for row in datareader:
		dataset.append(row)
X, Y, shape_in, shape_out = make_dataset(dataset[1:])




model = make_model(shape_in, shape_out)
model.fit(X, Y, epochs=3, shuffle=True, validation_split=0.078650036683785 , batch_size=32, verbose=1)
