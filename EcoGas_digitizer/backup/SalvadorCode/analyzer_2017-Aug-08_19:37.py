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
inputFile7 = "HVSCAN/002405/HV7/HV7.root"
inputFile6 = "HVSCAN/002405/HV6/HV6.root"

fIn7  = ROOT.TFile(inputFile7) # open ROOT file
data7 = fIn7.Get("data") # get the data tree

fIn6  = ROOT.TFile(inputFile6) # open ROOT file
data6 = fIn6.Get("data") # get the data tree

time = fIn7.Get("time") # get the time vector

# Loop over all the events for all channels
for i in range(0, data7.GetEntries()+1):

	data7.GetEntry(i)
	data6.GetEntry(i)

	ch7      = data7.channel
	evNum7   = data7.evNum
	trgTime7 = data7.trgTime
	pulse7   = data7.pulse

	ch6      = data6.channel
	evNum6   = data6.evNum
	trgTime6 = data6.trgTime
	pulse6   = data6.pulse

	# loop over the pulse
	for j in range(0, pulse7.size()):

		print time[j], pulse7[j], pulse6[j]

fIn7.Close()
fIn6.Close()

