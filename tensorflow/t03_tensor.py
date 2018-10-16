#coding=utf-8
import tensorflow as tf
'''
ts = tf.constant(3.0, dtype=tf.float32)
print("device:",ts.device)
print("dtype:",ts.dtype)
print("shape:",ts.shape)
print("name:",ts.name)
print("op:",ts.op)
print("value_index:",ts.value_index)       #从0开始
'''


#张量的运算
x = tf.constant(-3.0, dtype=tf.float32)
y = tf.constant(5.0, dtype=tf.float32)
z = tf.constant(3-4j, dtype=tf.complex64)


session=tf.Session()
init_op=tf.global_variables_initializer()
session.run(init_op)

ats=tf.abs(z)
print(session.run([z,ats]))

print(session.run(tf.truediv(x,y)))

ats=tf.abs(z)
print(ats.eval(session=session),z.eval(session=session))
print(tf.truediv(x,y).eval(session=session))


