import numpy as np
from signal import signal
""""
class sampler
sample given signal at given sampling frequency
"""


class sampler(object):
    def __init__(self):
        self.sampledSignal = signal()

    def sampleSignal(self, signal, samplingFrequency=1000):
        signalDuration = signal.time[-1] - signal.time[0]
        signalLength = len(signal.time)
        samplingIndexPeriod = np.floor(signalLength / (signalDuration * samplingFrequency)).astype(int)
        sampledDataIndex = np.arange(0, signalLength, samplingIndexPeriod, dtype=int)

        self.sampledSignal.time = signal.time[sampledDataIndex]
        self.sampledSignal.value = signal.value[sampledDataIndex]

        return self.sampledSignal
