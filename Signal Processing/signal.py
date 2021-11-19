"""
*******************************************
Signal Defination
Class: signal
variables: time, value
time is in seconds and value in Volts.
*******************************************
"""
class signal(object):
    def __init__(self, time=[], value=[]):
        self.time = time
        self.value = value