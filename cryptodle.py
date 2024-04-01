"""import signal

# Define the function you want to set a timeout for
def my_function():
    # Simulate a long-running operation
    import time
    time.sleep(10)  # Sleep for 10 seconds

# Define a function to handle the timeout
def timeout_handler(signum, frame):
    raise TimeoutError("Function execution exceeded the timeout.")

# Set the signal handler
signal.signal(signal.SIGALRM, timeout_handler)

# Set the timeout for 5 seconds
timeout_seconds = 10
"""
from z3 import *
import random
from multiprocessing import Process

answer="djzpt"

s=Solver()

g=[]
g=[5, 17, 14, 25, 9, 9, 19, 14, 14, 13, 17, 14, 18, 16, 8, 15, 5, 18, 23, 24, 23, 7, 24, 15, 19]


a=Int("a")
b=Int("b")
c=Int("c")
d=Int("d")
e=Int("e")

s.add(0<a)
s.add(0<b)
s.add(0<c)
s.add(0<d)
s.add(0<e)

s.add(a<27)
s.add(b<27)
s.add(c<27)
s.add(d<27)
s.add(e<27)

#s.add(a==(ord("k")-ord("a")))
#s.add(b==(ord("j")-ord("a")))
#s.add(c==(ord("z")-ord("a")))

r=[29, 30, 0, 24, 0]
for i in range(5):
        s.add(((g[5*i]-a)*(g[5*i+1]-b)*(g[5*i+2]-c)*(g[5*i+3]-d)*(g[5*i+4]-e))%31==r[i])

temp=['0']*26
for i in range(0,1):
        temp[i]=Solver()
        temp[i].add(s.assertions())
        temp[i].add(a==10)
        try:
                temp[i].check()
                print(temp[i].model())
        except:
                print("unsat")

