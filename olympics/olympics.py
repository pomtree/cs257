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

parser = argparse.ArgumentParser(description='##HELP STATEMENT')

parser.add_argument('--noc', type=str)

args = parser.parse_args()

#List the names of all the athletes from a specified NOC.
if(args.noc):
    #print('hello noc ' + args.noc)
    get_athletes_by_noc(args.noc)



#print(args.accumulate(args.integers))