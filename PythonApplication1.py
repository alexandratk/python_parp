import numpy as np
import time
from multiprocessing import Process, Queue

arr = np.random.randint(0, 1000, size=(1000, 10))

def maxmatrix(index, q):
    max = -1
    for j in range(len(arr[index])):
        if (max < arr[index][j]):
            max = arr[index][j]
    q.put(max)

if __name__ == '__main__':
    procs = []
    res = []
    q = Queue()
    for i in range(10):
        proc = Process(target=maxmatrix, args=(i, q))
        procs.append(proc)
    start = time.time()
    for proc in procs:
        proc.start()
    for proc in procs:
        proc.join()
    for proc in procs:
        res.append(q.get())
    maxall = max(res)
    end = time.time()
    res = end - start
    print('Max element: ', maxall)
    print('Time: ', res * 1000, ' ms')


    start = time.time()
    max = -1
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if (max < arr[i][j]):
                max = arr[i][j]
    end = time.time()
    res = end - start
    print('Max element: ', max)
    print('Time: ', res * 1000, ' ms')


    
    