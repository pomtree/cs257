'''
convert.py
Doug Pham and Tom Pree
Creates csv for each of our tables
'''
import csv

# athletes = {}

# read_file = 'big_data_file/smaller.csv'
# read_file = 'C:\\Users\\Thomas\\Desktop\\cs257\\cs257 repo - Copy\\webapp_new\\2019-20_pbp.csv'
# read_file = '/mnt/c/Users/Thomas/Desktop/cs257/cs257 repo - Copy/webapp_new/2019-20_pbp.csv'

# with open("big_data_file/smaller.csv", errors="ignore") as original_data_file,\
#         open('plays.csv', 'w') as plays_file:
#     reader = csv.reader(original_data_file)
#     writer = csv.writer(plays_file, lineterminator='\n')
#     # eat up and ignore the heading row of the data file
#     heading_row = next(reader)
#     play_id = 0
#     game_id = 0
#     player_id = 0
#     players = []
#     ppg_team = {}
#     teams_ppg_dict = {}
#     games_count = {}
#     reb_team = {}
#     teams_rebounds = {}
#     three_pt_makes = []
#     three_pt_misses = []
#     hook_makes = []
#     hook_misses = []
#     dunk_makes = []
#     dunk_misses = []
#     layup_makes = []
#     layup_misses = []
#     jump_makes = []
#     jump_misses = []
#     ft_makes = []
#     ft_misses = []
#     assists = []
#     blocks = []
#     fouls = []
#     fouled_c = []
#     rebounds = []
#     violations = []
#     turnovers = []
#     turnovers_caused = []

#     jb_makes = []
#     jb_misses = []
#     teams = []
#     for row in reader:
#         play_id = play_id + 1
#         url = row[0]
#         game_type = row[1]
#         location = row[2]
#         date = row[3]
#         time = row[4]
#         winning_team = row[5]
#         quarter = row[6]
#         secleft = row[7]
#         away_team = row[8]
#         away_play = row[9]
#         away_score = row[10]
#         home_team = row[11]
#         home_play = row[12]
#         home_score = row[13]
#         shooter = row[14]
#         shot_type = row[15]
#         shot_outcome = row[16]
#         shot_dist = row[17]
#         assister = row[18]
#         blocker = row[19]
#         foul_type = row[20]
#         fouler = row[21]
#         fouled = row[22]
#         rebounder = row[23]
#         rebound_type = row[24]
#         violation_player = row[25]
#         violation_type = row[26]
#         timeout_team = row[27]
#         ft_shooter = row[28]
#         ft_outcome = row[29]
#         enter_game = row[30]
#         leave_rame = row[31]
#         turnover_player = row[32]
#         turnover_type = row[33]
#         turnover_cause = row[34]
#         turnover_causer = row[35]
#         jb_away_player = row[36]
#         jb_home_player = row[37]
#         jb_poss = row[38]

#         if play_id % 5000 == 0:
#             print(play_id)

#         active_players = [shooter, assister, blocker, fouler, fouled, rebounder, violation_player,
#                           ft_shooter, turnover_player, turnover_causer, jb_home_player, jb_away_player]

#         i = 0
#         while i < len(active_players):
#             if active_players[i] == -1:
#                 active_players.remove(i)
#             else:
#                 if not active_players[i] in players:
#                     players.append(active_players[i])
#                     three_pt_makes.append(0)
#                     three_pt_misses.append(0)
#                     hook_makes.append(0)
#                     hook_misses.append(0)
#                     dunk_makes.append(0)
#                     dunk_misses.append(0)
#                     layup_makes.append(0)
#                     layup_misses.append(0)
#                     jump_makes.append(0)
#                     jump_misses.append(0)
#                     assists.append(0)
#                     blocks.append(0)
#                     fouls.append(0)
#                     fouled_c.append(0)
#                     rebounds.append(0)
#                     violations.append(0)
#                     turnovers.append(0)
#                     turnovers_caused.append(0)
#                     jb_makes.append(0)
#                     jb_misses.append(0)
#                     ft_makes.append(0)
#                     ft_misses.append(0)
#                     teams.append(0)

#                 i = i + 1

