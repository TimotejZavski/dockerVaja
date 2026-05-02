#!/bin/bash

output=$(python3 run.py)

echo "$output" | grep "zagon python aplikacije" || exit 1
echo "$output" | grep "odkrivam znanstveno fantastiko" || exit 1
echo "$output" | grep "Korak 1" || exit 1
echo "$output" | grep "Korak 2" || exit 1
echo "$output" | grep "Korak 3" || exit 1
echo "$output" | grep "konec :(" || exit 1
echo "$output" | grep "lalalalalal" || exit 1

echo "TEST OK"