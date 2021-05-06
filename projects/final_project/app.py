#!/usr/bin/env python3

#!/usr/bin/env python3
"""Flask application for final project"""

from flask import Flask, render_template, request
import sqlite3 as sql
import requests
app = Flask(__name__)

import sqlite3

conn = sqlite3.connect('database.db')
#print ("Opened database successfully");

#conn.execute('CREATE TABLE Playstation (cont TEXT,platform TEXT, cont_type TEXT, gamename TEXT, date TEXT)')
#print ("Table created successfully");
#conn.close()
#conn.execute('CREATE TABLE Xbox (cont TEXT,platform TEXT, cont_type TEXT, gamename TEXT, date TEXT)')
#print ("Table created successfully");
#conn.close()
#conn.execute('CREATE TABLE Pc (cont TEXT,platform TEXT, cont_type TEXT, gamename TEXT, date TEXT)')
#print ("Table created successfully");
#conn.close()

@app.route('/')
def home():
   return render_template('home.html')

@app.route('/newgame')
def new_game():
   return render_template('newgame.html')

@app.route('/rawdata')
def raw_data():
   all_known_games= requests.get("https://mycallmusa01.pythonanywhere.com/api/games")
   #print (all_known_games.json())
   return (all_known_games.json())


@app.route('/gameinventory')
def game_inventory():
   return render_template('gameinventory.html')

@app.route('/inventory_index')
def inventory_index():
   return render_template('index.html')

@app.route('/playstation')
def playstation():
   con = sql.connect('database.db')
   con.row_factory = sql.Row
   cur = con.cursor()
   cur.execute("select * from Playstation")
   rows = cur.fetchall();
   return render_template("playstation.html", rows = rows)

@app.route('/xbox')
def xbox():
   con = sql.connect('database.db')
   con.row_factory = sql.Row
   cur = con.cursor()
   cur.execute("select * from Xbox")
   rows = cur.fetchall();
   return render_template("xbox.html", rows = rows)

@app.route('/pc')
def pc():
   con = sql.connect('database.db')
   con.row_factory = sql.Row
   cur = con.cursor()
   cur.execute("select * from Pc")
   rows = cur.fetchall();
   return render_template("pc.html", rows = rows)


@app.route('/data',methods = ['POST', 'GET'])
def data():
   if request.method == 'POST':

            if len(request.form.get('platform')) == 11 :

                contr = request.form.get('user')
                platform = request.form.get('platform')
                conttype = request.form.get('contType')
                gname = request.form.get('game_name')
                date = request.form.get('date')

                with sql.connect('database.db') as con:
                    cur = con.cursor()
                    cur.execute("INSERT INTO Playstation (cont,platform,cont_type,gamename,date) VALUES (?,?,?,?,?)",(contr,platform, conttype, gname, date))
                    con.commit()


            if len(request.form.get('platform')) == 4 :

                contr = request.form.get('user')
                platform = request.form.get('platform')
                conttype = request.form.get('contType')
                gname = request.form.get('game_name')
                date = request.form.get('date')

                with sql.connect('database.db') as con:
                    cur = con.cursor()
                    cur.execute("INSERT INTO Xbox (cont,platform,cont_type,gamename,date) VALUES (?,?,?,?,?)",(contr,platform, conttype, gname, date))
                    con.commit()


            if len(request.form.get('platform')) == 2 :

                contr = request.form.get('user')
                platform = request.form.get('platform')
                conttype = request.form.get('contType')
                gname = request.form.get('game_name')
                date = request.form.get('date')

                with sql.connect('database.db') as con:
                    cur = con.cursor()
                    cur.execute("INSERT INTO Pc (cont,platform,cont_type,gamename,date) VALUES (?,?,?,?,?)",(contr,platform, conttype, gname, date))
                    con.commit()

            msg = "Game has been added to Inventory"
            return render_template("result.html",msg = msg)
            con.close()


if __name__ == "__main__":
  app.run()