import ROOT 
import re
import numpy
import time
import glob
import sys,os
###########################################
# analyzer.py works opening several files
# Next is to develop a array loop onening

#inputFile = "/home/analysis/HVSCAN/002409/HV8/HV8.root"
inputFile6 = "HVSCAN/002405/HV6/HV6.root"

fIn6  = ROOT.TFile(inputFile6) # open ROOT file
data6 = fIn6.Get("data") # get the data tree

time = fIn7.Get("time") # get the time vector

# Loop over all the events for all channels
for i in range(0, data6.GetEntries()+1):

	data6.GetEntry(i)

	ch6      = data6.channel
	evNum6   = data6.evNum
	trgTime6 = data6.trgTime
	pulse6   = data6.pulse

	#loop over the channels
	for k in range(0, ch6.size()):
		# loop over the pulse
		for j in range(0, pulse6.size()):
			print i, ch6, time, pulse6

fIn7.Close()
fIn6.Close()

