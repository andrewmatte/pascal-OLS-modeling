import math


span = 4*math.pi
num_samples = 50
interval = span/num_samples
samples = [interval*i for i in range(1, num_samples)]

outputs = [math.cos(f) for f in samples]
for i in range(len(outputs)):
    open("data.csv", "a").write(str(samples[i]) + ',' + str(outputs[i]) + "\n")
