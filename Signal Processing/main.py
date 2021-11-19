import numpy as np
import matplotlib.pyplot as plt
import scipy.fft
import sys
from copy import copy
from signal import signal
from visualisation import visualisation
from generator import generator
from sampler import sampler
from reconstructor import reconstructor



f = generator()

def WaveFormAnalysis():
    waveForm = input("Analog signals: Sine, Pulse or Triangular ?\n")

    if waveForm == "Sine":

        v1 = visualisation(title="Analog Signal Analysis", isSubPlot='yes')
        v1.createSubplots(noOfRows=2, noOfColumns=2)

        # Sine wave form visualisation
        sineForm = copy(f.sinWaveFormGenerate(frequency=100, noOfCycle=10, phase=0))
        v1.addToSubplot(sineForm, addToRows=0, addToColumns=0, plotColor='C0', plotTitle= "Sine Signal Visualisation")


        # Sine wave form with noise visualisation
        gaussian1 = copy(f.addNoise(sineForm, noiseType='gaussian', parameter1=0, parameter2=0.1))
        v1.addToSubplot(sineForm, plotColor='C0', plotLabel='S1')
        v1.addToSubplot(sineForm, addToRows=0, addToColumns=1, plotTitle='Sine Signal Visualisation', plotColor='C0')
        v1.addToSubplot(gaussian1, addToRows=0, addToColumns=1, plotTitle='Sine Signal With Noise Visualisation', plotColor='C2')

        # Sampling the analog sine form
        atd = sampler()
        samp = copy(atd.sampleSignal(gaussian1, samplingFrequency=1000))
        v1.addToSubplot(gaussian1, plotType='continuous', addToRows=1, addToColumns=0, plotTitle='Sine Signal With Noise Visualisation', plotColor='C2')
        v1.addToSubplot(samp, plotType='discrete', addToRows=1, addToColumns=0, plotTitle='Discrete Sine Signal', plotColor='C1')

        # Reconstructing the discrete signal
        dac = reconstructor()
        rec = copy(dac.reconstructSignal(samp))
        v1.addToSubplot(gaussian1, addToRows=1, addToColumns=1, plotTitle='Sine Signal With Noise Visualisation', plotColor='C2')
        v1.addToSubplot(samp, plotType='discrete', addToRows=1, addToColumns=1, plotTitle='Discrete Sine Signal', plotColor='C1')
        v1.addToSubplot(rec, addToRows=1, addToColumns=1, plotTitle='Reconstructed Sine Signal', plotColor='C3')


    elif waveForm == "Pulse":

        v1 = visualisation(title="Pulse wave form Analysis", isSubPlot='yes')
        v1.createSubplots(noOfRows=2, noOfColumns=2)

        # Pulse wave form visualisation
        pulseForm = copy(f.pulseWaveFormGenerate(frequency=100, phase=0, noOfCycle=10, dutyCycle=0.5, offset=0, amplitude=1))
        v1.addToSubplot(pulseForm, addToRows=0, addToColumns=0, plotTitle='Pulse Signal Visualisation', plotColor='C0')

        # Pulse wave form with noise visualisation
        gaussian1 = copy(f.addNoise(pulseForm, noiseType='gaussian', parameter1=0, parameter2=0.1))
        v1.addToSubplot(pulseForm, plotColor='C0', plotLabel='S1')
        v1.addToSubplot(pulseForm, addToRows=0, addToColumns=1, plotTitle='Pulse Signal Visualisation', plotColor='C0')
        v1.addToSubplot(gaussian1, addToRows=0, addToColumns=1, plotTitle='Pulse Signal With Noise Visualisation', plotColor='C2')

        # Sampling the analog pulse form
        atd = sampler()
        samp = copy(atd.sampleSignal(gaussian1, samplingFrequency=1000))
        v1.addToSubplot(gaussian1, plotType='continuous', addToRows=1, addToColumns=0, plotTitle='Pulse Signal With Noise Visualisation', plotColor='C2')
        v1.addToSubplot(samp, plotType='discrete', addToRows=1, addToColumns=0, plotTitle='Discrete Pulse Signal', plotColor='C1')

        # Reconstructing the discrete signal
        dac = reconstructor()
        rec = copy(dac.reconstructSignal(samp))
        v1.addToSubplot(gaussian1, addToRows=1, addToColumns=1, plotTitle='Pulse Signal With Noise Visualisation', plotColor='C2')
        v1.addToSubplot(samp, plotType='discrete', addToRows=1, addToColumns=1, plotTitle='Pulse Signal With Noise Visualisation', plotColor='C1')
        v1.addToSubplot(rec, addToRows=1, addToColumns=1, plotTitle='Reconstructed Pulse Signal', plotColor='C3')

    elif waveForm == "Triangular":

        v1 = visualisation(title="Triangular wave form Analysis", isSubPlot='yes')
        v1.createSubplots(noOfRows=2, noOfColumns=2)

        # Triangular wave form visualisation
        triangularForm = copy(f.triangularWaveFormGenerate(frequency=100, phase=0, noOfCycle=10, dutyCycle=0.5, offset=0, amplitude=1))
        v1.addToSubplot(triangularForm, addToRows=0, addToColumns=0, plotTitle='Triangular Signal Visualisation', plotColor='C0')

        # Triangular wave form with noise visualisation
        gaussian1 = copy(f.addNoise(triangularForm, noiseType='gaussian', parameter1=0, parameter2=0.1))
        v1.addToSubplot(triangularForm, plotColor='C0', plotLabel='S1')
        v1.addToSubplot(triangularForm, addToRows=0, addToColumns=1,plotTitle='Triangular Signal Visualisation', plotColor='C0')
        v1.addToSubplot(gaussian1, addToRows=0, addToColumns=1, plotTitle='Triangular Signal With Noise Visualisation', plotColor='C2')

        # Sampling the analog triangular form
        atd = sampler()
        samp = copy(atd.sampleSignal(gaussian1, samplingFrequency=1000))
        v1.addToSubplot(gaussian1, plotType='continuous', addToRows=1, addToColumns=0, plotTitle='Triangular Signal With Noise Visualisation', plotColor='C2')
        v1.addToSubplot(samp, plotType='discrete', addToRows=1, addToColumns=0, plotTitle='Discrete Triangular Signal', plotColor='C1')

        # Reconstructing the discrete signal
        dac = reconstructor()
        rec = copy(dac.reconstructSignal(samp))
        v1.addToSubplot(gaussian1, addToRows=1, addToColumns=1, plotTitle='Triangular Signal With Noise Visualisation', plotColor='C2')
        v1.addToSubplot(samp, plotType='discrete', addToRows=1, addToColumns=1, plotTitle='Discrete Triangular Signal', plotColor='C1')
        v1.addToSubplot(rec, addToRows=1, addToColumns=1, plotTitle='Reconstructed Triangular Signal', plotColor='C3')

    plt.show()


