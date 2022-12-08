import csv

# initialize values to calculate averages
averageowners = 0
averagerating = 0
averageprice = 0
numgames = 0

# track the current appid to skip duplicates
currentid = 0

# read game info from file
with open('data/steamspy_data_1000.csv', newline='', encoding='utf-8') as csvfile:
    steamdata = csv.DictReader(csvfile)
    for row in steamdata:
        # check if the current row is duplicated
        if row['appid'] != currentid:
            
            # prevent division by zero, anything with no ratings is safe to skip
            if (int(row['positive']) + int(row['negative'])) > 0:
                # clean the data, cast to int, and add to running total to allow averaging
                averageowners += (int(row['owners'].replace('"', '').replace(',', '').split(' .. ')[0]) + int(row['owners'].replace('"', '').replace(',', '').split(' .. ')[1])) / 2
                averagerating += int(row['positive']) / (int(row['positive']) + int(row['negative']))
                averageprice += int(row['price'])
                # track how many games we're including to divide averages properly
                numgames += 1
            # update the duplicate check
            currentid = row['appid']

# divide our sums by the number of games to get our averages
averageowners /= numgames
averagerating /= numgames
averageprice /= numgames

# write the averages to file
with open('data/globalAverages.csv', 'w', newline='') as averagesfile:
    averagewriter = csv.writer(averagesfile, delimiter=',')
    averagewriter.writerow(['averageowners', 'averagerating', 'averageprice'])
    averagewriter.writerow([averageowners, averagerating, averageprice])