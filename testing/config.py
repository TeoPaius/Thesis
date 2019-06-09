inputFilePath = "../input/guitar.wav"
outputFilePath = "../output/guitarNew.wav"
sampleRate = 96000.0  # hertz
noiseLen = 0.01       # seconds
noiseAmplitude = 0.01
detectionThreshold = 40
startOffset = 1       # seconds
startFreqCodingRange = 15000
endFreqCodingRange = 20000
scanWindow = noiseLen
freqGranularity = 256# power of 2
defaultStegoFileDuration = 5 # seconds
freqInterval = int((endFreqCodingRange - startFreqCodingRange) / freqGranularity)
subsampleFactor = 2 #dont change yet