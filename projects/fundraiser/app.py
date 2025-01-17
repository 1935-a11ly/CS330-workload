#!/usr/bin/env python3

#!/usr/bin/env python3
"""Flask application for fundraiser"""

from flask import Flask, render_template, request
import sqlite3 as sql

app = Flask(__name__)

import sqlite3

conn = sqlite3.connect('database.db')
print ("Opened database successfully");

#conn.execute('CREATE TABLE CardPurchases (name TEXT, date TEXT, merchant TEXT, denomination INT, quantity INT, amount INT)')
#print ("Table created successfully");
#conn.close()

#conn.execute('CREATE TABLE Discretion (discretion TEXT, amount INT)')
#print ("Table created successfully");
#conn.close()

#conn.execute('CREATE TABLE Tuition (name TEXT, discretion INT, amount INT)')
#print ("Table created successfully");
#conn.close()

@app.route('/')
def home():
   return render_template('home.html')

@app.route('/client')
def client():
   return render_template('index.html')

@app.route('/totals')
def totals():
   return render_template('totals.html')

@app.route('/student')
def student():
   return render_template('studenttuition.html')

@app.route('/manager')
def manager():
   return render_template('manager.html')

@app.route('/month')
def month():
   return render_template("month.html")

@app.route('/forstudent',methods = ['POST', 'GET'])
def forstudent():
   if request.method == 'POST':
      session = sql.connect('database.db')
      session.row_factory = sql.Row
      cur = session.cursor()
      z = request.form.get('schname')
      cur.execute("select name,sum(amount) from Tuition where name = '{}'".format(z))
      rows = cur.fetchall();
      return render_template("student.html",rows = rows)
      con.close()

@app.route('/qsearch',methods = ['POST', 'GET'])
def qsearch():
   if request.method == 'POST':
      x=request.form.get('d1')
      y=request.form.get('d2')
      la = sql.connect('database.db')
      la.row_factory = sql.Row
      cur = la.cursor()
      # cur.execute("select sum(quantity) from CardPurchases where Date >= '{}' and Date <= '{}'".format(x,y))
      cur.execute("select sum(quantity) from CardPurchases where Date >= 'x' and Date <= 'y'")
      rows = cur.fetchall();
      return render_template("query.html",rows = rows)

@app.route('/disc')
def disc():
   con = sql.connect('database.db')
   con.row_factory = sql.Row
   cur = con.cursor()
   cur.execute("select * from Discretion")
   rows = cur.fetchall();
   return render_template("disc.html",rows = rows)

@app.route('/data',methods = ['POST', 'GET'])
def data():
   if request.method == 'POST':
#        try:

            if float(request.form.get('pdamount')) > 0 : 
               pdu = request.form.get('pduse')
               amount = request.form.get('pdamount')

               with sql.connect('database.db') as con:
                  cur = con.cursor()
                  cur.execute("INSERT INTO Discretion (discretion,amount) VALUES (?,?)",(pdu,amount))
                  con.commit()

            if request.form.get('pduse') == "Tuition Credit":
               name = request.form.get('studentName')
               pdu = request.form.get('pduse')
               amount = request.form.get('pdamount')

               with sql.connect('database.db') as con:
                  cur = con.cursor()
                  cur.execute("INSERT INTO Tuition (name,discretion,amount) VALUES (?,?,?)",(name,pdu,amount))
                  con.commit()

            if int(request.form.get('amountAW')) > 0 : 
                nm = request.form.get('nm')
                dt = request.form.get('dt')
                merch = request.form.get('aW')
                denom = request.form.get('valAW')
                quan = request.form.get('quantityAW')
                amoun = request.form.get('amountAW')
                

                with sql.connect('database.db') as con:
                    cur = con.cursor()
                    cur.execute("INSERT INTO CardPurchases (name,date,merchant,denomination,quantity,amount) VALUES (?,?,?,?,?,?)",(nm,dt,merch,denom,quan,amoun))
                    con.commit()

            if int(request.form.get('amounAce')) > 0 : 
                n = request.form.get('nm')
                d = request.form.get('dt')
                m = request.form.get('ace')
                dt = request.form.get('de')
                q = request.form.get('qAce')
                a = request.form.get('amounAce')
                

                with sql.connect('database.db') as con:
                    cur = con.cursor()
                    cur.execute("INSERT INTO CardPurchases (name,date,merchant,denomination,quantity,amount) VALUES (?,?,?,?,?,?)",(n,d,m,dt,q,a))
                    con.commit()
            
            if int(request.form.get('amounC')) > 0 :
                n = request.form.get('nm')
                d = request.form.get('dt')
                m = request.form.get('caseys')
                dt = request.form.get('d')
                q = request.form.get('quanC')
                a = request.form.get('amounC')
        

                with sql.connect('database.db') as con:
                    cur = con.cursor()
                    cur.execute("INSERT INTO CardPurchases (name,date,merchant,denomination,quantity,amount) VALUES (?,?,?,?,?,?)",(n,d,m,dt,q,a))
                    con.commit()
            
            if int(request.form.get('amounfway')) > 0 : 
                n = request.form.get('nm')
                d = request.form.get('dt')
                m = request.form.get('fway')
                dt = request.form.get('dN')
                q = request.form.get('quanfway')
                a = request.form.get('amounfway')
                

                with sql.connect('database.db') as con:
                    cur = con.cursor()
                    cur.execute("INSERT INTO CardPurchases (name,date,merchant,denomination,quantity,amount) VALUES (?,?,?,?,?,?)",(n,d,m,dt,q,a))
                    con.commit()
            
            if int(request.form.get('amounfisks')) > 0 : 
                n = request.form.get('nm')
                d = request.form.get('dt')
                m = request.form.get('fisks')
                dt = request.form.get('DE')
                q = request.form.get('quanfisks')
                a = request.form.get('amounfisks')
                

                with sql.connect('database.db') as con:
                    cur = con.cursor()
                    cur.execute("INSERT INTO CardPurchases (name,date,merchant,denomination,quantity,amount) VALUES (?,?,?,?,?,?)",(n,d,m,dt,q,a))
                    con.commit()
            
            if int(request.form.get('amoundf')) > 0 :
                n = request.form.get('nm')
                d = request.form.get('dt')
                m = request.form.get('dfresh')
                dt = request.form.get('DEN')
                q = request.form.get('quandf')
                a = request.form.get('amoundf')
                

                with sql.connect('database.db') as con:
                    cur = con.cursor()
                    cur.execute("INSERT INTO CardPurchases (name,date,merchant,denomination,quantity,amount) VALUES (?,?,?,?,?,?)",(n,d,m,dt,q,a))
                    con.commit()
            
            if int(request.form.get('amounkwik')) > 0 :
                n = request.form.get('nm')
                d = request.form.get('dt')
                m = request.form.get('kwikstar')
                dt = request.form.get('DENO')
                q = request.form.get('quankwik')
                a = request.form.get('amounkwik')
                

                with sql.connect('database.db') as con:
                    cur = con.cursor()
                    cur.execute("INSERT INTO CardPurchases (name,date,merchant,denomination,quantity,amount) VALUES (?,?,?,?,?,?)",(n,d,m,dt,q,a))
                    con.commit()
            
            if int(request.form.get('amounpint')) > 0 : 
                n = request.form.get('nm')
                d = request.form.get('dt')
                m = request.form.get('pinters')
                dt = request.form.get('DENOM')
                q = request.form.get('quanpint')
                a = request.form.get('amounpint')
                

                with sql.connect('database.db') as con:
                    cur = con.cursor()
                    cur.execute("INSERT INTO CardPurchases (name,date,merchant,denomination,quantity,amount) VALUES (?,?,?,?,?,?)",(n,d,m,dt,q,a))
                    con.commit()
            
            if int(request.form.get('amounsub')) > 0 : 
                nm = request.form.get('nm')
                dt = request.form.get('dt')
                merch = request.form.get('subway')
                denom = request.form.get('DENOMI')
                quan = request.form.get('quansub')
                amoun = request.form.get('amounsub')
                

                with sql.connect('database.db') as con:
                    cur = con.cursor()
                    cur.execute("INSERT INTO CardPurchases (name,date,merchant,denomination,quantity,amount) VALUES (?,?,?,?,?,?)",(nm,dt,merch,denom,quan,amoun))
                    con.commit()

            if int(request.form.get('amounszq')) > 0 :  
                nm = request.form.get('nm')
                dt = request.form.get('dt')
                merch = request.form.get('szq')
                denom = request.form.get('DENOMIN')
                quan = request.form.get('quanszq')
                amoun = request.form.get('amounszq')
        

                with sql.connect('database.db') as con:
                    cur = con.cursor()
                    cur.execute("INSERT INTO CardPurchases (name,date,merchant,denomination,quantity,amount) VALUES (?,?,?,?,?,?)",(nm,dt,merch,denom,quan,amoun))
                    con.commit()
                    
            if int(request.form.get('amounatom')) > 0 :  
                nm = request.form.get('nm')
                dt = request.form.get('dt')
                merch = request.form.get('atomic')
                denom = request.form.get('DENOMINA')
                quan = request.form.get('quanatom')
                amoun = request.form.get('amounatom')
                

                with sql.connect('database.db') as con:
                    cur = con.cursor()
                    cur.execute("INSERT INTO CardPurchases (name,date,merchant,denomination,quantity,amount) VALUES (?,?,?,?,?,?)",(nm,dt,merch,denom,quan,amoun))
                    con.commit()

            if int(request.form.get('amounso')) > 0 :  
                nm = request.form.get('nm')
                dt = request.form.get('dt')
                merch = request.form.get('so')
                denom = request.form.get('DENOMINAT')
                quan = request.form.get('quanso')
                amoun = request.form.get('amounso')
        

                with sql.connect('database.db') as con:
                    cur = con.cursor()
                    cur.execute("INSERT INTO CardPurchases (name,date,merchant,denomination,quantity,amount) VALUES (?,?,?,?,?,?)",(nm,dt,merch,denom,quan,amoun))
                    con.commit()
                
#        except:
#            con.rollback()
#            msg = "error in insert operation"
      
