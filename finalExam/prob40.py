
inf1 = open("noise.txt",'r')
noise_full = inf1.readlines()

print(type(noise_full))

inf1.close()

hours = []
noise = []

for line in noise_full:
    print(type(line))


for line in noise_full:
    lineData = line.split(",")
    hour,noise_level, precip,wind = int(lineData[0]),float(lineData[1]),float(lineData[2]),float(lineData[3])

print("Done")

hour = 0
hour = (hour + 8)%24

print (hour)


'''
    if QUESTION4:
        hours.append(hour)
        noise.append(noise_level)

'''