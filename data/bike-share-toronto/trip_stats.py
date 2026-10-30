# trip_stats.py: summary of trip durations in a Bike Share Toronto trips file
filename = "mini-trips.csv"
infile = open(filename)
header = infile.readline()
durations = []

for line in infile:
    line = line.removesuffix('\n')
    row = line.split(',')
    duration = int(row[0])
    durations.append(duration)
infile.close

order = sorted(durations)

print (len(durations))
print(min(durations))
print(max(durations))
print(sum(durations)/len(durations))
print(order[len(durations)//2])