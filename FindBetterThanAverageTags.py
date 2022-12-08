import csv

# initialize variables for storing above-global averages
tagpairlist = []
betterowners = []
betterratings = []
betterprices = []
# initialize variables to store global averages
averageowners = 0
averagerating = 0
averageprice = 0

# read our global averages from file
with open('data/globalAverages.csv', newline='', encoding='utf-8') as csvfile:
    globaldata = csv.DictReader(csvfile)
    for row in globaldata:
        averageowners = float(row['averageowners'])
        averagerating = float(row['averagerating'])
        averageprice = float(row['averageprice'])

# read our tag pair averages from file, storing any better than the global average
with open('data/tagAverages.csv', newline='', encoding='utf-8') as tagfile:
    tagdata = csv.DictReader(tagfile)
    for row in tagdata:
        bettermetrics = []
        if float(row['averageowners']) > averageowners:
            bettermetrics.append(['owners', float(row['averageowners'])])
            betterowners.append([row['tags'], float(row['averageowners']) - averageowners])
        if float(row['averagerating']) > averagerating:
            bettermetrics.append(['rating', float(row['averagerating'])])
            betterratings.append([row['tags'], float(row['averagerating']) - averagerating])
        if float(row['averageprice']) > averageprice:
            bettermetrics.append(['price', float(row['averageprice'])])
            betterprices.append([row['tags'], float(row['averageprice']) - averageprice])
        if len(bettermetrics) > 0:
            tagpairlist.append([row['tags'], bettermetrics])

# function to let us sort our lists by second element instead of first
def returnSecond(elem):
    return elem[1]

# sort our lists, highest average first
betterowners.sort(key=returnSecond, reverse=True)
betterratings.sort(key=returnSecond, reverse=True)
betterprices.sort(key=returnSecond, reverse=True)

# write all better-than-global averages to file
with open('data/betterThanAverageTags.csv', 'w', newline='') as outputfile:
    tagwriter = csv.writer(outputfile, delimiter=',')
    tagwriter.writerow(['tags', 'difference'])
    for pair in tagpairlist:
        tagwriter.writerow([pair[0], pair[1]])

# write better-than-global owner/rating/price averages to file
with open('data/betterThanAverageOwners.csv', 'w', newline='') as ownerfile:
    ownerwriter = csv.writer(ownerfile, delimiter=',')
    ownerwriter.writerow(['tags', 'difference'])
    for row in betterowners:
        ownerwriter.writerow(row)

with open('data/betterThanAverageRatings.csv', 'w', newline='') as ratingfile:
    ratingwriter = csv.writer(ratingfile, delimiter=',')
    ratingwriter.writerow(['tags', 'difference'])
    for row in betterratings:
        ratingwriter.writerow(row)

with open('data/betterThanAveragePrices.csv', 'w', newline='') as pricefile:
    pricewriter = csv.writer(pricefile, delimiter=',')
    pricewriter.writerow(['tags', 'difference'])
    for row in betterprices:
        pricewriter.writerow(row)