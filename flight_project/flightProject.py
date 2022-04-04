from flask import Flask
from flask import render_template, request, redirect, url_for

import sqlite3
import json
import logging
import os
import datetime

logging.basicConfig(filename='flight_project.log' ,level=logging.DEBUG, datefmt='|%Y-%m-%d|%H:%M:%S|', format='%(asctime)s::%(levelname)-6s [%(filename)s:%(lineno)d]--->%(message)s')

app = Flask(__name__)
app.secret_key = "something only you know"

#--------------- SQL tables ---------------
users_table = \
    """CREATE TABLE IF NOT EXISTS "users" (
        "id_AI"	INTEGER,
	    "full_name"	VARCHAR NOT NULL,
	    "password"	VARCHAR NOT NULL,
	    "real_id"	VARCHAR UNIQUE NOT NULL,
	    FOREIGN KEY("id_AI") REFERENCES "tickets"("ticket_id"),
	    PRIMARY KEY("id_AI" AUTOINCREMENT)
);"""

tickets_table = \
    """CREATE TABLE IF NOT EXISTS "tickets" (
        "ticket_id"	INTEGER,
	    "user_id"	INTEGER,
	    "flight_id"	INTEGER,
	    FOREIGN KEY("flight_id") REFERENCES "flights"("flight_id"),
	    PRIMARY KEY("ticket_id" AUTOINCREMENT)
);"""

flights_table = \
    """CREATE TABLE IF NOT EXISTS "flights" (
        "flight_id"	INTEGER,
	    "timestamp"	DATETIME,
	    "remaining_seats"	INTEGER,
	    "origin_country_id"	INTEGER,
	    "dest_country_id"    INTEGER,
	    FOREIGN KEY("origin_country_id") REFERENCES "countries"("code_AI"),
	    FOREIGN KEY("dest_country_id") REFERENCES "countries"("code_AI"),
	    PRIMARY KEY("flight_id" AUTOINCREMENT)
);"""

countries_table = \
    """CREATE TABLE IF NOT EXISTS "countries" (
        "code_AI"	INTEGER,
	    "name"	VARCHAR,
	    PRIMARY KEY("code_AI" AUTOINCREMENT)
);"""

#--------------- create DB connections ---------------

def DB_conn():
    """
    create sql connection
    :return:
    """
    try:
        conn = sqlite3.connect(r"flight_project.db")
        logging.info("DB connection created")
        conn.row_factory = sqlite3.Row
    except:
        logging.exception(f"something wrong with DB_conn function")
    return conn

def create_table(conn, table):
    """
    create db tables
    :param conn: db conn
    :param table: the table
    :return:
    """
    try:
        cursor = conn.cursor()
        cursor.execute(table)
    except:
        logging.exception(f"something wrong with create_table function")

def tables():
    """
    create tables
    :return:
    """
    try:
        tables = [users_table, tickets_table, flights_table, countries_table]
        tables_name_log = ["users table", "tickets table", "flights table", "countries table"]
        for i in range(0, 4):
            create_table(DB_conn(), tables[i])
            logging.info(f"{tables_name_log[i]} as been created")
    except:
        logging.exception(f"something wrong with tables function")

#check if the table exist, it's for not create then again
try:
    if os.path.isfile("flight_project.db"):
        logging.info("the DB file exist.")
    else:
        logging.info("the DB file isn't exist.")
        logging.info("create DB file.")
        tables()
        logging.info("the DB has been created.")
except:
    logging.exception("something get wrong when creating the DB")

#--------------- functions ---------------
#---------- fetch DB data ----------
#----- users DB -----
def get_usersDB_data():
    """
    get the userDB raw data
    :return:
    """
    try:
        conn_DB = DB_conn()
        cursor = conn_DB.cursor()
        cursor.execute("SELECT * FROM users")
        rows = cursor.fetchall()
        return rows
    except:
        logging.exception(f"something wrong with get_usersDB_data function")

def get_usersDB_as_dict():
    """
    convert it into dict
    :return:
    """
    try:
        rows = get_usersDB_data()
        users_dict = {"id_AI": [], "full_name":[], "password":[], "real_id":[]}
        for rows in rows:
            users_dict["id_AI"].append(rows["id_AI"])
            users_dict["full_name"].append(rows["full_name"])
            users_dict["password"].append(rows["password"])
            users_dict["real_id"].append(rows["real_id"])
        logging.info("get userDB as a dict")
        return users_dict
    except:
        logging.exception(f"something wrong with get_usersDB_as_dict function")

