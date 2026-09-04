# system_check.py
# A simple DevOps script to check basic system information

import platform
import datetime

# 1. Variables and Strings
script_name = "System Health Checker"
author = "bolaye" # Put your name here!

# 2. Printing to the console
print(f"--- Running: {script_name} ---")
print(f"Author: {author}")
print(f"Time: {datetime.datetime.now()}")
print("-" * 30)

# 3. Using a built-in library to get system data
os_name = platform.system()
os_version = platform.release()
python_version = platform.python_version()

print(f"Operating System: {os_name} {os_version}")
print(f"Python Version: {python_version}")

# 4. Basic Conditional Logic (if/else)
if os_name == "Windows":
    print("Note: You are running this on a Windows machine.")
elif os_name == "Linux":
    print("Note: You are running this on a Linux machine. Great for DevOps!")
else:
    print(f"Note: You are running this on {os_name}.")

print("-" * 30)
print("Phase 2: Processing Infrastructure & Error Handling")
print("-" * 30)

# 5. Lists and Loops (Core DevOps: iterating over infrastructure)
servers = ["web-server-01", "db-server-02", "cache-server-03"]
print(f"Found {len(servers)} servers to check:")

for server in servers:
    print(f"  -> Checking {server}... Status: OK")

# 6. Error Handling (try/except)
# DevOps Reality: Files go missing, permissions fail. We must handle this gracefully!
config_file = "server_config.txt"

print(f"\nAttempting to read {config_file}...")
try:
    with open(config_file, "r") as file:
        content = file.read()
        print("Success! File content:", content)
except FileNotFoundError:
    print(f"⚠️ WARNING: {config_file} not found! Falling back to default settings.")
except Exception as e:
    print(f"❌ An unexpected error occurred: {e}")

print("-" * 30)
print("Script execution finished gracefully!")