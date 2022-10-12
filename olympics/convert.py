# Tom Pree 10/11/22 CS 257

import csv

# print('hello!')
print('reading input csv file...')

with open('athlete_events.csv', 'r') as file:
    reader = csv.reader(file)

    i = 0
    prev_id = -1
    years = []
    athletes = []
    athlete_instances = []
    games = []
    events = []
    sport_events = []
    links = []

    for row in reader:
        if i == 0:
            # print('i = 0')
            i = i + 1
            continue
        else:
            i = i + 1

        # initialize variables:
        ai_id = i - 1  # athlete instance ID
        a_id = int(row[0])
        name_full = row[1]
        name_first = row[1].split(' ')[0]
        name_last = row[1].split(' ')[-1]
        noc = row[7]
        year = int(row[9])
        season = row[10]
        city = row[11]
        sport = row[12]
        event = row[13]
        medal = row[14]

        # new athlete instance (each row)
        athlete_instances.append([ai_id, a_id, noc])

        # new athlete
        if a_id != prev_id:
            athletes.append([int(a_id), name_full, name_first, name_last])

        # new olympics
        if year not in years:
            years.append(year)
            games.append([len(years), year, season, city])
            games_id = len(games)
        else:
            games_id = years.index(year) + 1

        # new event
        if sport + event not in sport_events:
            sport_events.append(sport + event)
            events.append([len(events), sport, event])
            event_id = len(events)
        else:
            event_id = sport_events.index(sport + event)

        links.append([a_id, ai_id, event_id, games_id, medal])

        prev_id = a_id
        # if i > 100:
        #     break

print('done!')
print('begin writing output csv files...')

print('\twriting athletes...')
with open('athletes.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(athletes)

print('\twriting events...')
with open('events.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(events)

print('\twriting games...')
with open('games.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(games)

print('\twriting linking table...')
with open('linking_table.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(links)

print('\twriting athlete instances...')
with open('athlete_instances.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(athlete_instances)

print('done!')


# print(years)
# print(athletes)
# print(athlete_instances)
# print(games)
# print(events)
# print(links)
