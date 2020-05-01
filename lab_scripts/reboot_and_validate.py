#!/bin/python3

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
     power=APCPDU('10.103.3.41', 'apc', 'apc', 2),
     bootstr='login:',
     boot_max_s=30
)

board.reboot_and_validate()