#----- tickets DB -----

def get_ticketsDB_data():
    """
    get the ticketsDB raw data
    :return:
    """
    try:
        conn_DB = DB_conn()
        cursor = conn_DB.cursor()
        cursor.execute("SELECT * FROM tickets")
        rows = cursor.fetchall()
        return rows
    except:
        logging.exception(f"something wrong with get_ticketsDB_data function")

def get_ticketsDB_as_dict():
    """
    convert it into dict
    :return:
    """
    try:
        rows = get_ticketsDB_data()
        tickets_dict = {"ticket_id": [], "user_id":[], "flight_id":[]}
        for rows in rows:
            tickets_dict["ticket_id"].append(rows["ticket_id"])
            tickets_dict["user_id"].append(rows["user_id"])
            tickets_dict["flight_id"].append(rows["flight_id"])
        logging.info("get ticketsDB as a dict")
        return tickets_dict
    except:
        logging.exception(f"something wrong with get_ticketsDB_as_dict function")

#----- flights DB -----

def get_flightsDB_data():
    """
    get the flightsDB raw data
    :return:
    """
    try:
        conn_DB = DB_conn()
        cursor = conn_DB.cursor()
        cursor.execute("SELECT * FROM flights")
        rows = cursor.fetchall()
        return rows
    except:
        logging.exception(f"something wrong with get_flightsDB_data function")

def get_flightsDB_as_dict():
    """
    convert it into dict
    :return:
    """
    try:
        rows = get_flightsDB_data()
        flights_dict = {"flight_id": [], "timestamp":[], "remaining_seats":[], "origin_country_id":[], "dest_country_id":[]}
        for rows in rows:
            flights_dict["flight_id"].append(rows["flight_id"])
            flights_dict["timestamp"].append(rows["timestamp"])
            flights_dict["remaining_seats"].append(rows["remaining_seats"])
            flights_dict["origin_country_id"].append(rows["origin_country_id"])
            flights_dict["dest_country_id"].append(rows["dest_country_id"])
        logging.info("get flightsDB as a dict")
        return flights_dict
    except:
        logging.exception(f"something wrong with get_flightsDB_as_dict function")

#----- countries DB -----

def get_countriesDB_data():
    """
    get the flightsDB raw data
    :return:
    """
    try:
        conn_DB = DB_conn()
        cursor = conn_DB.cursor()
        cursor.execute("SELECT * FROM countries")
        rows = cursor.fetchall()
        return rows
    except:
        logging.exception(f"something wrong with get_countriesDB_data function")

def get_countriesDB_as_dict():
    """
    convert it into dict
    :return:
    """
    try:
        rows = get_countriesDB_data()
        countries_dict = {"code_AI": [], "name":[]}
        for rows in rows:
            countries_dict["name"].append(rows["name"])
            countries_dict["code_AI"].append(rows["code_AI"])
        logging.info("get countriesDB as a dict")
        return countries_dict
    except:
        logging.exception(f"something wrong with get_countriesDB_as_dict function")

#---------- DB functions ----------
#----- users -----
def post_user_to_DB(full_name, password, real_id):
    """
    post user to the DB
    :param full_name:
    :param password:
    :param real_id:
    :return:
    """
    try:
        conn_DB = DB_conn()
        cursor = conn_DB.cursor()
        query = f"INSERT INTO users ('full_name','password','real_id') VALUES ('{full_name}','{password}','{real_id}')"
        try:
            cursor.execute(query)
            conn_DB.commit()
            logging.info(f"full_name:{full_name},password:{password},real_id:{real_id} are inserted into users table")
        except sqlite3.IntegrityError:
            logging.warning(f"the real_id:{real_id} is already used in the DB")
    except:
        logging.exception(f"something wrong with send_user_to_DB function")

def update_user_from_DB(id_AI, full_name, password, real_id):
    """
    update user to the DB
    :param id_AI:
    :param full_name:
    :param password:
    :param real_id:
    :return:
    """
    try:
        conn_DB = DB_conn()
        cursor = conn_DB.cursor()
        query = f"UPDATE users SET full_name='{full_name}',password='{password}',real_id='{real_id}' WHERE id_AI={id_AI}"
        try:
            cursor.execute(query)
            conn_DB.commit()
            logging.info(f"full_name:{full_name},password:{password},real_id:{real_id} are updated at id_AI[{id_AI}] into users table")
        except sqlite3.IntegrityError:
            logging.warning(f"the real_id:{real_id} is already used in the DB")
    except:
        logging.exception(f"something wrong with update_user_from_DB function")

