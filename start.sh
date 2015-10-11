#!/bin/bash

source jes/bin/activate

#
# Execution Phase
#

python run.py $@

#
# Breakdown Phase
#

deactivate
