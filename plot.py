import numpy as np
import matplotlib.pyplot as plt
import scipy.io

# Load data
data = scipy.io.loadmat('dataset/P1_low1.mat')

fs = data['fs'][0,0]  # Sampling frequency
y = data['y']  # EEG signals
trig = data['trig'].flatten()  # Trigger signals

# Create time array in seconds
step = 1/fs
time_end = len(trig)/fs
time = np.arange(step, time_end+step, step)

# Figure 1: Plot Fz channel and vibrations
fig1, (ax1, ax2) = plt.subplots(2, 1, sharex=True)

ax1.plot(time, y[:, 0])
ax1.set_title('Channel Fz, Subject 1, High Accuracy')
ax1.set_ylabel('mV')

ax2.plot(time, trig, "red")
ax2.set_title('Vibrations on Different Regions')
ax2.set_xlabel('Time (sec)')
ax2.set_ylabel('-1: distractor | +1: nontarget | +2: target')

# Figure 2: Plot all 8 channels
regions = ["Fz", "C3", "Cz", "C4", "CP1", "CPz", "CP2", "Pz"]
fig2, axes = plt.subplots(8, 1, sharex=True)

for i in range(8):
    axes[i].plot(time, y[:, i])
    axes[i].set_title(regions[i])

axes[-1].set_xlabel('Time (sec)')
axes[-1].set_ylabel('mV')

plt.show()
print("Done")