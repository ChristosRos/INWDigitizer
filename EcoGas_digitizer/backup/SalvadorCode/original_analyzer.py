import ROOT 
import re
import numpy
import time
import glob
import sys,os



inputFile = "/home/analysis/HVSCAN/002409/HV8/HV8.root"
inputFile = "HVSCAN/002405/HV7/HV7.root"


fIn = ROOT.TFile(inputFile) # open ROOT file
data = fIn.Get("data") # get the data tree
time = fIn.Get("time") # get the time vector


# Loop over all the events for all channels
for i in range(0, data.GetEntries()+1):

	data.GetEntry(i)

	ch = data.channel
	evNum = data.evNum
	trgTime = data.trgTime
	pulse = data.pulse

	# loop over the pulse
	for j in range(0, pulse.size()):

		print time[j], pulse[j]



fIn.Close()

