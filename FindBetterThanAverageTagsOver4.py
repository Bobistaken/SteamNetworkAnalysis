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

# read our tag pair averages from file, storing any better than the global average. only reads from tag pairs with at least 5 games
with open('data/tagAveragesOver4.csv', newline='', encoding='utf-8') as tagfile:
    tagdata = csv.DictReader(tagfile)
    for row in tagdata:
        bettermetrics = []
        if float(row['averageowners']) > averageowners:
            bettermetrics.append(['owners', float(row['averageowners'])])
            betterowners.append([row['tags'], float(row['averageowners'])])
        if float(row['averagerating']) > averagerating:
            bettermetrics.append(['rating', float(row['averagerating'])])
            betterratings.append([row['tags'], float(row['averagerating'])])
        if float(row['averageprice']) > averageprice:
            bettermetrics.append(['price', float(row['averageprice'])])
            betterprices.append([row['tags'], float(row['averageprice'])])
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
with open('data/betterThanAverageTagsOver4.csv', 'w', newline='') as outputfile:
    tagwriter = csv.writer(outputfile, delimiter=',')
    tagwriter.writerow(['tags', 'owners_rating_price'])
    for pair in tagpairlist:
        tagwriter.writerow([pair[0], pair[1]])

# write better-than-global owner/rating/price averages to file
with open('data/betterThanAverageOwnersOver4.csv', 'w', newline='') as ownerfile:
    ownerwriter = csv.writer(ownerfile, delimiter=',')
    ownerwriter.writerow(['tags', 'owners'])
    for row in betterowners:
        ownerwriter.writerow(row)

with open('data/betterThanAverageRatingsOver4.csv', 'w', newline='') as ratingfile:
    ratingwriter = csv.writer(ratingfile, delimiter=',')
    ratingwriter.writerow(['tags', 'rating'])
    for row in betterratings:
        ratingwriter.writerow(row)

with open('data/betterThanAveragePricesOver4.csv', 'w', newline='') as pricefile:
    pricewriter = csv.writer(pricefile, delimiter=',')
    pricewriter.writerow(['tags', 'price'])
    for row in betterprices:
        pricewriter.writerow(row)