import matplotlib
matplotlib.use("QtAgg")
import matplotlib.pyplot as plt

filename = "C:/Users/Martin/Documents/ST2_AP_all_lectures/oop_3/files/data1.csv"
data = []
with open(filename) as f:
    header = f.readline()
    for line in f:
        data.append(float(line.strip()))

plt.plot(data)
plt.show()

