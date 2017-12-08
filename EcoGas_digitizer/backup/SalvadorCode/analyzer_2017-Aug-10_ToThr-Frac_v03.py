#!/usr/bin/env python
import ROOT
import re
import numpy
import time
import glob
import sys,os
from numpy import mean, sqrt, square, std
import numpy as np
import os
import os
first    = int(os.environ['Dig1'])
last     = int(os.environ['Dig2'])
HVPoint  = int(os.environ['HVPoint'])
Thr      = int(os.environ['Thr'])
Frac     = int(os.environ['Frac'])

def rms(x):
    return numpy.sqrt(x.dot(x)/x.size)

###########################################
# analyzer.py works opening several files
# Next is to develop a array loop onening

#inputFile = "/home/analysis/HVSCAN/002409/HV8/HV8.root"
inputFile=[0 for i in range(16)]
inputFile[1]  = "HVSCAN/ecogasboth2/run1/run1.root"
inputFile[2]  = "HVSCAN/ecogasboth2/run2/run2.root"
inputFile[3]  = "HVSCAN/ecogasboth2/run3/run3.root"
inputFile[4]  = "HVSCAN/ecogasboth2/run4/run4.root"
inputFile[5]  = "HVSCAN/ecogasboth2/run5/run5.root"
inputFile[6]  = "HVSCAN/ecogasboth2/run6/run6.root"

fIn   = [0 for i in range(16)]
data  = [0 for i in range(16)]
rms   = [0 for i in range(16)]
stdv  = [0 for i in range(16)]
mean  = [0 for i in range(16)]
pulse = [0 for i in range(16)]
high  = [0 for i in range(16)]
low   = [0 for i in range(16)]
ToThr = [0 for i in range(16)]
startime  = [0 for i in range(16)]
endtime   = [0 for i in range(16)]

for num in range(1,7):
	fIn[num]  = ROOT.TFile(inputFile[num]) # open ROOT file
	data[num] = fIn[num].Get("data") # get the data tree
time = fIn[num].Get("time") # get the time vector
# print num
#print "---------------"
run = HVPoint

# Loop over all the events for all channels
#for i in range(0, data[7].GetEntries()+1):
eff = 0
numToThr = 0
for i in range(first, last):

	data[run].GetEntry(i)

	trgTime    = data[run].trgTime

	pulse[0]  = data[run].pulse_ch0
	pulse[1]  = data[run].pulse_ch1
	pulse[2]  = data[run].pulse_ch2
	pulse[3]  = data[run].pulse_ch3
	pulse[4]  = data[run].pulse_ch4
	pulse[5]  = data[run].pulse_ch5
	pulse[6]  = data[run].pulse_ch6
	pulse[7]  = data[run].pulse_ch7
	pulse[8]  = data[run].pulse_ch8
	pulse[9]  = data[run].pulse_ch9
	pulse[10]  = data[run].pulse_ch10
	pulse[11]  = data[run].pulse_ch11
	pulse[12]  = data[run].pulse_ch12
	pulse[13]  = data[run].pulse_ch13
	pulse[14]  = data[run].pulse_ch14
	pulse[15]  = data[run].pulse_ch15

        evNum      = data[run].evNum
        trgTime    = data[run].trgTime

	for n in range(0,15):
		mean[n] = np.mean(pulse[n][:100])
		stdv[n] = np.std(pulse[n][:100])*10.0
###	print "================================================="
#	for j in strips:
	for n in range(0,15):
                low[n]   = 0
                high[n]  = 0
		ToThr[n] = 0
		found    = 0
		for j in range(0,pulse[n].size()):
#			print pulse[n][j]-mean[n]
			if (pulse[n][j]-mean[n]>Thr):

			  # Get max value of Pulse
			  if (found==1):
				if (pulse[n][j]-mean[n]>low[n]):
					low[n] = pulse[n][j]-mean[n]

			  # If End Time does not ends put the time of last value ...
			  if (found==1 and j==1023):
				end = 200*time[j]/1024.
				endtime[n]  = end
###				print " ... ending time = " + str(end) + " ==> " + str(end-start)
                                ToThr[n]=end-start

			  # Main Loop for Strat and End Time
			  if (found==0):
				start = 200*time[j]/1024.
###				print str(i) + "\n\t -->" + str(n) + ") Starting Time = " + str(start),
				found = 1
				startime[n] = start
			else:
			  if (found==1):
				found = 0
				end = 200*time[j]/1024.
				endtime[n]  = end
###				print " ... ending time = " + str(end) + " ==> " + str(end-start)
				ToThr[n]=end-start
				break
######	print max(ToThr),low[ToThr.index(max(ToThr))],startime[ToThr.index(max(ToThr))]
        if ( max(ToThr)>Frac ):
		numToThr = numToThr+1

print Frac,100*numToThr/(last-first)

for num in range(1,7):
	fIn[num].Close()

#inputFile[1]  = "HVSCAN/ecogasboth2/run1/run1.dqm.root"
#inputFile[2]  = "HVSCAN/ecogasboth2/run2/run2.dqm.root"
#inputFile[3]  = "HVSCAN/ecogasboth2/run3/run3.dqm.root"
#inputFile[4]  = "HVSCAN/ecogasboth2/run4/run4.dqm.root"
#inputFile[5]  = "HVSCAN/ecogasboth2/run5/run5.dqm.root"
#inputFile[6]  = "HVSCAN/ecogasboth2/run6/run6.dqm.root"
