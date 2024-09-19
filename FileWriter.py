import time
from TimeTagger import createTimeTagger, FileWriter
    
# create a Time Tagger instance
tagger = createTimeTagger()
tagger.reset()

# measure photon antibunching
ch1 = 1 # First channel for the data acquisition
ch2 = 2 # Second channel for the data acquisition

# Adjust trigger level on the channels to 0.5 Volt
tagger.setTriggerLevel(ch1, 0.5)
tagger.setTriggerLevel(ch2, 0.5)

print("Waiting time ...")
time.sleep(1)

fw = FileWriter(tagger, 'Measurement.ttbin', [ch1, ch2]) # Store tags from channels 

print("Measurement is running.")

# Run Correlation for 1 second to accumulate the data
fw.startFor(int(1e12), clear=True)
fw.waitUntilFinished()

# Number of total events recorded
print("Total events: ", fw.getTotalEvents())
# Total size of data acquired
print("Total size (number of bytes): ", fw.getTotalSize())