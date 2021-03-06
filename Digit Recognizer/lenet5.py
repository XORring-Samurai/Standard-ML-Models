# -*- coding: utf-8 -*-
"""LeNet5.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Jki1PmIHpWwl1PQlcG4WKajqEUP-W2gV
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import *
from tensorflow.keras.optimizers import *
from tensorflow.keras.losses import *
from tensorflow.python.ops.gen_batch_ops import batch

(X_train, y_train), (X_test, y_test) = mnist.load_data()

X_train = X_train.reshape(X_train.shape[0], 28, 28, 1)
X_test = X_test.reshape(X_test.shape[0], 28, 28, 1)

mean = np.mean(X_train)
deviation = np.std(X_train)
X_train = (X_train - mean) / deviation

X_test = (X_test - mean) / deviation

y_train = tf.keras.utils.to_categorical(y_train, 10)
y_test = tf.keras.utils.to_categorical(y_test, 10)

model = Sequential()
model.add(Conv2D(6, (5, 5), padding = 'valid', activation = 'relu', input_shape = (28, 28, 1)))
model.add(MaxPooling2D((2, 2)))
model.add(Conv2D(16, (5, 5), padding = 'valid', activation = 'relu'))
model.add(MaxPooling2D((2, 2)))
model.add(Flatten())
model.add(Dense(120, activation = 'relu'))
model.add(Dense(84, activation = 'relu'))
model.add(Dense(10, activation = 'softmax'))

model.summary()

model.compile(optimizer=Adam(learning_rate = 1e-3), loss = categorical_crossentropy, metrics = ['accuracy'])
hist = model.fit(X_train, y_train, epochs = 10, batch_size = 128, verbose = 1)

model.evaluate(X_test, y_test, verbose = 1)

predicted = model.predict(x = X_test, verbose = 1)

model.save('Digit Recognizer.h5')

