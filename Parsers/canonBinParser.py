import struct
import numpy as np
from Utils.parserTools import scanConvert, iqToRf
# from scipy.signal import hilbert


def readIQ(filename):
    headersize = 16

    file_obj = open(filename, 'rb')
    hdr = [int.from_bytes(file_obj.read(2), byteorder='little', signed=False) for i in range(2)]
    numAcquiredRxBeams = hdr[0]

    hdr = [int.from_bytes(file_obj.read(2), byteorder='little', signed=False) for i in range(2)]
    numParallelAcquisitions = hdr[1]

    hdr = [int.from_bytes(file_obj.read(2), byteorder='little', signed=False) for i in range(2)]
    numSamplesDrOut = hdr[0]
    numSamplesRbfOut = hdr[1]

    hdr = [int.from_bytes(file_obj.read(1), byteorder='little', signed=False) for i in range(4)]
    isPhaseInvertEn = hdr[0]

    hdr = [struct.unpack('f', file_obj.read(4))[0] for i in range(5)]
    decimationFactor = hdr[0]
    rbfDecimationFactor = hdr[1]
    rbfBeMixerFrequency = hdr[2]
    propagationVelCmPerSec = hdr[3]
    digitizingRateHz = hdr[4] 

    # read IQ data
    file_obj.seek(0)
    numSamplesIQAcq = numSamplesDrOut*2
    dataA = np.zeros((numSamplesDrOut*2, numAcquiredRxBeams))
    dataB = np.zeros((numSamplesDrOut*2, numAcquiredRxBeams))
    allData = np.zeros((numSamplesDrOut*2, numAcquiredRxBeams*(1+isPhaseInvertEn)))

    # IQ Acquisition, following parameter always zero
    isPhaseInvertEn = 0
    isRxFreqCompoundEn = 0
    isDiffplusEn = 0

    for ii in range(int(numAcquiredRxBeams/numParallelAcquisitions)):
        for jj in range(numParallelAcquisitions):
            hdr = [int.from_bytes(file_obj.read(4), byteorder='little', signed=False) for i in range(headersize)]
            allData[:headersize, (ii*numParallelAcquisitions) + jj] = hdr

            dat = np.array([int.from_bytes(file_obj.read(4), byteorder='little', signed=False) for i in range(numSamplesIQAcq)])
            dat[dat >= (2**23)] -= (2**24)

            dataA[:,ii*numParallelAcquisitions+jj] = dat[:numSamplesDrOut*2]

            allData[headersize:headersize+(numSamplesDrOut*2)+1, \
                    ii*numParallelAcquisitions+jj] = dat[:min(numSamplesDrOut*2, allData.shape[0]-headersize)]
            
            

    iq = dataA[np.arange(0, numSamplesDrOut*2, 2)] + 1j*dataA[np.arange(1,numSamplesDrOut*2,2)]
    bmode = 20*np.log10(abs(iq))

    return bmode, iq, digitizingRateHz

class FileStruct():
    def __init__(self, filedirectory, filename):
        self.name = filename
        self.directory = filedirectory

class DataOutputStruct():
    def __init__(self):
        self.scRF = None
        self.scBmode = None
        self.rf = None
        self.bMode = None

class InfoStruct():
    def __init__(self):
        # US System Configuration
        # US system: Canon Aplio i800 (V4.6SP0008)
        # Transducer: PVI-475BX (i8CX1)
        self.minFrequency = 1800000 #Hz
        self.maxFrequency = 6200000 #Hz
        self.lowBandFreq = 1000000 #Hz
        self.upBandFreq = 6000000 #Hz
        # Preset 1
        self.depth = 150 #mm
        # Preset 2
        # self.depth = 200

        self.studyMode = None
        self.filename = None
        self.filepath = None
        self.probe = None
        self.system = None
        self.studyID = None
        self.studyEXT = None
        self.width = None
        self.rxFrequency = None
        self.samplingFrequency = None
        self.lateralRes = None
        self.axialRes = None
        self.maxval = None

        # Scan Conversion Params
        self.tilt1 = None
        self.width1 = None
        self.startDepth1 = None
        self.endDepth1 = None

        # One if preSC, the other is postSC resolutions
        self.yResRF = None 
        self.xResRF = None
        self.yRes = None
        self.xRes = None

        # Quad 2 or accounting for change in line density
        self.quad2x = None



