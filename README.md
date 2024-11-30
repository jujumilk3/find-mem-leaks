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

| Stack | Method | Iter | Diff | Initial | Final | Ops | C | R | U | D |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| sqlalchemy1x | result_10000_operations | 1 | 18.73 | 36.84 | 55.57 | 10000 | 0.25 | 0.25 | 0.25 | 0.25 |
| sqlalchemy1x | result_10000_operations | 2 | 0.5 | 55.63 | 56.13 | 10000 | 0.25 | 0.25 | 0.25 | 0.25 |
| sqlalchemy1x | result_10000_operations | 3 | 4.22 | 56.11 | 60.33 | 10000 | 0.25 | 0.25 | 0.25 | 0.25 |
| sqlalchemy1x | result_10000_operations | 4 | -1.14 | 60.31 | 59.17 | 10000 | 0.25 | 0.25 | 0.25 | 0.25 |
| sqlalchemy1x | result_10000_operations | 5 | 0.3 | 59.2 | 59.5 | 10000 | 0.25 | 0.25 | 0.25 | 0.25 |
| sqlalchemy1x | result_10000_operations | 6 | 0.05 | 59.48 | 59.54 | 10000 | 0.25 | 0.25 | 0.25 | 0.25 |
| sqlalchemy1x | result_10000_operations | 7 | -0.5 | 59.52 | 59.02 | 10000 | 0.25 | 0.25 | 0.25 | 0.25 |
| sqlalchemy1x | result_10000_operations | 8 | -1.06 | 59.0 | 57.93 | 10000 | 0.25 | 0.25 | 0.25 | 0.25 |
| sqlalchemy1x | result_10000_operations | 9 | -0.4 | 57.96 | 57.56 | 10000 | 0.25 | 0.25 | 0.25 | 0.25 |
| sqlalchemy1x | result_10000_operations | 10 | 1.1 | 57.54 | 58.64 | 10000 | 0.25 | 0.25 | 0.25 | 0.25 |