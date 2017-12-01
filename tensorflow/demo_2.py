import tensorflow as tf
import numpy as np

feature_columns = [tf.feature_column.numeric_column("x",shape=[1])]

estimator = tf.estimator.LinearRegressor(feature_columns=feature_columns)

x_train = np.array([1, 2, 3, 4], dtype=np.float32)
y_train = np.array([0,-1,-2,-3], dtype=np.float32)


x_eval = np.array([2,8,5,1],dtype=np.float32)
y_eval = np.array([-1.01,-4.1,-7,0.])

input_fn = tf.estimator.inputs.numpy_input_fn({"x":x_train},y_train,batch_size=4,num_epochs=None,shuffle= True)
train_input_fn = tf.estimator.inputs.numpy_input_fn({"x":x_train},y_train,batch_size=4,num_epochs=1000,shuffle= True)
eval_input_fn = tf.estimator.inputs.numpy_input_fn({"x":x_eval},y_eval,batch_size=4,num_epochs=1000,shuffle= True)

estimator.train(input_fn= input_fn)
input_fn.



