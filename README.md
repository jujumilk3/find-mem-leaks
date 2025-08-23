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

| Stack | Method | Status | Round | Diff | Initial | Final | Ops | C | R | U | D |
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
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| sqlalchemy1x_sync_session | 10000_operations | ✅ | 1 | 15.59 | 40.71 | 56.3 | 10000 | 0.25 | 0.25 | 0.25 | 0.25 |
| sqlalchemy1x_sync_session | 10000_operations | ✅ | 2 | -11.79 | 56.33 | 44.54 | 10000 | 0.25 | 0.25 | 0.25 | 0.25 |
| sqlalchemy1x_sync_session | 10000_operations | ✅ | 3 | -2.44 | 45.13 | 42.7 | 10000 | 0.25 | 0.25 | 0.25 | 0.25 |
| sqlalchemy1x_sync_session | 10000_operations | ✅ | 4 | -1.33 | 43.43 | 42.1 | 10000 | 0.25 | 0.25 | 0.25 | 0.25 |
| sqlalchemy1x_sync_session | 10000_operations | ✅ | 5 | 0.07 | 42.68 | 42.75 | 10000 | 0.25 | 0.25 | 0.25 | 0.25 |
| sqlalchemy1x_sync_session | 100000_operations | ✅ | 1 | 0.12 | 40.53 | 40.65 | 100000 | 0.25 | 0.25 | 0.25 | 0.25 |
| sqlalchemy1x_sync_session | 100000_operations | ✅ | 2 | 10.8 | 41.54 | 52.35 | 100000 | 0.25 | 0.25 | 0.25 | 0.25 |
| sqlalchemy1x_sync_session | 100000_operations | ✅ | 3 | -9.18 | 52.51 | 43.33 | 100000 | 0.25 | 0.25 | 0.25 | 0.25 |
| sqlalchemy1x_sync_session | 100000_operations | ✅ | 4 | -2.18 | 44.02 | 41.84 | 100000 | 0.25 | 0.25 | 0.25 | 0.25 |
| sqlalchemy1x_sync_session | 100000_operations | ✅ | 5 | 0.5 | 42.45 | 42.95 | 100000 | 0.25 | 0.25 | 0.25 | 0.25 |
| sqlalchemy1x_sync_session | 1000000_operations | ✅ | 1 | 12.52 | 43.09 | 55.61 | 1000000 | 0.25 | 0.25 | 0.25 | 0.25 |
| sqlalchemy1x_sync_session | 1000000_operations | ✅ | 2 | -10.98 | 55.8 | 44.81 | 1000000 | 0.25 | 0.25 | 0.25 | 0.25 |
| sqlalchemy1x_sync_session | 1000000_operations | ✅ | 3 | -2.3 | 46.0 | 43.7 | 1000000 | 0.25 | 0.25 | 0.25 | 0.25 |
| sqlalchemy1x_sync_session | 1000000_operations | ✅ | 4 | -2.88 | 46.0 | 43.12 | 1000000 | 0.25 | 0.25 | 0.25 | 0.25 |
| sqlalchemy1x_sync_session | 1000000_operations | ✅ | 5 | -1.73 | 44.86 | 43.12 | 1000000 | 0.25 | 0.25 | 0.25 | 0.25 |
| sqlalchemy1x_sync_session | create_heavy | ✅ | 1 | 9.73 | 44.88 | 54.61 | 10000 | 0.5 | 0.2 | 0.2 | 0.1 |
| sqlalchemy1x_sync_session | create_heavy | ✅ | 2 | -11.48 | 54.69 | 43.2 | 10000 | 0.5 | 0.2 | 0.2 | 0.1 |
| sqlalchemy1x_sync_session | create_heavy | ✅ | 3 | 10.89 | 44.81 | 55.7 | 10000 | 0.5 | 0.2 | 0.2 | 0.1 |
| sqlalchemy1x_sync_session | create_heavy | ✅ | 4 | -11.73 | 55.78 | 44.05 | 10000 | 0.5 | 0.2 | 0.2 | 0.1 |
| sqlalchemy1x_sync_session | create_heavy | ✅ | 5 | 10.27 | 45.69 | 55.95 | 10000 | 0.5 | 0.2 | 0.2 | 0.1 |
| sqlalchemy1x_sync_session | read_heavy | ✅ | 1 | -11.86 | 56.03 | 44.17 | 10000 | 0.1 | 0.6 | 0.2 | 0.1 |
| sqlalchemy1x_sync_session | read_heavy | ✅ | 2 | -1.73 | 45.83 | 44.09 | 10000 | 0.1 | 0.6 | 0.2 | 0.1 |
| sqlalchemy1x_sync_session | read_heavy | ✅ | 3 | -1.84 | 45.72 | 43.88 | 10000 | 0.1 | 0.6 | 0.2 | 0.1 |
| sqlalchemy1x_sync_session | read_heavy | ✅ | 4 | -1.7 | 45.53 | 43.83 | 10000 | 0.1 | 0.6 | 0.2 | 0.1 |
| sqlalchemy1x_sync_session | read_heavy | ✅ | 5 | -1.52 | 45.52 | 44.0 | 10000 | 0.1 | 0.6 | 0.2 | 0.1 |
| sqlalchemy1x_sync_session | update_heavy | ✅ | 1 | -1.55 | 45.66 | 44.11 | 10000 | 0.2 | 0.2 | 0.5 | 0.1 |
| sqlalchemy1x_sync_session | update_heavy | ✅ | 2 | -1.53 | 45.77 | 44.23 | 10000 | 0.2 | 0.2 | 0.5 | 0.1 |
| sqlalchemy1x_sync_session | update_heavy | ✅ | 3 | -1.8 | 45.88 | 44.08 | 10000 | 0.2 | 0.2 | 0.5 | 0.1 |
| sqlalchemy1x_sync_session | update_heavy | ✅ | 4 | -1.2 | 45.83 | 44.62 | 10000 | 0.2 | 0.2 | 0.5 | 0.1 |
| sqlalchemy1x_sync_session | update_heavy | ✅ | 5 | -2.28 | 46.3 | 44.02 | 10000 | 0.2 | 0.2 | 0.5 | 0.1 |
| sqlalchemy1x_sync_session | delete_heavy | ✅ | 1 | 9.86 | 45.67 | 55.53 | 10000 | 0.1 | 0.2 | 0.2 | 0.5 |
| sqlalchemy1x_sync_session | delete_heavy | ✅ | 2 | -11.11 | 55.61 | 44.5 | 10000 | 0.1 | 0.2 | 0.2 | 0.5 |
| sqlalchemy1x_sync_session | delete_heavy | ✅ | 3 | -1.81 | 46.14 | 44.33 | 10000 | 0.1 | 0.2 | 0.2 | 0.5 |
| sqlalchemy1x_sync_session | delete_heavy | ✅ | 4 | -1.75 | 46.05 | 44.3 | 10000 | 0.1 | 0.2 | 0.2 | 0.5 |
| sqlalchemy1x_sync_session | delete_heavy | ✅ | 5 | -4.14 | 45.97 | 41.83 | 10000 | 0.1 | 0.2 | 0.2 | 0.5 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| sqlalchemy1x_async_scoped_session | 10000_operations | ✅ | 1 | -9.81 | 44.36 | 34.55 | 10000 | 0.25 | 0.25 | 0.25 | 0.25 |
| sqlalchemy1x_async_scoped_session | 10000_operations | ✅ | 2 | 8.67 | 36.94 | 45.61 | 10000 | 0.25 | 0.25 | 0.25 | 0.25 |
| sqlalchemy1x_async_scoped_session | 10000_operations | ✅ | 3 | 1.84 | 45.58 | 47.42 | 10000 | 0.25 | 0.25 | 0.25 | 0.25 |
| sqlalchemy1x_async_scoped_session | 10000_operations | ✅ | 4 | 2.25 | 47.39 | 49.64 | 10000 | 0.25 | 0.25 | 0.25 | 0.25 |
| sqlalchemy1x_async_scoped_session | 10000_operations | ✅ | 5 | -8.53 | 49.62 | 41.09 | 10000 | 0.25 | 0.25 | 0.25 | 0.25 |
| sqlalchemy1x_async_scoped_session | 100000_operations | ✅ | 1 | 2.22 | 43.36 | 45.58 | 100000 | 0.25 | 0.25 | 0.25 | 0.25 |
| sqlalchemy1x_async_scoped_session | 100000_operations | ✅ | 2 | 9.28 | 47.89 | 57.17 | 100000 | 0.25 | 0.25 | 0.25 | 0.25 |
| sqlalchemy1x_async_scoped_session | 100000_operations | ✅ | 3 | 0.0 | 57.31 | 57.31 | 100000 | 0.25 | 0.25 | 0.25 | 0.25 |
| sqlalchemy1x_async_scoped_session | 100000_operations | ✅ | 4 | -1.09 | 57.47 | 56.38 | 100000 | 0.25 | 0.25 | 0.25 | 0.25 |
| sqlalchemy1x_async_scoped_session | 100000_operations | ✅ | 5 | -0.78 | 56.62 | 55.84 | 100000 | 0.25 | 0.25 | 0.25 | 0.25 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| sqlalchemy1x_sync_scoped_session | 10000_operations | ✅ | 1 | 27.17 | 42.67 | 69.84 | 10000 | 0.25 | 0.25 | 0.25 | 0.25 |
| sqlalchemy1x_sync_scoped_session | 10000_operations | ✅ | 2 | 0.98 | 69.84 | 70.83 | 10000 | 0.25 | 0.25 | 0.25 | 0.25 |
| sqlalchemy1x_sync_scoped_session | 10000_operations | ✅ | 3 | 1.91 | 70.83 | 72.73 | 10000 | 0.25 | 0.25 | 0.25 | 0.25 |
| sqlalchemy1x_sync_scoped_session | 10000_operations | ✅ | 4 | 1.0 | 72.73 | 73.73 | 10000 | 0.25 | 0.25 | 0.25 | 0.25 |
| sqlalchemy1x_sync_scoped_session | 10000_operations | ✅ | 5 | 0.11 | 73.73 | 73.84 | 10000 | 0.25 | 0.25 | 0.25 | 0.25 |
| sqlalchemy1x_sync_scoped_session | 100000_operations | ✅ | 1 | 2.94 | 73.84 | 76.78 | 100000 | 0.25 | 0.25 | 0.25 | 0.25 |
| sqlalchemy1x_sync_scoped_session | 100000_operations | ✅ | 2 | 0.48 | 76.78 | 77.27 | 100000 | 0.25 | 0.25 | 0.25 | 0.25 |
| sqlalchemy1x_sync_scoped_session | 100000_operations | ✅ | 3 | 1.05 | 77.27 | 78.31 | 100000 | 0.25 | 0.25 | 0.25 | 0.25 |
| sqlalchemy1x_sync_scoped_session | 100000_operations | ✅ | 4 | 0.09 | 78.31 | 78.41 | 100000 | 0.25 | 0.25 | 0.25 | 0.25 |
| sqlalchemy1x_sync_scoped_session | 100000_operations | ✅ | 5 | 0.47 | 78.41 | 78.88 | 100000 | 0.25 | 0.25 | 0.25 | 0.25 |
| sqlalchemy1x_sync_scoped_session | 1000000_operations | ✅ | 1 | -1.95 | 78.88 | 76.92 | 1000000 | 0.25 | 0.25 | 0.25 | 0.25 |
| sqlalchemy1x_sync_scoped_session | 1000000_operations | ✅ | 2 | 1.28 | 77.0 | 78.28 | 1000000 | 0.25 | 0.25 | 0.25 | 0.25 |
| sqlalchemy1x_sync_scoped_session | 1000000_operations | ✅ | 3 | 0.05 | 78.28 | 78.33 | 1000000 | 0.25 | 0.25 | 0.25 | 0.25 |
| sqlalchemy1x_sync_scoped_session | 1000000_operations | ✅ | 4 | -2.31 | 78.33 | 76.02 | 1000000 | 0.25 | 0.25 | 0.25 | 0.25 |
| sqlalchemy1x_sync_scoped_session | 1000000_operations | ✅ | 5 | 0.27 | 76.09 | 76.36 | 1000000 | 0.25 | 0.25 | 0.25 | 0.25 |
| sqlalchemy1x_sync_scoped_session | create_heavy | ✅ | 1 | 0.14 | 76.36 | 76.5 | 10000 | 0.5 | 0.2 | 0.2 | 0.1 |
| sqlalchemy1x_sync_scoped_session | create_heavy | ✅ | 2 | 0.2 | 76.5 | 76.7 | 10000 | 0.5 | 0.2 | 0.2 | 0.1 |
| sqlalchemy1x_sync_scoped_session | create_heavy | ✅ | 3 | 0.0 | 76.7 | 76.7 | 10000 | 0.5 | 0.2 | 0.2 | 0.1 |
| sqlalchemy1x_sync_scoped_session | create_heavy | ✅ | 4 | 0.02 | 76.7 | 76.72 | 10000 | 0.5 | 0.2 | 0.2 | 0.1 |
| sqlalchemy1x_sync_scoped_session | create_heavy | ✅ | 5 | 0.02 | 76.72 | 76.73 | 10000 | 0.5 | 0.2 | 0.2 | 0.1 |
| sqlalchemy1x_sync_scoped_session | read_heavy | ✅ | 1 | 0.0 | 76.73 | 76.73 | 10000 | 0.1 | 0.6 | 0.2 | 0.1 |
| sqlalchemy1x_sync_scoped_session | read_heavy | ✅ | 2 | 0.02 | 76.73 | 76.75 | 10000 | 0.1 | 0.6 | 0.2 | 0.1 |
| sqlalchemy1x_sync_scoped_session | read_heavy | ✅ | 3 | 0.0 | 76.75 | 76.75 | 10000 | 0.1 | 0.6 | 0.2 | 0.1 |
| sqlalchemy1x_sync_scoped_session | read_heavy | ✅ | 4 | 0.0 | 76.75 | 76.75 | 10000 | 0.1 | 0.6 | 0.2 | 0.1 |
| sqlalchemy1x_sync_scoped_session | read_heavy | ✅ | 5 | 0.02 | 76.75 | 76.77 | 10000 | 0.1 | 0.6 | 0.2 | 0.1 |
| sqlalchemy1x_sync_scoped_session | update_heavy | ✅ | 1 | -0.36 | 76.77 | 76.41 | 10000 | 0.2 | 0.2 | 0.5 | 0.1 |
| sqlalchemy1x_sync_scoped_session | update_heavy | ✅ | 2 | 0.3 | 76.41 | 76.7 | 10000 | 0.2 | 0.2 | 0.5 | 0.1 |
| sqlalchemy1x_sync_scoped_session | update_heavy | ✅ | 3 | 0.08 | 76.7 | 76.78 | 10000 | 0.2 | 0.2 | 0.5 | 0.1 |
| sqlalchemy1x_sync_scoped_session | update_heavy | ✅ | 4 | 0.12 | 76.78 | 76.91 | 10000 | 0.2 | 0.2 | 0.5 | 0.1 |
| sqlalchemy1x_sync_scoped_session | update_heavy | ✅ | 5 | 0.06 | 76.91 | 76.97 | 10000 | 0.2 | 0.2 | 0.5 | 0.1 |
| sqlalchemy1x_sync_scoped_session | delete_heavy | ✅ | 1 | 0.0 | 76.97 | 76.97 | 10000 | 0.1 | 0.2 | 0.2 | 0.5 |
| sqlalchemy1x_sync_scoped_session | delete_heavy | ✅ | 2 | 0.0 | 76.97 | 76.97 | 10000 | 0.1 | 0.2 | 0.2 | 0.5 |
| sqlalchemy1x_sync_scoped_session | delete_heavy | ✅ | 3 | 0.0 | 76.97 | 76.97 | 10000 | 0.1 | 0.2 | 0.2 | 0.5 |
| sqlalchemy1x_sync_scoped_session | delete_heavy | ✅ | 4 | 0.0 | 76.97 | 76.97 | 10000 | 0.1 | 0.2 | 0.2 | 0.5 |
| sqlalchemy1x_sync_scoped_session | delete_heavy | ✅ | 5 | 0.0 | 76.97 | 76.97 | 10000 | 0.1 | 0.2 | 0.2 | 0.5 |
