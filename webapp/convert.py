'''
convert.py
Doug Pham and Tom Pree

Creates csv for each of our tables
'''

import csv

athletes = {}
with open('2019-20_pbp.csv') as original_data_file,\
        open('plays.csv', 'w') as plays_file:
    reader = csv.reader(original_data_file)
    writer = csv.writer(plays_file, lineterminator='\n')
    heading_row = next(reader) # eat up and ignore the heading row of the data file
    for row in reader:
        athlete_id = row[0]
        athlete_name = row[1]
        if athlete_id not in athletes:
            athletes[athlete_id] = athlete_name
            writer.writerow([athlete_id, athlete_name])