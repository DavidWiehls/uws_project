import numpy as np
import matplotlib.pyplot as plt
import scipy.io

# Load data
data = scipy.io.loadmat('dataset/P1_high1.mat')

fs = data['fs'][0,0]  # Sampling frequency
y = data['y']  # EEG signals
trig = data['trig'].flatten()  # Trigger signals

# Create time array in seconds
step = 1/fs
time_end = len(trig)/fs
time = np.arange(step, time_end+step, step)

## "trig" contains -1, 1, and 2, which indicate the type of stimulus. Here we create a time array to know when they occur.
list_trig_target = []
list_trig_nontarget = []
list_trig_distractor = []

for i in range(len(trig)):
    if trig[i] == 1:
        list_trig_target.append(i)
    elif trig[i] == 2:
        list_trig_nontarget.append(i)
    elif trig[i] == -1:
        list_trig_distractor.append(i)

## Now we select from 300ms to 600ms after the stimulus
y_target = []
y_nontarget = []
y_distractor = []

## Target
for i in range(len(list_trig_target)):
    y_target.append(y[list_trig_target[i]+int(0.3*fs):list_trig_target[i]+int(0.6*fs), :])
## Nontarget
for i in range(len(list_trig_nontarget)):
    y_nontarget.append(y[list_trig_nontarget[i]+int(0.3*fs):list_trig_nontarget[i]+int(0.6*fs), :])
## Distractor
for i in range(len(list_trig_distractor)):
    y_distractor.append(y[list_trig_distractor[i]+int(0.3*fs):list_trig_distractor[i]+int(0.6*fs), :])
    
## We now have 3 lists of 3D arrays, each containing the EEG signals for each stimulus type. We can now average them to get the average signal for each stimulus type.
y_target = np.mean(y_target, axis=0)
y_nontarget = np.mean(y_nontarget, axis=0)
y_distractor = np.mean(y_distractor, axis=0)


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