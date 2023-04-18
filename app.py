from flask import Flask, jsonify, request, redirect, render_template

from repository.db_connector import (
    delete_game,
    get_games,
    get_game_by_id,
    insert_game,
    update_game,
)


app = Flask("Games")


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/games/<int:id>")
def game_by_id(id):
    games = [get_game_by_id(id)]
    return jsonify(games=games), 200


@app.route("/games")
def games():
    games = get_games()
    return jsonify(games=games), 200


@app.route("/save_game", methods=["POST"])
def save_game():
    data = request.get_json()
    name = data["name"]
    description = data["description"]
    price = float(data["price"])
    insert_game(name, description, price)
    return redirect("/games")



@app.route("/update_game/<int:id>", methods=["PUT"])
def update(id):
    data = request.get_json()
    update_game(
        id=id,
        name=data["name"],
        description=data["description"],
        price=float(data["price"]),
    )
    return redirect("/games")


@app.route("/delete_game", methods=["POST"])
def delete_game():
    delete_game(data["id"])
    return redirect("/games")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
