import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import tensorflow as tf


텐서 = tf.constant( [3,4,5] , tf.float32)

텐서2 = tf.constant( [6,7,8] ) 

텐서3 = tf.constant( [ [1,2,3],
                        [3,4,5] ] )

w = tf.Variable(1.0)
w.assign(2)

print(w)