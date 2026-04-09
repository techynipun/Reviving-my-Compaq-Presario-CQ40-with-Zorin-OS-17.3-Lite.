import psutil
import time

def get_battery():
    battery = psutil.sensors_battery()
    if battery:
        status = "Charging" if battery.power_plugged else "Discharging"
        return f"{battery.percent}% ({status})"
    return "No battery info"

while True:
    cpu_percent = psutil.cpu_percent(interval=1)
    
    ram = psutil.virtual_memory()
    ram_percent = ram.percent
    ram_used = ram.used / (1024 ** 3)
    ram_total = ram.total / (1024 ** 3)

    battery_info = get_battery()

    print("=" * 40)
    print(f"CPU Usage: {cpu_percent}%")
    print(f"RAM Usage: {ram_percent:.1f}% ({ram_used:.2f}GB / {ram_total:.2f}GB)")
    print(f"Battery: {battery_info}")
    print("=" * 40)
    
    time.sleep(5)
