#!/bin/python3
import os
from farmcore import SDWire, APCPDU

# power off board
apc = APCPDU(os.environ.get("APCPDU_IP_ADD", None), 
          os.environ.get("APCPDU_USERNAME", "apc"),  
          os.environ.get("APCPDU_PASSWORD", "apc"), 
          int(os.environ.get("APCPDU_PORT", 1)))
apc.off()

# Load sd card on host
SDWire().to_host()