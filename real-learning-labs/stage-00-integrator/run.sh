#!/usr/bin/env bash

export APP_ENV="${APP_ENV:-development}"
python3 "$(dirname "$0")/app.py"
status=$?
echo "run_finished exit_code=$status"
exit "$status"