def getImage(filename, filedirectory, refname, refdirectory):
    Files = FileStruct(filedirectory, filename)
    RefFiles = FileStruct(refdirectory, refname)

    [ImgInfo, RefInfo, ImgData, RefData] = getData(Files, RefFiles)
    
    return ImgData.scBmode, ImgData, ImgInfo, RefData, RefInfo



def getData(Files, RefFiles):
    ImgInfo = readFileInfo(Files.name, Files.directory)
    [ImgData, ImgInfo] = readFileImg(ImgInfo, str(Files.directory + Files.name))

    RefInfo = readFileInfo(RefFiles.name, RefFiles.directory)
    [RefData, RefInfo] = readFileImg(RefInfo, str(RefFiles.directory + RefFiles.name))

    return [ImgInfo, RefInfo, ImgData, RefData]

def readFileInfo(filename, filepath):    
    studyID = filename[:-4]
    studyEXT = filename[-4:]

    Info = InfoStruct()
    Info.studyMode = "RF"
    Info.filename = filename
    Info.filepath = filepath
    Info.probe = "C5-?"
    Info.system = "EPIQ7"
    Info.studyID = studyID
    Info.studyEXT = studyEXT
    Info.rxFrequency = None #20000000
    Info.samplingFrequency = None #20000000

    # Scan Convert Settings
    Info.tilt1 = 0
    Info.width1 = 70 #degrees

    return Info

def readFileImg(Info, filePath):
    bmode, iqData, Info.rxFrequency = readIQ(filePath)
    Info.samplingFrequency = Info.rxFrequency
    rfData = iqToRf(iqData, Info.rxFrequency)
    ModeIM = rfData

    Info.endDepth1 = Info.depth/1000 #m
    Info.startDepth1 = Info.endDepth1/4 #m

    [scBmode, hCm1, wCm1, _] = scanConvert(bmode, Info.width1, Info.tilt1, Info.startDepth1, Info.endDepth1)
    # TODO: Left off here (line 23, philips_read_PhilipsImg.m). Was not able to check final outim, inIm_ind(x/y). If something's off, look here
    [_, hCm1, wCm1, scModeIM] = scanConvert(ModeIM, Info.width1, Info.tilt1, Info.startDepth1, Info.endDepth1)

    # import matplotlib.pyplot as plt
    # plt.imshow(scBmode, cmap="Greys_r")
    # plt.show()

    Info.depth = hCm1*10 #mm
    Info.width = wCm1*10 #mm
    Info.lateralRes = Info.width/scBmode.shape[1]
    Info.axialRes = Info.depth/scBmode.shape[0]
    Info.maxval = np.amax(scBmode)

    Data = DataOutputStruct()
    Data.scRF = scModeIM
    Data.scBmode = scBmode * (255/Info.maxval)
    Data.rf = ModeIM
    Data.bMode = bmode * (255/np.amax(bmode))
    
    # Data.scRF = ModeIM
    # Data.scBmode = bmode
    # Info.maxval = np.amax(bmode)

    # Info.height = 126.8344
    # Info.width = Info.height*bmode.shape[0]/bmode.shape[1]
    # Info.lateralRes = Info.width/bmode.shape[0]
    # Info.axialRes = Info.height/bmode.shape[1]

    return Data, Info


if __name__ == "__main__":
    getImage("20220112112155_IQ.bin","/Users/davidspector/Home/Stanford/Project_Data/Misc Data/","20220112112155_IQ.bin","/Users/davidspector/Home/Stanford/Project_Data/Misc Data/")


