import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


class HeartRateData:
    def __init__(self, file_path: str, fs: float):
        self.data = pd.read_csv(file_path)["ecg"].tolist()
        self.fs = fs

    def extract_heartrate(self, thr: float):
        value_record = 0
        time = 0
        t_old = None
        heartrates = []
        timestamps = []
        for i, value in enumerate(self.data):
            if value > thr:
                if value > value_record:
                    value_record = value
                    time = i / self.fs
            else:
                if value_record > 0:
                    if t_old is not None:
                        hr = 60.0 / (time - t_old)
                        heartrates.append(hr)
                        timestamps.append(time)
                    t_old = time
                time = 0
                value_record = 0

        return (heartrates, timestamps)

if __name__ == "__main__":
    signal = HeartRateData("files/data_1_rows.csv", fs=300.0)
    heartrates, timestamps = signal.extract_heartrate(thr=0.6)
    plt.subplot(2, 1, 1)
    plt.plot(np.linspace(0, len(signal.data) / signal.fs, len(signal.data)), signal.data)
    plt.subplot(2, 1, 2)
    plt.plot(timestamps, heartrates)
    plt.xlabel("Time (s)")
    plt.ylabel("Heart Rate (bpm)")
    plt.title("Heart Rate Over Time")
    plt.show()
