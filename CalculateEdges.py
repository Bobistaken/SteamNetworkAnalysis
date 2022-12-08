import csv

# initialize an empty master list of edges
edges = []

# read the game data to compile tag/price/rating/owner info
with open('data/steamspy_data_16000_data.csv', newline='', encoding='utf-8') as csvfile:
    taglist = []
    pricelist = []
    ratinglist = []
    ownerslist = []
    steamdata = csv.DictReader(csvfile)
    for row in steamdata:
        tagdata = row['tags'].replace('{', '').replace('}', '').split(', ')
        tags = []
        for tag in tagdata:
            tagheader = tag[1:]
            tagend = 0
            for char in tagheader:
                if char == '\'':
                    break
                tagend += 1
            tags.append(tagheader[:tagend])
        owners = row['owners'].replace('"', '').split(' .. ')
        taglist.append([row['appid'], tags])
        pricelist.append(row['price'])
        ratinglist.append([row['positive'], row['negative']])
        ownerslist.append(owners)

    # iterate over the first 1000 edges, calculating weight for each
    for i in range(1000):
        for j in range(1000 - i - 1):
            edgeweight = 0
            for tag in taglist[i][1]:
                if taglist[i + j + 1][1].count(tag):
                    edgeweight += 1

            # if the edge has any shared tags, add it to the master list
            if edgeweight > 0:
                edges.append([taglist[i][0], taglist[i + j + 1][0], edgeweight, pricelist[i], pricelist[i + j + 1], ratinglist[i], ratinglist[i + j + 1], ownerslist[i], ownerslist[i + j + 1]])

            # give some feedback while the program is running to track progress
            if (i % 100 == 0) & (j == 0):
                print(i)

# write the list of edges to disk
with open('data/edges_1000.csv', 'w', newline='') as outputfile:
    edgewriter = csv.writer(outputfile, delimiter=',')
    edgewriter.writerow(['firstid', 'secondid', 'edgeweight', 'firstprice', 'secondprice', 'firstratings', 'secondratings', 'firstowners', 'secondowners'])
    for edge in edges:
        edgewriter.writerow(edge)