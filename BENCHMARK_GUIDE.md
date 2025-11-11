# Benchmark Guide

This guide explains how to run comprehensive memory leak benchmarks across various SQLAlchemy configurations.

## Quick Start

### Run a Quick Test

```bash
./run_scenario.sh --quick
```

This runs a single scenario with balanced CRUD operations and 10,000 operations.

### Run Specific Scenario

```bash
./run_scenario.sh --scenario sqlalchemy1x --config balanced --scale small
```

### Run All Scenarios

```bash
./run_scenario.sh --all
```

## Benchmark Components

### 1. Scenarios

The benchmark suite includes 6 main scenarios:

- **sqlalchemy1x**: SQLAlchemy 1.4.54 standalone
- **sqlalchemy1x_fastapi**: SQLAlchemy 1.4.54 + FastAPI
- **sqlalchemy1x_fastapi_dependency_injector**: SQLAlchemy 1.4.54 + FastAPI + Dependency Injector
- **sqlalchemy2x**: SQLAlchemy 2.x standalone
- **sqlalchemy2x_fastapi**: SQLAlchemy 2.x + FastAPI
- **sqlalchemy2x_fastapi_dependency_injector**: SQLAlchemy 2.x + FastAPI + Dependency Injector

Each scenario tests 4 session management patterns:
- Async sessions
- Async scoped sessions
- Sync sessions
- Sync scoped sessions

### 2. CRUD Ratio Configurations

Various workload patterns to test different usage scenarios:

#### Standard Configurations
- **balanced**: 25% Create, 25% Read, 25% Update, 25% Delete
- **create_heavy**: 50% Create, 20% Read, 20% Update, 10% Delete
- **read_heavy**: 10% Create, 60% Read, 20% Update, 10% Delete
- **update_heavy**: 20% Create, 20% Read, 50% Update, 10% Delete
- **delete_heavy**: 10% Create, 20% Read, 20% Update, 50% Delete

#### Specialized Configurations
- **write_intensive**: 40% Create, 10% Read, 40% Update, 10% Delete
- **read_only**: 5% Create, 85% Read, 5% Update, 5% Delete
- **mixed_workload**: 30% Create, 40% Read, 20% Update, 10% Delete
- **create_only**: 90% Create, 5% Read, 3% Update, 2% Delete
- **transaction_heavy**: 35% Create, 15% Read, 35% Update, 15% Delete
- **crud_cycle**: 30% Create, 30% Read, 25% Update, 15% Delete
- **moderate_read**: 20% Create, 50% Read, 20% Update, 10% Delete

### 3. Operation Scales

- **tiny**: 1,000 operations (debug)
- **small**: 10,000 operations (quick test)
- **medium**: 100,000 operations (standard test)
- **large**: 1,000,000 operations (stress test)

## Using the Python Script Directly

### Install Dependencies

First, install dependencies for the scenario you want to test:

```bash
cd sqlalchemy1x
pip install -r requirements.txt
cd ..
```

### Run with Custom Parameters

```bash
python3 run_benchmarks.py \
  --scenarios sqlalchemy1x sqlalchemy2x \
  --configs balanced read_heavy \
  --scales small medium \
  --rounds 5
```

### Available Options

```bash
python3 run_benchmarks.py --help
```

Options:
- `--scenarios`: Choose specific scenarios or "all"
- `--configs`: Choose specific CRUD configurations or "all"
- `--scales`: Choose operation scales or "all"
- `--rounds`: Number of test rounds per configuration (default: 5)
- `--quick`: Run quick test (balanced config, small scale, 3 rounds)

## Test Matrices

Pre-defined test combinations are available in `benchmark_configs.yaml`:

### Quick Test
```bash
python3 run_benchmarks.py --quick
```

### Framework Comparison
```bash
python3 run_benchmarks.py \
  --scenarios sqlalchemy1x sqlalchemy1x_fastapi sqlalchemy1x_fastapi_dependency_injector \
  --configs balanced mixed_workload \
  --scales small medium
```

### Version Comparison
```bash
python3 run_benchmarks.py \
  --scenarios sqlalchemy1x sqlalchemy2x \
  --configs balanced read_heavy write_intensive \
  --scales small medium
```

## Understanding Results

### Output Format

Results are printed in markdown table format:

```
| Stack | Method | Status | Round | Diff | Initial | Final | Ops | C | R | U | D |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
```

- **Stack**: Scenario name
- **Method**: CRUD configuration and scale
- **Status**: ✅ (success) or ❌ (failure)
- **Round**: Test round number
- **Diff**: Memory difference (MB)
- **Initial**: Initial memory (MB)
- **Final**: Final memory (MB)
- **Ops**: Number of operations
- **C/R/U/D**: Create/Read/Update/Delete ratios

### Memory Leak Indicators

Look for these patterns:

