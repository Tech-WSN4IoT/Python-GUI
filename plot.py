import matplotlib.pyplot as plt
import numpy as np
import matplotlib.dates as mdates
import csv
import time

# def graph():
	# date, value = np.loadtxt("test1.csv", delimiter=',', unpack=True)
	# fig = plt.figure()
	# ax1 = fig.add_subplot(1,1,1, axisbg='white')
	# plt.plot(x=date, y=value, fmt='-')
	# plt.title('title')
	# plt.ylabel('Temparature')
	# plt.xlabel('Time')
	# plt.show()
	
#graph()
while True:
	f = open('test1.csv')
	csv_f = csv.reader(f)

	times = []
	temps = []

	for row in csv_f:
		times.append(row[0])
		temps.append(row[1])
	f.close()	
	print(times)
	print(temps)
	#plt.ion()
	plt.plot(times,temps)
	plt.title('Temperature over time')
	plt.ylabel('Temperature')
	plt.xlabel('Time')
	plt.show(block=False)	#plt.show() is a blocking function and will not execute further lines until window is closed
	time.sleep(5)
	plt.close()
	#time.sleep()
	
	
	#matplotlib.pyplot.close("all")
