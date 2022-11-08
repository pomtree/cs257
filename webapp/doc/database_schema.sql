CREATE TABLE plays (id SERIAL, game_id integer, current_score_h integer, current_score_a integer, secs_left integer, qrt integer, shooter integer, shot_type integer, shot_outcome boolean, shot_dist integer, asstr integer, blkr integer, foul_type integer, fouler integer, fouled integer, rebounder integer, rb_type integer, v_player integer, v_type integer, to_team integer, ft_shooter integer, ft_outcome boolean, to_player integer, to_type integer, to_cause integer, to_causer integer, jb_a_player integer, jb_h_player integer, jb_pos integer, description text);

CREATE TABLE players (id SERIAL, csv_id text, name text, three_attempts integer, three_makes integer, lap_attempts integer, layup_makes integer, jumper_attempts integer, jumper_makes integer, hook_attempts integer, hook_makes integer, blocks integer, fouls integer, fouled integer, rbs integer, vs integer, ft_attempts integer, ft_makes integer, tos integer, tos_caused integer);

CREATE TABLE teams (id SERIAL, abbriviation text, name text, wins integer, losses integer, h_wins integer, a_wins integer, ot_wins integer, ot_losses integer);

CREATE TABLE games(id SERIAL, type boolean, loc text, date text, time text, winner integer, loser integer, home integer, away integer, w_score integer, l_score integer, qrts integer);

CREATE TABLE teams_players(id SERIAL, team_id integer, player_id integer);