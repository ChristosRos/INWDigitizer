import ROOT
import re
import numpy
import time
import glob
import sys,os
from numpy import mean, sqrt, square
import numpy as np

def rms(x):
    return numpi.sqrt(x.dot(x)/x.size)

###########################################
# analyzer.py works opening several files
# Next is to develop a array loop onening

#inputFile = "/home/analysis/HVSCAN/002409/HV8/HV8.root"
inputFile=[0 for i in range(16)]
inputFile[1]  = "HVSCAN/002405/HV1/HV1.root"
inputFile[2]  = "HVSCAN/002405/HV2/HV2.root"
inputFile[3]  = "HVSCAN/002405/HV3/HV3.root"
inputFile[4]  = "HVSCAN/002405/HV4/HV4.root"
inputFile[5]  = "HVSCAN/002405/HV5/HV5.root"
inputFile[6]  = "HVSCAN/002405/HV6/HV6.root"
inputFile[7]  = "HVSCAN/002405/HV7/HV7.root"
inputFile[8]  = "HVSCAN/002405/HV8/HV8.root"
inputFile[9]  = "HVSCAN/002405/HV9/HV9.root"
inputFile[10] = "HVSCAN/002405/HV10/HV10.root"
inputFile[11] = "HVSCAN/002405/HV11/HV11.root"
inputFile[12] = "HVSCAN/002405/HV12/HV12.root"
inputFile[13] = "HVSCAN/002405/HV13/HV13.root"
inputFile[14] = "HVSCAN/002405/HV14/HV14.root"
inputFile[15] = "HVSCAN/002405/HV15/HV15.root"

fIn  = [0 for i in range(16)]
data = [0 for i in range(16)]
rms  = [0 for i in range(16)]
for num in range(4,9):
 fIn[num]  = ROOT.TFile(inputFile[num]) # open ROOT file
 data[num] = fIn[num].Get("data") # get the data tree

time = fIn[7].Get("time") # get the time vector

# Loop over all the events for all channels
#for i in range(0, data[7].GetEntries()+1):
for i in range(0, 2):

	data[7].GetEntry(i)
	data[6].GetEntry(i)
	trgTime7 = data[7].trgTime

	pulse7   = data[7].pulse
	pulse6   = data[6].pulse

        ch6      = data[6].channel
        evNum6   = data[6].evNum
        trgTime6 = data[6].trgTime

	print i, pulse6
#	# loop over the pulse
#	for j in range(0, pulse7.size()):
#		b = 0
#		print time[j], pulse7[j], pulse6[j]
	rms[6] = np.sqrt(np.mean(np.dot(pulse6,pulse6))/1024.)
	print " --> " + str(rms[6])
        rms[6] = np.mean(pulse6)
	print " --> " + str(rms[6])

fIn[7].Close()
fIn[6].Close()
