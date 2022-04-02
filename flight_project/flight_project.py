from flask import Flask
from flask import render_template, request, redirect, url_for, flash
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
    try:
        conn = sqlite3.connect(r"flight_project.db")
        logging.info("DB connection created")
        conn.row_factory = sqlite3.Row
    except:
        logging.exception(f"something wrong with DB_conn function")
    return conn

def create_table(conn, table):
    try:
        cursor = conn.cursor()
        cursor.execute(table)
    except:
        logging.exception(f"something wrong with create_table function")

def tables():
    try:
        tables = [users_table, tickets_table, flights_table, countries_table]
        tables_name_log = ["users table", "tickets table", "flights table", "countries table"]
        for i in range(0, 4):
            create_table(DB_conn(), tables[i])
            logging.info(f"{tables_name_log[i]} as been created")
    except:
        logging.exception(f"something wrong with tables function")

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
    try:
        conn_DB = DB_conn()
        cursor = conn_DB.cursor()
        cursor.execute("SELECT * FROM users")
        rows = cursor.fetchall()
        return rows
    except:
        logging.exception(f"something wrong with get_usersDB_data function")

def get_usersDB_as_dict():
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
    try:
        conn_DB = DB_conn()
        cursor = conn_DB.cursor()
        cursor.execute("SELECT * FROM tickets")
        rows = cursor.fetchall()
        return rows
    except:
        logging.exception(f"something wrong with get_ticketsDB_data function")

def get_ticketsDB_as_dict():
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
    try:
        conn_DB = DB_conn()
        cursor = conn_DB.cursor()
        cursor.execute("SELECT * FROM flights")
        rows = cursor.fetchall()
        return rows
    except:
        logging.exception(f"something wrong with get_flightsDB_data function")

def get_flightsDB_as_dict():
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
    try:
        conn_DB = DB_conn()
        cursor = conn_DB.cursor()
        cursor.execute("SELECT * FROM countries")
        rows = cursor.fetchall()
        return rows
    except:
        logging.exception(f"something wrong with get_countriesDB_data function")

def get_countriesDB_as_dict():
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
                    print(f"the real_id:{real_id} is already used in the DB")
    except:
        logging.exception(f"something wrong with delete_user_from_DB function")

#----- tickets -----
def post_tickets_to_DB(user_id, flight_id):
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
    try:
        if check_if_real_id_in_usersDB(get_usersDB_as_dict(), user.real_id) == True:
            if check_password_of_real_id(user) == True:
                logging.info(f"login to {user.real_id}")
                return True
        else:
            logging.info(f"{user.real_id} isn't in the DB")
            return False
    except:
        logging.exception(f"something wrong with login function")

def check_password_of_real_id(user):
    try:
        for i in range(len(get_usersDB_as_dict()["real_id"])-1):
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

def countries_DB():
    try:
        countries_list = ["Israel", "London", "New York", "Washington", "Tokyo", "Osaka"]
        if countries_DB_empty() == True:
            for i in range(len(countries_list)-1):
                conn_DB = DB_conn()
                cursor = conn_DB.cursor()
                query = f'INSERT INTO countries ("name") VALUES ("{countries_list[i]}")'
                cursor.execute(query)
                conn_DB.commit()
            logging.info(f"countries_DB is fully created")
        else:
            logging.info(f"countries_DB table is already created")
    except:
        logging.exception(f"something wrong with countries_DB function")

countries_DB()

#---------- flights DB ----------
def date_time_list():
    try:
        timestamp_list = [datetime.datetime(2022, 4, 1, 20, 0),
                          datetime.datetime(2022, 4, 1, 18, 0),
                          datetime.datetime(2022, 4, 1, 8, 0),
                          datetime.datetime(2022, 4, 2, 12, 0),
                          datetime.datetime(2022, 4, 2, 20, 0),
                          datetime.datetime(2022, 4, 3, 20, 0)
                          ]
        return timestamp_list
    except:
        logging.exception(f"something wrong with date_time function")

