import csv

# initialize an array for all 20 weights, tracking [running total, number of elements] for later averaging
pricedifferencebyweight = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]

# dictate how many edge sets to read
for i in range(100):
    # print progress tracker
    print(i)
    # open a file to read our null edges
    with open('data/Null Models/null_edges_' + str(i) + '.csv', newline='', encoding='utf-8') as csvfile:
        edgedata = csv.DictReader(csvfile)
        # for every edge in our null data, randomize the second node
        for row in edgedata:
            # make sure both nodes have an associated price, and that both nodes are different
            if (row['firstprice'] != '') & (row['secondprice'] != '') & (row['firstid'] != row['secondid']):
                # add the price difference to the running total
                pricedifferencebyweight[int(row['edgeweight']) - 1][0] += abs(int(row['firstprice']) - int(row['secondprice']))
                # increment the number of elements in the sum
                pricedifferencebyweight[int(row['edgeweight']) - 1][1] += 1

# initialize our final averages
averagepricedifferencebyweight = []
# track which weight we're checking
count = 1

# calculate our average per weight and add to the output array, with -1 marking unrepresented weight
for diff in pricedifferencebyweight:
    if diff[1] != 0:
        averagepricedifferencebyweight.append([diff[0] / diff[1], count])
    else:
        averagepricedifferencebyweight.append([-1, count])
    count += 1

# write our averages to file
with open('data/nullPriceDifferenceByWeight.csv', 'w', newline='') as outputfile:
    diffwriter = csv.writer(outputfile, delimiter=',')
    for diff in averagepricedifferencebyweight:
        diffwriter.writerow(diff)