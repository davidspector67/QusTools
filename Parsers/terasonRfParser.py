from scipy.io import loadmat
import numpy as np
from scipy.signal import hilbert

def getImage(filePath, OmniOn=1):
    # Credit: Steven R. Broadstone, D.Sc., Teratech Corporation dba Terason
    # Parser inspired by MATLAB code writen by Steven
    # Written to parse RF data taken with two focal zones

    input = loadmat(filePath)
    b_data_Zone1 = np.array(input["b_data_Zone1"])
    b_data_Zone2 = np.array(input["b_data_Zone2"])

    # Blend the zones overlap
    M, N = b_data_Zone1.shape
    if OmniOn == 1:
        b_data1 = (b_data_Zone1[:M, :int(N/2)] + b_data_Zone1[:M, int(N/2):])/2
        b_data2 = (b_data_Zone1[:M, :int(N/2)] + b_data_Zone2[:M, int(N/2):])/2
    else:
        b_data1 = b_data_Zone1[:M, :int(N/2)]
        b_data2 = b_data_Zone2[:M, :int(N/2)]
    
    # Hardcoded vals are specific to Terason images used for a study
    rf_data = np.zeros(b_data1.shape)
    b_data_av = (b_data1[140:280,:]+b_data2[140:280,:])/2
    rf_data[:140, :] = b_data1[:140,:]
    rf_data[140:280,:] = b_data_av
    rf_data[280:,:] = b_data2[280:,:]

    bmode = np.zeros(rf_data.shape)
    for i in range(rf_data.shape[1]):
        bmode[:,i] = 20*np.log10(abs(hilbert(rf_data[:,i])))

    # dynrange of 40
    bmode = np.clip(bmode, np.amax(bmode)-40, np.amax(bmode))
    bmode -= np.amin(bmode)
    bmode *= (255/np.amax(bmode))

    return bmode, rf_data