def delete_user_from_DB(id_AI):
    """
    delete user to the DB
    :param id_AI:
    :return:
    """
    try:
        conn_DB = DB_conn()
        cursor = conn_DB.cursor()
        for i in get_usersDB_as_dict()["id_AI"]:
            if i == id_AI:
                query = f"DELETE FROM users WHERE id_AI={id_AI}"
                logging.info(f"id_AI[{id_AI}] has been deleted from users table")
                try:
                    cursor.execute(query)
                    conn_DB.commit()
                except sqlite3.IntegrityError:
                    logging.exception(f"the real_id:{real_id} is already used in the DB")
    except:
        logging.exception(f"something wrong with delete_user_from_DB function")

#----- tickets -----
def post_tickets_to_DB(user_id, flight_id):
    """
    post tickets to the DB
    :param user_id:
    :param flight_id:
    :return:
    """
    try:
        conn_DB = DB_conn()
        cursor = conn_DB.cursor()
        query = f"INSERT INTO tickets ('user_id','flight_id') VALUES ('{user_id}','{flight_id}')"
        try:
            cursor.execute(query)
            conn_DB.commit()
            logging.info(f"user_id:{user_id},flight_id:{flight_id} are inserted into tickets table")
        except:
            logging.exception(f"something wrong with the sql in send_tickets_to_DB function")
    except:
        logging.exception(f"something wrong with send_tickets_to_DB function")

def update_tickets_from_DB(ticket_id, user_id, flight_id,):
    """
    update tickets to the DB
    :param ticket_id:
    :param user_id:
    :param flight_id:
    :return:
    """
    try:
        conn_DB = DB_conn()
        cursor = conn_DB.cursor()
        query = f"UPDATE tickets SET user_id='{user_id}',flight_id='{flight_id}' WHERE ticket_id={ticket_id}"
        try:
            cursor.execute(query)
            conn_DB.commit()
            logging.info(f"user_id:{user_id},flight_id:{flight_id} are updated at ticket_id[{ticket_id}] into tickets table")
        except:
            logging.exception(f"something wrong with the sql in update_tickets_from_DB function")
    except:
        logging.exception(f"something wrong with update_tickets_from_DB function")

def delete_tickets_from_DB(ticket_id):
    """
    delete tickets to the DB
    :param ticket_id:
    :return:
    """
    try:
        conn_DB = DB_conn()
        cursor = conn_DB.cursor()
        for i in get_ticketsDB_as_dict()["ticket_id"]:
            if i == ticket_id:
                query = f"DELETE FROM tickets WHERE ticket_id={ticket_id}"
                logging.info(f"ticket_id[{ticket_id}] has been deleted from tickets table")
                try:
                    cursor.execute(query)
                    conn_DB.commit()
                except:
                    logging.exception(f"something wrong with the sql in delete_tickets_from_DB function")
    except:
        logging.exception(f"something wrong with delete_tickets_from_DB function")

#----- flights -----
def post_flights_to_DB(timestamp, remaining_seats, origin_country_id, dest_country_id):
    """
    post flights to the DB
    :param timestamp:
    :param remaining_seats:
    :param origin_country_id:
    :param dest_country_id:
    :return:
    """
    try:
        conn_DB = DB_conn()
        cursor = conn_DB.cursor()
        query = f"INSERT INTO flights ('timestamp','remaining_seats','origin_country_id','dest_country_id') VALUES ('{timestamp}','{remaining_seats}','{origin_country_id}','{dest_country_id}')"
        try:
            cursor.execute(query)
            conn_DB.commit()
            logging.info(f"timestamp:{timestamp},remaining_seats:{remaining_seats},origin_country_id:{origin_country_id},dest_country_id:{dest_country_id} are inserted into flights table")
        except:
            logging.exception(f"something wrong with the sql in send_flights_to_DB function")
    except:
        logging.exception(f"something wrong with send_flights_to_DB function")

