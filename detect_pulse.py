from pulsesensor import Pulsesensor
import time
import numpy as np

p = Pulsesensor()
p.startAsyncBPM()

try:
    measurement = []
    for i in range(20):
        bpm = p.BPM
        if bpm > 0: # check if bpm from pulse sensor is detected (i.e. greater than 0)
            print("BPM: %d" % bpm)
            measurement.append(bpm)
        else: # no heartbeat detected
            print(bpm)
            measurement.append(bpm)
            print("No Heartbeat found")
        time.sleep(1) # update bpm every second
    bpm_ar = np.asarray(bpm)
    bpm_ar = bpm_ar[bpm_ar != 0] 
    bpm_ar = bpm_ar[:6] 
    np.save("data.npy", bpm_ar)
    print(bpm_arr,datetime.now().strftime("%Y:%m:%d:%H:%M%S"))
except:
    p.stopAsyncBPM()
