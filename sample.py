#!/usr/bin/env python

import numpy as np
from random import randrange, seed

def percent_diff(a, b):
   return ((a - b)/b) * 100.0

##
## Simple Example
##

print("+++++ Simple Example +++++")

# Let's say that there are only 2 minutes in each hour
# with that in mind we have the following data sets
# for the first and second minute

data_minute_1 = [2,2,2,2]
data_minute_2 = [4]
print("minute 1 data: {0}".format(data_minute_1))
print("minute 2 data: {0}".format(data_minute_2))

# Let's compute the mean for each of the minute's worth of data
mean_minute_1 = np.mean(data_minute_1)
mean_minute_2 = np.mean(data_minute_2)

print("minute 1 mean: {0}".format(mean_minute_1))
print("minute 2 mean: {0}".format(mean_minute_2))

# Next let's compute the mean of first and second means
mean_minute = np.mean([mean_minute_1, mean_minute_2])
print("minute mean: {0}".format(mean_minute))

# Next group the first minute and second minute data sets
data_total = data_minute_1 + data_minute_2

# Compute the mean of the grouped data
mean_total = np.mean(data_total)
print("total mean: {0}".format(mean_total))
print("% diff in means: {0:.2f}".format(((mean_minute - mean_total)/mean_total) * 100.0))
print("--------------------------")
print("")
print("")


print("+++++ Generated Data Example +++++")
print("")

##
## Example with data generated from a normal distribution and
## random number of points
##

# Randomly seed the number generator
seed()


# Generate normally distributed array of random number.
# Each member in the array represents a single minute of data
# received by the Pulse API
minute_data = {} 
for i in range(1,61):
    minute_data[i] = np.random.normal(loc=0.0, scale=1.0, size=randrange(1, 10))

# Compute the means of each of the minute arrays
minute_mean = {}
for key in minute_data:
   # calculate the mean for this minute of data
   minute_mean[key] = np.mean(minute_data[key])

print("+++++ Minute Data Statistics +++++")
for key in minute_data:
    d = minute_data[key]
    print("minute {0}: {1} points, mean: {2}, median: {3}, min: {4}, max: {5}".format(
	    key, len(d), np.mean(d), np.median(d), np.min(d), np.max(d)))
print("----------------------------------")
print("")

# Compute the hourly mean from the minute means
minute_mean_data = [v for v in minute_mean.values()]
hour_min = np.min(minute_mean_data)
hour_max = np.max(minute_mean_data)
hour_range = hour_max - hour_min
hour_mean = np.mean(minute_mean_data)
hour_median = np.mean(minute_mean_data)
print("hour_mean: {0}, hour_median: {1}, hour_min: {2}, hour_max: {3}, hour_range: {4}".format(
	hour_median, hour_mean, hour_min, hour_max, hour_range))

# Collect all the minute data into an hourly array
hour_data = np.array([])
for key in minute_data:
     hour_data = np.append(hour_data, minute_data[key])

total_min = np.min(hour_data)
total_max = np.max(hour_data)
total_range = total_max - total_min
total_mean = np.mean(hour_data)
total_median = np.median(hour_data)

print("min % diff: {0:.2f}, hour_min: {1}, total_min: {2}".format(
	percent_diff(hour_min, total_min), hour_min, total_min))
print("max % diff: {0:.2f}, hour_max: {1}, hour_min: {2}".format(
	percent_diff(hour_max, total_max), hour_max, total_max))
print("range % diff: {0:.2f}, hour_range: {1}, total_range: {2}".format(
	percent_diff(hour_range, total_range), hour_range, total_range))
print("mean % diff: {0:.2f}, hour_mean: {1}, total_mean: {2}".format(
	percent_diff(hour_mean, total_mean), hour_mean, total_mean))
print("median % diff: {0:.2f}, hour_median: {1}, total_median: {2}".format(
	percent_diff(hour_median, total_median), hour_median, total_median))
print("")
print("----------------------------------")
print("")
print("")



