import csv, random

# initialize a dict of what nodes exist
possiblenodes = {}

# read game info from file
with open('data/steamspy_data_1000.csv', newline='', encoding='utf-8') as nodefile:
    nodedata = csv.DictReader(nodefile)
    for node in nodedata:
        # if the current game hasn't been added to the dict of games, add it. this prevents duplicates
        if node['appid'] not in possiblenodes.keys():
            # clean and store the relevant info
            possiblenodes[node['appid']] = [node['appid'], node['price'], [node['positive'], node['negative']], node['owners'].replace('"', '').split(' .. ')]

# read real edge data from file
with open('data/edges_1000.csv', newline='', encoding='utf-8') as edgefile:
    edgedata = csv.DictReader(edgefile)
    # store the edge data for repeat iteration
    iteredgedata = []
    for edge in edgedata:
        iteredgedata.append(edge)
    
    # generate many sets of random edges
    for i in range(100):
        # initialize the new set of edges
        newedges = []
        # randomize a version of each real edge
        for edge in iteredgedata:
            # print feedback to track progress
            print(str(i) + '  ' + edge['firstid'])
            # randomly select a node from the list
            nodeselect = random.choice(list(possiblenodes.items()))
            # randomize the second node in the edge
            newedges.append([edge['firstid'], nodeselect[0], edge['edgeweight'], edge['firstprice'], nodeselect[1][1], edge['firstratings'], nodeselect[1][2], edge['firstowners'], nodeselect[1][3]])

        # write the new null edge set to file
        with open('data/Null Models/null_edges_' + str(i) + '.csv', 'w', newline='') as outputfile:
            nullwriter = csv.writer(outputfile, delimiter=',')
            nullwriter.writerow(['firstid', 'secondid', 'edgeweight', 'firstprice', 'secondprice', 'firstratings', 'secondratings', 'firstowners', 'secondowners'])
            for edge in newedges:
                nullwriter.writerow(edge)