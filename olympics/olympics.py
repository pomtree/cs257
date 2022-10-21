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

def most_medals():
    print("NOCs by most gold medals won (individuals, not sports):")
    try:
        connection = get_connection()
        cursor = connection.cursor()
        query = '''
            SELECT COUNT(linking_table.medal), athlete_instances.noc
            FROM linking_table, athlete_instances
            WHERE linking_table.medal = 'Gold'
            AND linking_table.athlete_instance_id = athlete_instances.id
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

parser = argparse.ArgumentParser(description='##HELP STATEMENT')

parser.add_argument('--noc', type=str)
parser.add_argument('--most_medals', action='store_true')

args = parser.parse_args()

#List the names of all the athletes from a specified NOC.
if args.noc:
    #print('hello noc ' + args.noc)
    get_athletes_by_noc(args.noc)

if args.most_medals:
    most_medals()


#print(args.accumulate(args.integers))