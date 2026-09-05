#!/bin/bash
# A simple network diagnostic script

TARGET="github.com"
REPORT="network_report.txt"

echo "Starting network diagnostics for $TARGET..."
echo "-----------------------------------" > $REPORT

# 1. Check DNS
echo "1. DNS Resolution:" >> $REPORT
nslookup $TARGET >> $REPORT
echo "" >> $REPORT

# 2. Check HTTP Headers and SSL
echo "2. HTTP Headers & SSL Info:" >> $REPORT
curl -sI https://$TARGET >> $REPORT

echo "-----------------------------------" >> $REPORT
echo "Diagnostics complete! Check $REPORT for details."