import multiprocessing as mp
from heapq import merge

def parallel_sort(data, num_workers=4):
    chunks = []
    sorted_chunks = []
    for i in range(num_workers):
        start_index = 0 + i*len(data)//num_workers
        end_index =  1 if (i+1)*len(data)//num_workers == 0 else (i+1)*len(data)//num_workers
        chunks.append(data[start_index:end_index])
    with mp.Pool(processes=num_workers) as pool:
        sorted_chunks = (pool.map(sorted, chunks))

    return list(merge(*sorted_chunks))


