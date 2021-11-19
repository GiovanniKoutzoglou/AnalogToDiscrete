import numpy as np
import matplotlib.pyplot as plt
"""
Visualisation class display waveform in  a figure
"""
class visualisation(object):
    def __init__(self, title="", isFreResponsePlotAlso = 'no', isSubPlot = 'no'):
        if((isSubPlot == 'no') and (isFreResponsePlotAlso == 'no')):
            self.__fig1 = plt.figure(figsize=(10,4))
            self.__axes1 = self.__fig1.add_axes([0.1, 0.1, 0.8, 0.8])
            self.__axes1.set_xlabel('Time(s)')
            self.__axes1.set_ylabel('Amplitude')

        if((isSubPlot == 'no') and (isFreResponsePlotAlso == 'yes')):
            self.__createFrequencyResponseFigure()

    def __createFrequencyResponseFigure(self):
        self.__frequencyResponse = plt.figure(figsize=(10,4))
        plt.title('Frequency Response')
        self.__axesf = self.__frequencyResponse.add_axes([0.1, 0.1, 0.8, 0.8])
        self.__axesf.set_xlabel('Frequency')
        self.__axesf.set_ylabel('Amplitude')
        self.__axesf.grid(which='both', axis='both')
        self.__axesf.margins(0, 0.1)
        self.__xticks = []
        self.__xtickLabels = []

    def addWaveForm(self, signal, plotType = 'continuous', plotColor = 'C1', plotLabel = 'Signal'):
        if plotType == 'continuous':
            self.__axes1.plot(signal.time, signal.value, color = plotColor, label = plotLabel)
        else:
           self.__axes1.stem(signal.time, signal.value, linefmt = plotColor, markerfmt = plotColor+ 'o', basefmt = 'black', label = plotLabel)

        self.__axes1.grid(True)
        self.__fig1.show()

    def addFrequencyResponse(self, w, h, wc, frequencyResponseColor = 'C0', freqView = 'log', ampView = 'log', label = 'frequencyResponse'):
        if (freqView == 'linear' and ampView == 'log'):
            self.__axesf.plot(w, 20 * np.log10(abs(h)), color=frequencyResponseColor, label=label)
        elif (freqView == 'linear' and ampView == 'linear'):
            self.__axesf.plot(w, abs(h), color=frequencyResponseColor, label=label)
        elif (freqView == 'log' and ampView == 'linear'):
            self.__axesf.semilogx(w, abs(h), color=frequencyResponseColor, label=label)
        else:
            self.__axesf.semilogx(w, 20 * np.log10(abs(h)), color=frequencyResponseColor, label=label)

        if (isinstance(wc, list)):
            for wci in wc:
                self.__axesf.axvline(x=wci, color=frequencyResponseColor)
                self.__xticks.append(wci)
                self.__xtickLabels.append(str(round(wci, 2)))
        else:
            self.__axesf.axvline(x=wc, color=frequencyResponseColor)
            self.__xticks.append(wc)
            self.__xtickLabels.append(str(round(wc, 2)))

        self.__axesf.set_xticks(self.__xticks)
        self.__axesf.set_xticklabels(self.__xtickLabels)
        self.__frequencyResponse.legend(loc='best')
        self.__frequencyResponse.show()

    def createSubplots(self, noOfRows = 1, noOfColumns = 1):
        self.__subPlotFig, self.__subPlotAxes = plt.subplots(noOfRows,noOfColumns)
        self.__subPlotFig.subplots_adjust(hspace=0.4)

    def addToSubplot(self, signal, addToRows = 0, addToColumns = 0, plotType = 'continuous', plotColor = 'C0', plotTitle = "Analog Signal", xlabel = "Time", ylabel = "Magnitude", plotLabel='S1'):
        if(plotType == 'continuous'):
            self.__subPlotAxes[addToRows,addToColumns].plot(signal.time, signal.value, color=plotColor)
        else:
            self.__subPlotAxes[addToRows, addToColumns].stem(signal.time, signal.value, linefmt = plotColor, markerfmt = plotColor+ 'o', basefmt = 'black')
        self.__subPlotAxes[addToRows,addToColumns].set_title(plotTitle)
        self.__subPlotAxes[addToRows,addToColumns].set_xlabel(xlabel)
        self.__subPlotAxes[addToRows,addToColumns].set_ylabel(ylabel)