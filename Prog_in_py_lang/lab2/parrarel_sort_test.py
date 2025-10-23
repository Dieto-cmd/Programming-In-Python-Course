from parrarel_sorting_multiprocessing import parallel_sort
import random
import time
import statistics

import matplotlib.pyplot as plt
import pandas as pd

def benchmark_and_plot():
    sizes = [1000, 5000, 10000, 50000, 100000,1000000, 10000000,20000000]
    process_counts = [1, 2, 4, 8]
    results = []

    for n in sizes:
        base_data = [random.randint(0, 1000000) for _ in range(n)]
        for p in process_counts:
            data_copy = list(base_data)  
            start = time.perf_counter()
            parallel_sort(data_copy, p)
            end = time.perf_counter()
            execution_time = end - start
            results.append({"size": n, "processes": p, "time": execution_time})
            print(f"n={n}, p={p}, time={execution_time:.6f}s")

    df = pd.DataFrame(results)

    plt.figure(figsize=(10, 6))
    for p in process_counts:
        sub = df[df["processes"] == p].sort_values("size")
        plt.plot(sub["size"], sub["time"], marker='o', label=f"{p} processes")

    plt.xlabel("Input Size")
    plt.ylabel("Time (s)")
    plt.title("Parallel Sort Performance Benchmark (median of 5 runs)")
    plt.xscale("log")   
    plt.yscale("log")
    plt.legend()
    plt.grid(True, which="both", ls="--")
    plt.show()

if __name__ == "__main__":
    benchmark_and_plot()
