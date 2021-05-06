#!/usr/bin/env python3

#!/usr/bin/env python3
"""Flask api server for final project"""

import json
from flask import Flask, Response, jsonify
import random

app = Flask(__name__)

@app.route("/api/games")
def all_games():
    all_game_names = [

        "GT Sport", 
        "Yakuza 6", 
        "Street Fighter 5", 
        "Infamous: Second Son", 
        "The Last of Us Remastered ", 
        "Ratchet and Clank", 
        "Uncharted 4: A Thief's End", 
        "Ghost of Tsushima", 
        "Bloodborne", 
        "Marvel's Spider-Man", 
        "God of War", 
        "The Last of Us Part 2", 
        "Forza Motorsport 7", 
        "Ori and the Will of the Wisps", 
        "Gears of War: Ultimate Edition", 
        "Sunset Overdrive", 
        "Halo 5: Guardians", 
        "Gears 5", 
        "Forza Horizon 4", 
        "Quantum Break", 
        "State of Decay 2", 
        "Halo Wars 2", 
        "Ori and the Will of the Wisps", 
        "Ashen", 
        "Half-Life: Alyx", 
        "Total War series", 
        "Disco Elysium", 
        "Mount & Blade II: Bannerlord", 
        "Dota 2/League of Legends", 
        "Age of Empires 2: Definitive Edition", 
        "Rimworld", 
        "Crusader Kings 2", 
        "Guild Wars 2", 
        "All the golden oldies", 
        "A Monster's Expedition", 
        "Microsoft Flight Simulator",

    ]
    randomGame = random.choice(all_game_names)
    outputFormat = Response(json.dumps
    ({
        "name":randomGame,
    }))
    outputFormat.headers["Access-Control-Allow-Origin"] = "*"
    outputFormat.headers["Content-Type"] = "application/json"
    return outputFormat

@app.route("/api/games/playstation")
def playstation():
    playstation_games_names = [

        "GT Sport", 
        "Yakuza 6", 
        "Street Fighter 5", 
        "Infamous: Second Son", 
        "The Last of Us Remastered ", 
        "Ratchet and Clank", 
        "Uncharted 4: A Thief's End", 
        "Ghost of Tsushima", 
        "Bloodborne", 
        "Marvel's Spider-Man", 
        "God of War", 
        "The Last of Us Part 2", 

    ]
    randomPlaystationGame = random.choice(playstation_games_names)
    outputFormat = Response(json.dumps
    ({
        "psg_name":randomPlaystationGame,
    }))
    outputFormat.headers["Access-Control-Allow-Origin"] = "*"
    outputFormat.headers["Content-Type"] = "application/json"
    return outputFormat

@app.route("/api/games/xbox")
def xbox():
    xbox_games = [

        "Forza Motorsport 7", 
        "Ori and the Will of the Wisps", 
        "Gears of War: Ultimate Edition", 
        "Sunset Overdrive", 
        "Halo 5: Guardians", 
        "Gears 5", 
        "Forza Horizon 4", 
        "Quantum Break", 
        "State of Decay 2", 
        "Halo Wars 2", 
        "Ori and the Will of the Wisps", 
        "Ashen", 
        
    ]
    randomXboxGame = random.choice(xbox_games)
    outputFormat = Response(json.dumps
    ({
        "xbg_name":randomXboxGame,
    }))
    outputFormat.headers["Access-Control-Allow-Origin"] = "*"
    outputFormat.headers["Content-Type"] = "application/json"
    return outputFormat

@app.route("/api/games/pc")
def pc():
    pc_games = [

        "Half-Life: Alyx", 
        "Total War series", 
        "Disco Elysium", 
        "Mount & Blade II: Bannerlord", 
        "Dota 2/League of Legends", 
        "Age of Empires 2: Definitive Edition", 
        "Rimworld", 
        "Crusader Kings 2", 
        "Guild Wars 2", 
        "All the golden oldies", 
        "A Monster's Expedition", 
        "Microsoft Flight Simulator",
        
    ]
    randomPcGame = random.choice(pc_games)
    outputFormat = Response(json.dumps
    ({
        "pcg_name":randomPcGame,
    }))
    outputFormat.headers["Access-Control-Allow-Origin"] = "*"
    outputFormat.headers["Content-Type"] = "application/json"
    return outputFormat

if __name__ == "__main__":
    app.run()