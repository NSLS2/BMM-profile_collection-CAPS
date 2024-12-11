from ophyd.epics_motor import EpicsMotor
from ophyd.device import Device, Component as Cpt

class Goiniometer(Device):
    tth = Cpt(EpicsMotor, '-Ax:VTTH}Mtr')
    th = Cpt(EpicsMotor, '-Ax:VTH}Mtr')

goinio = Goiniometer('XF:06BM-ES{SixC', name='goinio')