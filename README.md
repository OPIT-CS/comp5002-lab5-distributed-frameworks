# COMP-5002 Lab 5 • Parallel Data Aggregation with Dask

**Module** Module 11. Distributed Data and Computing Frameworks  
**Objective** Use Dask DataFrame to run a parallel groupby-mean on a large synthetic dataset, compare timings with Pandas, and explain performance, lazy evaluation, and framework abstractions.

## Prerequisites

- Python 3 installed.
- Pandas installed: `pip install pandas`
- Dask installed: `pip install "dask[dataframe]" distributed`
- Git basics: `clone`, `add`, `commit`, `push`
- Concepts from Module 11:
  - Large dataset challenges
  - High-level distributed frameworks
  - Dask DataFrame basics (Pandas-like API)
  - Lazy evaluation

## Background

Many workloads group records by an identifier and compute aggregates such as mean, sum, or count. Dask partitions data and executes the same operations across partitions with a scheduler, providing a familiar API while using multiple cores or machines.

## Files Provided

- `README.md` this file
- `lab5_dask_aggregation.py` starter with data generation, Pandas baseline, and Dask placeholders
- `analysis.md` where you record timings and answers

## Tasks

**General instructions**

- Clone your GitHub Classroom repository.
- Install the required libraries.
- Edit `lab5_dask_aggregation.py` to complete the tasks.
- Run both Pandas and Dask versions, then record timings in `analysis.md`.
- Commit frequently and push before the deadline.

---

### Task 1 Understand data generation and sequential baseline

1. Open `lab5_dask_aggregation.py`.
2. Read `generate_sample_dataframe(num_rows)` to see how the synthetic DataFrame with `id` and `value` is created.
3. Read `run_sequential_aggregation(df)` to see the Pandas `groupby('id')['value'].mean()` baseline.

---

### Task 2 Implement parallel aggregation with Dask DataFrame

1. In `run_parallel_dask_aggregation(df, npartitions)`:
   - Convert Pandas to Dask: `ddf = dd.from_pandas(df, npartitions=npartitions)`.
   - Apply the same groupby-mean on `ddf`.
   - Trigger computation with `.compute()` and return the result.

---

### Task 3 Run and record timings

1. Review the `main` block to see how data is generated and how timings are measured.
2. Adjust `NUM_ROWS` and `NUM_PARTITIONS` if needed for your machine.
3. Run `python lab5_dask_aggregation.py`.
4. Record **Sequential (Pandas)** and **Parallel (Dask)** times in `analysis.md`.

---

### Task 4 Analysis (`analysis.md`)

1. **Performance comparison** Did Dask provide a speedup on your machine for the chosen sizes?
2. **Ease of use** How close was the Dask API to Pandas for this task?
3. **Lazy evaluation** Where did computation actually start, and why is laziness useful here?
4. **Abstraction** What complexities did Dask handle compared with `multiprocessing` or MPI (partitioning, scheduling, collection, possible resilience)?

---

## Submission

1. Ensure `lab5_dask_aggregation.py` runs and prints timing output.
2. Ensure `analysis.md` includes your timings and answers.
3. Stage: `git add lab5_dask_aggregation.py analysis.md` (or `git add .`)
4. Commit: `git commit -m "Complete Lab 5 Dask Aggregation"`
5. Push: `git push origin main` (or your default branch)
6. Verify on GitHub that `lab5_dask_aggregation.py` and `analysis.md` are updated.
