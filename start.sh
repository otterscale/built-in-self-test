#!/bin/bash
timeout=0

if [[ -n $BENCHMARK_ARGS_FIO_RUNTIME ]]; then
        timeout=$(( $BENCHMARK_ARGS_FIO_RUNTIME *2 ))
elif [[ -n $BENCHMARK_ARGS_WARP_DURATION ]]; then
        timeout=86400
else
        exit 1
fi
set -e
timeout $timeout python3 bist.py 

if [[ $? -eq 124 ]]; then
	echo "Error: timeout"
	exit 1
fi