import ROOT
import re
import numpy
import time
import glob
import sys,os
from numpy import mean, sqrt, square, std
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
for num in range(1,2):
 fIn[num]  = ROOT.TFile(inputFile[num]) # open ROOT file
 data[num] = fIn[num].Get("data") # get the data tree
# print num
#print "---------------"

time = fIn[1].Get("time") # get the time vector

# Loop over all the events for all channels
#for i in range(0, data[7].GetEntries()+1):
for i in range(29, 30):

	data[1].GetEntry(i)

	trgTime    = data[1].trgTime

	pulse_ch6  = data[1].pulse_ch6
	pulse_ch7  = data[1].pulse_ch7
	pulse_ch8  = data[1].pulse_ch8

        evNum      = data[1].evNum
        trgTime    = data[1].trgTime

#	print i, evNum
	# loop over the pulse
	mean6 = np.mean(pulse_ch6[:100])
	mean7 = np.mean(pulse_ch7[:100])
	mean8 = np.mean(pulse_ch8[:100])
#	print std

	for j in range(0, pulse_ch7.size()):
		b = 0
		print j, time[j], pulse_ch7[j]-mean7, pulse_ch8[j]-mean8, pulse_ch6[j]-mean6
#	rms[6] = np.sqrt(np.mean(np.dot(pulse6,pulse6))/1024.)
#	print " --> " + str(rms[6])
#        rms[6] = np.mean(pulse6)
#	print " --> " + str(rms[6])

fIn[1].Close()
