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
