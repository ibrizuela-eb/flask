from flask import Flask, jsonify, request, redirect, render_template
from flask_cors import CORS, cross_origin

from repository.database import get_connection
from repository.game_repository import GameRepository


app = Flask("Games")
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route("/")
@cross_origin()
def home():
    return render_template('index.html')


@app.route("/games/<int:id>")
@cross_origin()
def game_by_id(id):
    games = [GameRepository(get_connection()).get_game_by_id(id)]
    return jsonify(games=games), 200


@app.route("/games")
@cross_origin()
def games():
    games = GameRepository(get_connection()).get_games()
    return jsonify(games=games), 200


@app.route("/save_game", methods=["POST"])
@cross_origin()
def save_game():
    data = request.get_json()
    name = data["name"]
    description = data["description"]
    price = float(data["price"])
    GameRepository(get_connection()).insert_game(name, description, price)
    return redirect("/games")


@app.route("/update_game/<int:id>", methods=["PUT"])
@cross_origin()
def update(id):
    data = request.get_json()
    GameRepository(get_connection()).update_game(
        id=id,
        name=data["name"],
        description=data["description"],
        price=float(data["price"]),
    )
    return redirect("/games")


@app.route("/delete_game", methods=["POST"])
@cross_origin()
def delete_game():
    GameRepository(get_connection()).delete_game(data["id"])
    return redirect("/games")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
