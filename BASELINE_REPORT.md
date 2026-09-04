# API Performance Baseline Report

## 1. Objective

Measure the baseline performance of the seven critical mobile APIs using the same local Django environment.

Metrics:
- Response time
- Database query count
- CPU usage
- Memory usage

## 2. Critical APIs

1. Login — `GET /api/login/`
2. Driver Location — `GET /api/drivers/location/`
3. Nearby Drivers — `GET /api/drivers/nearby/`
4. Create Ride — `GET /api/rides/` (demo benchmark implementation)
5. Ride Details — `GET /api/rides/<id>/`
6. Ride History — `GET /api/rides/history/`
7. Notifications — `GET /api/notifications/`

## 3. Measurement Method

The benchmark:
- sends 20 requests to every endpoint;
- records wall-clock response time in milliseconds;
- uses Django `connection.queries` to count SQL queries;
- uses `psutil` to measure process CPU time and RSS memory change;
- reports average and median response time;
- reports average/max query count.

## 4. Expected Baseline

Run:

```powershell
python manage.py migrate
python seed_data.py
python benchmark.py
```

The terminal prints the actual measurements from the machine where the project is executed.

## 5. Important Note About CPU

CPU usage is environment-dependent. A tiny local request can produce a CPU percentage above 100% because CPU time is divided by a very short wall-clock interval. This is not a production capacity measurement. For a meaningful production baseline, repeat the test under sustained load with a tool such as Locust or k6.

## 6. Baseline Acceptance Criteria

Record the benchmark output and compare future builds against it.

Suggested regression thresholds:
- Response time: investigate if average increases by more than 20%.
- Database queries: investigate any unexpected increase.
- CPU: investigate sustained increases above the baseline.
- Memory: investigate steadily increasing memory usage across repeated requests.

## 7. Result Table

The following table is populated from the output of `benchmark.py`.

| API | Response Time | DB Queries | CPU Usage | Memory Usage |
|---|---:|---:|---:|---:|
| Login | Run benchmark | Run benchmark | Run benchmark | Run benchmark |
| Driver Location | Run benchmark | Run benchmark | Run benchmark | Run benchmark |
| Nearby Drivers | Run benchmark | Run benchmark | Run benchmark | Run benchmark |
| Create Ride | Run benchmark | Run benchmark | Run benchmark | Run benchmark |
| Ride Details | Run benchmark | Run benchmark | Run benchmark | Run benchmark |
| Ride History | Run benchmark | Run benchmark | Run benchmark | Run benchmark |
| Notifications | Run benchmark | Run benchmark | Run benchmark | Run benchmark |

## 8. Conclusion

This project provides a repeatable baseline process for all seven critical APIs. The numbers should be generated on the developer/test machine rather than invented, because response time, CPU and memory depend on the machine and runtime environment.


## 9. Measured Local Baseline

Run `python benchmark.py` after installing requirements. The script records the actual measurements from the execution machine.
