import csv

# initialize storage lists
taglist = []
steamspydata = []

# read what tags to consider from file
with open('data/possibleTags.csv', newline='', encoding='utf-8') as tagfile:
    tagdata = csv.reader(tagfile, delimiter=',')
    for row in tagdata:
        for tag in row:
            taglist.append(tag)

# read our game data from file
with open('data/steamspy_data_1000.csv', newline='', encoding='utf-8') as nodefile:
    nodedata = csv.DictReader(nodefile)
    # store our game data to a list
    for row in nodedata:
        steamspydata.append(row)

    # for each tag, compare it to every tag it hasn't been compared to yet
    for i in range(len(taglist)):
        # print feedback to track progress
        print(taglist[i])
        # the tag needs to be compared to every tag after it in the list
        for j in range((len(taglist) - i - 1)):
            # print feedback to track progress
            print('    ' + taglist[j + i + 1])
            # initialize a list to store tag pair stats
            stats = []
            # start building the filename for the tag pair
            filename = 'tagData_'
            # find the names of the tag pair
            tagcheck = [taglist[i], taglist[j + i + 1]]
            # add the current tags to the filename
            for tag in tagcheck:
                filename += tag + '_'
            # find every game that has both tags
            for row in steamspydata:
                # clean the game info tags for comparison
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

                # check if the game has both tags
                tagsinrow = True
                for tag in tagcheck:
                    if tag in tags:
                        continue
                    else:
                        tagsinrow = False
                        break

                # if the game has both tags, add the currently considered game stats to the list
                if tagsinrow:
                    # clean the owner range
                    owners = row['owners'].replace('"', '').replace(',', '').split(' .. ')
                    # find the midpoint of the owner range
                    ownermidpoint = (int(owners[0]) + int(owners[1])) // 2
                    # store the relevant info of the current game
                    stats.append([row['appid'], ownermidpoint, row['average_forever'], row['median_forever'], row['positive'], row['negative'], row['price']])

            # if the tag pair has any games, write their info to file
            if len(stats) > 0:
                with open('data/Tag Data/' + filename + '.csv', 'w', newline='') as outputfile:
                    tagwriter = csv.writer(outputfile, delimiter=',')
                    tagwriter.writerow(['appid', 'ownermidpoint', 'average_forever', 'median_forever', 'positive', 'negative', 'price'])
                    for row in stats:
                        tagwriter.writerow(row)
