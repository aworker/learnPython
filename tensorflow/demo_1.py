import tensorflow as tf
import time

time1 = time.time()

#Model parameters
W = tf.Variable([.3], dtype=tf.float32)
b = tf.Variable([-.3],dtype=tf.float32)

#Model input and output
x = tf.placeholder(tf.float32)
linear_model = W * x + b
y = tf.placeholder(tf.float32)

#loss function
loss = tf.reduce_sum(tf.square(linear_model-y))

optimizer = tf.train.GradientDescentOptimizer(0.01)
train = optimizer.minimize(loss)


#training data
x_train = [1,2,3,4]
y_train = [0,-1,-2,-3]

#training loop
init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)

for i in  range(1000):
    sess.run(train,{x: x_train, y : y_train})


#evaluate training accuracy
curr_loss = sess.run(loss, {x: x_train, y: y_train})
curr_W = sess.run(W)
curr_b = sess.run(b)

time2 = time.time()

# print(curr_W)
# print(curr_b)
# print(curr_loss)
print(time2-time1)






