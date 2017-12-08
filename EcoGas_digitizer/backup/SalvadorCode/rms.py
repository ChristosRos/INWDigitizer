        # loop over the pulse 
        for n in range(0,15): 
                mean[n] = np.mean(pulse[n][:100])
                stdv[n] = np.std(pulse[n][:100])*10.0
                if (debug==4): print stdv[n],
#               rms= 0
#               for k in range(0,100):
#                       rms = rms + (pulse[n][k]-mean[n])*(pulse[n][k]-mean[n])
#               stdv[n] = 5*sqrt(rms/(last-first))
#               if (debug==4): print stdv[n]

#               np.sqrt(x.dot(x)/x.size)

