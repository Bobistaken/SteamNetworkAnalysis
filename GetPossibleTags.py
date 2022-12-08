import csv

# initialize a list of all tags
taglist = []
# read our game data from file
with open('data/steamspy_data_1000.csv', newline='', encoding='utf-8') as csvfile:
    steamdata = csv.DictReader(csvfile)
    for row in steamdata:
        # clean our tag info
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

        # store a non-duplicate list of tags that have games
        for tag in tags:
            if tag not in taglist:
                taglist.append(tag)

# write our list of possible tags to file
with open('data/possibleTags.csv', 'w', newline='') as outputfile:
    tagwriter = csv.writer(outputfile, delimiter=',')
    tagwriter.writerow(taglist)