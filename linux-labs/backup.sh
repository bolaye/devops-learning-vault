#!/bin/bash
# A simple backup script

echo "Starting backup process..."
echo "Compressing web-server-logs..."
tar -czf backup.tar.gz web-server-logs/
echo "Backup completed successfully!"