#         if shot_outcome == 'make':
#             shot_outcome = 1
#         else:
#             shot_outcome = 0
#         if ft_outcome == 'make':
#             ft_outcome = 1
#         else:
#             ft_outcome = 0
#         for player in players:
#             index = players.index(player)

#             if assister == player:
#                 assists[index] = assists[index] + 1

#             if blocker == player:
#                 blocks[index] = blocks[index] + 1

#             if fouler == player:
#                 fouls[index] = fouls[index] + 1

#             if fouled == player:
#                 fouled_c[index] = fouled_c[index] + 1

#             if violation_player == player:
#                 violations[index] = violations[index] + 1

#             if turnover_player == player:
#                 turnovers[index] = turnovers[index] + 1

#             if turnover_causer == player:
#                 turnovers_caused[index] = turnovers_caused[index] + 1

#             if jb_away_player == player:
#                 teams[index] = away_team
#                 if jb_poss == away_team:
#                     jb_makes[index] = jb_makes[index] + 1
#                 else:
#                     jb_misses[index] = jb_misses[index] + 1

#             if jb_home_player == player:
#                 teams[index] = home_team
#                 if jb_poss == home_team:
#                     jb_makes[index] = jb_makes[index] + 1
#                 else:
#                     jb_misses[index] = jb_misses[index] + 1
#             if ft_shooter == player:
#                 if ft_outcome == 1:
#                     ft_makes[index] = ft_makes[index] + 1
#                 else:
#                     ft_misses[index] = ft_misses[index] + 1
#             if shooter == player:
#                 if len(away_play) > 3:
#                     teams[index] = away_team
#                 if len(home_play) > 3:
#                     teams[index] = home_team
#                 if shot_type == '3-pt jump shot':
#                     if shot_outcome == 1:
#                         three_pt_makes[index] = three_pt_makes[index] + 1
#                     else:
#                         three_pt_misses[index] = three_pt_misses[index] + 1
#                 if shot_type == '2-pt jump shot':
#                     if shot_outcome == 1:
#                         jump_makes[index] = jump_makes[index] + 1
#                     else:
#                         jump_misses[index] = jump_misses[index] + 1
#                 if shot_type == '2-pt hook shot':
#                     if shot_outcome == 1:
#                         hook_makes[index] = hook_makes[index] + 1
#                     else:
#                         hook_misses[index] = hook_misses[index] + 1
#                 if shot_type == '2-pt dunk':
#                     if shot_outcome == 1:
#                         dunk_makes[index] = dunk_makes[index] + 1
#                     else:
#                         dunk_misses[index] = dunk_misses[index] + 1
#                 if shot_type == '2-pt layup':
#                     if shot_outcome == 1:
#                         layup_makes[index] = layup_makes[index] + 1
#                     else:
#                         layup_misses[index] = layup_misses[index] + 1
#         turnover_team = 0
#         if len(home_play) > len(away_play):
#             play = home_play  # or awayplay
#         else:
#             play = away_play
#         write_row = [play_id, game_id, home_score, away_score, secleft, quarter, shooter, shot_type, shot_outcome, shot_dist, assister, blocker, foul_type, fouler, fouled, rebounder, rebound_type,
#                      violation_player, violation_type, turnover_team, ft_shooter, ft_outcome, turnover_player, turnover_type, turnover_cause, turnover_causer, jb_away_player, jb_home_player, jb_poss,  play]
#         i = 0
#         while i < len(write_row):
#             if write_row[i] == '':
#                 write_row[i] = -1
#             i = i + 1
#         writer.writerow(write_row)
# i = 0
# while i < len(players):
#     print(players[i])
#     print(three_pt_makes[i]/(three_pt_makes[i] + three_pt_misses[i] + 0.00001))
#     print(layup_makes[i]/(layup_makes[i] + layup_misses[i] + 0.00001))
#     i = i + 1


#     if three_pt_makes[i] + three_pt_misses[i] > 0:
#         print(three_pt_makes[i]/(three_pt_makes[i] + three_pt_misses[i]))
#         print('\t' + str(three_pt_makes[i]) + ' - ' + str(three_pt_misses[i]))
#     if layup_makes[i] + layup_misses[i] > 0:
#         print(layup_makes[i]/(layup_makes[i] + layup_misses[i]))
#     print()
#     i = i + 1





