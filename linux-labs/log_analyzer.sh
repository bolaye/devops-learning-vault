#!/bin/bash
# A script to analyze web server logs

LOG_DIR="web-server-logs"
ERROR_COUNT=$(grep -c "ERROR" "$LOG_DIR/error.log")

echo "--- Log Analysis Report ---"
echo "Checking logs in: $LOG_DIR"
   
if [ "$ERROR_COUNT" -gt 0 ]; then
    echo "️ WARNING: Found $ERROR_COUNT errors in the error log!"
    echo "Here are the errors:"
    grep "ERROR" "$LOG_DIR/error.log"
else
    echo "✅ No errors found. System is healthy."
fi
   
echo "---------------------------"