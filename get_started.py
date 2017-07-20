# https://www.tensorflow.org/get_started/get_started

import tensorflow as tf

session = tf.Session()

## Data looks like:
# "id": int(info[0]),
# "survived": int(info[1]),
# "class": int(info[2]),
# "name": info[3],
# "sex": mk_sex(info[4]),
# "age": mk_float(info[5]),
# "sibsp": int(info[6]),
# "parch": int(info[7]),
# "ticket": mk_ticket(info[8]),
# "fare": float(info[9]),
# "cabin": info[10],
# "embarked": mk_embarked(info[11])

pass_class = tf.placeholder(tf.int32)
pass_sex = tf.placeholder(tf.int32)
pass_age = tf.placeholder(tf.float32)
# pass_sibsp = tf.placeholder(tf.int32)
# pass_parch = tf.placeholder(tf.int32)
# pass_fare = tf.placeholder(tf.float32)
# pass_embarked = tf.placeholder(tf.int32)

w_1 = tf.Variable([.3], dtype=tf.float32)
w_2 = tf.Variable([.3], dtype=tf.float32)
w_3 = tf.Variable([.3], dtype=tf.float32)

model = w_1 * pass_class + w_2 * pass_sex + w_3 * pass_age
init = tf.global_variables_initializer()
session.run(init)

# print session.run(model, {pass_class:[1,2,3], pass_sex:[0,0,1], pass_age:[10.0,15.5,20.0]})
