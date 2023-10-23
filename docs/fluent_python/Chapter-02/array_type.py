import time
from array import array
from random import random

def cost_time(f):

    def inner(*arg, **kwarg):
        start_time = time.time()
        res = f(*arg, **kwarg)
        end_time = time.time()
        print('Cost time {:.3f} ms'.format((end_time - start_time) * 1000))
        return res
    
    return inner


@cost_time
def generate_floats():
    floats = array('d', (random() for i in range(10**7)))
    print(floats[-1])
    return floats

@cost_time
def write_float(floats):
    fp = open('floats.bin', 'wb')
    floats.tofile(fp)
    fp.close()


@cost_time
def read_floats(floats):
    floats2 = array('d')
    fp = open('floats.bin', 'rb')
    floats2.fromfile(fp, 10**7)
    fp.close()
    print(floats2[-1])

floats1 = generate_floats()
write_float(floats1)
read_floats(floats1)