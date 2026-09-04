import os, time, statistics, subprocess, sys, psutil, urllib.request
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "performance_baseline.settings")
import django
django.setup()
from django.test import Client
from django.db import connection, reset_queries

ENDPOINTS = [
    ("Login", "/api/login/?username=demo"),
    ("Driver Location", "/api/drivers/location/?driver_id=1"),
    ("Nearby Drivers", "/api/drivers/nearby/"),
    ("Create Ride", "/api/rides/"),
    ("Ride Details", "/api/rides/1/"),
    ("Ride History", "/api/rides/history/"),
    ("Notifications", "/api/notifications/"),
]

client = Client()
process = psutil.Process(os.getpid())
rows = []
for name, path in ENDPOINTS:
    times, queries, mems, cpus = [], [], [], []
    for _ in range(20):
        reset_queries()
        mem_before = process.memory_info().rss
        cpu_before = process.cpu_times()
        t0 = time.perf_counter()
        response = client.get(path)
        elapsed = (time.perf_counter() - t0) * 1000
        cpu_after = process.cpu_times()
        mem_after = process.memory_info().rss
        times.append(elapsed)
        queries.append(len(connection.queries))
        mems.append(max(0, mem_after - mem_before) / (1024*1024))
        cpu = ((cpu_after.user + cpu_after.system) - (cpu_before.user + cpu_before.system))
        cpus.append(cpu / max(elapsed/1000, 0.000001) * 100)
    rows.append((name, path, response.status_code, statistics.mean(times), statistics.median(times),
                 statistics.mean(queries), max(queries), statistics.mean(cpus), statistics.mean(mems)))

print("\nPERFORMANCE BASELINE")
print("="*120)
print(f"{'API':22} {'Status':7} {'Avg ms':10} {'Median ms':12} {'Avg Queries':13} {'Max Q':8} {'CPU %*':10} {'Mem Δ MB':10}")
for r in rows:
    print(f"{r[0]:22} {r[2]:7} {r[3]:10.2f} {r[4]:12.2f} {r[5]:13.2f} {r[6]:8} {r[7]:10.2f} {r[8]:10.3f}")
print("\n* CPU% is process CPU time divided by request wall time. Because local requests are very short, CPU% can exceed 100%; use longer load tests for production capacity.")
