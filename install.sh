#!/bin/bash

#
# Setup Phase
#

echo "[SHELL] Setting up the execution environment"

if [ ! -d ./penenv ]; then
    echo "[SHELL] Setting up new virtual environment"
    virtualenv --clear penenv
fi

source penenv/bin/activate

echo "[SHELL] Installing required python packages"
pip install -r requirements.txt

python init.py

deactivate
