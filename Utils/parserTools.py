import numpy as np
from numpy.matlib import repmat
from scipy.interpolate import RectBivariateSpline

class OutImStruct():
    def __init__(self):
        self.data = None
        self.orig = None
        self.xmap = None
        self.ymap = None

def scanConvert(inIm, width, tilt, startDepth, endDepth, desiredHeight=500):
    # ScanConvert sector image
    # Inputs:
    #      InIm          Input image
    #      Width         Sector width of input image in degrees 
    #      Tilt          Tilt of sector image in degrees  
    #      StartDepth    Axial depth of first sample in meters 
    #      EndDepth      Axial depth of last sample in meters   
    #      DesiredHeight Desired vertical size of output image in pixels 
    #      (default 500)
    # 
    #    Outputs:
    #      OutIm         Output (scanconverted) image(s)  
    #      HCm,WCm       Height and Width of image in centimeters 

    #Convert to radians
    width = width*np.pi/180
    tilt = tilt*np.pi/180

    frames = 1
    [samples, beams] = inIm.shape
    depthIncrement = (endDepth-startDepth)/(samples - 1)
    startAngle = 3*np.pi/2 + tilt - width/2
    angleIncrement = width/(beams+1)

    outIm = inIm
    transpose = 0
    background = 0
    height = desiredHeight
    width = 0

    # Set size of image if not defined
    stopAngle = startAngle+((beams-1)*angleIncrement)
    stopDepth = startDepth+((samples-1)*depthIncrement)
    angleRange = np.arange(startAngle, stopAngle+angleIncrement, angleIncrement)

    xmin = -1*max(np.cos((startAngle%np.pi))*np.array([startDepth, stopDepth]))
    xmax = -1*min(np.cos((stopAngle%np.pi))*np.array([startDepth, stopDepth]))
    ymin = min(np.sin((angleRange%np.pi))*startDepth)
    ymax = max(np.sin((angleRange%np.pi))*stopDepth)
    widthScale = abs((xmax-xmin)/(ymax-ymin))

    if not width:
        width = int(np.ceil(height*widthScale))
    
    # Interpolate Image
    radI = 1
    latI = 1
    radSize = samples
    latSize = beams
    if radI > 1 or latI > 1:
        # WARNING: this code has not been tested and may not work. It's not needed for current project
        x = np.array(list(range(radSize)))
        y = np.array(list(range(latSize)))
        xi = np.array(list(range(0, radSize, 1/radI)))
        yi = np.array(list(range(0, latSize, 1/latI)))

        if transpose:
            nyIm = np.zeros((len(yi), len(xi), frames))
        else:
            nyIm = np.zeros((len(xi), len(yi), frames))

        for i in range(frames):
            if transpose:
                nyIm[:,:,i] = RectBivariateSpline(x, y, np.double(outIm[:,:,i])).ev(xi, yi)
            else:
                nyIm[:,:,i] = RectBivariateSpline(y, x, np.double(outIm[:,:,i])).ev(yi, xi)

        outIm = nyIm
    
    nr = (samples+((samples-1)*(radI-1)))
    nb = (beams+((beams-1)*(latI-1)))
    t0 = startAngle
    dt = angleIncrement*(beams)/(nb)
    r0 = startDepth
    dr = depthIncrement*(samples)/(nr)
    nbF = nb
    nrF = nr
    t0F = t0
    dtF = dt
    r0F = r0
    drF = dr

    # Subtract 180 degrees to get transudcer in top of image if startAngle > pi
    t0 = t0 % np.pi
    t0F = t0F % np.pi

    # Define physical limits of image
    stopAngle = t0 + (nb*dt)
    stopDepth = r0 + (nr*dr)
    angleRange = np.arange(t0, stopAngle+dt, dt)
    y0 = min(r0*np.sin(angleRange))
    ymax = max(stopDepth*np.sin(angleRange))
    x0 = min([-1*stopDepth*np.cos(t0), -1*startDepth*np.cos(t0)])
    xmax = max(-1*startDepth*np.cos(stopAngle), -1*stopDepth*np.cos(stopAngle))

    heightCm = (ymax-y0)*100
    widthCm = (xmax-x0)*100

    # Make (x,y)-plane representation of physical image
    xmat = (np.transpose(np.ones((1, height)))*np.arange(0, width, 1))/(width-1)
    ymat = (np.transpose(np.arange(0, height, 1).reshape((1, height)))*np.ones((1, width)))/(height-1)
    xmat = (xmat*(xmax-x0)) + x0
    ymat = (ymat*(ymax-y0)) + y0

    # Transform into polar coordinates (angle, range)
    anglemat = np.arctan2(ymat, -1*xmat)
    rmat = np.sqrt((xmat**2) + (ymat**2))

    # Convert phys. angle and range into beam and sample
    anglemat = np.ceil((anglemat - t0F)/dtF)
    rmat = np.ceil((rmat - r0F)/drF)

    # Find pixels outside active sector
    backgr = np.argwhere((rmat<1))
    backgr = np.concatenate((backgr, np.argwhere(rmat>=nrF)), axis=0)
    backgr = np.concatenate((backgr, np.argwhere(anglemat<1)), axis=0)
    backgr = np.concatenate((backgr, np.argwhere(anglemat>nbF)), axis=0)
    if transpose:
        scMap = (rmat-1)*nbF + anglemat
    else:
        scMap = (anglemat-1)*nrF + rmat

    # Mapping system added to Matlab by Ahmed El Kaffas - April 1st, 2019
    for i in range(backgr.shape[0]):
        scMap[backgr[i,0],backgr[i,1]] = (nbF*nrF)+1
    if np.amax(scMap)<((nbF*nrF)+1):
        scMap[0] = (nbF*nrF)+1
    # inIm_indy = np.zeros(outIm.shape)
    inIm_indx = repmat(np.arange(0, outIm.shape[1]), int(outIm.shape[0]), 1) # <-- maps (y,x) in Iin to indt in Iin
    inIm_indy = np.transpose(repmat(np.arange(0, outIm.shape[0]), int(outIm.shape[1]), 1)) # <-- maps (y,x) in Iout to indr in Iin

    if frames > 1:
        # WARNING: Not tested yet
        scIm = np.zeros((height, width, frames))
        for i in range(frames):
            out = outIm[:,:,i]
            out = np.append(out, background) #?
            scIm[:,:,i] = out[scMap]
        outIm = scIm
    else:
        outIm = np.append(np.transpose(outIm), background)
        inIm_indy = np.append(np.transpose(inIm_indy), background)
        inIm_indx = np.append(np.transpose(inIm_indx), background)

        scMap = np.array(scMap).astype(np.uint64) - 1
        outIm = outIm[scMap]
        inIm_indy = inIm_indy[scMap]
        inIm_indx = inIm_indx[scMap]

        outIm = np.reshape(outIm, (height, width))
        inIm_indy = np.reshape(inIm_indy, (height, width))
        inIm_indx = np.reshape(inIm_indx, (height, width))
    
    hCm = heightCm
    wCm = widthCm
    
    OutIm = OutImStruct()
    OutIm.data = outIm
    OutIm.orig = inIm
    OutIm.ymap = inIm_indy
    OutIm.xmap = inIm_indx
    return outIm, hCm, wCm, OutIm

def iqToRf(iqData, rxFrequency):
    rfData = np.zeros(iqData.shape)
    t = [i*(1/rxFrequency) for i in range(iqData.shape[0])]
    for i in range(iqData.shape[1]):
        rfData[:,i] = np.real(np.multiply(iqData[:,i], np.exp(1j*(2*np.pi*rxFrequency*np.transpose(t)))))

    return rfData