# Name: Kris Kleiner
# Date: April 26, 2026
# Assignment: Module 6 - Movies: Table Queries
# Purpose: Query the movies database tables using Python and MySQL.

import mysql.connector
from mysql.connector import errorcode


config = {
    "user": "movies_user",
    "password": "popcorn",
    "host": "localhost",
    "database": "movies",
    "raise_on_warnings": True
}


try:
    db = mysql.connector.connect(**config)
    cursor = db.cursor()

    # Query 1: Select all fields from studio table
    print("-- DISPLAYING Studio RECORDS --")
    cursor.execute("SELECT * FROM studio")
    studios = cursor.fetchall()

    for studio in studios:
        print("Studio ID: {}\nStudio Name: {}\n".format(studio[0], studio[1]))

    # Query 2: Select all fields from genre table
    print("-- DISPLAYING Genre RECORDS --")
    cursor.execute("SELECT * FROM genre")
    genres = cursor.fetchall()

    for genre in genres:
        print("Genre ID: {}\nGenre Name: {}\n".format(genre[0], genre[1]))

    # Query 3: Movie names with runtime less than 2 hours
    print("-- DISPLAYING Short Film RECORDS --")
    cursor.execute("SELECT film_name, film_runtime FROM film WHERE film_runtime < 120")
    films = cursor.fetchall()

    for film in films:
        print("Film Name: {}\nRuntime: {}\n".format(film[0], film[1]))

    # Query 4: Film names and directors grouped by director
    print("-- DISPLAYING Director RECORDS in Order --")
    cursor.execute("SELECT film_name, film_director FROM film ORDER BY film_director")
    directors = cursor.fetchall()

    for director in directors:
        print("Film Name: {}\nDirector: {}\n".format(director[0], director[1]))

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("The supplied username or password is invalid.")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("The specified database does not exist.")
    else:
        print(err)

finally:
    if 'db' in locals() and db.is_connected():
        cursor.close()
        db.close()