def update_flights_from_DB(flight_id, timestamp, remaining_seats, origin_country_id, dest_country_id):
    """
    update flights to the DB
    :param flight_id:
    :param timestamp:
    :param remaining_seats:
    :param origin_country_id:
    :param dest_country_id:
    :return:
    """
    try:
        conn_DB = DB_conn()
        cursor = conn_DB.cursor()
        query = f"UPDATE flights SET timestamp='{timestamp}',remaining_seats='{remaining_seats}',origin_country_id='{origin_country_id}',dest_country_id='{dest_country_id}' WHERE flight_id={flight_id}"
        try:
            cursor.execute(query)
            conn_DB.commit()
            logging.info(f"timestamp:{timestamp},remaining_seats:{remaining_seats},origin_country_id:{origin_country_id},dest_country_id:{dest_country_id} are updated at flight_id[{flight_id}] into flights table")
        except:
            logging.exception(f"something wrong with the sql in update_flights_from_DB function")
    except:
        logging.exception(f"something wrong with update_flights_from_DB function")

def delete_flights_from_DB(flight_id):
    """
    delete flights to the DB
    :param flight_id:
    :return:
    """
    try:
        conn_DB = DB_conn()
        cursor = conn_DB.cursor()
        for i in get_flightsDB_as_dict()["flight_id"]:
            if i == flight_id:
                query = f"DELETE FROM flights WHERE flight_id={flight_id}"
                logging.info(f"flight_id[{flight_id}] has been deleted from flights table")
                try:
                    cursor.execute(query)
                    conn_DB.commit()
                except:
                    logging.exception(f"something wrong with the sql in delete_flights_from_DB function")
    except:
        logging.exception(f"something wrong with delete_flights_from_DB function")

#----- countries -----
def post_countries_to_DB(name):
    """
    post countries to the DB
    :param name:
    :return:
    """
    try:
        conn_DB = DB_conn()
        cursor = conn_DB.cursor()
        query = f"INSERT INTO countries ('name') VALUES ('{name}')"
        try:
            cursor.execute(query)
            conn_DB.commit()
            logging.info(f"name:{name} is inserted into countries table")
        except:
            logging.exception(f"something wrong with the sql in send_countries_to_DB function")
    except:
        logging.exception(f"something wrong with send_countries_to_DB function")

def update_countries_from_DB(code_AI, name):
    """
    update countries to the DB
    :param code_AI:
    :param name:
    :return:
    """
    try:
        conn_DB = DB_conn()
        cursor = conn_DB.cursor()
        query = f"UPDATE countries SET name='{name}' WHERE code_AI={code_AI}"
        try:
            cursor.execute(query)
            conn_DB.commit()
            logging.info(f"name:{name} is updated at code_AI[{code_AI}] into countries table")
        except:
            logging.exception(f"something wrong with the sql in update_countries_from_DB function")
    except:
        logging.exception(f"something wrong with update_countries_from_DB function")

def delete_countries_from_DB(code_AI):
    """
    delete countries to the DB
    :param code_AI:
    :return:
    """
    try:
        conn_DB = DB_conn()
        cursor = conn_DB.cursor()
        for i in get_countriesDB_as_dict()["code_AI"]:
            if i == code_AI:
                query = f"DELETE FROM countries WHERE code_AI={code_AI}"
                logging.info(f"code_AI[{code_AI}] has been deleted from countries table")
                try:
                    cursor.execute(query)
                    conn_DB.commit()
                except:
                    logging.exception(f"something wrong with the sql in delete_countries_from_DB function")
    except:
        logging.exception(f"something wrong with delete_user_from_DB function")

#--------------- program flow functions ---------------
#----- users -----
def check_if_real_id_in_usersDB(users_dict, real_id):
    """
    check if real_id in usersDB
    :param users_dict:
    :param real_id:
    :return:
    """
    try:
        for i in users_dict["real_id"]:
            try:
                if i == real_id or int(i)== real_id:
                    return True
            except:
                logging.info(f"{real_id} is found in {users_dict['real_id']}")
        else:
            return False
    except:
        logging.exception(f"something wrong with check_if_real_id_in_usersDB function")

def create_user(user):
    """
    create user
    :param user:
    :return:
    """
    try:
        if check_if_real_id_in_usersDB(get_usersDB_as_dict(), user.real_id) == False:
            post_user_to_DB(user.full_name, user.password, user.real_id)
            logging.info(f"{user.real_id} has been created")
            return True
        else:
            logging.info(f"{user.real_id} is already in the DB")
            return False
    except:
        logging.exception(f"something wrong with create_user function")

