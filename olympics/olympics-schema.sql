CREATE TABLE athletes (id SERIAL, name_full text, name_first text, name_last text);

CREATE TABLE athlete_instances (id SERIAL, athlete_id integer, noc text);

CREATE TABLE events (id SERIAL, category text, subcategory text);

CREATE TABLE games (id SERIAL, year integer, season text, city text);

CREATE TABLE linking_table (athlete_id integer, athlete_instance_id integer, event_id integer, game_id integer, medal text);
