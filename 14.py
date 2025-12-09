import time
lst = list(range(1_000_000))
start = time.time()
[x*2 for x in lst]
print(time.time()-start)

#
import numpy as np 
arr = np.arange(1_000_000)
start = time.time()
arr*2
print(time.time()-start)
