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
inputFile[1]  = "HVSCAN/ecogasboth2/run1/run1.dqm.root"
inputFile[2]  = "HVSCAN/ecogasboth2/run2/run2.dqm.root"
inputFile[3]  = "HVSCAN/ecogasboth2/run3/run3.dqm.root"
inputFile[4]  = "HVSCAN/ecogasboth2/run4/run4.dqm.root"
inputFile[5]  = "HVSCAN/ecogasboth2/run5/run5.dqm.root"
inputFile[6]  = "HVSCAN/ecogasboth2/run6/run6.dqm.root"

fIn  = [0 for i in range(16)]
data = [0 for i in range(16)]
rms  = [0 for i in range(16)]
for num in range(5,6):
 fIn[num]  = ROOT.TFile(inputFile[num]) # open ROOT file
 data[num] = fIn[num].Get("data") # get the data tree
 print num
print "---------------"

time = fIn[5].Get("time") # get the time vector

# Loop over all the events for all channels
#for i in range(0, data[7].GetEntries()+1):
for i in range(0, 1):

	data[5].GetEntry(i)

	trgTime   = data[5].trgTime

	pulse_ch0 = data[5].pulse_ch0

        evNum     = data[5].evNum
        trgTime   = data[5].trgTime

	print i, evNum
	# loop over the pulse
	for j in range(0, pulse_ch0.size()):
		b = 0
		print j, time[j], pulse_ch0[j]
#	rms[6] = np.sqrt(np.mean(np.dot(pulse6,pulse6))/1024.)
#	print " --> " + str(rms[6])
#        rms[6] = np.mean(pulse6)
#	print " --> " + str(rms[6])

fIn[5].Close()
