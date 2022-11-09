'''
convert.py
Doug Pham and Tom Pree

Creates csv for each of our tables
'''

import csv

athletes = {}
with open('big_data_file/smaller.csv') as original_data_file,\
        open('plays.csv', 'w') as plays_file:
    reader = csv.reader(original_data_file)
    writer = csv.writer(plays_file, lineterminator='\n')
    # eat up and ignore the heading row of the data file
    heading_row = next(reader)

    play_id = 0

    game_id = 0

    player_id = 0
    players = []
    three_pt_makes = []
    three_pt_misses = []




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

        if away_play == 'End of Game':
            #print('end of game')
            game_id = game_id + 1

        if not shooter in players:
            players.append(shooter)
            three_pt_makes.append(0)
            three_pt_misses.append(0)
        
        index = players.index(shooter)

        if shot_outcome == 'make':
            shot_outcome = 1
        else:
            shot_outcome = 0        
            
        if ft_outcome == 'make':
            ft_outcome = 1
        else:
            ft_outcome = 0



        if shot_type == '3-pt jump shot':
            if shot_outcome == 1:
                three_pt_makes[index] = three_pt_makes[index] + 1
            else:
                three_pt_misses[index] = three_pt_misses[index] + 1

        
        turnover_team = 0

        if len(home_play) > len(away_play):
            play = home_play # or awayplay
        else:
            play = away_play


        write_row = [play_id, game_id, home_score, away_score, secleft, quarter, shooter, shot_type, shot_outcome, shot_dist, assister, blocker, foul_type, fouler, fouled, rebounder, rebound_type, violation_player, violation_type, turnover_team, ft_shooter, ft_outcome, turnover_player, turnover_type, turnover_cause, turnover_causer, jb_away_player, jb_home_player, jb_poss,  play]

        i = 0
        while i < len(write_row):
            if write_row[i] == '':
                write_row[i] = -1
            i = i + 1
        

        

        writer.writerow(write_row)

i = 0
while i < len(players):
    print(players[i])
    print(three_pt_makes[i]/(three_pt_makes[i] + three_pt_misses[i] + 0.00001))
    i = i + 1