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

    play_id = 0
    for row in reader:
        play_id = play_id + 1
        url = row[0]
        game_type = row[1]
        location = row[2]
        date = row[3]
        time = row[4]
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
        violation_player = row[25]
        violation_type = row[26]
        timeout_team = row[27]
        ft_shooter = row[28]
        ft_outcome = row[29]
        enter_game = row[30]
        leave_rame = row[31]
        turnover_player = row[32]
        turnover_type = row[33]
        turnover_cause = row[34]
        turnover_causer = row[35]
        jb_away_player = row[36]
        jb_home_player = row[37]
        jb_poss = row[38]


        game_id = 0
        turnover_team = 0
        play = home_play # or awayplay

        if shot_outcome == 'make':
            shot_outcome = 1
        else:
            shot_outcome = 0        
            
        if ft_outcome == 'make':
            ft_outcome = 1
        else:
            ft_outcome = 0


        write_row = [play_id, game_id, home_score, away_score, secleft, quarter, shooter, shot_type, shot_outcome, shot_dist, assister, blocker, foul_type, fouler, fouled, rebounder, rebound_type, violation_player, violation_type, turnover_team, ft_shooter, ft_outcome, turnover_player, turnover_type, turnover_cause, turnover_causer, jb_away_player, jb_home_player, jb_poss,  play]

        i = 0
        while i < len(write_row):
            if write_row[i] == '':
                write_row[i] = -1
            i = i + 1
        

        

        writer.writerow(write_row)