def login(user):
    """
    login into the user
    :param user:
    :return:
    """
    try:
        if check_if_real_id_in_usersDB(get_usersDB_as_dict(), user.real_id) == True:
            if check_password_of_real_id(user) == True:
                logging.info(f"login to {user.real_id}")
                return True
            logging.info(f"something wrong with check_password_of_real_id(user) function")
        else:

            logging.info(f"{user.real_id} isn't in the DB")
            return False
    except:
        logging.exception(f"something wrong with login function")

def check_password_of_real_id(user):
    """
    verify the password is match to the real_id
    :param user:
    :return:
    """
    try:
        for i in range(len(get_usersDB_as_dict()["real_id"])):
            if user.real_id == get_usersDB_as_dict()["real_id"][i]:
                if user.password == get_usersDB_as_dict()["password"][i]:
                    logging.info("the passwords match")
                    return True
                else:
                    logging.info("the passwords are not match")
                    logging.info(f"login to {user.real_id} faild")
                    return False
            else:
                logging.critical("check_if_real_id_in_usersDB function faild, the real_id is not in the DB")
    except:
        logging.exception(f"something wrong with verify_password function")

def get_id_AI_of_real_id(user):
    """
    get the id_AI of real_id
    :param user:
    :return:
    """
    try:
        for i in range(len(get_usersDB_as_dict()["real_id"])-1):
            if user.real_id == get_usersDB_as_dict()["real_id"][i]:
                logging.info(f"id_AI= {get_usersDB_as_dict()['id_AI'][i]} | real_id={user.real_id}")
                return get_usersDB_as_dict()["id_AI"][i]
            else:
                logging.critical("check_if_real_id_in_usersDB function faild, the real_id is not in the DB")
    except:
        logging.exception(f"something wrong with verify_password function")

#---------- countries DB ----------
def countries_DB_empty():
    """
    check if the countries DB is empty
    :return:
    """
    try:
        conn_DB = DB_conn()
        cursor = conn_DB.cursor()
        query = f'SELECT name FROM countries'
        cursor.execute(query)
        record = cursor.fetchone()
        if record == None:
            logging.info(f"the countries_DB is empty")
            return True
        else:
            logging.info(f"the countries_DB isn't empty")
            return False
    except:
        logging.exception(f"something wrong with countries_DB_empty function")

def add_countries_DB():
    """
    add a countries into DB
    :return:
    """
    try:
        countries_list = ["Israel", "London", "New York", "Washington", "Tokyo", "Osaka"]
        if countries_DB_empty() == True:
            for i in range(len(countries_list)-1):
                post_countries_to_DB(countries_list[i])
            logging.info(f"countries_DB is fully created")
        else:
            logging.info(f"countries_DB table is already created")
    except:
        logging.exception(f"something wrong with countries_DB function")

add_countries_DB()

#---------- flights DB ----------
def date_time_list(add_datetime = None):
    """
    create date_time list
    :param add_datetime:
    :return:
    """
    try:
        timestamp_list = [datetime.datetime(2022, 4, 1, 20, 0),
                          datetime.datetime(2022, 4, 1, 18, 0),
                          datetime.datetime(2022, 4, 1, 8, 0),
                          datetime.datetime(2022, 4, 2, 12, 0),
                          datetime.datetime(2022, 4, 2, 20, 0),
                          datetime.datetime(2022, 4, 3, 20, 0)
                          ]
        if add_datetime != None:
            timestamp_list.append(add_datetime)
            logging.info(f"{add_datetime} added to date_time_list")
            return timestamp_list
        else:
            return timestamp_list
    except:
        logging.exception(f"something wrong with date_time function")

def country_id(country):
    """
    get country_id
    :param country:
    :return:
    """
    try:
        countries_list = get_countriesDB_as_dict()["name"]
        for i in range(len(countries_list)):
            if country == countries_list[i]:
                return i+1
    except:
        logging.exception(f"something wrong with country_id function")

def flight(timestamp, seats, origin_country_id, dest_country_id):
    """
    add flight
    :param timestamp:
    :param seats:
    :param origin_country_id:
    :param dest_country_id:
    :return:
    """
    try:
        post_flights_to_DB(timestamp, seats, origin_country_id, dest_country_id)
        logging.info("flight added")
    except:
        logging.exception(f"something wrong with flight function")

def flights_DB_empty(flight_id):
    """
    check if flights_DB is empty
    :param flight_id:
    :return:
    """
    try:
        flight_id_list = get_flightsDB_as_dict()["flight_id"]
        if flight_id_list:
            for i in flight_id_list:
                if i == flight_id:
                    logging.info(f"flight number:{flight_id} is already exist")
                    return False
        logging.info(f"the flights_DB is empty")
        logging.info(f"flight number {flight_id} created")
        return True
    except:
        logging.exception(f"something wrong with flights_DB_empty function")

