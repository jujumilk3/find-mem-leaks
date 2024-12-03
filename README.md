# find-mem-leaks

Test project to find mem leaks from various python packages and archs.

## Commands

Install memray

```bash
pip install memray
```

Run each projects by using memray

```bash
cd {{project_name}}  # e.g intended_with_fastapi
memray run main.py
```

Check created memray report

```bash
memray flamegraph {{memray_file_name}}.bin
```

## Results

### sqlalchemy1x

| Stack | Method | ✅ | Iter | Diff | Initial | Final | Ops | C | R | U | D |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| sqlalchemy1x_async_session | 10000_operations | ✅ | 1 | 18.73 | 36.84 | 55.57 | 10000 | 0.25 | 0.25 | 0.25 | 0.25 |
| sqlalchemy1x_async_session | 10000_operations | ✅ | 2 | 0.5 | 55.63 | 56.13 | 10000 | 0.25 | 0.25 | 0.25 | 0.25 |
| sqlalchemy1x_async_session | 10000_operations | ✅ | 3 | 4.22 | 56.11 | 60.33 | 10000 | 0.25 | 0.25 | 0.25 | 0.25 |
| sqlalchemy1x_async_session | 10000_operations | ✅ | 4 | -1.14 | 60.31 | 59.17 | 10000 | 0.25 | 0.25 | 0.25 | 0.25 |
| sqlalchemy1x_async_session | 10000_operations | ✅ | 5 | 0.3 | 59.2 | 59.5 | 10000 | 0.25 | 0.25 | 0.25 | 0.25 |
| sqlalchemy1x_async_session | 100000_operations | ✅ | 1 | 24.71 | 41.95 | 66.66 | 100000 | 0.25 | 0.25 | 0.25 | 0.25 |
| sqlalchemy1x_async_session | 100000_operations | ✅ | 2 | 1.43 | 66.77 | 68.2 | 100000 | 0.25 | 0.25 | 0.25 | 0.25 |
| sqlalchemy1x_async_session | 100000_operations | ✅ | 3 | 2.3 | 68.28 | 70.58 | 100000 | 0.25 | 0.25 | 0.25 | 0.25 |
| sqlalchemy1x_async_session | 100000_operations | ✅ | 4 | 1.4 | 70.64 | 72.04 | 100000 | 0.25 | 0.25 | 0.25 | 0.25 |
| sqlalchemy1x_async_session | 100000_operations | ✅ | 5 | 12.42 | 72.15 | 84.57 | 100000 | 0.25 | 0.25 | 0.25 | 0.25 |
| sqlalchemy1x_async_session | 1000000_operations | ✅ | 1 | 78.62 | 41.02 | 119.64 | 1000000 | 0.25 | 0.25 | 0.25 | 0.25 |
| sqlalchemy1x_async_session | 1000000_operations | ✅ | 2 | -30.87 | 119.72 | 88.86 | 1000000 | 0.25 | 0.25 | 0.25 | 0.25 |
| sqlalchemy1x_async_session | 1000000_operations | ✅ | 3 | -28.65 | 88.91 | 60.26 | 1000000 | 0.25 | 0.25 | 0.25 | 0.25 |
| sqlalchemy1x_async_session | 1000000_operations | ✅ | 4 | -19.73 | 60.55 | 40.82 | 1000000 | 0.25 | 0.25 | 0.25 | 0.25 |
| sqlalchemy1x_async_session | 1000000_operations | ✅ | 5 | 40.23 | 43.07 | 83.3 | 1000000 | 0.25 | 0.25 | 0.25 | 0.25 |
| sqlalchemy1x_async_session | create_heavy | ✅ | 1 | 23.86 | 41.43 | 65.28 | 10000 | 0.5 | 0.2 | 0.2 | 0.1 |
| sqlalchemy1x_async_session | create_heavy | ✅ | 2 | 5.92 | 65.35 | 71.27 | 10000 | 0.5 | 0.2 | 0.2 | 0.1 |
| sqlalchemy1x_async_session | create_heavy | ✅ | 3 | 5.03 | 71.27 | 76.3 | 10000 | 0.5 | 0.2 | 0.2 | 0.1 |
| sqlalchemy1x_async_session | create_heavy | ✅ | 4 | -2.59 | 76.3 | 73.71 | 10000 | 0.5 | 0.2 | 0.2 | 0.1 |
| sqlalchemy1x_async_session | create_heavy | ✅ | 5 | -1.0 | 73.71 | 72.71 | 10000 | 0.5 | 0.2 | 0.2 | 0.1 |
| sqlalchemy1x_async_session | read_heavy | ✅ | 1 | 20.21 | 41.04 | 61.25 | 10000 | 0.1 | 0.6 | 0.2 | 0.1 |
| sqlalchemy1x_async_session | read_heavy | ✅ | 2 | 1.27 | 61.25 | 62.52 | 10000 | 0.1 | 0.6 | 0.2 | 0.1 |
| sqlalchemy1x_async_session | read_heavy | ✅ | 3 | 1.54 | 62.57 | 64.11 | 10000 | 0.1 | 0.6 | 0.2 | 0.1 |
| sqlalchemy1x_async_session | read_heavy | ✅ | 4 | -4.75 | 64.09 | 59.34 | 10000 | 0.1 | 0.6 | 0.2 | 0.1 |
| sqlalchemy1x_async_session | read_heavy | ✅ | 5 | -0.82 | 59.38 | 58.57 | 10000 | 0.1 | 0.6 | 0.2 | 0.1 |
| sqlalchemy1x_async_session | update_heavy | ✅ | 1 | 23.46 | 40.65 | 64.11 | 10000 | 0.2 | 0.2 | 0.5 | 0.1 |
| sqlalchemy1x_async_session | update_heavy | ✅ | 2 | 5.91 | 64.11 | 70.02 | 10000 | 0.2 | 0.2 | 0.5 | 0.1 |
| sqlalchemy1x_async_session | update_heavy | ✅ | 3 | -2.16 | 70.0 | 67.84 | 10000 | 0.2 | 0.2 | 0.5 | 0.1 |
| sqlalchemy1x_async_session | update_heavy | ✅ | 4 | 3.27 | 67.84 | 71.11 | 10000 | 0.2 | 0.2 | 0.5 | 0.1 |
| sqlalchemy1x_async_session | update_heavy | ✅ | 5 | -1.23 | 71.11 | 69.87 | 10000 | 0.2 | 0.2 | 0.5 | 0.1 |
| sqlalchemy1x_async_session | delete_heavy | ✅ | 1 | 21.18 | 41.28 | 62.46 | 10000 | 0.1 | 0.2 | 0.2 | 0.5 |
| sqlalchemy1x_async_session | delete_heavy | ✅ | 2 | 2.91 | 62.47 | 65.38 | 10000 | 0.1 | 0.2 | 0.2 | 0.5 |
| sqlalchemy1x_async_session | delete_heavy | ✅ | 3 | 1.72 | 65.46 | 67.18 | 10000 | 0.1 | 0.2 | 0.2 | 0.5 |
| sqlalchemy1x_async_session | delete_heavy | ✅ | 4 | -1.07 | 67.18 | 66.11 | 10000 | 0.1 | 0.2 | 0.2 | 0.5 |
| sqlalchemy1x_async_session | delete_heavy | ✅ | 5 | -2.12 | 66.19 | 64.07 | 10000 | 0.1 | 0.2 | 0.2 | 0.5 |
| sqlalchemy1x_sync_session | 10000_operations | ✅ | 1 | 15.59 | 40.71 | 56.3 | 10000 | 0.25 | 0.25 | 0.25 | 0.25 |
| sqlalchemy1x_sync_session | 10000_operations | ✅ | 2 | -11.79 | 56.33 | 44.54 | 10000 | 0.25 | 0.25 | 0.25 | 0.25 |
| sqlalchemy1x_sync_session | 10000_operations | ✅ | 3 | -2.44 | 45.13 | 42.7 | 10000 | 0.25 | 0.25 | 0.25 | 0.25 |
| sqlalchemy1x_sync_session | 10000_operations | ✅ | 4 | -1.33 | 43.43 | 42.1 | 10000 | 0.25 | 0.25 | 0.25 | 0.25 |
| sqlalchemy1x_sync_session | 10000_operations | ✅ | 5 | 0.07 | 42.68 | 42.75 | 10000 | 0.25 | 0.25 | 0.25 | 0.25 |
