import ROOT
import itertools as it
import re
import numpy
import pandas as pd
import time
import math
import glob
import sys,os
from subprocess import call

# define fixed time vector of 1024 ns
time = ROOT.TVectorD(1024)
for i in range(0, 1024): time[i] = i




def loadFiles(dir):

    nEvents = 0

    dataFiles = pd.read_csv(dir, header=-1)
    files = dataFiles.ix[list(range(len(dataFiles)))].values
    nEvents = len(files)

    Record_length = [len(dataFiles.head(8)),[int(s) for s in files[0][0].split() if s.isdigit()][0]]
    nEvents = nEvents / (1024 + 8)

    Evnt_selection = [[[None for k in xrange(Record_length[j])] for j in xrange(2)] for i in xrange(nEvents)]
    for i in range(nEvents):
        for k in range(Record_length[0]):
            Evnt_selection[i][0][k] = files[k+i*(Record_length[1]+Record_length[0])][0]
        for k in range(Record_length[1]):
            # ADC_count* V_p-p (=1V) / 2^(12bit) (conversion formula)
            Evnt_selection[i][1][k] = float(files[k+Record_length[0] + i*(Record_length[1]+Record_length[0])][0])


    return nEvents, files, Evnt_selection




def getInt(s):
    return int(re.search(r'\d+', s).group())

def getFloat(s):
    return float(re.search(r'\d+\.\d+', s).group())


################################################################################

#integer = getInt()
#directory = loadFiles()


def run(runid):

    dir = "/Users/croskas/PhD/RPC/Testbeam/%s/" % runid

    print "Analyze run %s" % runid


    for x in os.listdir(dir):

        HVdir = dir + x
        print "Running in dir %s" % HVdir

        tFull = ROOT.TTree("data", "data") # full events
        tStrip = ROOT.TTree("data", "data") # stripped events

        evNum = numpy.zeros(1, dtype=int)
        trgTime = numpy.zeros(1, dtype=int)

        tFull.Branch("evNum", evNum, "evNum/I")
        tFull.Branch("trgTime", trgTime, "trgTime/I")

        tStrip.Branch("evNum", evNum, "evNum/I")
        tStrip.Branch("trgTime", trgTime, "trgTime/I")

        pulses = []
        for i in range(0, 16):
            pulse = ROOT.vector('double')()
            pulses.append(pulse)

            tFull.Branch("pulse_ch%d" % i, pulses[i]) # , "pulse[1024]/F"
            tStrip.Branch("pulse_ch%d" % i, pulses[i]) # , "pulse[1024]/F"

        directory = loadFiles(HVdir)
        ### load all waves into memory
        nEvents, files, Evnt_selection = directory

        print "LOOOOP", nEvents

        ff = math.ceil(nEvents / (nEvents*0.05))
        print ff
        entriesWritten = 0

        for i in range(0, len(files[0])):


            integer = getInt(files[0][i])
            if "Record Length" in files[0][i]: continue
            elif "BoardID" in files[0][i]: continue
            elif "Channel" in files[0][i]: continue
            elif "Event Number" in files[0][i]: evNum[0] = integer
            elif "Pattern" in files[0][i]: continue
            elif "Trigger Time Stamp" in files[0][i]: trgTime[0] = integer
            elif "DC offset (DAC)" in files[0][i]: continue
            elif "Start Index Cell" in files[0][i]: continue

        for j in range(0, 16):
            for i in range(len(Evnt_selection)):
                for k in range(len(Evnt_selection[i][1])):
                    pulses[j].push_back(float(Evnt_selection[i][1][k]) * 1000 / 4096)




            # write and clean
                if (i+1)%(1024+8) == 0:

                    entriesWritten += 1
                    #if 1283 == entriesWritten: break

                tFull.Fill()


                if entriesWritten%ff== 0:

                    print "Fill stripped ", i, tFull.GetEntries()
                    tStrip.Fill()

                #print "WRITE", evNum, trgTime
                for k in range(0, 16): pulses[k].clear()



        dir2 = '/Users/croskas/PhD/RPC/Testbeam/ROOT_files'

        f1 = ROOT.TFile("%s/%s.root" % (dir2, x), "recreate")
        tFull.Write()
        time.Write("time")
        f1.Close()

        f1 = ROOT.TFile("%s/%s.dqm.root" % (dir2, x), "recreate")
        tStrip.Write()
        time.Write("time")
        f1.Close()

        files = None # clear memory








# PROBLEMATIC:
# BINARY: 2381, 2380







#runs = [2375, 2379, 2383, 2385, 2388, 2390, 2392, 2394, 2396, 2398, 2400, 2402, 2404] # first -> OK
#runs = [2406, 2408, 2410, 2412, 2414, 2416, 2418, 2420, 2422, 2424, 2426, 2428, 2430, 2432] # second -> OK
#runs = [2377, 2382, 2384, 2386, 2389, 2391, 2393, 2395, 2397, 2399, 2401, 2403, 2405] # third -> OK
#runs = [2407, 2409, 2411, 2413, 2415, 2417, 2419, 2421, 2423, 2425, 2427, 2429, 2431, 2433] # fourth -> OK

#runs = [2381]

runs = [00002]

#runs = [ 2389, 2391, 2393, 2395, 2397, 2399, 2401, 2403, 2405] # third


#runs = [2398, 2402, 2399, 2419, 2396, 2395, 2424, 2401, 2397, 2393, 2392, 2390]
#runs = [2409, 2403, 2412, 2420, 2413, 2416, 2423]
#runs = [2410, 2404, 2411, 2421, 2414, 2415, 2422]
#runs = [2564]

for runid in runs:

    runid = "%.6d" % runid
    run(runid)