def flights1(flight_id):
    """
    add the first flight
    :param flight_id:
    :return:
    """
    try:
        timestamp = date_time_list()[0]
        origin_country_id = country_id("Israel")
        dest_country_id = country_id("London")
        if flights_DB_empty(flight_id) == True:
            flight(timestamp, 20, origin_country_id, dest_country_id)
    except:
        logging.exception(f"something wrong with flights001 function")
flights1(1)

def flights2(flight_id):
    """
    add the second flight
    :param flight_id:
    :return:
    """
    try:
        timestamp = date_time_list()[1]
        origin_country_id = country_id("Israel")
        dest_country_id = country_id("New York")
        if flights_DB_empty(flight_id) == True:
            flight(timestamp, 20, origin_country_id, dest_country_id)
    except:
        logging.exception(f"something wrong with flights001 function")
flights2(2)

def flights3(flight_id):
    """
    add the third flight
    :param flight_id:
    :return:
    """
    try:
        timestamp = date_time_list()[1]
        origin_country_id = country_id("New York")
        dest_country_id = country_id("Tokyo")
        if flights_DB_empty(flight_id) == True:
            flight(timestamp, 20, origin_country_id, dest_country_id)
    except:
        logging.exception(f"something wrong with flights001 function")
flights3(3)

def decrease_remaining_seats(flight_id):
    """
    decrease remaining seats
    :param flight_id:
    :return:
    """
    try:
        remaining_seats_list = get_flightsDB_as_dict()["remaining_seats"]
        remaining_seats = remaining_seats_list[flight_id-1]
        remaining_seats -= 1
        if remaining_seats >= 0:
            conn_DB = DB_conn()
            cursor = conn_DB.cursor()
            query = f"UPDATE flights SET remaining_seats='{remaining_seats}' WHERE flight_id={flight_id}"
            try:
                cursor.execute(query)
                conn_DB.commit()
                logging.info(f"remaining_seats:{remaining_seats} are updated at flight_id[{flight_id}] into flights table")
                return True
            except:
                logging.exception(f"something wrong with the sql in decrease_remaining_seats function")
        else:
            logging.info(f"no more remaining_seats")
            return False
    except:
        logging.exception(f"something wrong with update_flights_from_DB function")

def show_avaliable_flights():
    """
    show avaliable flights
    :return:
    """
    try:
        return get_flightsDB_as_dict()
    except:
        logging.exception(f"something wrong with show_avaliable_flights function")

#---------- tickets DB ----------
#----- tickets -----
def buy_ticket(user_id, flight_id):
    """
    buy tickets
    :param user_id:
    :param flight_id:
    :return:
    """
    try:
        if decrease_remaining_seats(flight_id) == True:
            post_tickets_to_DB(user_id, flight_id)
            logging.info(f"{user_id} buy ticket")
            return True
        else:
            return False #no more remaining_seats
    except:
        logging.exception(f"something wrong with buy_ticket function")

def ticket_of_user(id_AI):
    """
    get the tickets user
    :param id_AI:
    :return:
    """
    try:
        return get_ticketsDB_as_dict()
    except:
        logging.exception(f"something wrong with ticket_of_user function")

def delete_ticket_of_user(id_AI):
    """
    delete a ticket of a user
    :param id_AI:
    :return:
    """
    try:
        delete_ticket_of_user(id_AI)
    except:
        logging.exception(f"something wrong with delete_ticket_of_user function")



#---------------DB class---------------
class User():
    def __init__(self, full_name, password, real_id):
        self.full_name = full_name
        self.password = password
        self.real_id = real_id
"""
class Flights():
    def __init__(self, flight_id, timestamp, remaining_seats, origin_country_id, dest_country_id):
        self.flight_id = flight_id
        self.timestamp = timestamp
        self.remaining_seats = remaining_seats
        self.origin_country_id = origin_country_id
        self.dest_country_id = dest_country_id
        
"""
#-----USERS-----

@app.route('/signUp', methods=["GET", "POST", "PUT", "DELETE"])
def sign_up():
    if request.method == "GET":
        return render_template("signUP.html")
    elif request.method == "POST":
        user = User(request.form["full_name"], request.form["password"], request.form["real_id"]) #User is class
        if create_user(user) == True:
            return render_template("login.html")
        else:
            return render_template("id_used.html")

