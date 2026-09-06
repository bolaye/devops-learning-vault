# health_monitor.py
import urllib.request
import time
import datetime

TARGET_URL = "https://github.com"
CHECK_INTERVAL = 5 

print(f"🤖 Starting Health Monitor for {TARGET_URL}")
print(f"Logs are being saved to health.log. Press Ctrl+C to stop.\n")

try:
    while True:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        try:
            response = urllib.request.urlopen(TARGET_URL)
            status_code = response.getcode()
            
            if status_code == 200:
                message = f"✅ [{timestamp}] SUCCESS: {TARGET_URL} is UP (Status: {status_code})"
            else:
                message = f"⚠️ [{timestamp}] WARNING: {TARGET_URL} returned status {status_code}"
                
        except Exception as e:
            message = f" [{timestamp}] FAILURE: {TARGET_URL} is DOWN! Error: {e}"
            
        # 1. Print to the screen
        print(message)
        
        # 2. Append to the log file
        with open("health.log", "a", encoding="utf-8") as log_file:
            log_file.write(message + "\n")
            
        time.sleep(CHECK_INTERVAL)

except KeyboardInterrupt:
    print("\n🛑 Health Monitor stopped by user.")