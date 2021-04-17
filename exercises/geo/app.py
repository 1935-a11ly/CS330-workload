import requests
from flask import Flask, request, render_template, send_from_directory
from flask import redirect, url_for
import records 

app = Flask(__name__)

# Optimization methods illustrated in lecture 

all_available_regions = []
all_available_continents = []
all_available_countries = []
CACHE = {}

#  get_data_from_db function structured as in lecture with change from postgres to postgresql

def  get_data_from_db(host:str, port:int, user:str, nameOfDatabase:str, query: str) -> list:
    dataBase = records.Database(f"postgresql://{user}:@{host}:{port}/{nameOfDatabase}")
    rowNumber = dataBase.query(query)
    return rowNumber 

@app.route("/", methods=["GET", "POST"])
def index():

    global CACHE 

    if request.method == "GET":
        return render_template("index.html")
        
    if request.form.get("country_name"):
        country = request.form.get("country_name")
        if country in CACHE:
            result = CACHE[country]
        else:
            result =  get_data_from_db(
                host = "localhost",
                port = 2345,
                user = "musami01",
                nameOfDatabase = "world",
                query = f"select * from country where code = '{country}';",
            )
            CACHE[country] = result
        return render_template("results.html", retrievedData = result)

    if request.form.get("region_name"):
        region = request.form.get("region_name")
        if region in CACHE:
            result = CACHE[region]
        else:
            result =  get_data_from_db(
                host = "localhost",
                port = 2345,
                user = "musami01",
                nameOfDatabase = "world",
                query = f"select * from country where region = '{region}';",
            )
            CACHE[region] = result
        return render_template("results.html", retrievedData=result)
    if request.form.get("continent_name"):
        continent = request.form.get("continent_name")
        if continent in CACHE:
            result = CACHE[continent]
            
        else:
            result =  get_data_from_db(
                host = "localhost",
                port = 2345,
                user = "musami01",
                nameOfDatabase = "world",
                query = f"select * from country where continent = '{continent}';",
            )
            CACHE[continent] = result
        return render_template("results.html", retrievedData = result)
        


@app.route("/<string:scope>")
def search(scope: str):

    global all_available_countries 
    global all_available_regions 
    global all_available_continents

    if scope=="country":
        if not all_available_countries:
            all_available_countries =  get_data_from_db(
                host = "localhost",
                port = 2345,
                user = "musami01",
                nameOfDatabase = "world",
                query = "select code,name from country;"
            )
        return render_template("country.html", options = all_available_countries)


    if scope=="region":
        if not all_available_regions:
            all_available_regions =  get_data_from_db(
                host = "localhost",
                port = 2345,
                user = "musami01",
                nameOfDatabase = "world",
                query = "select distinct region from country;"
            )
        return render_template("region.html", options = all_available_regions)


    if scope=="continent":
        if not all_available_continents:
            all_available_continents =  get_data_from_db(
                host = "localhost",
                port = 2345,
                user = "musami01",
                nameOfDatabase = "world",
                query = "select distinct continent from country;"
            )
        return render_template("continent.html", options = all_available_continents)

if __name__ == "__main__":
    app.run()