@app.route('/signIn', methods=["GET", "POST", "PUT", "DELETE"])
def sign_in():
    if request.method == "GET":
        return render_template("signIn.html")
    elif request.method == "POST":
        user = User(None, request.form["password"], request.form["real_id"]) #User is class
        if login(user) == True:
            return render_template("tickets.html")
        else:
            return render_template("id_used.html")


@app.route("/tickets_site", methods=["GET", "POST", "PUT", "DELETE"])
def tickets():
    if request.method == "GET":
        output = render_template("tickets.html")
        return render_template('tickets.html',output=output)
    elif request.method == "POST":
        ticket_input = request.form.getlist("tickets")
        if ticket_input[0] == "show":
            return show_avaliable_flights()
        if ticket_input[0] == "buy":
            return render_template('home.html')
        if ticket_input[0] == "delete":
            return render_template('tickets.html')
        return render_template('tickets.html')

@app.route("/flights_site", methods=["GET", "POST", "PUT", "DELETE"])
def flights():
    if request.method == "GET":
        return render_template("flights_table_and_choosing.html")
    elif request.method == "POST":
        flightsClass = get_flightsDB_as_dict()
        return render_template('flights_table_and_choosing.html', flights=flights)


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")

#!!!!!!!!!!!this is to test the restAPI, will not be in the final version!!!!!!!!!!!
#\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/
@app.route('/users', methods=["GET", "POST", "PUT", "DELETE"])
def getUser():
    if request.method == "GET":
        return render_template("users.html")
    elif request.method == "POST":
        post_user_to_DB(request.form["full_name"], request.form["password"], request.form["real_id"])
        return f"{get_usersDB_as_dict()}"

@app.route('/users/<int:id>', methods=["GET", "POST", "PUT", "DELETE"])
def getUserByID(id):
    if request.method == "GET":
        for i in get_users_data():
            if i[0] == id:
                return f"{get_usersDB_as_dict()[id - 1]}"
        return f"{id}: we dont have this user"
    elif request.method == 'PUT':
        conn_DB = DB_conn()
        cursor = conn_DB.cursor()
        full_name = request.form["full_name"]
        password = request.form["password"]
        real_id = request.form["real_id"]
        query = f"UPDATE users SET full_name='{full_name}',password='{password}',real_id='{real_id}' WHERE id_AI={id}"
        cursor.execute(query)
        conn_DB.commit()
        return f"{get_usersDB_as_dict()}"
    elif request.method == 'DELETE':
        conn_DB = DB_conn()
        cursor = conn_DB.cursor()
        full_name = request.form["full_name"]
        password = request.form["password"]
        real_id = request.form["real_id"]
        for i in get_users_data():
            if i[0] == id:
                query = f"DELETE FROM users WHERE id_AI={id}"
                cursor.execute(query)
                conn_DB.commit()
        return f"{get_usersDB_as_dict()}"
    return f"{id}: we dont have this user"

#-----tickets-----

@app.route('/tickets', methods=["GET", "POST", "PUT", "DELETE"])
def getAllTickets():
    if request.method == "GET":
        return f"{get_tickets_data()}"
    elif request.method == "POST":
        conn_DB = DB_conn()
        cursor = conn_DB.cursor()
        user_id = request.form["user_id"]
        flight_id = request.form["flight_id"]
        query = f'INSERT INTO tickets ("user_id","flight_id") VALUES ("{user_id}","{flight_id}")'
        cursor.execute(query)
        conn_DB.commit()
        return f"{get_tickets_data()}"

@app.route('/tickets/<int:id>', methods=["GET", "POST", "PUT", "DELETE"])
def getTicketsByID(id):
    if request.method == "GET":
        for i in get_tickets_data():
            if i[0] == id:
                return f"{get_tickets_data()[id - 1]}"
        return f"{id}: we dont have this user"
    elif request.method == 'PUT':
        conn_DB = DB_conn()
        cursor = conn_DB.cursor()
        user_id = request.form["user_id"]
        flight_id = request.form["flight_id"]
        query = f"UPDATE tickets SET user_id='{user_id}',flight_id='{flight_id}' WHERE ticket_id={id}"
        cursor.execute(query)
        conn_DB.commit()
        return f"{get_tickets_data()}"
    elif request.method == 'DELETE':
        conn_DB = DB_conn()
        cursor = conn_DB.cursor()
        user_id = request.form["user_id"]
        flight_id = request.form["flight_id"]
        for i in get_tickets_data():
            if i[0] == id:
                query = f"DELETE FROM tickets WHERE ticket_id={id}"
                cursor.execute(query)
                conn_DB.commit()
        return f"{get_tickets_data()}"
    return f"{id}: we dont have this user"

