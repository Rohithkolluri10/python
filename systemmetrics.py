import psutil
import time

cpu_usage = psutil.cpu_percent(interval=1)
memory_info = psutil.virtual_memory()

print(f"CPU Usage: {cpu_usage}%")
print(f"Memory Usage: {memory_info.percent}%")