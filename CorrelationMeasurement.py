import matplotlib.pyplot as plt
from time import sleep

from TimeTagger import createTimeTagger, Correlation
    
# create a Time Tagger instance
tagger = createTimeTagger()
tagger.reset()

# measure photon antibunching
corr_ch1 = 1 # first photon channel for antubunching measurements
corr_ch2 = 2 # second photon channel for antibunching measurements
bwcorr = 1000 # 1 ns
nbins = 1000
corr = Correlation(tagger, corr_ch1, corr_ch2, bwcorr, nbins)
print("\nCorrelation measurement is running.")

# collect data for 10 seconds and plot
sleep(10)

# normalized correlation -> Photon Antibunching
xcorr = corr.getIndex()
# ycorr = corr.getDataNormalized()
ycorr = corr.getData()

plt.plot(xcorr, ycorr)
plt.show()
