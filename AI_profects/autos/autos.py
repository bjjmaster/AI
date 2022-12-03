import numpy as np
import autos_prepare
import tensorflow as tf
import keras as k

features_train = autos_prepare.features_train[: 10]
#features_valid = autos_prepare.features_valid
target_train = autos_prepare.target_train[: 10]
#target_valid = autos_prepare.target_valid
#features_train = np.array([0.3, 0.7, 0.9])
#target_train = np.array([0.5, 0.9, 1])

model = tf.keras.Sequential([
    tf.keras.layers.Dense(100),
    tf.keras.layers.Dense(10),
    tf.keras.layers.Dense(1)
])
model.compile(loss=tf.keras.losses.mse, optimizer=tf.keras.optimizers.SGD())
fitt = model.fit(x=features_train, y=target_train, epochs=10)