teams_assists = {}
teams_rebounds = {}
team_abr = {}
small = "smaller"
big = "2019-20_pbp"
with open("big_data_file/"+ big +".csv", errors="ignore") as original_data_file,\
        open('teams.csv', 'w') as teams_file:
    reader = csv.reader(original_data_file)
    writer = csv.writer(teams_file, lineterminator='\n')
    # eat up and ignore the heading row of the data file
    heading_row = next(reader)
    for row in reader:

        quarter = row[6]
        away_play = row[9]
        away_score = row[10]
        winning_team = row[5]
        away_team = row[8]
        home_team = row[11]
        home_score = row[13]
        home_play = row[12]
        rebounder = row[23]
        assister = row[18]


        # Teams number of rebounds for one game
        if home_team not in teams_rebounds:
            teams_rebounds[home_team] = 0
        elif rebounder != "" and home_play != "":
            teams_rebounds[home_team] += 1

        if away_team not in teams_rebounds:
            teams_rebounds[away_team] = 0
        elif rebounder != "" and away_play != "":
            teams_rebounds[away_team] += 1

        # Teams number of assists for one game
        if home_team not in teams_assists:
            teams_assists[home_team] = 0
        elif assister != "" and home_play != "":
            teams_assists[home_team] += 1

        if away_team not in teams_assists:
            teams_assists[away_team] = 0
        elif assister != "" and away_play != "":
            teams_assists[away_team] += 1


        # Keeps track of teams games and whether they won at home or not
        # Also accounts for overtime wins
        ot_win = 0
        ot_loss = 0
        if away_play == "End of Game":

            home_team_full_name = ""
            away_team_full_name = ""
            if away_team == "ATL":
                away_team_full_name = "Atlanta Hawks"
            elif home_team == "ATL":
                home_team_full_name = "Atlanta Hawks"
            if away_team == "BRK":
                away_team_full_name = "Brooklyn Nets" 
            elif home_team == "BRK":
                home_team_full_name = "Brooklyn Nets"
            if away_team == "BOS":
                away_team_full_name = "Boston Celtics"
            elif home_team == "BOS":
                home_team_full_name = "Boston Celtics"
            if away_team == "CHO":
                away_team_full_name = "Charlotte Hornets"
            elif home_team == "CHO":
                home_team_full_name = "Charlotte Hornets"
            if away_team == "CHI":
                away_team_full_name = "Chicago Bulls"
            elif home_team == "CHI":
                home_team_full_name = "Chicago Bulls"
            if away_team == "CLE":
                away_team_full_name = "Cleveland Cavaliers"
            elif home_team == "CLE":
                home_team_full_name = "Cleveland Cavaliers"
            if away_team == "DAL":
                away_team_full_name = "Dallas Mavericks"
            elif home_team == "DAL":
                home_team_full_name = "Dallas Mavericks"
            if away_team == "DEN":
                away_team_full_name = "Denver Nuggets"
            elif home_team == "DEN":
                home_team_full_name = "Denver Nuggets"
            if away_team == "DET":
                away_team_full_name = "Detroit Pistons"
            elif home_team == "DET":
                home_team_full_name = "Detroit Pistons"
            if away_team == "GSW":
                away_team_full_name = "Golden State Warriors"
            elif home_team == "GSW":
                home_team_full_name = "Golden State Warriors"
            if away_team == "HOU":
                away_team_full_name = "Houston Rockets"
            elif home_team == "HOU":
                home_team_full_name = "Houston Rockets"
            if away_team == "IND":
                away_team_full_name = "Indiana Pacers"
            elif home_team == "IND":
                home_team_full_name = "Indiana Pacers"
            if away_team == "LAC":
                away_team_full_name = "Los Angeles Clippers"
            elif home_team == "LAC":
                home_team_full_name = "Los Angeles Clippers"
            if away_team == "LAL":
                away_team_full_name = "Los Angeles Lakers"
            elif home_team == "LAL":
                home_team_full_name = "Los Angeles Lakers"
            if away_team == "MEM":
                away_team_full_name = "Memphis Grizzlies"
            elif home_team == "MEM":
                home_team_full_name = "Memphis Grizzlies"
            if away_team == "MIA":
                away_team_full_name = "Miami Heat"
            elif home_team == "MIA":
                home_team_full_name = "Miami Heat"
            if away_team == "MIL":
                away_team_full_name = "Milwaukee Bucks"
            elif home_team == "MIL":
                home_team_full_name = "Milwaukee Bucks"
            if away_team == "MIN":
                away_team_full_name = "Minnesota Timberwolves"
            elif home_team == "MIN":
                home_team_full_name = "Minnesota Timberwolves"
            if away_team == "NOP":
                away_team_full_name = "New Orleans Pelicans"
            elif home_team == "NOP":
                home_team_full_name = "New Orleans Pelicans"
            if away_team == "NYK":
                away_team_full_name = "New York Knicks"
            elif home_team == "NYK":
                home_team_full_name = "New York Knicks"
            if away_team == "OKC":
                away_team_full_name = "Oklahoma City Thunder"
            elif home_team == "OKC":
                home_team_full_name = "Oklahoma City Thunder"
            if away_team == "ORL":
                away_team_full_name = "Orlando Magic"
            elif home_team == "ORL":
                home_team_full_name = "Orlando Magic"
            if away_team == "PHI":
                away_team_full_name = "Philadelphia 76ers"
            elif home_team == "PHI":
                home_team_full_name = "Philadelphia 76ers"
            if away_team == "PHO":
                away_team_full_name = "Phoenix Suns"
            elif home_team == "PHO":
                home_team_full_name = "Phoenix Suns"
            if away_team == "POR":
                away_team_full_name = "Portland Trail Blazers"
            elif home_team == "POR":
                home_team_full_name = "Portland Trail Blazers"
            if away_team == "SAC":
                away_team_full_name = "Sacramento Kings"
            elif home_team == "SAC":
                home_team_full_name = "Sacramento Kings"
            if away_team == "SAS":
                away_team_full_name = "San Antonio Spurs"
            elif home_team == "SAS":
                home_team_full_name = "San Antonio Spurs"
            if away_team == "TOR":
                away_team_full_name = "Toronto Raptors"
            elif home_team == "TOR":
                home_team_full_name = "Toronto Raptors"
            if away_team == "UTA":
                away_team_full_name = "Utah Jazz"
            elif home_team == "UTA":
                home_team_full_name = "Utah Jazz"
            if away_team == "WAS":
                away_team_full_name = "Washington Wizards"
            elif home_team == "WAS":
                home_team_full_name = "Washington Wizards"
            

            if winning_team == home_team:
                home_team_win = 1
                home_team_loss = 0
                if int(quarter) > 4:
                    ot_win = home_team_win
                    ot_loss = home_team_loss
            else:
                home_team_win = 0
                home_team_loss = 1
                if int(quarter) > 4:
                    ot_win = home_team_win
                    ot_loss = home_team_loss

        

            writer.writerow([home_team, home_team_full_name, home_team_win, home_team_loss, home_team_win, home_team_loss, 0, 0, ot_win, ot_loss, home_score, teams_rebounds[home_team], teams_assists[home_team]])


        # Keeps track of teams games and whether they won at away or not
        # Also accounts for overtime wins

            if winning_team == away_team:
                away_team_win = 1
                away_team_loss = 0
                if int(quarter) > 4:
                    ot_win = away_team_win
                    ot_loss = away_team_loss
            else:
                away_team_win = 0
                away_team_loss = 1
                if int(quarter) > 4:
                    ot_win = away_team_win
                    ot_loss = away_team_loss
                    
            writer.writerow([away_team, away_team_full_name, away_team_win, away_team_loss, 0, 0, away_team_win, away_team_loss, ot_win, ot_loss, away_score, teams_rebounds[away_team], teams_assists[away_team]])


            #Resets dictionary of stats for the next game
            teams_rebounds[home_team] = 0
            teams_rebounds[away_team] = 0

            teams_assists[home_team] = 0
            teams_assists[away_team] = 0
