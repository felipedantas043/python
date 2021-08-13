from ppadb.device import Device
from teste_scrcpy import connectAdb

device, client = connectAdb.connect()
device.shell("input keyevent 27")