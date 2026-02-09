import sounddevice as sd
import numpy as np
import csv
import matplotlib
matplotlib.use('QtAgg')  # Use non-interactive backend
import matplotlib.pyplot as plt
# -------------------------------
# Step 1: List input devices
# -------------------------------
print("Available input devices:")
for i, dev in enumerate(sd.query_devices()):
    if dev['max_input_channels'] > 0:
        print(i, dev['name'], dev['max_input_channels'])

# -------------------------------
# Step 2: Choose device
# -------------------------------
device_index = int(input("Enter device index to record from: "))

# -------------------------------
# Step 3: Record 5 seconds of audio
# -------------------------------
duration = 5  # seconds
samplerate = 44100  # Hz
channels = 1  # mono

print("Recording...")
audio = sd.rec(int(duration * samplerate), samplerate=samplerate,
               channels=channels, dtype='float32', device=device_index)
sd.wait()
print("Recording finished!")

# -------------------------------
# Step 4: Check amplitude (sanity)
# -------------------------------
print("Mean amplitude:", np.abs(audio).mean())

# -------------------------------
# Step 5: Save to CSV
# -------------------------------
csv_filename = "recording.csv"
with open(csv_filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    # Flatten in case of multi-channel
    for sample in audio:
        writer.writerow(sample)
        
print(f"Saved recording as {csv_filename}")

# print this to figure as well
print("Displaying waveform...")
plt.plot(np.linspace(0, duration, len(audio)), audio)
plt.title("Recorded Audio Waveform")
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.show()