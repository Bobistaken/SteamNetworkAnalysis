import csv

# initialize an array for all 20 weights, tracking [running total, number of elements] for later averaging
pricedifferencebyweight = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]

# open the file storing the edges
with open('data/edges_1000.csv', newline='', encoding='utf-8') as csvfile:
    edgedata = csv.DictReader(csvfile)
    for row in edgedata:
        # make sure both nodes have prices, and that they aren't the same node
        if (row['firstprice'] != '') & (row['secondprice'] != '') & (row['firstid'] != row['secondid']):
            # add the difference between the prices to the running total
            pricedifferencebyweight[int(row['edgeweight']) - 1][0] += abs(int(row['firstprice']) - int(row['secondprice']))
            # increment the counter for later averaging
            pricedifferencebyweight[int(row['edgeweight']) - 1][1] += 1

# initialize our final averages
averagepricedifferencebyweight = []
# track which weight we're checking
count = 1
# initialize a global price difference average
averagepricedifference = [0, 0]

# calculate our average per weight and add to the output array, with -1 marking unrepresented weight
for diff in pricedifferencebyweight:
    if diff[1] != 0:
        averagepricedifferencebyweight.append([diff[0] / diff[1], count])
        # update our global average tracker
        averagepricedifference[0] += diff[0]
        averagepricedifference[1] += diff[1]
    else:
        averagepricedifferencebyweight.append([-1, count])
    count += 1

# print the global average price difference to console
print(averagepricedifference[0] / averagepricedifference[1])

# write our averages to file
with open('data/priceDifferenceByWeight.csv', 'w', newline='') as outputfile:
    diffwriter = csv.writer(outputfile, delimiter=',')
    for diff in averagepricedifferencebyweight:
        diffwriter.writerow(diff)