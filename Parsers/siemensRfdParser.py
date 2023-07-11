# Remember to set analysisParams.endFrame in read_philips_info
# set frame
# fix while loop in philipsMatParser.py

class AnalysisParamsStruct():
    def __init__(self):
        self.axialWinSize = 2
        self.lateralWinSize = 2
        self.axialOverlap = 0 # in percent
        self.lateralOverlap = 0 # in percent
        self.minFrequency = 7000000
        self.maxFrequency = 17000000
        self.frame = 51 # set first frame you want to look at
        self.frameFreq = 40 # Set step size you want to use
        self.focus = 0
        self.t_tilt= 0
        self.t_width = 70
        self.startDepth = 0.04
        self.endDepth = 0.16
        self.endHeight = 500
        self.clip_fact = 0.95
        self.dyn_range = 55
        self.depth = 0.16
        self.width = 0.265

class FileStruct():
    def __init__(self, filedirectory, filename):
        self.name = filename
        self.directory = filedirectory

def getImage(filename, filedirectory, refname, refdirectory):
    AnalysisParams = AnalysisParamsStruct()
    Files = FileStruct(filedirectory, filename)
    RefFiles = FileStruct(refdirectory, refname)

    [ImgInfo, RefInfo, ImgData, RefData] = getData(Files, RefFiles, AnalysisParams)


def getData(Files, RefFiles, AnalysisParams):
    imgInfo = readFileInfo(Files.name, Files.directory)


def readFileInfo(filename, filepath):
    FileHeader = readHeader(str(filepath+filename))

def readHeader(filepath):
    file_obj = open(filepath, 'rb', )

def tmpRead(FourCC, fid, FileAsChars):
    # Credit Shelby Brunke, Jerome Mai, Siemens Ultrasound, 2003
