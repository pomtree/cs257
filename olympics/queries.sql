-- List all the NOCs (National Olympic Committees), in alphabetical order by abbreviation. These entities, by the way, are mostly equivalent to countries. But in some cases, you might find that a portion of a country participated in a particular games (e.g. one guy from Newfoundland in 1904) or some other oddball situation.
SELECT DISTINCT noc
FROM athlete_instances
ORDER BY noc;

-- List the names of all the athletes from Jamaica. If your database design allows it, sort the athletes by last name.
SELECT DISTINCT athletes.name_full, athletes.name_last, athletes.name_first
FROM athletes, athlete_instances, linking_table
WHERE athletes.id = linking_table.athlete_id
AND athlete_instances.noc = 'JAM'
AND athlete_instances.id = linking_table.athlete_instance_id
ORDER BY athletes.name_last ASC;

-- List all the medals won by Greg Louganis, sorted by year. Include whatever fields in this output that you think appropriate.
SELECT linking_table.medal, games.year, games.season, games.city, events.category, events.subcategory
FROM linking_table, games, events, athletes
WHERE athletes.id = linking_table.athlete_id
AND games.id = linking_table.game_id
AND events.id = linking_table.event_id
AND athletes.name_first = 'Gregory'
AND athletes.name_last = 'Louganis'
AND NOT linking_table.medal = 'NA'
ORDER BY games.year;

-- List all the NOCs and the number of gold medals they have won, in decreasing order of the number of gold medals.
SELECT COUNT(linking_table.medal), athlete_instances.noc
FROM linking_table, athlete_instances
WHERE linking_table.medal = 'Gold'
AND linking_table.athlete_instance_id = athlete_instances.id
GROUP BY athlete_instances.noc
ORDER BY COUNT(linking_table.medal) DESC;