1. **Consistent Growth**: Memory diff consistently positive across rounds
2. **Large Spikes**: Sudden large memory increases
3. **No Stabilization**: Memory keeps growing instead of stabilizing
4. **Comparison**: Compare similar scenarios to identify problematic patterns

### Example Analysis

```
Round 1: +25 MB (startup overhead expected)
Round 2: +5 MB  (some growth)
Round 3: +5 MB  (continued growth - potential leak)
Round 4: +4 MB  (continued growth - potential leak)
Round 5: +5 MB  (continued growth - confirms leak)
```

A healthy pattern shows:
- Large initial growth (startup)
- Decreasing or stable growth in subsequent rounds
- Occasional garbage collection drops (negative diffs)

## Running Individual Scenarios

Each scenario directory contains individual Python files that can be run directly:

```bash
cd sqlalchemy1x
python3 main_async.py
```

Edit the `__main__` section in each file to configure:
- Number of operations
- CRUD ratios
- Number of rounds

## Advanced Usage

### Custom CRUD Ratios

Create a custom test by editing `benchmark_configs.yaml` or by running individual scripts:

```python
# In sqlalchemy1x/main_async.py
result = asyncio.run(
    main(
        num_operations=50000,
        create_ratio=0.45,
        read_ratio=0.30,
        update_ratio=0.15,
        delete_ratio=0.10,
    )
)
```

### Continuous Testing

Run benchmarks periodically and compare results over time:

```bash
# Run and save results
./run_scenario.sh --all > results_$(date +%Y%m%d).txt

# Compare with previous runs
diff results_20241110.txt results_20241111.txt
```

### Automated Testing

Integrate with CI/CD:

```bash
# In your CI pipeline
./run_scenario.sh --quick || exit 1
```

## Total Possible Combinations

- **Scenarios**: 6
- **Session Patterns**: 4 per scenario
- **CRUD Configs**: 12
- **Operation Scales**: 4

**Total**: 6 × 4 × 12 × 4 = **1,152 unique test combinations**

With 5 rounds each: **5,760 individual benchmark runs**

## Performance Considerations

### Estimated Run Times

- **Quick test** (~3 mins): 1 scenario, 1 config, 1 scale, 3 rounds
- **Standard test** (~30 mins): 2 scenarios, 3 configs, 2 scales, 5 rounds
- **Comprehensive test** (~8 hours): All scenarios, all configs, 2 scales, 5 rounds
- **Full stress test** (~24+ hours): All scenarios, all configs, all scales, 5 rounds

### Resource Requirements

- **Memory**: At least 2GB free RAM
- **Disk**: ~1GB for databases and logs
- **CPU**: Multi-core recommended for faster execution

## Troubleshooting

### Import Errors

Install dependencies for the specific scenario:

```bash
cd <scenario_directory>
pip install -r requirements.txt
```

### Database Locked

Delete existing test databases:

```bash
find . -name "test.db*" -delete
```

### Timeout Issues

Reduce operation scale or increase timeout in `run_benchmarks.py`:

```python
timeout=7200,  # 2 hours
```

## Analyzing Results

### Automated Analysis

Use the analysis script to identify memory leak patterns:

```bash
# Analyze results file
./run_scenario.sh --quick > results.txt
python3 analyze_results.py results.txt

# Pipe directly
./run_scenario.sh --quick | python3 analyze_results.py

# Save analysis
./run_scenario.sh --all | tee results.txt | python3 analyze_results.py > analysis.txt
```

### Analysis Features

The analyzer provides:

1. **Leak Detection**: Identifies scenarios with consistent memory growth
2. **Stable Scenarios**: Highlights well-behaved implementations
3. **Comparative Analysis**: Compares different SQLAlchemy versions and patterns
4. **Statistical Summary**: Average growth rates, total growth, final memory

### Leak Detection Criteria

A scenario is flagged as a leak suspect if:
- Average growth > 2 MB per round after first round
- No memory stabilization in last 3 rounds
- Total memory growth > 50 MB across 5+ rounds

### Manual Analysis

Look for these patterns in raw results:

```
✅ Good Pattern:
Round 1: +25 MB (startup overhead)
Round 2: +2 MB  (stabilizing)
Round 3: -1 MB  (GC cleanup)
Round 4: +1 MB  (stable)
Round 5: 0 MB   (stable)

⚠️  Potential Leak:
Round 1: +25 MB
Round 2: +5 MB
Round 3: +5 MB
Round 4: +4 MB
Round 5: +5 MB  (consistent growth)
```

## Contributing

To add new configurations:

1. Add CRUD ratios to `benchmark_configs.yaml`
2. Add test matrices for common use cases
3. Update this guide with new configurations
4. Run tests and document results

## Next Steps

1. Run a quick test to verify setup
2. Choose appropriate test matrix for your needs
3. Analyze results and identify patterns
4. Compare scenarios to understand memory behavior
5. Document findings in README.md
