from flask import Flask
from flask import render_template,request,redirect,url_for
import sqlite3

app=Flask(__name__)

def create_DB_connection():
    conn=sqlite3.connect(r"users.db")
    return conn

def create_table(conn,table):
    cursor=conn.cursor()
    cursor.execute(table)

sql_create_users_table=\
    """CREATE TABLE IF NOT EXISTS "users" (
        "id_AI"	INTEGER,
	    "full_name"	VARCHAR,
	    "password"	VARCHAR,
	    "real_id"	VARCHAR
);"""
conn=create_DB_connection()
create_table(conn,sql_create_users_table)

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/users", methods=["POST","GET"])
def user():
    if request.method=='GET':
        conn_DB=create_DB_connection()
        cursor=conn_DB.cursor()
        id_AI=request.form.get('id')
        full_name=request.form.get('full_name')
        password=request.form.get('password')
        real_id=request.form.get('real_id')
        query=f"INSERT INTO users VALUES ({id_AI},{full_name},{password},{real_id})"
        cursor.execute(query)
        conn_DB.commit()
        return render_template("html_site.html")

#debug=True
app.run()
