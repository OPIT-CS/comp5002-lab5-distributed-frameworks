# Lab 5 Analysis

## Environment and recorded results

- Python version:
- Pandas version:
- Dask version:
- Number of rows:
- Approximate Pandas DataFrame memory:
- Dask workers:
- Dask partitions:
- Pandas aggregation time:
- Dask cluster startup time:
- Dask aggregation time:
- Verification passed: [yes/no]

## Analysis questions

1. **Performance comparison**

   Was Dask faster or slower than Pandas for this dataset? Explain the result in terms of task size, scheduling, process startup, serialization, communication, and result-collection overhead.

2. **Workers and partitions**

   What is the difference between a Dask worker and a Dask DataFrame partition? Why can it be useful to have more partitions than workers?

3. **Lazy evaluation**

   Which Dask operations in your implementation were lazy? What happened when `.compute()` was called, and why can delayed execution be useful?

4. **Framework overhead**

   Why can a high-level parallel framework be slower than optimized single-process Pandas for a relatively small in-memory groupby even though Dask can use multiple workers?

5. **Data ingestion**

   This lab converts an existing Pandas DataFrame with `dd.from_pandas`. Why can this become a bottleneck for genuinely large datasets, and what would a more scalable Dask ingestion approach look like?

6. **Abstraction**

   Which concerns does Dask handle for you compared with directly using `multiprocessing.Pool` or `mpi4py`? Consider partitioning, task scheduling, worker management, dependency tracking, and result collection.

7. **Correctness before performance**

   Why must the Pandas and Dask outputs be checked for numerical agreement before drawing conclusions from their execution times?
