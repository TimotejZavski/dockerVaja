#!/bin/bash

output=$(python3 run.py)

echo "$output" | grep "zagon python aplikacije" || exit 1
echo "$output" | grep "konec" || exit 1

echo "TEST OK"
