#!/bin/python3
import os
from farmcore import Hub, Board, SerialConsole, SDWire, APCPDU

SDWire().to_board()

hub = Hub(
     usb_device='1-2'
)

board = Board(
     name='raspberrypi3_fullmetalupdate',
     hub=hub,
     console=SerialConsole(
         port=hub.get_serial('devnode'),
         baud=115200
     ),
     power=APCPDU(os.environ.get("APCPDU_IP_ADD", None), 
          os.environ.get("APCPDU_USERNAME", "apc"),  
          os.environ.get("APCPDU_PASSWORD", "apc"), 
          int(os.environ.get("APCPDU_PORT", 1))),
     bootstr='login:',
     boot_max_s=30
)

board.reboot_and_validate()

