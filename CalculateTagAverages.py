import csv, os

# open a file to write our averages
with open('data/tagAveragesOver4.csv', 'w', newline='') as averagesfile:
    averagewriter = csv.writer(averagesfile, delimiter=',')
    averagewriter.writerow(['tags', 'averageowners', 'averagerating', 'averageprice'])
    
    # check each file in our tag data
    for file in os.listdir('data/Tag Data'):
        # print feedback so progress can be tracked
        print(file)
        # open the file we're currently considering
        with open('data/Tag Data/' + file, newline='', encoding='utf-8') as csvfile:
            # if the file represents a tag pair, store the tags. else skip to the next file
            if len(file.split('_')) > 1:
                tags = [file.split('_')[1], file.split('_')[2]]
            else:
                continue
            # initialize our averages and game counter
            owners = 0
            ratings = 0
            prices = 0
            games = 0
            tagdata = csv.DictReader(csvfile)
            # update our tracked averages
            for row in tagdata:
                owners += int(row['ownermidpoint'])
                ratings += int(row['positive']) / (int(row['positive']) + int(row['negative']))
                prices += int(row['price'])
                games += 1

            # divide by the number of games to get our averages
            owners /= games
            ratings /= games
            prices /= games

            # for each pair that has at least 5 games, write the averages to file
            if games > 4:
                averagewriter.writerow([tags, owners, ratings, prices])