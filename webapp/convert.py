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
    # eat up and ignore the heading row of the data file
    heading_row = next(reader)
    for row in reader:
        athlete_id = row[0]
        athlete_name = row[1]

        winning_team = row[5]
        quarter = row[6]
        secleft = row[7]
        away_team = row[8]
        away_play = row[9]
        away_score = row[10]
        home_team = row[11]
        home_play = row[12]
        home_score = row[13]
        shooter = row[14]
        shot_type = row[15]
        shot_outcome = row[16]
        shot_dist = row[17]
        assister = row[18]
        blocker = row[19]
        foul_type = row[20]
        fouler = row[21]
        fouled = row[22]
        rebounder = row[23]
        rebound_type = row[24]
        violoation_player = row[25]
        violation_type = row[26]
        timeout_team = row[27]
        ft_shooter = row[28]
        ft_num = row[29]
        enter_game = row[30]
        leave_rame = row[31]
        turnover_player = row[32]
        turnover_type = row[33]
        turnover_cause = row[34]
        turnover_causer = row[35]
        jb_away_player = row[36]
        jb_home_player = row[37]
        jb_poss = row[38]

if athlete_id not in athletes:
    athletes[athlete_id] = athlete_name
    writer.writerow([athlete_id, athlete_name])
