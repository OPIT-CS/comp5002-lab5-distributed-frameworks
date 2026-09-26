# COMP-5002 Lab 5 • Parallel Data Aggregation with Dask

**Module** Module 11. Distributed Data and Computing Frameworks  
**Objective** Use Dask DataFrame to run a partitioned groupby-mean on a synthetic dataset, compare it with Pandas, and explain lazy evaluation, scheduling overhead, partitioning, and framework abstractions.

## Prerequisites

- Python 3 installed.
- Pandas and NumPy installed.
- Dask DataFrame and Distributed installed.
- Git basics: `clone`, `add`, `commit`, `push`.
- Concepts from Module 11:
  - distributed data-processing challenges;
  - high-level distributed frameworks;
  - Dask DataFrame basics;
  - partitions and workers;
  - lazy evaluation.

Install the Python dependencies with:

```bash
python -m pip install pandas numpy "dask[dataframe]" distributed
```

## Background

Many workloads group records by an identifier and compute aggregates such as mean, sum, or count. Dask DataFrame offers a Pandas-like API while representing work as a task graph over partitions that can be scheduled across workers.

This lab deliberately begins with a Pandas DataFrame and converts it with `dd.from_pandas` because the goal is to compare APIs and execution models on one machine. For genuinely large or distributed datasets, creating one large Pandas object first is usually the wrong ingestion pattern. Production Dask workloads commonly read partitioned data directly with Dask, for example from Parquet or CSV.

Dask is also not expected to beat Pandas for every in-memory workload. Scheduler, serialization, communication, and process overhead can make Dask slower on small or simple datasets. That is a valid result to analyse.

## Files Provided

- `README.md` this file
- `lab5_dask_aggregation.py` starter with deterministic data generation, Pandas baseline, and a Dask TODO
- `analysis.md` where you record environment information, timings, and answers

## Tasks

**General instructions**

- Clone your GitHub Classroom repository.
- Install the required libraries.
- Edit `lab5_dask_aggregation.py` to complete the Dask TODO.
- Run the Pandas and Dask versions and verify that their results agree.
- Record observations in `analysis.md`.
- Commit frequently and push before the deadline.

---

### Task 1 — Review data generation and the Pandas baseline

Read `generate_sample_dataframe(num_rows)` and `run_sequential_aggregation(df)`.

The starter:

- uses a fixed NumPy random seed so runs are reproducible;
- stores IDs as `int32` to reduce memory use;
- reports the approximate Pandas DataFrame memory footprint;
- performs `groupby("id")["value"].mean()` as the Pandas baseline.

The same Pandas DataFrame is reused for the Dask experiment because neither aggregation mutates it. Do not add unnecessary `.copy()` calls.

---

### Task 2 — Implement the Dask aggregation

Complete `run_parallel_dask_aggregation(df, npartitions)`.

Your implementation must:

1. convert the Pandas DataFrame to a Dask DataFrame with the requested number of partitions;
2. create the same groupby-mean operation as the Pandas baseline;
3. keep that aggregation lazy until `.compute()` is called;
4. call `.compute()` and return the resulting Pandas Series.

The function's timer intentionally includes both construction of the Dask collection/task graph from the existing Pandas DataFrame and the actual computation.

---

### Task 3 — Understand workers and partitions

The starter keeps these concepts separate:

- `NUM_WORKERS` controls the number of worker processes in the local Dask cluster;
- `NUM_PARTITIONS` controls how many DataFrame partitions Dask schedules across those workers.

There may be more partitions than workers. Workers execute tasks; partitions describe pieces of the data.

The defaults are conservative so the lab runs on typical student laptops. If your machine has sufficient memory, you may increase `NUM_ROWS` after obtaining one successful run.

---

### Task 4 — Run and verify

Run:

```bash
python lab5_dask_aggregation.py
```

The script reports:

- Python, Pandas, and Dask versions;
- row count;
- worker and partition counts;
- DataFrame memory usage;
- Pandas aggregation time;
- Dask cluster startup time;
- Dask aggregation time;
- correctness verification.

The script must finish with:

```
Verification: Pandas and Dask results match.
```

Do not interpret timing results if verification fails.

---

### Task 5 — Analysis

Answer the questions in `analysis.md` about:

1. whether Dask was faster or slower and why;
2. workers versus partitions;
3. lazy evaluation and the role of `.compute()`;
4. why framework overhead matters;
5. why starting from a large Pandas DataFrame is not a scalable ingestion pattern;
6. which concerns Dask handles compared with lower-level multiprocessing or MPI;
7. why correctness verification is required before performance conclusions.

---

## Submission

1. Ensure `lab5_dask_aggregation.py` runs successfully and verification passes.
2. Ensure `analysis.md` contains your recorded environment, timings, and answers.
3. Stage: `git add lab5_dask_aggregation.py analysis.md` (or `git add .`)
4. Commit: `git commit -m "Complete Lab 5 Dask Aggregation"`
5. Push: `git push origin main` (or your default branch)
6. Verify on GitHub that `lab5_dask_aggregation.py` and `analysis.md` are updated.
