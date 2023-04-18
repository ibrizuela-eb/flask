from repository.database import get_connection


def insert_game(name, description, price):
    connection = get_connection()
    with connection.cursor() as cursor:
        cursor.execute(
            "INSERT INTO games(name, description, price) VALUES (%s, %s, %s)",
            (name, description, price),
        )
    connection.commit()
    connection.close()


def get_games():
    connection = get_connection()
    games = []
    with connection.cursor() as cursor:
        cursor.execute("SELECT id, name, description, price FROM games")
        games = cursor.fetchall()
    connection.close()
    return games


def get_game_by_id(id):
    connection = get_connection()
    game = None
    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT id, name, description, price FROM games WHERE id = %s",
            id
        )
        game = cursor.fetchone()
    connection.close()
    return game


def update_game(id, name, description, price):
    connection = get_connection()
    with connection.cursor() as cursor:
        cursor.execute(
            "UPDATE games SET name = %s, description = %s, price = %s WHERE id = %s",
            (name, description, price, id)
        )
    connection.commit()
    connection.close()


def delete_game(id):
    connection = get_connection()
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM games WHERE id = %s", id)
    connection.commit()
    connection.close()
