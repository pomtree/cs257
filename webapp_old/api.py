'''
    api.py
    Jeff Ondich, 25 April 2016
    Updated 8 November 2021

    Tiny Flask API to support the tiny books web application.
'''
import sys
import flask
import json
import config
import psycopg2

api = flask.Blueprint('api', __name__)

def get_connection():
    ''' Returns a connection to the database described in the
        config module. May raise an exception as described in the
        documentation for psycopg2.connect. '''
    return psycopg2.connect(database=config.database,
                            user=config.user,
                            password=config.password)

@api.route('/plays/') 
def get_authors():
    ''' Returns a list of all the authors in our database. See
        get_author_by_id below for description of the author
        resource representation.

        By default, the list is presented in alphabetical order
        by surname, then given_name. You may, however, use
        the GET parameter sort to request sorting by birth year.

            http://.../authors/?sort=birth_year

        Returns an empty list if there's any database failure.
    '''
    query = '''SELECT qrt FROM plays '''


    quarter_list = []
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(query, tuple())
        for row in cursor:
            quarter = {'qrt':row[0]}
            quarter_list.append(quarter)
        cursor.close()
        connection.close()
    except Exception as e:
        print(e, file=sys.stderr)

    return json.dumps(quarter_list)

@api.route('/team/')
def get_books_for_author(author_id):
    query = '''SELECT books.id, books.title, books.publication_year
               FROM books, authors, books_authors
               WHERE books.id = books_authors.book_id
                 AND authors.id = books_authors.author_id
                 AND authors.id = %s
               ORDER BY books.publication_year'''
    book_list = []
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(query, (author_id,))
        for row in cursor:
            book = {'id':row[0], 'title':row[1], 'publication_year':row[2]}
            book_list.append(book)
        cursor.close()
        connection.close()
    except Exception as e:
        print(e, file=sys.stderr)

    return json.dumps(book_list)






@api.route('/team/')
def get_team_stats(team_abr):
    query = '''
               SELECT teams.abbreviation, teams.name, SUM(teams.wins),
               SUM(teams.losses), SUM(teams.h_wins), SUM(teams.h_losses),
               SUM(teams.a_wins), SUM(teams.a_losses), SUM(teams.ot_wins),
               SUM(teams.ot_losses), AVG(teams.points), AVG(teams.rebounds), 
               AVG(teams.assists)
               FROM teams
               WHERE teams.abbreviation = %s
               GROUP BY teams.abbreviation, teams.name
               '''
    teams_list = []
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(query, (team_abr,))
        for row in cursor:
            team = {'abbreviation':row[0], 'full_name':row[1], 'total_wins':row[2], 'total_losses':row[3], 'h_wins':row[4], 'h__losses':row[5], 'a_wins':row[6], 'a_losses':row[7], 'ot_wins':row[8], 'ot_losses':row[9], 'points_per_game':row[10], 'rebounds_per_game':row[11], 'assists_per_game':row[12]}
            teams_list(team)
        cursor.close()
        connection.close()
    except Exception as e:
        print(e, file=sys.stderr)

    return json.dumps(teams_list)

