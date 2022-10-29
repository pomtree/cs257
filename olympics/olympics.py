#Thomas Pree
#10/20/2022 CS 257 Carleton College


import argparse
import sys
import psycopg2
import config


#From Jeff's repo:
def get_connection():
    try:
        return psycopg2.connect(database=config.database,
                                user=config.user,
                                password=config.password)
    except Exception as e:
        print(e, file=sys.stderr)
        exit()

#Modified from Jeff's get_authors:
#prints all the athletes associated at one point with given NOC
def get_athletes_by_noc(noc):
    print("Athletes from " + noc + ":")
    #athletes = []
    try:
        connection = get_connection()
        cursor = connection.cursor()
        query = '''
            SELECT DISTINCT athletes.name_full
            FROM athletes, athlete_instances, linking_table
            WHERE athletes.id = linking_table.athlete_id
            AND athlete_instances.noc =\'''' + noc + '''\'
            AND athlete_instances.id = linking_table.athlete_instance_id
            ORDER BY athletes.name_full ASC'''
        cursor.execute(query)
        for row in cursor:
            name_full = row[0]
            print('\t' + name_full)
            #athletes.append(f'{given_name} {surname}')

    except Exception as e:
        print(e, file=sys.stderr)

    connection.close()
    #return athletes

#prints NOCs sorted by gold medals one in games held between start-end years.
def most_medals_years(start, end):
    print("NOCs by most gold medals won (individuals, not sports) in year range:")
    try:
        connection = get_connection()
        cursor = connection.cursor()
        query = '''
            SELECT COUNT(linking_table.medal), athlete_instances.noc
            FROM linking_table, athlete_instances, games
            WHERE linking_table.medal = 'Gold'
            AND games.year >= ''' + str(start) + '''
            AND games.year <= ''' + str(end) + '''
            AND linking_table.athlete_instance_id = athlete_instances.id
            AND linking_table.game_id = games.id
            GROUP BY athlete_instances.noc
            ORDER BY COUNT(linking_table.medal) DESC'''
        cursor.execute(query)
        for row in cursor:
            count = str(row[0])
            noc = row[1]
            print('\t' + noc + ": " + count)
            #athletes.append(f'{given_name} {surname}')

    except Exception as e:
        print(e, file=sys.stderr)

    connection.close()
    #return athletes


#initialize arg parser
parser = argparse.ArgumentParser(description='''
usage: olympics.py [--noc NOC] [--most_medals] [--start start_year] [--end_year]\n
NOC lists all athletes associated with that NOC.\n
Most Medals lists all NOCs, sorted by the number of gold medals they've won
    Optinal arguments:
    Start year: the earilest year to count gold medals in Most Medals.\n
    End year: the latest year to count gold medals in Most Medals.\n
''')

parser.add_argument('--noc', type=str)
parser.add_argument('--most_medals', action='store_true')
parser.add_argument('--start', type=int)
parser.add_argument('--end', type=int)

args = parser.parse_args()

#List the names of all the athletes from a specified NOC.
if args.noc:
    #print('hello noc ' + args.noc)
    get_athletes_by_noc(args.noc)

#calls most medals, gives default values to start/end if none given.
if args.most_medals:
    if not args.start:
        print('no start')
        args.start = -1
    if not args.end:
        args.end = 3000
    most_medals_years(args.start, args.end)


#print(args.accumulate(args.integers))