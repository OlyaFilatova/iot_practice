study plan based on [the generated path](../generated/suggested-path.md)
## Theory
- [ ] Parallelism vs Concurrency
- [ ] CPU-bound vs I/O-bound workloads
- [ ] GIL (Global Interpreter Lock) - and how multiprocessing bypasses it
- [ ] Process lifecycle (fork/spawn, parent/child)
- [ ] Inter-process communication (IPC) mechanisms:
    - [ ] pipes
    - [ ] queues
    - [ ] shared memory
    - [ ] sockets
    - [ ] files / mmap
- [ ] Synchronization primitives
- [ ] locks
    - [ ] semaphores
    - [ ] events
    - [ ] barriers
    - [ ] condition variables
- [ ] Process pools vs manual process mgmt
- [ ] Deadlocks, race conditions
- [ ] Copy-on-write memory
- [ ] Serialization / pickling limitations
- [ ] Data partitioning strategies
    - [ ] task parallelism
    - [ ] data parallelism
- [ ] Scaling across multiple machines (very common interview point)
    - [ ] multiprocessing vs distributed systems (Ray, Dask, Spark, Celery)
- [ ] Why processes instead of threads?
- [ ] Why a queue gets stuck / how to avoid blocked pipes
- [ ] Deadlock examples & fixes
- [ ] How to benchmark multiprocessing code
- [ ] How to handle child process crashes
- [ ] How to reduce overhead of pickle
- [ ] Why certain workloads don't scale
- [ ] When multiprocessing performs worse
- [ ] How to run multiprocessing in Docker or Kubernetes
- [ ] Resource limits (CPU count)
- [ ] Logging across processes
- [ ] Monitoring / metrics collection
- [ ] Inter-process priority management
- [ ] Autoscaling worker pools
- [ ] Clean shutdown instructions inside containers

- python standard lib `multiprocessing`
    - [ ] Core APIs
        - [ ] `Process`
        - [ ] `Pool`
        - [ ] `Queue`, `Pipe`
        - [ ] `Value`, `Array`, `shared_memory`
        - [ ] `Manager`
        - [ ] `Lock`, `Semaphore`, `Event`, `Barrier`, `Condition`
    - [ ] Advanced Concepts
        - [ ] `spawn` vs `fork` vs `forkserver`
        - [ ] Using `multiprocessing` safely with `if __name__ == "__main__":`
        - [ ] Passing large objects efficiently
        - [ ] Avoiding unnecessary serialization
        - [ ] Worker initialization (`initializer` functions)
        - [ ] Graceful shutdowns & handling timeouts
        - [ ] Error propagation between child and parent processes

- [ ] Choose and start studying one of the following frameworks
    1. Ray - most important (industry-standard parallel Python)
    2. Dask - data parallelism, cluster scale
    3. Joblib - scientific computing parallel loops
    4. Celery - distributed task queues (process-based, real-world)
    5. PyTorch multiprocessing (if doing ML)

## Projects

- [ ] Stage 1 - Basics (1 week)

        Implement:

    - [ ] simple parallel loops
    - [ ] parallel map with `Pool`
    - [ ] reading/writing queues

            Exercises:

    - [ ] Compute factorials in parallel
    - [ ] Parallel file processing
    - [ ] Measure speed improvements with `time.perf_counter()`

- [ ] Stage 2 - Intermediate (2–3 weeks)

        Implement:

    - [ ] shared memory arrays
    - [ ] worker pools with state
    - [ ] long-running workers
    - [ ] using locks to prevent corruption
    - [ ] profiling multiprocessing code

            Exercises:

    - [ ] Image resizing pipeline
    - [ ] CPU-bound numerical tasks
    - [ ] Producer-consumer system using `Queue`

- [ ] Stage 3 - Advanced (3–6 weeks)

        Real-world components

    - [ ] multiprocessing + async mix
    - [ ] graceful shutdown strategies
    - [ ] backpressure management
    - [ ] queues with bounded sizes
    - [ ] metrics and logging
    - [ ] error recovery and retry logic
    - [ ] memory limits (avoid OOM)
    - [ ] process supervision
    - [ ] parallel pipelines (multi-stage processing)

            Exercises:

    - [ ] Build a parallel ETL system
    - [ ] Build a modular pipeline (extract → process → store)
    - [ ] Run 10–20 CPU workers safely

- [ ] PyQt + gRPC + multiprocessing + aiohttp project
    - [ ] Build a PyQt GUI that launches tasks asynchronously

        * Never blocking the event loop
        * Using asyncio + Qt integration

    - [ ] Add a gRPC server running in background

        * Async service methods
        * Streaming responses

    - [ ] Add a multiprocessing worker subsystem

        * ProcessPoolExecutor or raw Process
        * Queue-based pipelines (Producer → Worker → Collector)

    - [ ] Add high-performance data passing

        * Shared memory for images or arrays
        * Zero-copy handoffs

    - [ ] Add monitoring components

        * aiohttp endpoint `/metrics`
        * Worker heartbeat
        * GUI displays worker health

    - [ ] Add fault tolerance

        * On process crash:

            * GUI shows warning
            * gRPC restarts worker
            * Task is requeued

## Ideas for final project

### 1. Distributed Parallel Data Pipeline

Description:

Build a system that:

1. Reads large datasets (GBs)
2. Splits work into chunks
3. Runs CPU-heavy processing in parallel using:

* `multiprocessing`
* OR Ray (recommended)
4. Uses:

* queues for communication
* shared memory for large arrays
5. Has:

* Retry handling
* Logging
* Monitoring dashboard (Prometheus/Grafana or simple Flask API)
* Configuration file
6. Stores results into:

* PostgreSQL or DuckDB

### Professional Features to Include

* Graceful shutdown (SIGTERM handling)
* Worker health checks
* Metrics: throughput, latency, CPU usage
* Backpressure (don't read too fast)
* Process pool resizing logic


### 2. High-Performance Image or Video Processing Pipeline

### Features:

* Uses shared memory (zero-copy) for frames
* Pipe or Queue to push frames between workers
* Multiple processing stages:
  * decode → transform → encode
* Real-time scheduling
* CPU affinity pinning
* Batch processing optimizations

### 3. Local MapReduce Engine in Pure Python

Implement:

* A Job Manager
* Worker processes
* Distributed shuffle
* Fault tolerance (reassign failed tasks)
* Remote Worker API (use multiprocessing + RPC via ZeroMQ)

### 📌 4. GUI-based Distributed Processing System

with Qt + asyncio + multiprocessing + gRPC + aiohttp

1. Accepts tasks (e.g., image/video/file/computation jobs)
2. Sends tasks to an async gRPC server
3. gRPC server dispatches work to a multiprocessing worker pool
4. Workers perform heavy CPU processing
5. Progress updates are streamed back via:

   * gRPC streaming
   * or aiohttp SSE endpoints
6. GUI displays:

   * Realtime worker progress
   * Logs
   * Throughput metrics
7. Supports:

   * Cancellation
   * Retries
   * Load balancing
   * Worker failures
   * Graceful shutdown
