import numpy as np
from tkinter import *
import matplotlib.pyplot as plt
from myMath import myWave
from scipy.fftpack import fft as fftScy
from testing.config import *

refAmplitude = 0.00001

def timeToFrequency(samples, sRate, timeLen, offset):
    Fs = sRate # sampling rate
    Ts = 1 / Fs  # sampling interval


    t = np.array([i + offset for i in np.arange(0,timeLen, Ts)])  # time vector

    n = timeLen*sRate  # length of the signal
    k = np.arange(n)
    T = n / Fs
    frq = k / T  # two sides frequency range
    frq = frq[range(int(n / 2))]  # one side frequency range

    Y = np.fft.fft(samples) / n  # fft computing and normalization
    Y = abs(Y[range(int(n / 2))]*2)
    #
    # fig = plt.figure(num=None, figsize=(8, 6), dpi=80, facecolor='w', edgecolor='k')
    # ax = []
    # ax.append(fig.add_subplot(2, 1, 1))
    # ax.append(fig.add_subplot(2, 1, 2))
    # fig.set_dpi(100)
    # ax[0].plot(t, samples[:int(timeLen*sRate)])
    # ax[0].set_xlabel('Time')
    # ax[0].set_ylabel('Amplitude')
    freqValues = [max(i, 0) for i in 20*np.log10(Y/refAmplitude)]
    # ax[1].plot(frq, freqValues, 'r')  # plotting the spectrum
    # ax[1].set_xlabel('Freq (Hz)')
    # ax[1].set_ylabel('dB')

    # plt.grid()
    # plt.show()

    return (frq, freqValues, (t, samples[:int(timeLen*sRate)], frq, freqValues))


def timeToFreq(samples, sRate, timeLen):
    N = len(samples)

    T = 1.0 / sRate
    x = np.linspace(0.0, N * T, N)
    y = samples
    yf = np.fft.fft(y)
    xf = np.linspace(0.0, 1.0 / (2.0 * T), N // 2)
    plt.plot(xf, 2.0 / N * np.abs(yf[0:N // 2]))

    plt.grid()
    plt.show()

def detectFrequencyes(freqDomain, frqValues, targetRange=None):
    start = -1
    end = 999999
    result = []
    interval = freqDomain[1] - freqDomain[0]
    for i in range(0, len(freqDomain)):
        if freqDomain[i] > startFreqCodingRange:
            start = i - 1
            break
    for i in range(int(startFreqCodingRange), int(endFreqCodingRange), freqInterval * 16):
        approxDown = int(int(i) / interval) * interval
        approxUp = int(int(i) / interval + 1) * interval
        if (approxUp + approxDown) / 2 > int(i):
            approx = approxDown
        else:
            approx = approxUp
        idx = np.where(freqDomain == approx)[0][0]
        value = frqValues[idx]
        if value > detectionThreshold:
            result.append((i,value))
    return result
#
# y = myWave.generateSineWave(48000,3,0.5,10000)
# timeToFrequency(y,48000,3)