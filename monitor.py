import psutil

def check_system():
    print("CPU:", psutil.cpu_percent(), "%")
    print("Memory:", psutil.virtual_memory().percent, "%")