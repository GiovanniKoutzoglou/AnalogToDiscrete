import numpy as np
from signal import signal
"""
Function generator class, which generates some predefined functions for
specific duration.
frequency: frequency in Hz
amplitude: amplitude in V
offset: offset in volt
phase: phase in degree
numberOfCycle: number of cycle to generate
"""
class generator(object):
    def __init__(self,dataPerCycle=100):
        self.__dataPerCycle = dataPerCycle
        self.signal = signal()

    def __clearStoreSignal(self):
        self.signal.time = []
        self.signal.value = []

    def __phaseShifter(self, frequency = 50, phase = 0):
        self.numberOfShiftPoint = np.floor((phase/360) * (self.__dataPerCycle)).astype(int)
        self.signal.value = np.roll(self.signal.value, -1*self.numberOfShiftPoint)

    def sinWaveFormGenerate(self, frequency = 50, amplitude = 1, phase = 0, offset = 0, noOfCycle = 10):
        self.__clearStoreSignal()
        duration = noOfCycle/frequency
        self.signal.time = np.linspace(0, duration, num = np.floor(self.__dataPerCycle * noOfCycle).astype(int), endpoint = True, dtype = float)
        self.signal.value = amplitude * (np.sin((2 * np.pi * frequency)*self.signal.time, dtype = float)) + offset
        self.__phaseShifter(frequency, phase)

        return self.signal

    def pulseWaveFormGenerate(self, frequency = 50, amplitude = 1, dutyCycle = 0.5, phase = 0, offset = 0, noOfCycle = 10):
        self.__clearStoreSignal()
        duration = noOfCycle/frequency
        self.signal.time = np.linspace(0, duration, num = np.floor(self.__dataPerCycle * noOfCycle).astype(int), endpoint = True, dtype = float)
        primeLength = self.__dataPerCycle
        onLength = np.floor(primeLength * dutyCycle).astype(int)
        primeSignal = np.append(np.ones(onLength), -1 * np.ones(primeLength - onLength))
        self.signal.value = amplitude * (np.tile(primeSignal, noOfCycle)) + offset
        self.__phaseShifter(frequency, phase)

        return self.signal

    def triangularWaveFormGenerate(self, frequency = 50, amplitude = 1, dutyCycle = 0.5, phase = 0, offset = 0, noOfCycle = 10):
        self.__clearStoreSignal()
        duration = noOfCycle / frequency
        self.signal.time = np.linspace(0, duration, num = np.floor(self.__dataPerCycle * noOfCycle).astype(int), endpoint = True, dtype = float)
        primeLength = self.__dataPerCycle
        onLength = np.floor(primeLength * dutyCycle).astype(int)
        primeSignal = np.append(np.linspace(-1, 1, onLength, endpoint=False), np.linspace(1, -1, (primeLength - onLength), endpoint=False))
        self.signal.value = amplitude * (np.tile(primeSignal, noOfCycle)) + offset
        self.__phaseShifter(frequency, phase)

        return self.signal

    def addNoise(self, signal, noiseType = 'Gaussian', parameter1 = 0, parameter2 = 1):
        self.__clearStoreSignal()
        self.signal.time = signal.time
        if(noiseType == 'Uniform'):
            self.signal.value = signal.value + np.random.uniform(low = parameter1, hign = parameter2, size = len(signal.value))
        else:
            self.signal.value = signal.value + np.random.normal(loc = parameter1, scale = parameter2, size = len(signal.value))

        return self.signal
