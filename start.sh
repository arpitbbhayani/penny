#!/bin/bash

source penenv/bin/activate

#
# Execution Phase
#

python run.py $@

#
# Breakdown Phase
#

deactivate
