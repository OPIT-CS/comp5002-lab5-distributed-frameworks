# Lab 5 Analysis

## Recorded timings

- Dask partitions used: [enter number, e.g., os.cpu_count()]
- Sequential (Pandas) time: [enter time] s
- Parallel (Dask) time: [enter time] s
- Speedup (Sequential / Parallel): [enter value]×

## Analysis questions

1. **Performance comparison**  
   Did Dask provide a noticeable speedup on your machine for the chosen data size?

2. **Ease of use**  
   How similar was the Dask code in `run_parallel_dask_aggregation` to the Pandas baseline, and how much effort was needed?

3. **Lazy evaluation**  
   When was computation actually triggered in your function, and why is laziness helpful here?

4. **Abstraction**  
   Which complexities did Dask handle for you vs using `multiprocessing.Pool` or `mpi4py` (partitioning, scheduling, result collection, potential fault tolerance)?
