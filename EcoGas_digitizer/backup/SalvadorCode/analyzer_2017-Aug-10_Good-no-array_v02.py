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

fIn   = [0 for i in range(16)]
data  = [0 for i in range(16)]
rms   = [0 for i in range(16)]
mean  = [0 for i in range(16)]
pulse = [0 for i in range(16)]

for num in range(1,2):
 fIn[num]  = ROOT.TFile(inputFile[num]) # open ROOT file
 data[num] = fIn[num].Get("data") # get the data tree
# print num
#print "---------------"
run = 1
time = fIn[1].Get("time") # get the time vector

# Loop over all the events for all channels
#for i in range(0, data[7].GetEntries()+1):
for i in range(24, 25):

	data[1].GetEntry(i)

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

#	print i, evNum
	# loop over the pulse
	for k in range(0,15):
		mean[k] = np.mean(pulse[k][:100])
#	print std

	for j in range(0, pulse[0].size()):
		b = 0
		print j, time[j], 
		for k in range(0,15):
			print pulse[k][j]-mean[k],
		print ""
#	rms[6] = np.sqrt(np.mean(np.dot(pulse6,pulse6))/1024.)
#	print " --> " + str(rms[6])
#        rms[6] = np.mean(pulse6)
#	print " --> " + str(rms[6])

fIn[1].Close()
