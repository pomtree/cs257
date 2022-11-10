'''
convert.py
Doug Pham and Tom Pree

Creates csv for each of our tables
'''

import csv

athletes = {}
with open('big_data_file/smaller.csv', errors="ignore") as original_data_file,\
        open('plays.csv', 'w') as plays_file:
    reader = csv.reader(original_data_file)
    writer = csv.writer(plays_file, lineterminator='\n')
    # eat up and ignore the heading row of the data file
    heading_row = next(reader)

    play_id = 0

    game_id = 0

    player_id = 0
    players = []

    teams = []
    teams_dict = {}
    games_count = {}
    ppg_team = {}

    three_pt_makes = []
    three_pt_misses = []

    hook_makes = []
    hook_misses = []

    dunk_makes = []
    dunk_misses = []

    layup_makes = []
    layup_misses = []

    jump_makes = []
    jump_misses = []

    ft_makes = []
    ft_misses = []

    assists = []
    blocks = []
    fouls = []
    fouled_c = []
    rebounds = []
    violations = []
    turnovers = []
    turnovers_caused = []
    
    jb_makes = []
    jb_misses = []

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
            # print('end of game')
            game_id = game_id + 1

            if home_team not in teams_dict:
                teams_dict[home_team] = int(home_score)
                games_count[home_team] = 1
            else:
                teams_dict[home_team] += int(home_score)
                games_count[home_team] += 1

            if away_team not in teams_dict:
                teams_dict[away_team] = int(away_score)
                games_count[away_team] = 1
            else:
                teams_dict[away_team] += int(away_score)
                games_count[away_team] += 1

        active_players = [shooter, assister, blocker, fouler, fouled, rebounder, violation_player, ft_shooter, turnover_player, turnover_causer, jb_home_player, jb_away_player]

        i = 0
        while i < len(active_players):
            if active_players[i] == -1:
                active_players.remove(i) 
            else:
                if not active_players[i] in players:
                    players.append(active_players[i])

                    three_pt_makes.append(0)
                    three_pt_misses.append(0)

                    hook_makes.append(0)
                    hook_misses.append(0)

                    dunk_makes.append(0)
                    dunk_misses.append(0)

                    layup_makes.append(0)
                    layup_misses.append(0)

                    jump_makes.append(0)
                    jump_misses.append(0)

                    assists.append(0)
                    blocks.append(0)
                    fouls.append(0)
                    fouled_c.append(0)
                    rebounds.append(0)
                    violations.append(0)
                    turnovers.append(0)
                    turnovers_caused.append(0)

                    jb_makes.append(0)
                    jb_misses.append(0)

                    ft_makes.append(0)
                    ft_misses.append(0)

                    teams.append(0)

                i = i + 1
            



        if shot_outcome == 'make':
            shot_outcome= 1
        else:
            shot_outcome = 0

        if ft_outcome == 'make':
            ft_outcome= 1
        else:
            ft_outcome= 0

        for player in players:
            index= players.index(player)
      
            if assister == player:
                assists[index] = assists[index] + 1
       
            if blocker == player:
                blocks[index] = blocks[index] + 1
        
            if fouler == player:
                fouls[index] = fouls[index] + 1
          
            if fouled == player:
                fouled_c[index] = fouled_c[index] + 1
          
            if violation_player == player:
                violations[index] = violations[index] + 1
                
            if turnover_player == player:
                turnovers[index] = turnovers[index] + 1
           
            if turnover_causer == player:
                turnovers_caused[index] = turnovers_caused[index] + 1
            
            if jb_away_player == player:
                teams[index] = away_team
                if jb_poss == away_team:
                    jb_makes[index] = jb_makes[index] + 1
                else:
                    jb_misses[index] = jb_misses[index] + 1
            
            if jb_home_player == player:
                teams[index] = home_team
                if jb_poss == home_team:
                    jb_makes[index] = jb_makes[index] + 1
                else:
                    jb_misses[index] = jb_misses[index] + 1

            if ft_shooter == player:
                if ft_outcome == 1:
                    ft_makes[index] = ft_makes[index] + 1
                else:
                    ft_misses[index] = ft_misses[index] + 1

            if shooter == player:
                if len(away_play) > 3:
                    teams[index] = away_team
                if len(home_play) > 3:
                    teams[index] = home_team

                if shot_type == '3-pt jump shot':
                    if shot_outcome == 1:
                        three_pt_makes[index]= three_pt_makes[index] + 1
                    else:
                        three_pt_misses[index]= three_pt_misses[index] + 1

                if shot_type == '2-pt jump shot':
                    if shot_outcome == 1:
                        jump_makes[index]= jump_makes[index] + 1
                    else:
                        jump_misses[index]= jump_misses[index] + 1

                if shot_type == '2-pt hook shot':
                    if shot_outcome == 1:
                        hook_makes[index]= hook_makes[index] + 1
                    else:
                        hook_misses[index]= hook_misses[index] + 1

                if shot_type == '2-pt dunk':
                    if shot_outcome == 1:
                        dunk_makes[index]= dunk_makes[index] + 1
                    else:
                        dunk_misses[index]= dunk_misses[index] + 1

                if shot_type == '2-pt layup':
                    if shot_outcome == 1:
                        layup_makes[index]= layup_makes[index] + 1
                    else:
                        layup_misses[index]= layup_misses[index] + 1


        turnover_team= 0

        if len(home_play) > len(away_play):
            play= home_play # or awayplay
        else:
            play= away_play


        write_row= [play_id, game_id, home_score, away_score, secleft, quarter, shooter, shot_type, shot_outcome, shot_dist, assister, blocker, foul_type, fouler, fouled, rebounder, rebound_type, violation_player, violation_type, turnover_team, ft_shooter, ft_outcome, turnover_player, turnover_type, turnover_cause, turnover_causer, jb_away_player, jb_home_player, jb_poss,  play]

        i= 0
        while i < len(write_row):
            if write_row[i] == '':
                write_row[i]= -1
            i= i + 1


        writer.writerow(write_row)

i= 0
while i < len(players):
    print(players[i])
    if three_pt_makes[i] + three_pt_misses[i] > 0:
        print(three_pt_makes[i]/(three_pt_makes[i] + three_pt_misses[i]))
        print('\t' + str(three_pt_makes[i]) + ' - ' + str(three_pt_misses[i]))
    if layup_makes[i] + layup_misses[i] > 0:
        print(layup_makes[i]/(layup_makes[i] + layup_misses[i]))
    print()
    i= i + 1

for team in teams_dict:
    ppg_team[home_team] = teams_dict[team] / games_count[team]

print(ppg_team)

with open('big_data_file/players.csv',  "w") as player_file:
    writer = csv.writer(player_file, lineterminator='\n')
    i= 0
    while i < len(players):
        real_name = players[i].split('-')
        write_row = [i, players[i], real_name, teams[i], teams[i], three_pt_makes[i] + three_pt_misses[i], three_pt_makes[i], layup_makes[i] + layup_misses[i], layup_makes[i], jump_makes[i] + jump_misses[i], jump_makes[i], hook_makes[i] + hook_misses[i], blocks[i], fouls[i], fouled_c[i], rebounds[i], violations[i], ft_makes[i] + ft_misses[i], ft_makes[i], turnovers[i], turnovers_caused[i], assists[i], jb_makes[i] + jb_misses[i], jb_makes[i]]
        print(write_row)
        print()
        writer.writerow(write_row)
    
        i = i + 1