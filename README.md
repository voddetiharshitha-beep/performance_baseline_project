# Django API Performance Baseline

## Windows / PowerShell setup

```powershell
python -m venv venv
venv\Scripts\Activate.ps1
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python seed_data.py
python benchmark.py
```

If PowerShell blocks activation, run:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Then activate the environment again.

## APIs

- `/api/login/`
- `/api/drivers/location/`
- `/api/drivers/nearby/`
- `/api/rides/`
- `/api/rides/1/`
- `/api/rides/history/`
- `/api/notifications/`

## What the benchmark measures

- Average and median response time
- Average and maximum database query count
- Process CPU usage
- Process RSS memory change

The report is in `BASELINE_REPORT.md`.