def flights_DB_empty():
    try:
        conn_DB = DB_conn()
        cursor = conn_DB.cursor()
        query = f'SELECT flight_id FROM flights'
        cursor.execute(query)
        record = cursor.fetchone()
        if record == None:
            logging.info(f"the flights_DB is empty")
            return True
        else:
            logging.info(f"the flights_DB isn't empty")
            return False
    except:
        logging.exception(f"something wrong with flights_DB_empty function")

def flights_001():  #flight from israel to london
    try:
        timestamp = date_time_list()[0]
        origin_country_id = get_countriesDB_as_dict()["name"][0]
        dest_country_id = get_countriesDB_as_dict()["name"][1]
        if flights_DB_empty() == True:
            remaining_seats = 20
            conn_DB = DB_conn()
            cursor = conn_DB.cursor()
            query = f'INSERT INTO flights ("timestamp","remaining_seats","origin_country_id","dest_country_id") VALUES ("{timestamp}","{remaining_seats}","{origin_country_id}","{dest_country_id}")'
            cursor.execute(query)
            conn_DB.commit()
            logging.info(f"flight_001 has been config")
        else:
            logging.info(f"flight_001 is already config")
    except:
        logging.exception(f"something wrong with flights_001 function")

flights_001()

def avaliable_flights():
    flights_001 = get_flightsDB_as_dict()
    return flights_001

def decrease_remaining_seats(flight_id):
    try:
        remaining_seats = get_flightsDB_as_dict()["remaining_seats"]
        remaining_seats -= 1
        if remaining_seats >= 1:
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
#---------- tickets DB ----------

#----- tickets -----
def buy_ticket(user_id, flight_id):
    try:
        if decrease_remaining_seats(flight_id) == True:
            post_tickets_to_DB(user_id, flight_id)
            logging.info(f"{user_id} buy ticket")
            return True
        else:
            return False
    except:
        logging.exception(f"something wrong with buy_ticket function")

def ticket_of_user(user):
    try:
        get
    except:
        logging.exception(f"something wrong with buy_ticket function")

def delete_ticket_of_user(user):
    try:
        pass
    except:
        logging.exception(f"something wrong with buy_ticket function")



#---------------DB class---------------
class User():
    def __init__(self, full_name, password, real_id):
        self.full_name = full_name
        self.password = password
        self.real_id = real_id



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
            return render_template("login.html")
        else:
            return render_template("id_used.html")


@app.route("/createUser")


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")


if __name__ == "__main__":
    app.run(debug=True)


"""
@app.route('/users', methods=['GET', 'POST'])
def getUsers():
    if request.method == 'GET':
        return json.dumps(users)
    elif request.method == 'POST':
        user = request.get_json()
        # user["id"]=request.form['id';
        # user["id"]=request;
        # user["id"]=re;
        print(user)
        users.append(user)
        return json.dumps(users)

@app.route('/userspost',methods=['POST'])
def postUser():
    temp=request.get_json()
    id=len(users)
    temp['id']=id
    users.append(temp)
    return redirect(url_for('getUSerById',id=temp['id']))
"""



"""
def get_user_id():
    conn_DB = DB_conn()
    cursor = conn_DB.cursor()
    query = f'INSERT INTO users ("full_name","password","real_id") VALUES ("{full_name}","{password}","{real_id}")'
    cursor.execute(query)
    conn_DB.commit()
"""


"""
@app.route('/users/<int:id>', methods=["GET", "POST", "PUT", "DELETE"])
def getUserByID(id):
    if request.method == "GET":
        for i in get_users_data():
            if i[0] == id:
                return f"{get_users_data()[id - 1]}"
        return f"{id}: we dont have this user"
    elif request.method == 'PUT':
        conn_DB = DB_conn()
        cursor = conn_DB.cursor()
        full_name = request.form["full_name"]
        password = request.form["password"]
        real_id = request.form["real_id"]
        print(f"id={id}")
        query = f"UPDATE users SET full_name='{full_name}',password='{password}',real_id='{real_id}' WHERE id_AI={id}"
        cursor.execute(query)
        conn_DB.commit()
        return f"{get_users_data()}"
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
        return f"{get_users_data()}"
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
        print(f"id={id}")
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
"""
