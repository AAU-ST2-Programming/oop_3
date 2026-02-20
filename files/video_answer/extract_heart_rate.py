import matplotlib
matplotlib.use("QtAgg")
import matplotlib.pyplot as plt

class HeartRate:
    def __init__(self, file_path:str, fs: float):
        self.file_path = file_path
        self.fs = fs
        data: list[float] = []
        # open file
        with open(file_path, mode="r") as f:
            self.header = f.readline()
            for line in f:
                line = line.strip()
                if line:
                    data.append(float(line))
        self.data = data

        # calculate time liste
        time = []
        for i in range(len(data)):
            time.append(i)
        
        time = [i/fs for i in range(len(data))]
        self.time = time

    def calculate_heartrate(self, threshold: float):
        value_record = 0
        time_record = 0
        t_old = None
        heartrate = []
        timestamps = []

        for i, value in enumerate(self.data):
            if value > threshold:
                if value > value_record:
                    value_record = value
                    time_record = i/self.fs
            else:
                if value_record>0:
                    if t_old is not None:
                        hr = 60.0/(time_record - t_old)
                        heartrate.append(hr)
                        timestamps.append(time_record)
                    t_old = time_record
                time_record = 0
                value_record = 0
        return heartrate, timestamps

if __name__ == "__main__":
    fs = 300
    file_path = "files/data_1_rows.csv"
    signal = HeartRate(file_path=file_path, fs=fs)
    heartrate, timestamps = signal.calculate_heartrate(threshold=0.6)
    plt.subplot(2,1,1)
    plt.title("EKG")
    plt.plot(signal.time, signal.data)
    
    plt.subplot(2,1,2)
    plt.plot(timestamps, heartrate)
    plt.xlabel("Time (s)")
    plt.ylabel("Heart Rate (bpm)")
    plt.title("Heart Rate Over Time")
    plt.show()

    print("Done.")