WaveFormAnalysis()

Fs = 100  # Sampling Freq
def DiscreteFourierTransform():

    v1 = visualisation(title="Analog Signal Analysis", isSubPlot='yes')
    v1.createSubplots(noOfRows=2, noOfColumns=2)

    # Sine wave form visualisation
    sineForm = copy(f.sinWaveFormGenerate(frequency=10, noOfCycle=10, phase=0))
    v1.addToSubplot(sineForm, addToRows=0, addToColumns=0, plotColor='C7', plotTitle="Sine Signal Visualisation")

    # Sampling the analog sine form
    atd = sampler()
    samp = copy(atd.sampleSignal(sineForm, samplingFrequency=100))
    v1.addToSubplot(sineForm, plotType='continuous', addToRows=0, addToColumns=1, plotTitle='Sine Signal With Noise Visualisation', plotColor='C0')
    v1.addToSubplot(samp, plotType='discrete', addToRows=0, addToColumns=1, plotTitle='Discrete Sine Signal', plotColor='C7')

    # Discrete Fourier Transform of the Sine form(From Time Domain to Frequency Domain)
    signalLen = len(samp.time)
    fftLen = (int)(pow(2, np.log2(signalLen)) + 1)
    fftPoints = copy(scipy.fft.fft(samp.value, n=fftLen))
    fftnewPoints = fftPoints.astype(int)
    freq = np.linspace(0, Fs, fftLen + 1, endpoint=True)
    fftSignal = signal(freq[np.arange(0, fftLen, 1, dtype=int)], 50 * (abs(fftnewPoints[np.arange(0, fftLen, 1, dtype=int)])))
    v1.addToSubplot(fftSignal, plotType='discrete', addToRows=1, addToColumns=0, plotTitle='Fast Fourier Transform', plotColor='C7', xlabel="Frequency(Hz)", ylabel="FFT values")

    plt.delaxes(v1.addToSubplot(fftSignal, plotType='discrete', addToRows=1, addToColumns=1, plotTitle='Fast Fourier Transform',
                        plotColor='C7', xlabel="Frequency(Hz)", ylabel="FFT values"))
    plt.show()

DiscreteFourierTransform()

sys.exit('Break program here !')