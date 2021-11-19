import numpy as np
import scipy.signal as scipySignal
from signal import signal
"""
Class reconstructor:
Reconstructs the signal
"""
class reconstructor(object):
    def __init__(self):
        self.reconstructedSignal = signal()
        self.__dataPerSecond = 100000

    def reconstructSignal(self, discreteSignal, connectFilter = 'no', lowPassCutOff = 10000):
        self.__clearStoredSignal()
        noOfDataBetweenConsecutiveSamples = np.floor((discreteSignal.time[1] - discreteSignal.time[0]) * self.__dataPerSecond).astype(int)
        timeInterpolationbase = np.linspace(discreteSignal.time[0], discreteSignal.time[1], noOfDataBetweenConsecutiveSamples, endpoint = False) - discreteSignal.time[0]

        for index in range(len(discreteSignal.value)):
            interpolatedTime = (timeInterpolationbase + discreteSignal.time[index])
            interpolatedValues = discreteSignal.value[index] * (np.ones(noOfDataBetweenConsecutiveSamples, dtype=float))
            self.reconstructedSignal.time = np.append(self.reconstructedSignal.time, interpolatedTime)
            self.reconstructedSignal.value = np.append(self.reconstructedSignal.value, interpolatedValues)
        if(connectFilter == 'yes'):
            self.filterReconstructedSignal(lowPassCutOff)

        return self.reconstructedSignal

    def filterReconstructedSignal(self, lowPassCutoff):
        fc = (lowPassCutoff * 2)/(self.__dataPerSecond)
        b,a = scipySignal.butter(4, fc, btype = 'low', analog = 'False', output = 'ba')
        self.reconstructedSignal.value = scipySignal.filtfilt(b,a, self.reconstructedSignal.value, method= 'pad')

    def __clearStoredSignal(self):
        self.reconstructedSignal.time = []
        self.reconstructedSignal.value = []


