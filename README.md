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
| sqlalchemy1x_async_scoped_session | 1000000_operations | ✅ | 1 | 27.86 | 42.92 | 70.78 | 1000000 | 0.25 | 0.25 | 0.25 | 0.25 |
| sqlalchemy1x_async_scoped_session | 1000000_operations | ✅ | 2 | 1.69 | 70.95 | 72.64 | 1000000 | 0.25 | 0.25 | 0.25 | 0.25 |
| sqlalchemy1x_async_scoped_session | 1000000_operations | ✅ | 3 | 0.16 | 72.81 | 72.97 | 1000000 | 0.25 | 0.25 | 0.25 | 0.25 |
| sqlalchemy1x_async_scoped_session | 1000000_operations | ✅ | 4 | 2.53 | 72.97 | 75.5 | 1000000 | 0.25 | 0.25 | 0.25 | 0.25 |
| sqlalchemy1x_async_scoped_session | 1000000_operations | ✅ | 5 | -0.05 | 75.5 | 75.45 | 1000000 | 0.25 | 0.25 | 0.25 | 0.25 |
| sqlalchemy1x_async_scoped_session | create_heavy | ✅ | 1 | 0.08 | 75.45 | 75.53 | 10000 | 0.5 | 0.2 | 0.2 | 0.1 |
| sqlalchemy1x_async_scoped_session | create_heavy | ✅ | 2 | 0.02 | 75.53 | 75.55 | 10000 | 0.5 | 0.2 | 0.2 | 0.1 |
| sqlalchemy1x_async_scoped_session | create_heavy | ✅ | 3 | 0.0 | 75.55 | 75.55 | 10000 | 0.5 | 0.2 | 0.2 | 0.1 |
| sqlalchemy1x_async_scoped_session | create_heavy | ✅ | 4 | 0.02 | 75.55 | 75.56 | 10000 | 0.5 | 0.2 | 0.2 | 0.1 |
| sqlalchemy1x_async_scoped_session | create_heavy | ✅ | 5 | 0.0 | 75.56 | 75.56 | 10000 | 0.5 | 0.2 | 0.2 | 0.1 |
| sqlalchemy1x_async_scoped_session | read_heavy | ✅ | 1 | 0.0 | 75.56 | 75.56 | 10000 | 0.1 | 0.6 | 0.2 | 0.1 |
| sqlalchemy1x_async_scoped_session | read_heavy | ✅ | 2 | 0.0 | 75.56 | 75.56 | 10000 | 0.1 | 0.6 | 0.2 | 0.1 |
| sqlalchemy1x_async_scoped_session | read_heavy | ✅ | 3 | 0.03 | 75.56 | 75.59 | 10000 | 0.1 | 0.6 | 0.2 | 0.1 |
| sqlalchemy1x_async_scoped_session | read_heavy | ✅ | 4 | 0.06 | 75.59 | 75.66 | 10000 | 0.1 | 0.6 | 0.2 | 0.1 |
| sqlalchemy1x_async_scoped_session | read_heavy | ✅ | 5 | 0.0 | 75.66 | 75.66 | 10000 | 0.1 | 0.6 | 0.2 | 0.1 |
| sqlalchemy1x_async_scoped_session | update_heavy | ✅ | 1 | 0.02 | 75.66 | 75.67 | 10000 | 0.2 | 0.2 | 0.5 | 0.1 |
| sqlalchemy1x_async_scoped_session | update_heavy | ✅ | 2 | 0.0 | 75.67 | 75.67 | 10000 | 0.2 | 0.2 | 0.5 | 0.1 |
| sqlalchemy1x_async_scoped_session | update_heavy | ✅ | 3 | 0.0 | 75.67 | 75.67 | 10000 | 0.2 | 0.2 | 0.5 | 0.1 |
| sqlalchemy1x_async_scoped_session | update_heavy | ✅ | 4 | 0.02 | 75.67 | 75.69 | 10000 | 0.2 | 0.2 | 0.5 | 0.1 |
| sqlalchemy1x_async_scoped_session | update_heavy | ✅ | 5 | 0.02 | 75.69 | 75.7 | 10000 | 0.2 | 0.2 | 0.5 | 0.1 |
| sqlalchemy1x_async_scoped_session | delete_heavy | ✅ | 1 | 0.0 | 75.7 | 75.7 | 10000 | 0.1 | 0.2 | 0.2 | 0.5 |
| sqlalchemy1x_async_scoped_session | delete_heavy | ✅ | 2 | 0.0 | 75.7 | 75.7 | 10000 | 0.1 | 0.2 | 0.2 | 0.5 |
| sqlalchemy1x_async_scoped_session | delete_heavy | ✅ | 3 | 0.02 | 75.7 | 75.72 | 10000 | 0.1 | 0.2 | 0.2 | 0.5 |
| sqlalchemy1x_async_scoped_session | delete_heavy | ✅ | 4 | 0.0 | 75.72 | 75.72 | 10000 | 0.1 | 0.2 | 0.2 | 0.5 |
| sqlalchemy1x_async_scoped_session | delete_heavy | ✅ | 5 | 0.39 | 75.72 | 76.11 | 10000 | 0.1 | 0.2 | 0.2 | 0.5 |
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
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| sqlalchemy2x_async_session | 10000_operations | ✅ | 1 | 13.62 | 46.2 | 59.83 | 10000 | 0.25 | 0.25 | 0.25 | 0.25 |
| sqlalchemy2x_async_session | 10000_operations | ✅ | 2 | 2.34 | 59.8 | 62.14 | 10000 | 0.25 | 0.25 | 0.25 | 0.25 |
| sqlalchemy2x_async_session | 10000_operations | ✅ | 3 | 1.61 | 62.09 | 63.7 | 10000 | 0.25 | 0.25 | 0.25 | 0.25 |
| sqlalchemy2x_async_session | 10000_operations | ✅ | 4 | 2.41 | 63.7 | 66.11 | 10000 | 0.25 | 0.25 | 0.25 | 0.25 |
| sqlalchemy2x_async_session | 10000_operations | ✅ | 5 | 2.08 | 66.11 | 68.19 | 10000 | 0.25 | 0.25 | 0.25 | 0.25 |
| sqlalchemy2x_async_session | 100000_operations | ✅ | 1 | 5.64 | 68.19 | 73.83 | 100000 | 0.25 | 0.25 | 0.25 | 0.25 |
| sqlalchemy2x_async_session | 100000_operations | ✅ | 2 | 0.02 | 73.83 | 73.84 | 100000 | 0.25 | 0.25 | 0.25 | 0.25 |
| sqlalchemy2x_async_session | 100000_operations | ✅ | 3 | -3.98 | 73.84 | 69.86 | 100000 | 0.25 | 0.25 | 0.25 | 0.25 |
| sqlalchemy2x_async_session | 100000_operations | ✅ | 4 | 0.06 | 69.86 | 69.92 | 100000 | 0.25 | 0.25 | 0.25 | 0.25 |
| sqlalchemy2x_async_session | 100000_operations | ✅ | 5 | 0.03 | 69.88 | 69.91 | 100000 | 0.25 | 0.25 | 0.25 | 0.25 |
| sqlalchemy2x_async_session | create_heavy | ✅ | 1 | 0.02 | 69.91 | 69.92 | 10000 | 0.5 | 0.2 | 0.2 | 0.1 |
| sqlalchemy2x_async_session | create_heavy | ✅ | 2 | 0.09 | 69.92 | 70.02 | 10000 | 0.5 | 0.2 | 0.2 | 0.1 |
| sqlalchemy2x_async_session | create_heavy | ✅ | 3 | 0.08 | 70.02 | 70.09 | 10000 | 0.5 | 0.2 | 0.2 | 0.1 |
| sqlalchemy2x_async_session | create_heavy | ✅ | 4 | 0.08 | 70.09 | 70.17 | 10000 | 0.5 | 0.2 | 0.2 | 0.1 |
| sqlalchemy2x_async_session | create_heavy | ✅ | 5 | 0.09 | 70.12 | 70.22 | 10000 | 0.5 | 0.2 | 0.2 | 0.1 |
| sqlalchemy2x_async_session | read_heavy | ✅ | 1 | 0.12 | 70.22 | 70.34 | 10000 | 0.1 | 0.6 | 0.2 | 0.1 |
| sqlalchemy2x_async_session | read_heavy | ✅ | 2 | 0.73 | 70.3 | 71.03 | 10000 | 0.1 | 0.6 | 0.2 | 0.1 |
| sqlalchemy2x_async_session | read_heavy | ✅ | 3 | 0.03 | 70.98 | 71.02 | 10000 | 0.1 | 0.6 | 0.2 | 0.1 |
| sqlalchemy2x_async_session | read_heavy | ✅ | 4 | 0.27 | 70.97 | 71.23 | 10000 | 0.1 | 0.6 | 0.2 | 0.1 |
| sqlalchemy2x_async_session | read_heavy | ✅ | 5 | 0.12 | 71.19 | 71.31 | 10000 | 0.1 | 0.6 | 0.2 | 0.1 |
| sqlalchemy2x_async_session | update_heavy | ✅ | 1 | 0.06 | 71.27 | 71.33 | 10000 | 0.2 | 0.2 | 0.5 | 0.1 |
| sqlalchemy2x_async_session | update_heavy | ✅ | 2 | 0.14 | 71.28 | 71.42 | 10000 | 0.2 | 0.2 | 0.5 | 0.1 |
| sqlalchemy2x_async_session | update_heavy | ✅ | 3 | 0.06 | 71.42 | 71.48 | 10000 | 0.2 | 0.2 | 0.5 | 0.1 |
| sqlalchemy2x_async_session | update_heavy | ✅ | 4 | 0.03 | 71.44 | 71.47 | 10000 | 0.2 | 0.2 | 0.5 | 0.1 |
| sqlalchemy2x_async_session | update_heavy | ✅ | 5 | 0.11 | 71.47 | 71.58 | 10000 | 0.2 | 0.2 | 0.5 | 0.1 |
| sqlalchemy2x_async_session | delete_heavy | ✅ | 1 | 0.0 | 71.58 | 71.58 | 10000 | 0.1 | 0.2 | 0.2 | 0.5 |
| sqlalchemy2x_async_session | delete_heavy | ✅ | 2 | 0.05 | 71.58 | 71.62 | 10000 | 0.1 | 0.2 | 0.2 | 0.5 |
| sqlalchemy2x_async_session | delete_heavy | ✅ | 3 | 0.0 | 71.58 | 71.58 | 10000 | 0.1 | 0.2 | 0.2 | 0.5 |
| sqlalchemy2x_async_session | delete_heavy | ✅ | 4 | 0.03 | 71.58 | 71.61 | 10000 | 0.1 | 0.2 | 0.2 | 0.5 |
| sqlalchemy2x_async_session | delete_heavy | ✅ | 5 | 0.16 | 71.61 | 71.77 | 10000 | 0.1 | 0.2 | 0.2 | 0.5 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| sqlalchemy2x_sync_session | 10000_operations | ✅ | 1 | 4.81 | 45.39 | 50.2 | 10000 | 0.25 | 0.25 | 0.25 | 0.25 |
| sqlalchemy2x_sync_session | 10000_operations | ✅ | 2 | 2.41 | 50.28 | 52.69 | 10000 | 0.25 | 0.25 | 0.25 | 0.25 |
| sqlalchemy2x_sync_session | 10000_operations | ✅ | 3 | 2.19 | 52.75 | 54.94 | 10000 | 0.25 | 0.25 | 0.25 | 0.25 |
| sqlalchemy2x_sync_session | 10000_operations | ✅ | 4 | 0.84 | 54.94 | 55.78 | 10000 | 0.25 | 0.25 | 0.25 | 0.25 |
| sqlalchemy2x_sync_session | 10000_operations | ✅ | 5 | 0.2 | 55.84 | 56.05 | 10000 | 0.25 | 0.25 | 0.25 | 0.25 |
| sqlalchemy2x_sync_session | 100000_operations | ✅ | 1 | 1.28 | 56.05 | 57.33 | 100000 | 0.25 | 0.25 | 0.25 | 0.25 |
| sqlalchemy2x_sync_session | 100000_operations | ✅ | 2 | 2.41 | 57.33 | 59.73 | 100000 | 0.25 | 0.25 | 0.25 | 0.25 |
| sqlalchemy2x_sync_session | 100000_operations | ✅ | 3 | 2.31 | 59.8 | 62.11 | 100000 | 0.25 | 0.25 | 0.25 | 0.25 |
| sqlalchemy2x_sync_session | 100000_operations | ✅ | 4 | 0.73 | 62.11 | 62.84 | 100000 | 0.25 | 0.25 | 0.25 | 0.25 |
| sqlalchemy2x_sync_session | 100000_operations | ✅ | 5 | 0.8 | 62.84 | 63.64 | 100000 | 0.25 | 0.25 | 0.25 | 0.25 |
| sqlalchemy2x_sync_session | create_heavy | ✅ | 1 | 0.05 | 63.64 | 63.69 | 10000 | 0.5 | 0.2 | 0.2 | 0.1 |
| sqlalchemy2x_sync_session | create_heavy | ✅ | 2 | 2.3 | 63.75 | 66.05 | 10000 | 0.5 | 0.2 | 0.2 | 0.1 |
| sqlalchemy2x_sync_session | create_heavy | ✅ | 3 | 0.02 | 66.05 | 66.06 | 10000 | 0.5 | 0.2 | 0.2 | 0.1 |
| sqlalchemy2x_sync_session | create_heavy | ✅ | 4 | 1.77 | 66.06 | 67.83 | 10000 | 0.5 | 0.2 | 0.2 | 0.1 |
| sqlalchemy2x_sync_session | create_heavy | ✅ | 5 | 0.31 | 67.83 | 68.14 | 10000 | 0.5 | 0.2 | 0.2 | 0.1 |
| sqlalchemy2x_sync_session | read_heavy | ✅ | 1 | 0.06 | 68.14 | 68.2 | 10000 | 0.1 | 0.6 | 0.2 | 0.1 |
| sqlalchemy2x_sync_session | read_heavy | ✅ | 2 | 0.0 | 68.2 | 68.2 | 10000 | 0.1 | 0.6 | 0.2 | 0.1 |
| sqlalchemy2x_sync_session | read_heavy | ✅ | 3 | 0.03 | 68.2 | 68.23 | 10000 | 0.1 | 0.6 | 0.2 | 0.1 |
| sqlalchemy2x_sync_session | read_heavy | ✅ | 4 | 0.0 | 68.23 | 68.23 | 10000 | 0.1 | 0.6 | 0.2 | 0.1 |
| sqlalchemy2x_sync_session | read_heavy | ✅ | 5 | 0.62 | 68.3 | 68.92 | 10000 | 0.1 | 0.6 | 0.2 | 0.1 |
| sqlalchemy2x_sync_session | update_heavy | ✅ | 1 | 0.14 | 68.92 | 69.06 | 10000 | 0.2 | 0.2 | 0.5 | 0.1 |
| sqlalchemy2x_sync_session | update_heavy | ✅ | 2 | 1.59 | 69.06 | 70.66 | 10000 | 0.2 | 0.2 | 0.5 | 0.1 |
| sqlalchemy2x_sync_session | update_heavy | ✅ | 3 | 1.89 | 70.66 | 72.55 | 10000 | 0.2 | 0.2 | 0.5 | 0.1 |
| sqlalchemy2x_sync_session | update_heavy | ✅ | 4 | 0.34 | 72.55 | 72.89 | 10000 | 0.2 | 0.2 | 0.5 | 0.1 |
| sqlalchemy2x_sync_session | update_heavy | ✅ | 5 | 0.0 | 72.89 | 72.89 | 10000 | 0.2 | 0.2 | 0.5 | 0.1 |
| sqlalchemy2x_sync_session | delete_heavy | ✅ | 1 | 0.0 | 72.89 | 72.89 | 10000 | 0.1 | 0.2 | 0.2 | 0.5 |
| sqlalchemy2x_sync_session | delete_heavy | ✅ | 2 | 1.36 | 72.89 | 74.25 | 10000 | 0.1 | 0.2 | 0.2 | 0.5 |
| sqlalchemy2x_sync_session | delete_heavy | ✅ | 3 | 0.03 | 74.25 | 74.28 | 10000 | 0.1 | 0.2 | 0.2 | 0.5 |
| sqlalchemy2x_sync_session | delete_heavy | ✅ | 4 | 1.7 | 74.28 | 75.98 | 10000 | 0.1 | 0.2 | 0.2 | 0.5 |
| sqlalchemy2x_sync_session | delete_heavy | ✅ | 5 | 0.03 | 75.98 | 76.02 | 10000 | 0.1 | 0.2 | 0.2 | 0.5 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |