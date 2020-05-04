#!/bin/python3

from farmcore import SDWire, APCPDU

# power off board
APCPDU('10.103.3.41', 'apc', 'apc', 2).off()

# Load sd card on host
SDWire().to_host()