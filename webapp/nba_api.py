'''
    books_webapp.py
    Jeff Ondich, 25 April 2016
    Updated 4 November 2020

    Tiny Flask API to support the tiny books web application.
'''
import sys
import flask
import json
import config
import psycopg2

########### Initializing Flask ###########
# We're using a Flask "Blueprint" to enable us to put the website pages
# in the main Flask application (in books_webapp.py) and the API over
# here. Since the website and the API are conceptually separate, I like
# to keep them in separate files. This gets more worthwhile as the
# application grows.
api = flask.Blueprint('api', __name__)

limit = 20

########### Utility functions ###########
def get_connection():
    ''' Returns a connection to the database described in the
        config module. May raise an exception as described in the
        documentation for psycopg2.connect. '''
    return psycopg2.connect(database=config.database,
                            user=config.user,
                            password=config.password)


########### The API endpoints ###########


@api.route('/players/search')
def get_players():
    query = '''SELECT id, name, three_attempts, three_makes, layup_attempts, layup_makes , layup_makes , jumper_attempts , jumper_makes , hook_attempts , hook_makes , blocks , fouls , fouled , rbs , vs , ft_attempts , ft_makes , tos , tos_caused, team, assists
        FROM players
        
        '''
   

    sort_argument = flask.request.args.get('sort')

    search_argument = flask.request.args.get('q')

    if sort_argument == 'threes':
        query += 'WHERE three_attempts > 10'
        sort_argument = 'CAST(three_makes AS FLOAT) / CAST(three_attempts AS FLOAT)'

    print('hello?')

    if search_argument:

        

        print(search_argument)
        print(search_argument.split(', '))
        for search in search_argument.split(','):
            print(search.strip())
            if query.__contains__('WHERE'):
                query += ' OR '
            else:
                query += ' WHERE '
            print('querry append...')
            query += 'UPPER(name) LIKE \'%' + search.strip().upper() + '%\' '




    if sort_argument:
        #query += 'blocks'
        query += 'ORDER BY ' + sort_argument + ' DESC'

    query += ' LIMIT ' + str(limit)

    print(query)

    player_list = []
    try:
        print('trying ')
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(query)
        for row in cursor:
            # print(row[1])
            player = {'id': row[0],
                      'name': row[1].split()[0][2] + '. ' + row[1].split()[1],
                      'three_attempts': row[2],
                      'three_makes': row[3],
                      'layup_attempts': row[4],
                      'layup_makes': row[5],
                      'layup_makes': row[6],
                      'jumper_attempts': row[7],
                      'jumper_makes': row[8],
                      'hook_attempts': row[9],
                      'hook_makes': row[10],
                      'blocks': row[11],
                      'fouls': row[12],
                      'fouled': row[13],
                      'rbs': row[14],
                      'vs': row[15],
                      'ft_attempts': row[16],
                      'ft_makes': row[17],
                      'tos': row[18],
                      'tos_caused': row[19],
                      'team': row[20],
                      'assists': row[21]}
            player_list.append(player)
            #print(row[11])

        cursor.close()
        connection.close()
    except Exception as e:
        print(e, file=sys.stderr)

    return json.dumps(player_list)


@api.route('/players/details/<player_ids>')
def get_player_details(player_ids):
    query = '''SELECT id, name, three_attempts, three_makes, layup_attempts, layup_makes , layup_makes , jumper_attempts , jumper_makes , hook_attempts , hook_makes , blocks , fouls , fouled , rbs , vs , ft_attempts , ft_makes , tos , tos_caused, team, assists
    FROM players '''

    id_string = player_ids
    
    #print('please help')
    #print('%s')
    #print(id_string)

    ids = id_string.split(',')

    query += 'WHERE id = ' + ids.pop(0)

    for id in ids:
        query += 'OR id = ' + id + ' '

    print(query)

    player_list = []
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(query)
        for row in cursor:
            #book = {'id': row[0], 'title': row[1], 'publication_year': row[2]}
            player = {'id': row[0],
                    'name': row[1].split()[0][2] + '. ' + row[1].split()[1],
                    'three_attempts': row[2],
                    'three_makes': row[3],
                    'layup_attempts': row[4],
                    'layup_makes': row[5],
                    'layup_makes': row[6],
                    'jumper_attempts': row[7],
                    'jumper_makes': row[8],
                    'hook_attempts': row[9],
                    'hook_makes': row[10],
                    'blocks': row[11],
                    'fouls': row[12],
                    'fouled': row[13],
                    'rbs': row[14],
                    'vs': row[15],
                    'ft_attempts': row[16],
                    'ft_makes': row[17],
                    'tos': row[18],
                    'tos_caused': row[19],
                    'team': row[20],
                    'assists': row[21]
                    }
        

            player_list.append(player)
        cursor.close()
        connection.close()
    except Exception as e:
        print(e, file=sys.stderr)

    return json.dumps(player_list)