#        finally:
            msg = "Purchase Complete"
            return render_template("result.html",msg = msg)
            con.close()

@app.route('/list')
def list():
   con = sql.connect('database.db')
   con.row_factory = sql.Row
   
   cur = con.cursor()
   cur.execute("select * from CardPurchases")
   
   rows = cur.fetchall();
   return render_template("list.html",rows = rows)


@app.route('/aw')
def aw():
   con = sql.connect('database.db')
   con.row_factory = sql.Row
   
   cur = con.cursor()
   cur.execute("select sum(quantity),merchant from CardPurchases where merchant = 'A&W 10%(Sold as LIS Card)'")

   rows = cur.fetchall();
   return render_template("aw.html",rows = rows)

@app.route('/ace')
def ace():
   con = sql.connect('database.db')
   con.row_factory = sql.Row
   
   cur = con.cursor()
   cur.execute("select sum(quantity),merchant from CardPurchases where merchant = 'Ace 10%'")
   
   rows = cur.fetchall();
   return render_template("ace.html",rows = rows)

@app.route('/caseys')
def caseys():
   con = sql.connect('database.db')
   con.row_factory = sql.Row
   
   cur = con.cursor()
   cur.execute("select sum(quantity),merchant from CardPurchases where merchant = 'Caseys 3%'")
   
   rows = cur.fetchall();
   return render_template("caseys.html",rows = rows)

@app.route('/fareway')
def fareway():
   con = sql.connect('database.db')
   con.row_factory = sql.Row
   
   cur = con.cursor()
   cur.execute("select sum(quantity),merchant from CardPurchases where merchant = 'Fareway 3%'")
   
   rows = cur.fetchall();
   return render_template("fareway.html",rows = rows)

@app.route('/fisks')
def fisks():
   con = sql.connect('database.db')
   con.row_factory = sql.Row
   
   cur = con.cursor()
   cur.execute("select sum(quantity),merchant from CardPurchases where merchant = 'Fisks 5%'")
   
   rows = cur.fetchall();
   return render_template("fisks.html",rows = rows)

@app.route('/dfresh')
def dfresh():
   con = sql.connect('database.db')
   con.row_factory = sql.Row
   
   cur = con.cursor()
   cur.execute("select sum(quantity),merchant from CardPurchases where merchant = 'Dollar Fresh 3%'")
   
   rows = cur.fetchall();
   return render_template("dfresh.html",rows = rows)

@app.route('/kwikstar')
def kwikstar():
   con = sql.connect('database.db')
   con.row_factory = sql.Row
   
   cur = con.cursor()
   cur.execute("select sum(quantity),merchant from CardPurchases where merchant = 'Kwik Star 5% **'")
   
   rows = cur.fetchall();
   return render_template("kwikstar.html",rows = rows)

@app.route('/pinters')
def pinters():
   con = sql.connect('database.db')
   con.row_factory = sql.Row
   
   cur = con.cursor()
   cur.execute("select sum(quantity),merchant from CardPurchases where merchant = 'Pinters 3%'")
   
   rows = cur.fetchall();
   return render_template("pinters.html",rows = rows)

@app.route('/subway')
def subway():
   con = sql.connect('database.db')
   con.row_factory = sql.Row
   
   cur = con.cursor()
   cur.execute("select sum(quantity),merchant from CardPurchases where merchant = 'Subway 5%'")
   
   rows = cur.fetchall();
   return render_template("subway.html",rows = rows)

@app.route('/szq')
def szq():
   con = sql.connect('database.db')
   con.row_factory = sql.Row
   
   cur = con.cursor()
   cur.execute("select sum(quantity),merchant from CardPurchases where merchant = 'Sue-Z-Q 10%'")
   
   rows = cur.fetchall();
   return render_template("szq.html",rows = rows)

@app.route('/atomic')
def atomic():
   con = sql.connect('database.db')
   con.row_factory = sql.Row
   
   cur = con.cursor()
   cur.execute("select sum(quantity),merchant from CardPurchases where merchant = 'Atomic 5%'")
   
   rows = cur.fetchall();
   return render_template("atomic.html",rows = rows)

@app.route('/special')
def special():
   con = sql.connect('database.db')
   con.row_factory = sql.Row
   
   cur = con.cursor()
   cur.execute("select sum(quantity),merchant from CardPurchases where merchant = 'Special Orders'")
   
   rows = cur.fetchall();
   return render_template("special.html",rows = rows)

@app.route('/gfund')
def generalFund():
   con = sql.connect('database.db')
   con.row_factory = sql.Row
   
   cur = con.cursor()
   cur.execute("select sum(amount),discretion from Discretion where discretion = 'Donation to General Fund'")
   
   rows = cur.fetchall();
   return render_template("gfund.html",rows = rows)

@app.route('/allfund')
def allstudentsFund():
   con = sql.connect('database.db')
   con.row_factory = sql.Row
   
   cur = con.cursor()
   cur.execute("select sum(amount),discretion from Discretion where discretion = 'Adopt a Student Fund'")
   
   rows = cur.fetchall();
   return render_template("allfund.html",rows = rows)

if __name__ == "__main__":
  app.run()