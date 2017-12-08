import ROOT 
import re
import numpy
import time
import glob
import sys,os
from numpy import mean, sqrt, square, std
import numpy as np

#inputFile = "HVSCAN/002405/HV7/HV7.root"
inputFile = "HVSCAN/ecogasboth2/run5/run5.dqm.root"

fIn = ROOT.TFile(inputFile) # open ROOT file
data = fIn.Get("data") # get the data tree
time = fIn.Get("time") # get the time vector

# Loop over all the events for all channels
#for i in range(0, data.GetEntries()+1):
for i in range(55, 56):
#for i in range(1, 1000):
	data.GetEntry(i)

	ch = data.channel
	evNum = data.evNum
	trgTime = data.trgTime
	pulse = data.pulse

	# loop over the pulse
	for j in range(0, pulse.size()):
		a = 0
		print i, j, time[j], pulse[j]
        print "-------------------------------------"

#        rms = np.sqrt(np.mean(np.dot(pulse,pulse))/1024.)
#        print " --> " + str(rms)
        mean = np.mean(pulse)
        std  = np.std(pulse)
        print str(i) + ") --> " + str(mean) + ", Std = " + str(std)

        # Get Peak for each Over Threshold
        Threshold = mean+5*1.5
        for j in range(0, pulse.size()):
                a = 0
                if pulse[j]>Threshold:
			print j, time[j], pulse[j]
        print "-------------------------------------"




fIn.Close()

