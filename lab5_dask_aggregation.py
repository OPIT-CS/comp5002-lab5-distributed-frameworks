# lab5_dask_aggregation.py
import os
import sys
import time

import dask
import dask.dataframe as dd
import numpy as np
import pandas as pd
from dask.distributed import Client, LocalCluster

# Conservative defaults for typical student laptops.
NUM_ROWS = 500_000
NUM_UNIQUE_IDS = 1_000
RANDOM_SEED = 5002


def available_cpu_count():
    """Return the CPU count available to this process, with a compatibility fallback."""
    process_cpu_count = getattr(os, "process_cpu_count", None)
    if process_cpu_count is not None:
        count = process_cpu_count()
    else:
        count = os.cpu_count()
    return count or 1


NUM_WORKERS = min(4, available_cpu_count())
NUM_PARTITIONS = max(NUM_WORKERS * 2, 1)


def generate_sample_dataframe(num_rows):
    """Generate a deterministic Pandas DataFrame for the experiment."""
    if num_rows <= 0:
        raise ValueError("num_rows must be > 0")

    print(f"Generating Pandas DataFrame with {num_rows:,} rows...")
    start_time = time.perf_counter()

    rng = np.random.default_rng(RANDOM_SEED)
    ids = rng.integers(
        0,
        NUM_UNIQUE_IDS,
        size=num_rows,
        dtype=np.int32,
    )
    values = rng.random(num_rows) * 100.0

    df = pd.DataFrame({"id": ids, "value": values})

    elapsed = time.perf_counter() - start_time
    memory_mib = df.memory_usage(index=True, deep=True).sum() / (1024**2)

    print(f"Data generation time: {elapsed:.4f} seconds")
    print(f"Approximate DataFrame memory: {memory_mib:.2f} MiB")
    return df


def run_sequential_aggregation(df):
    """Run the groupby-mean baseline with Pandas."""
    print("Running aggregation with Pandas...")
    start_time = time.perf_counter()
    result = df.groupby("id")["value"].mean()
    elapsed = time.perf_counter() - start_time
    print(f"Pandas aggregation time: {elapsed:.4f} seconds")
    return result


def run_parallel_dask_aggregation(df, npartitions):
    """Run the same groupby-mean using Dask DataFrame."""
    if npartitions <= 0:
        raise ValueError("npartitions must be > 0")

    print(f"Running aggregation with Dask ({npartitions} partitions)...")
    start_time = time.perf_counter()

    result = None

    # --- TODO: Task 2 - Implement the Dask aggregation ---
    # 1) Convert df to a Dask DataFrame with npartitions partitions.
    # 2) Build the same groupby-mean expression as the Pandas baseline.
    # 3) Trigger execution with .compute() and assign the Pandas Series to result.
    # --- End TODO ---

    if result is None:
        raise NotImplementedError(
            "Complete Task 2: run_parallel_dask_aggregation"
        )

    elapsed = time.perf_counter() - start_time
    print(f"Dask aggregation time: {elapsed:.4f} seconds")
    return result


def verify_results(pandas_result, dask_result):
    """Verify that both frameworks computed numerically equivalent results."""
    pd.testing.assert_series_equal(
        pandas_result.sort_index(),
        dask_result.sort_index(),
        check_exact=False,
        check_dtype=False,
        rtol=1e-12,
        atol=1e-12,
    )


def main():
    print(f"Python: {sys.version.split()[0]} ({sys.implementation.name})")
    print(f"Pandas: {pd.__version__}")
    print(f"Dask: {dask.__version__}")
    print(f"Rows: {NUM_ROWS:,}")
    print(f"Workers: {NUM_WORKERS}")
    print(f"Partitions: {NUM_PARTITIONS}")
    print("-" * 40)

    pandas_df = generate_sample_dataframe(NUM_ROWS)
    print("-" * 40)

    sequential_result = run_sequential_aggregation(pandas_df)
    print("-" * 40)

    cluster_start = time.perf_counter()
    with LocalCluster(
        n_workers=NUM_WORKERS,
        threads_per_worker=1,
        processes=True,
    ) as cluster:
        with Client(cluster) as client:
            cluster_startup = time.perf_counter() - cluster_start
            print(f"Dask cluster startup time: {cluster_startup:.4f} seconds")
            print(f"Dask dashboard: {client.dashboard_link}")

            parallel_result = run_parallel_dask_aggregation(
                pandas_df,
                NUM_PARTITIONS,
            )

            verify_results(sequential_result, parallel_result)
            print("Verification: Pandas and Dask results match.")

    print("-" * 40)
    print("Lab 5 finished.")


if __name__ == "__main__":
    main()