#-----flights-----

@app.route('/flights', methods=["GET", "POST", "PUT", "DELETE"])
def getAllFlights():
    if request.method == "GET":
        return f"{get_flights_data()}"
    elif request.method == "POST":
        conn_DB = DB_conn()
        cursor = conn_DB.cursor()
        timestamp = request.form["timestamp"]
        remaining_seats = request.form["remaining_seats"]
        origin_country_id = request.form["origin_country_id"]
        dest_country_id = request.form["dest_country_id"]
        # try:
        query = f'INSERT INTO flights ("timestamp","remaining_seats","origin_country_id","dest_country_id") VALUES ("{timestamp}","{remaining_seats}","{origin_country_id}","{dest_country_id}")'
        cursor.execute(query)
        conn_DB.commit()
        return f"{get_flights_data()}"
    # except:
    #     return render_template("ID_exist.html")

@app.route('/flights/<int:id>', methods=["GET", "POST", "PUT", "DELETE"])
def getFlightsByID(id):
    if request.method == "GET":
        for i in get_flights_data():
            if i[0] == id:
                return f"{get_flights_data()[id - 1]}"
        return f"{id}: we dont have this user"
    elif request.method == 'PUT':
        conn_DB = DB_conn()
        cursor = conn_DB.cursor()
        timestamp = request.form["timestamp"]
        remaining_seats = request.form["remaining_seats"]
        origin_country_id = request.form["origin_country_id"]
        dest_country_id = request.form["dest_country_id"]
        query = f"UPDATE flights SET timestamp='{timestamp}',remaining_seats='{remaining_seats}',origin_country_id='{origin_country_id}',dest_country_id='{dest_country_id}' WHERE flight_id={id}"
        cursor.execute(query)
        conn_DB.commit()
        return f"{get_flights_data()}"
    elif request.method == 'DELETE':
        conn_DB = DB_conn()
        cursor = conn_DB.cursor()
        timestamp = request.form["timestamp"]
        remaining_seats = request.form["remaining_seats"]
        origin_country_id = request.form["origin_country_id"]
        dest_country_id = request.form["dest_country_id"]
        for i in get_flights_data():
            if i[0] == id:
                query = f"DELETE FROM flights WHERE flight_id={id}"
                cursor.execute(query)
                conn_DB.commit()
        return f"{get_flights_data()}"
    return f"{id}: we dont have this user"


#-----countries-----

@app.route('/countries', methods=["GET", "POST", "PUT", "DELETE"])
def getAllCountries():
    if request.method == "GET":
        return f"{get_countries_data()}"
    elif request.method == "POST": #if you want to add a new countries
        conn_DB = DB_conn()
        cursor = conn_DB.cursor()
        name = request.form["name"]
        # try:
        query = f'INSERT INTO countries ("name") VALUES ("{name}")'
        cursor.execute(query)
        conn_DB.commit()
        return f"{get_countries_data()}"

@app.route('/countries/<int:id>', methods=["GET", "POST", "PUT", "DELETE"])
def getCountriesByID(id):
    if request.method == "GET":
        for i in get_countries_data():
            if i[0] == id:
                return f"{get_countries_data()[id - 1]}"
        return f"{id}: we dont have this countries"
    elif request.method == 'PUT':
        conn_DB = DB_conn()
        cursor = conn_DB.cursor()
        name = request.form["name"]
        query = f"UPDATE countries SET name='{name}' WHERE code_AI={id}"
        cursor.execute(query)
        conn_DB.commit()
        return f"{get_countries_data()}"
    elif request.method == 'DELETE':
        conn_DB = DB_conn()
        cursor = conn_DB.cursor()
        name = request.form["name"]
        for i in get_countries_data():
            if i[0] == id:
                query = f"DELETE FROM countries WHERE code_AI={id}"
                cursor.execute(query)
                conn_DB.commit()
        return f"{get_countries_data()}"
    return f"{id}: we dont have this user"
#/\/\/\/\/\/\/\/\/\this is to test the restAPI, will not be in the final version/\/\/\/\/\/\/\/\/\/\

if __name__ == "__main__":
    app.run()
